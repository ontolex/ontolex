from rdflib import *
g = Graph()
import sys
g.parse(sys.argv[1], format="json-ld")
for s, p, o in g:
  print("%s %s %s" % (str(s.encode("utf8")), str(p.encode("utf8")), str(o.encode("utf8"))))
