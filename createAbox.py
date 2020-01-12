# coding=utf-8
import logging
import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON, XML
from rdflib import ConjunctiveGraph
from rdflib import Namespace, BNode, Literal, RDF
#import rdfextras
from rdflib.namespace import DC, FOAF
#rdfextras.registerplugins() # so we can Graph.query()
owlNS = Namespace("http://www.w3.org/2002/07/owl#")
owlClass = owlNS["Class"]
owlObjectProperty = owlNS["ObjectProperty"]
owlDatatypeProperty = owlNS["DatatypeProperty"]
rdfNS = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfProperty = rdfNS["Property"]
rdfType = rdfNS["type"]
rdfsNS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
rdfsSubClassOf = rdfsNS["subClassOf"]
rdfsDomain = rdfsNS["domain"]
rdfsRange = rdfsNS["range"]
graph = ConjunctiveGraph()
graph.load("./data/Film_Tbox.owl")

s=graph.serialize(format='n3')
#print(s)
#print("graph has %s statements." % len(graph))


def isSubClassOf(subClass, superClass, graph):
    if subClass == superClass: return True
    for parentClass in graph.objects(subClass, rdfsSubClassOf):
        if isSubClassOf(parentClass, superClass, graph):
            return True
        else:
            return False


#in danh sach tat cac ca class trong file owl
print(list(graph.subjects(rdfType, owlClass)))
#in dan hsach tat ca cac thuoc tinh trong file owl
print(list(graph.subjects(rdfType, owlObjectProperty)))
#in danh sach ca data property

# list(graph.subjects(rdfType, owlObjectProperty))
#define a blank node
performance = BNode('_:perf1')
#dinh nghia du lieu dang triples


def TruyVan(query, graph, instances =None):
    if instances is None: instances = set()
    for instance in graph.subjects(rdfType, query): instances.add(instance)
    for subClass in graph.subjects(rdfsSubClassOf, query):
        TruyVan(subClass, graph, instances)
    return instances

#print(TruyVan(personClass, graph))
sparql = SPARQLWrapper('http://dbpedia.org/sparql')
sparql.setQuery("""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dbpedia2: <http://dbpedia.org/property/>
PREFIX dbpedia: <http://dbpedia.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl-db: <http://dbpedia.org/ontology/>
PREFIX owl-me: <http://www.semprog.com/film#>

CONSTRUCT {
?movies owl-me:has_Actor  ?actor.
?movies owl-me:has_Name  ?film_title.
?movies owl-me:has_Award  ?giaithuong.
?movies owl-me:has_Director  ?director.
?movies owl-me:has_Images ?anh.
?movies owl-me:made_in ?quocgia.
?movies owl-me:TypeFilm  ?theloaiphim.
?movies owl-me:has_Start  ?start.
?movies owl-me:has_Producer ?producer.
?movies owl-me:has_Language ?ngonngu.
?movies  a owl-me:Movie.
?quocgia  a owl-me:Country.
?actor a owl-me:Actor.
?director a owl-me:Director.

}
WHERE
{
?movies  a  owl-db:Film;
rdfs:label ?film_title;
?rel1 ?quocgia.
?quocgia a <http://schema.org/Country>.
?movies dbpedia2:starring ?actor.
?actor foaf:name ?actorname.
?movies <http://dbpedia.org/ontology/releaseDate> ?start.
?movies dbpedia2:director ?director.
 ?director foaf:name ?directorname.
?movies dbpedia2:genre  ?theloaiphim.
?movies dbpedia2:distributor ?producer.

OPTIONAL{
?movies dbpedia2:award ?giaithuong;
 dbpedia2:language ?ngonngu.
 ?director foaf:depiction ?anh.
}
FILTER(!isLiteral(?film_title) || langMatches(lang(?film_title), "EN"))

}
ORDER BY(?quocgia  )
""")

sparql.setReturnFormat(XML)
results = sparql.query().convert()
#Print all statements in dataGraph
for stmt in results:
    graph.add(stmt)
# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in graph:
    print((s.encode("utf-8", errors='replace'), p.encode("utf-8", errors='replace'), o.encode("utf-8", errors='replace')))

# For each foaf:Person in the store print out its mbox property.
# Bind a few prefix, namespace pairs for more readable output
graph.bind("dc", DC)
graph.bind("foaf", FOAF)

#print( graph.serialize(format='n3'))
print(len(graph))
#xuat du lieu ra file
file = open("./data/knowledge_Film.owl", "ab")
file.write(graph.serialize(format='pretty-xml'))


