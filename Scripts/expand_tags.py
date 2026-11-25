from bs4 import BeautifulSoup
import argparse
import os

from mermaid_lib import turtle_to_mermaid

namespaces = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "semiotics": "http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "void": "http://www.w3.org/2006/vcard/ns#",
        "lexinfo": "http://www.lexinfo.net/ontology/3.0/lexinfo#",
        "lexicog": "http://www.w3.org/ns/lemon/lexicog#",
        "voaf": "http://purl.org/vocommons/voaf#",
        }

tags_to_expand = {
        "range": {"rel": "rdfs:range"},
        "domain": {"rel": "rdfs:domain"},
        "subclass": {"rel": "rdfs:subClassOf"},
        "subproperty": {"rel": "rdfs:subPropertyOf"},
        "inverse": {"rel": "owl:inverseOf"},
        "equivalentclass": {"rel": "owl:equivalentClass"},
        "equivalentproperty": {"rel": "owl:equivalentProperty"},
        }

tags_text = {
        "range": "Range:",
        "domain": "Domain:",
        "subclass": "Subclass:",
        "subproperty": "Subproperty:",
        "inverse": "Inverse Property:",
        "equivalentclass": "Equivalent Class:",
        "equivalentproperty": "Equivalent Property:",
        }

characteristics = {
        "functional": ("owl:FunctionalProperty", "Functional"),
        "inverse-functional": ("owl:InverseFunctionalProperty", "Inverse Functional"),
        "symmetric": ("owl:SymmetricProperty", "Symmetric"),
        }

def build_or(parts, contents, soup, dfn_about, sep=" OR "):
    if len(parts) > 1:
        new_contents = soup.new_tag('span', typeof="rdf:List")
        first_contents, first_attrs = transform_contents(soup, parts[0], dfn_about)
        first_tag = soup.new_tag('span', rel="rdf:first", **first_attrs)
        first_tag.append(first_contents)
        new_contents.append(first_tag)
        new_contents.append(sep)
        rest_contents, rest_attrs = build_or(parts[1:], contents, soup, dfn_about)
        rest_tag = soup.new_tag('span', rel="rdf:rest", **rest_attrs)
        if rest_contents:
            rest_tag.append(rest_contents)
        new_contents.append(rest_tag)
        return new_contents, {}
    elif len(parts) == 1:
        new_contents = soup.new_tag('span', typeof="rdf:List")
        part_contents, part_attrs = transform_contents(soup, parts[0], dfn_about)
        part_tag = soup.new_tag('span', rel="rdf:first", **part_attrs)
        part_tag.append(part_contents)
        res_tag = soup.new_tag('span', rel="rdf:rest", resource="rdf:nil")
        new_contents.append(part_tag)
        new_contents.append(res_tag)
        return new_contents, {}
    else:
        return None, {"resource": "rdf:nil"}

