# coding=utf-8
import rdflib.graph as g
filename = "C:/python_project/project1/data/knowledge_Film.rdf" #replace with something interesting
import rdflib
import rdfextras
rdfextras.registerplugins() # so we can Graph.query()
g=rdflib.Graph()
g.parse(filename, format="xml")
g.serialize(format='xml')
results = g.query("""
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
PREFIX mysource: <http://dbpedia.org/resource/>

select distinct  *
where{
?movie a owl-me:Movie;
owl-me:has_Name  ?film_title;
owl-me:has_Producer  ?producer.
filter( regex(lcase(str(str(?producer))), lcase(str("columbia_picture")) ))
FILTER(langMatches(lang(?film_title), "en"))
}
ORDER BY(?movie)




""") #get every predicate and object about the uri

for x, y, z  in results.result:
        print( x,y.encode("utf-8", errors='replace'),z.encode("utf-8", errors='replace'))

#file = open("C:/python_project/project1/data/final.txt", "ab")
#file.write(results)
