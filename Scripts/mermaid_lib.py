"""Generate a Mermaid flowchart from a Turtle RDF example.

Used both by convert_to_mermaid.py (a CLI wrapper, for manual/local
preview) and by expand_tags.py (which calls turtle_to_mermaid() directly
at HTML-build time to render the diagram for each `<aside src="...">`
example, from the same Turtle file that supplies the aside's listing).
"""
from rdflib.namespace import RDF
from rdflib import Graph, URIRef, BNode
import re

# Literals longer than this are truncated, with "...".
MAX_LITERAL = 30

# Diagrams with at least this many nodes are laid out left to right.
WIDE_DIAGRAM_NODES = 12


def make_name(n):
    s = str(n)
    i = 0
    if '#' in s:
        i = s.rindex('#')
    if '/' in s:
        i = max(i, s.rindex('/'))
    t = s[i + 1:]
    if t == "":
        return "_node"
    else:
        return t


def escape_label(text):
    # Mermaid reserves double quotes as the label delimiter; escape any
    # characters that would otherwise break out of the quoted label.
    text = text.replace("&", "#amp;")
    text = text.replace("\"", "#quot;")
    text = text.replace("<", "#lt;")
    text = text.replace(">", "#gt;")
    return text


def shorten(text):
    """Truncate a literal that is too long for a node, marking the cut."""
    return text if len(text) <= MAX_LITERAL else text[:MAX_LITERAL].rstrip() + "..."


def write_obj(o):
    if isinstance(o, URIRef):
        return "<%s>" % str(o)
    elif isinstance(o, BNode):
        return "[]"
    text = shorten(str(o)).replace("\\", "\\\\")
    return "%s@%s" % (text, o.language) if o.language else text


def make_id(name):
    id = re.sub(r"[\W]", "_", name)
    if id == "" or id[0].isdigit():
        id = "n_" + id
    return id


def edge_label(p):
    """The label of an edge: the local name, or `rdf:_1` for container membership."""
    name = make_name(p)
    return "rdf:" + name if str(p).startswith(str(RDF)) and re.fullmatch(r"_\d+", name) else name


def natural_key(text):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", text)]


def turtle_to_mermaid(ttl_text, direction=None, elk=False):
    """`direction` ("LR" or "TD") overrides the layout chosen from the size;
    `elk` selects the ELK layout engine, which places edge labels better."""
    g = Graph()
    g.parse(data=ttl_text, format="turtle")

    roots = set([s for s, p, o in g if len(list(g.subjects(None, s))) == 0])

    # Blank nodes are drawn without any id or name in the label (see
    # https://github.com/ontolex/morph/issues/43): they still need a
    # stable, unique identifier to wire up edges in the Mermaid source,
    # just not one that's shown to the reader.
    bnode_ids = {}

    def node_id(n):
        if isinstance(n, BNode):
            if n not in bnode_ids:
                bnode_ids[n] = "bnode%d" % (len(bnode_ids) + 1)
            return bnode_ids[n]
        return make_id(make_name(n))

    seen_node = set([])
    lines_out = ["flowchart"]

    def gen(s):
        id = node_id(s)
        class_of = None
        if s not in seen_node:
            seen_node.add(s)
            for o in g.objects(s, RDF.type):
                if not class_of:
                    class_of = o
            args = []
            # Several properties between the same two nodes share one arrow,
            # labelled e.g. "constituent / rdf:_1".
            edges = {}
            for p, o in g.predicate_objects(s):
                if p != RDF.type and (isinstance(o, URIRef) or isinstance(o, BNode)):
                    o_id = gen(o)
                    edges.setdefault(o_id, []).append(edge_label(p))
                elif p != RDF.type:
                    prop_name = make_name(p)
                    args.append("%s=%s" % (prop_name, write_obj(o)))
            for o_id, labels in edges.items():
                labels.sort(key=natural_key)
                lines_out.append("    %s -->|%s| %s" % (id, escape_label(" / ".join(labels)), o_id))
            if isinstance(s, BNode):
                header = None
            elif class_of:
                header = "%s : %s" % (make_name(s), make_name(class_of))
            else:
                header = make_name(s)
            # An empty quoted label is a Mermaid syntax error; a single
            # space renders as a blank box, which is what a label-less
            # blank node (https://github.com/ontolex/morph/issues/43)
            # should look like.
            # As in the GraphViz diagrams, a rule separates the name and type
            # of a node from its properties.
            label = "<br/>".join(escape_label(line) for line in args)
            if header is not None:
                label = escape_label(header) + ("<hr/>" + label if label else "")
            label = label or " "
            lines_out.append("    %s[\"%s\"]" % (id, label))
        return id

    if roots:
        # `roots` is a set, whose iteration order depends on Python's
        # per-process hash randomization; sort for deterministic, stable
        # output across regenerations.
        for s in sorted(roots, key=str):
            gen(s)
    else:
        gen(next(g.subjects()))

    # Top-down layouts spread sibling nodes sideways, so big graphs become
    # very wide and unreadable once scaled to the page (see
    # https://github.com/ontolex/morph/issues/78); lay those out left to
    # right instead, which spreads siblings vertically.
    n_nodes = sum(1 for l in lines_out if l.endswith('"]'))
    direction = direction or ("LR" if n_nodes >= WIDE_DIAGRAM_NODES else "TD")
    lines_out[0] = "flowchart %s" % direction

    text = "\n".join(lines_out) + "\n"
    if elk:
        text = "---\nconfig:\n  layout: elk\n---\n" + text
    return text
