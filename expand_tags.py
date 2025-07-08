from bs4 import BeautifulSoup
import argparse

namespaces = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "semiotics": "http://www.ontologydesignpatterns.org/cp/owl/semiotics.owl#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "void": "http://www.w3.org/2006/vcard/ns#",
        "voaf": "http://purl.org/vocommons/voaf#",
        }

tags_to_expand = {
        "range": {"rel": "rdfs:range"},
        "domain": {"rel": "domain"},
        "subclass": {"rel": "rdfs:subClassOf"},
        "subproperty": {"rel": "rdfs:subPropertyOf"},
        "inverse": {"rel": "owl:inverseOf"},
        "equivalentClass": {"rel": "owl:equivalentClass"},
        }

tags_text = {
        "range": "Range:",
        "domain": "Domain:",
        "subclass": "Subclass:",
        "subproperty": "Subproperty:",
        "inverse": "Inverse Property:",
        "equivalentClass": "Equivalent Class:",
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
        new_contents.append(" OR ")
        rest_contents, rest_attrs = build_or(parts[1:], contents, soup, dfn_about)
        rest_tag = soup.new_tag('span', rel="rdf:rest", **rest_attrs)
        if rest_contents:
            rest_tag.append(rest_contents)
        new_contents.append(rest_tag)
        return new_contents, {}
    else:
        return None, {"resource": "rdf:nil"}

def transform_contents(soup, contents, dfn_about):
    if "," in contents:
        # Commas seperate multiple values, return each as a span
        new_contents = soup.new_tag('span')
        for part in contents.split(","):
            part = part.strip()
            part_contents, part_attrs = transform_contents(soup, part, dfn_about)
            part_tag = soup.new_tag('span', **part_attrs)
            part_tag.append(part_contents)
            new_contents.append(part_tag)
        return new_contents, {}
    elif " min " in contents or " max " in contents or " exactly " in contents:
        if " min " in contents:
            parts = contents.split(" min ")
        elif " max " in contents:
            parts = contents.split(" max ")
        else:#if " exactly " in contents:
            parts = contents.split(" exactly ")
        if len(parts) != 2:
            raise ValueError("Invalid OWL cardinality format: " + contents)
        restriction = soup.new_tag('span', typeof='owl:Restriction')
        prop_contents, prop_attrs = transform_contents(soup, parts[0], dfn_about)
        prop_tag = soup.new_tag('span', rel="owl:onProperty", **prop_attrs)
        prop_tag.append(prop_contents)
        restriction.append(prop_tag)
        if " min " in contents:
            restriction.append(" min ")
            card_tag = soup.new_tag('span', rel="owl:minCardinality", datatype="xsd:integer")
        elif " max " in contents:
            restriction.append(" max ")
            card_tag = soup.new_tag('span', rel="owl:maxCardinality", datatype="xsd:integer")
        else:#if " exactly " in contents:
            restriction.append(" exactly ")
            card_tag = soup.new_tag('span', rel="owl:cardinality", datatype="xsd:integer")
        parts2 = parts[1].split(" ")
        card_tag.string = parts2[0]
        restriction.append(card_tag)
        if len(parts2) > 1:
            range_contents, range_attrs = transform_contents(soup, " ".join(parts2[1:]), dfn_about)
            all_tag = soup.new_tag('span', rel="owl:allValuesFrom", **range_attrs)
            all_tag.append(range_contents)
            restriction.append(all_tag)
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
            strong_tag.string = tags_text[t]
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
    dfn_about_map["is evoked by"] = "ontolex:isEvokedBy"
    dfn_about_map["is lexicalized sense of"] = "ontolex:isLexicalizedSenseOf"
    dfn_about_map["is concept of"] = "ontolex:isConceptOf"
    dfn_about_map["is syntactic behavior of"] = "ontolex:isSyntacticBehaviorOf"


    return dfn_about_map

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Expand HTML tags in a file.')
    parser.add_argument('input_file', type=str, help='Path to the input HTML file')
    parser.add_argument('output_file', type=str, help='Path to the output HTML file')
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    expand_tags(soup)

    with open(args.output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))