def transform_contents(soup, contents, dfn_about):
    if "," in contents:
        # Commas seperate multiple values, return each as a span
        new_contents = soup.new_tag('span')
        first = True
        for part in contents.split(","):
            if not first:
                new_contents.append(", ")
            first = False
            part = part.strip()
            part_contents, part_attrs = transform_contents(soup, part, dfn_about)
            part_tag = soup.new_tag('span', **part_attrs)
            part_tag.append(part_contents)
            new_contents.append(part_tag)
        return new_contents, {}
    elif " min " in contents or " max " in contents or " exactly " in contents:
        if " min " in contents:
            parts = contents.split(" min ")
            keyword = " min "
            unqualified_prop, qualified_prop = "owl:minCardinality", "owl:minQualifiedCardinality"
        elif " max " in contents:
            parts = contents.split(" max ")
            keyword = " max "
            unqualified_prop, qualified_prop = "owl:maxCardinality", "owl:maxQualifiedCardinality"
        else:#if " exactly " in contents:
            parts = contents.split(" exactly ")
            keyword = " exactly "
            unqualified_prop, qualified_prop = "owl:cardinality", "owl:qualifiedCardinality"
        if len(parts) != 2:
            raise ValueError("Invalid OWL cardinality format: " + contents)
        restriction = soup.new_tag('span', typeof='owl:Restriction')
        prop_contents, prop_attrs = transform_contents(soup, parts[0], dfn_about)
        prop_tag = soup.new_tag('span', rel="owl:onProperty", **prop_attrs)
        prop_tag.append(prop_contents)
        restriction.append(prop_tag)
        restriction.append(keyword)
        parts2 = parts[1].split(" ")
        # A trailing class after the cardinality number (e.g. "min 2 [=observable=]")
        # produces a *qualified* cardinality restriction (owl:onClass), rather than
        # a plain owl:{min,max,}Cardinality restriction.
        if len(parts2) > 1:
            card_tag = soup.new_tag('span', property=qualified_prop, datatype="xsd:nonNegativeInteger")
            card_tag.string = parts2[0]
            restriction.append(card_tag)
            restriction.append(" ")
            class_contents, class_attrs = transform_contents(soup, " ".join(parts2[1:]), dfn_about)
            class_tag = soup.new_tag('span', rel="owl:onClass", **class_attrs)
            class_tag.append(class_contents)
            restriction.append(class_tag)
        else:
            card_tag = soup.new_tag('span', property=unqualified_prop, datatype="xsd:integer")
            card_tag.string = parts2[0]
            restriction.append(card_tag)
        return restriction, {}
    elif " only " in contents:
        parts = contents.split(" only ")
        if len(parts) != 2:
            raise ValueError("Invalid OWL only format: " + contents)
        restriction = soup.new_tag('span', typeof='owl:Restriction')
        prop_contents, prop_attrs = transform_contents(soup, parts[0], dfn_about)
        prop_tag = soup.new_tag('span', rel="owl:onProperty", **prop_attrs)
        prop_tag.append(prop_contents)
        restriction.append(prop_tag)
        restriction.append(" only ")
        range_contents, range_attrs = transform_contents(soup, parts[1], dfn_about)
        all_tag = soup.new_tag('span', rel="owl:allValuesFrom", **range_attrs)
        all_tag.append(range_contents)
        restriction.append(all_tag)
        return restriction, {}
    elif " OR " in contents:
        # This generates an OWL unionOf tag
        parts_contents, parts_attrs = build_or(contents.split(" OR "), contents, soup, dfn_about)
        new_contents = soup.new_tag('span', rel="owl:unionOf", **parts_attrs)
        new_contents.append(parts_contents)
        return new_contents, {}
    elif " o " in contents:
        parts_contents, parts_attrs = build_or(contents.split(" o "), contents, soup, dfn_about, sep=" o ")
        new_contents = soup.new_tag('span', rel="owl:propertyChainAxiom", **parts_attrs)
        new_contents.append(parts_contents)
        return new_contents, {}
    elif contents.startswith("[=") and contents.endswith("=]"):
        if contents[2:-2].lower() in dfn_about:
            return contents, {"resource": dfn_about[contents[2:-2].lower()]}
        else:
            raise ValueError(f"DFN reference not found: \'{contents[2:-2].lower()}\'")
    elif ":" in contents and " " not in contents:
        if contents.startswith("http://") or contents.startswith("https://"):
            new_contents = soup.new_tag('a', href=contents,
                                        resource=contents)
            new_contents.string = contents
            return new_contents, {}
        else:
            for prefix, uri in namespaces.items():
                if contents.startswith(prefix + ":"):
                    new_contents = soup.new_tag('a', href=uri + contents[len(prefix) + 1:],
                                                resource=contents)
                    new_contents.string = contents
                    return new_contents, {}
            raise ValueError(f"Content of tag does not look like a URI: {contents}")
    else:
        raise ValueError("Could not transform contents: " + contents)


