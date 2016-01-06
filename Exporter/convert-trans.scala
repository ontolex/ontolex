for(line <- io.Source.fromFile("/home/jmccrae/Downloads/Ontolex Translations - Sheet1.csv").getLines.drop(1)) {
  val Array(mod,name,typ,_,en,de,fr,es,it,nl,sv,pt,af,ro) = line.split(",", -1)

  typ match {
    case "c" =>
      println("<owl:Class rdf:about=\"&%s;%s\">" format (mod, name))
    case "o" =>
      println("<owl:ObjectProperty rdf:about=\"&%s;%s\">" format (mod, name))
    case "d" =>
      println("<owl:DatatypeProperty rdf:about=\"&%s;%s\">" format (mod, name))
    case "a" =>
      println("<owl:AnnotationProperty rdf:about=\"&%s;%s\">" format (mod, name))
  }
  println("  <rdfs:label xml:lang=\"de\">" + de + "</rdfs:label>")
  println("  <rdfs:label xml:lang=\"fr\">" + fr + "</rdfs:label>")
  println("  <rdfs:label xml:lang=\"es\">" + es + "</rdfs:label>")
  println("  <rdfs:label xml:lang=\"it\">" + it + "</rdfs:label>")
  println("  <rdfs:label xml:lang=\"nl\">" + nl + "</rdfs:label>")
  if(sv != "") {
    println("  <rdfs:label xml:lang=\"sv\">" + sv + "</rdfs:label>")
  }
  if(pt != "") {
    println("  <rdfs:label xml:lang=\"pt\">" + pt + "</rdfs:label>")
  }
  if(af != "") {
    println("  <rdfs:label xml:lang=\"af\">" + af + "</rdfs:label>")
  }
  if(ro != "") {
    println("  <rdfs:label xml:lang=\"ro\">" + ro + "</rdfs:label>")
  }
  typ match {
    case "c" =>
      println("</owl:Class>")
    case "o" =>
      println("</owl:ObjectProperty>")
    case "d" =>
      println("</owl:DatatypeProperty>")
    case "a" =>
      println("</owl:AnnotationProperty>")
  }
  println()
  println()
}
