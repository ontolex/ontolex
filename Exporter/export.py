import sys

in_doc = False
in_doc_trigger = """</p><textarea readonly="" accesskey="," id="wpTextbox1" cols="80" rows="25" style="" lang="en" dir="ltr" name="wpTextbox1">"""
end_doc_trigger = """</textarea><div class="templatesUsed">"""
doc = ""

for line in open("spec-raw.html").readlines():
    if line.startswith(in_doc_trigger) and not in_doc:
        in_doc = True
        doc += line[len(in_doc_trigger):] 
    elif line.startswith(end_doc_trigger) and in_doc:
        in_doc = False
    elif in_doc:
        doc += line.replace("&lt;","<")

def apply_template(template, args):
    if template == "Class":
        sys.stdout.write("<div class='entity'>")
        sys.stdout.write("<h3>%s (Class)</h3>\n" % args[0])
        sys.stdout.write("<p><strong>URI:</strong> http://www.w3.org/nl/lemon/%s/%s</h3>\n" % (args[1],args[2]))
        sys.stdout.write("<div class='comment'>%s</div>" % args[3])
        sys.stdout.write("<div class='description'>%s</div>" % args[4])
        sys.stdout.write("</div>")
    elif template == "DatatypeProperty":
        sys.stdout.write("<div class='entity'>")
        sys.stdout.write("<h3>%s (Datatype Property)</h3>\n" % args[0])
        sys.stdout.write("<p><strong>URI:</strong> http://www.w3.org/nl/lemon/%s/%s</h3>\n" % (args[1],args[2]))
        sys.stdout.write("<div class='comment'>%s</div>" % args[3])
        sys.stdout.write("<div class='description'>%s</div>" % args[4])
        sys.stdout.write("</div>")
    elif template == "ObjectProperty":
        sys.stdout.write("<div class='entity'>")
        sys.stdout.write("<h3>%s (Object Property)</h3>\n" % args[0])
        sys.stdout.write("<p><strong>URI:</strong> http://www.w3.org/nl/lemon/%s/%s</h3>\n" % (args[1],args[2]))
        sys.stdout.write("<div class='comment'>%s</div>" % args[3])
        sys.stdout.write("<div class='description'>%s</div>" % args[4])
        sys.stdout.write("</div>")
    elif template == "Individual":
        sys.stdout.write("<div class='entity'>")
        sys.stdout.write("<h3>%s (Individual)</h3>\n" % args[0])
        sys.stdout.write("<p><strong>URI:</strong> http://www.w3.org/nl/lemon/%s/%s</h3>\n" % (args[1],args[2]))
        sys.stdout.write("<div class='comment'>%s</div>" % args[3])
        sys.stdout.write("<div class='description'>%s</div>" % args[4])
        sys.stdout.write("</div>")
    elif template == "Example":
        sys.stdout.write("<div>")
        sys.stdout.write("<p style='width:100%%;'><img src='https://raw.githubusercontent.com/cimiano/ontolex/master/Examples/%s.png' class='example'/></p>" % (args[0]))
        sys.stdout.write("%s" % args[1])
        sys.stdout.write("</div>")
    else:
        print(template)
        sys.exit(-1)


while "{{" in doc:
    template_name = doc[doc.index("{{")+2:doc.index("|",doc.index("{{"))]
    args = doc[doc.index("|",doc.index("{{"))+1:doc.index("}}",doc.index("{{"))].split("|")
    sys.stdout.write(doc[:doc.index("{{")])
    apply_template(template_name, args)
    n = doc.index("}}",doc.index("{{"))+2
    doc = doc[n:]
print(doc)