def expand_tags(soup):
    dfn_about = build_dfn_about_map(soup)

    for t in tags_to_expand:
        for tag in soup.find_all(t):
            new_contents, new_attrs = transform_contents(soup, tag.contents[0], dfn_about)
            new_attrs = {**new_attrs, **tags_to_expand[t]}
            new_tag = soup.new_tag('div', **new_attrs)
            strong_tag = soup.new_tag('strong')
            strong_tag.string = tags_text[t] + " "
            new_tag.append(strong_tag)
            new_tag.append(new_contents)
            tag.replace_with(new_tag)

    for c in characteristics:
        for tag in soup.find_all(c):
            new_tag = soup.new_tag('div', rel="rdf:type", resource=characteristics[c][0])
            strong_tag = soup.new_tag('strong')
            strong_tag.string = characteristics[c][1]
            new_tag.append(strong_tag)
            tag.replace_with(new_tag)

def expand_asides(soup, base_dir):
    """Render the Mermaid diagram for each `<aside src="...">` example,
    generated at build time from the Turtle file it points at (the same
    file that supplies the aside's inline Turtle listing), and insert it
    as a `<pre class="mermaid">` before that listing.
    """
    for aside in soup.find_all(["aside", "div"], src=True):
        src = aside["src"]
        ttl_path = os.path.join(base_dir, src)
        with open(ttl_path) as f:
            text = f.read()
        # a .LR file next to the Turtle file asks for a left-to-right layout
        direction = "LR" if os.path.exists(os.path.splitext(ttl_path)[0] + ".LR") else None
        # likewise an .elk file asks for the ELK layout engine
        elk = os.path.exists(os.path.splitext(ttl_path)[0] + ".elk")
        mermaid_text = turtle_to_mermaid(text, direction, elk)

        pre = soup.new_tag("pre", **{"class": "mermaid"})
        pre.string = mermaid_text
        aside.insert(0, pre)
        del aside["src"]


def build_dfn_about_map(soup):
    dfn_about_map = {}

    # Find all <div> elements with an 'about' attribute
    for div in soup.find_all('div', attrs={'about': True}):
        dfn = div.find('dfn')
        if dfn:
            key = dfn.get_text(strip=True)
            value = div['about']
            dfn_about_map[key.lower()] = value

    dfn_about_map["is sense of"] = "ontolex:isSenseOf"
    dfn_about_map["is reference of"] = "ontolex:isReferenceOf"
    dfn_about_map["is denoted by"] = "ontolex:isDenotedBy"
    dfn_about_map["is evoked by"] = "ontolex:isEvokedBy"
    dfn_about_map["is lexicalized sense of"] = "ontolex:isLexicalizedSenseOf"
    dfn_about_map["is concept of"] = "ontolex:isConceptOf"
    dfn_about_map["is definition of"] = "ontolex:isDefinitionOf"
    dfn_about_map["is syntactic behavior of"] = "ontolex:isSyntacticBehaviorOf"
    dfn_about_map["onto map"] = "synsem:OntoMap"


    return dfn_about_map

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Expand HTML tags in a file.')
    parser.add_argument('input_file', type=str, help='Path to the input HTML file')
    parser.add_argument('output_file', type=str, help='Path to the output HTML file')
    parser.add_argument('--base', default=None,
                        help='Directory that the src of example asides is relative to (default: directory of the input file)')
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    expand_tags(soup)
    expand_asides(soup, args.base or os.path.dirname(os.path.abspath(args.input_file)))

    with open(args.output_file, 'w', encoding='utf-8') as file:
        result = str(soup)

        # Remove new lines after `<div property="rdfs:comment">` and the next </div>
        result = result.replace('<div property="rdfs:comment">\n  ', '<div property="rdfs:comment">')
        result = result.replace('\n  </div>', '</div>')
        file.write(result)
