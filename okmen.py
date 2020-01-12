from argparse import Namespace
import rdflib
raw_data = """<?xml version="1.0"?>
<rdf:RDF
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:dbp="http://dbpedia.org/ontology/"
xmlns:dbprop="http://dbpedia.org/property/"
xmlns:foaf="http://xmlns.com/foaf/0.1/">
    <rdf:Description rdf:about="http://dbpedia.org/page/Johann_Sebastian_Bach">
      <dbp:birthDate>1685-03-21</dbp:birthDate>
      <dbp:deathDate>1750-07-28</dbp:deathDate>
      <dbp:birthPlace>Eisenach</dbp:birthPlace>
      <dbp:deathPlace>Leipzig</dbp:deathPlace>
      <dbprop:shortDescription>German composer and organist</dbprop:shortDescription>
      <foaf:name>Johann Sebastian Bach</foaf:name>
      <rdf:type rdf:resource="http://dbpedia.org/class/yago/GermanComposers"/>
      <rdf:type rdf:resource="http://xmlns.com/foaf/0.1/Person"/>
    </rdf:Description>
</rdf:RDF>"""
import rdflib
graph = rdflib.Graph()
graph.parse(data=raw_data)

output = []

for s, p, o in graph:
    if type(o) == rdflib.term.Literal:
        output.append(o.toPython())

print (', '.join(output))
qres = graph.query(
    """SELECT *
       WHERE {
          ?a ?m ?b .

       }""",
    initNs=dict(
        foaf=Namespace("http://xmlns.com/foaf/0.1/")))

for row in qres.result:
    print("%s" % row)
