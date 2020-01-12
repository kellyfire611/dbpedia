# coding=utf-8
from flask import Flask, render_template, request, make_response

import rdflib.graph as g
app = Flask(__name__, template_folder='templates')
filename = "./data/knowledge_Film.rdf" #replace with something interesting
import rdflib
#import rdfextras
#rdfextras.registerplugins() # so we can Graph.query()
g=rdflib.Graph()
g.parse(filename, format="xml")
g.serialize(format='xml')
@app.route('/')
def index():
  return render_template('timkiemphim.html')
@app.route('/my-link/')
def my_link():
  return "alert('I got clicked!');"
@app.route('/login', methods=['GET', 'POST'])



def login():
   message = None
   if request.method == 'POST':
        cautruyvan = request.form['mydata']
        loaitruyvan = request.form['loaitruyvan']
        keywords = cautruyvan.replace(" ","_")
        if(loaitruyvan == "film"):
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
                  SELECT ?film_title ?movie ?actor
                  where{
                    ?movie a owl-me:Movie;
                    owl-me:has_Name  ?film_title.
                    ?actor a owl-me:Actor.
                    ?movie owl-me:has_Actor  ?actor.
                    filter( regex(lcase(str(?film_title)), lcase(str('"""+keywords+ """')) ))
                    FILTER(langMatches(lang(?film_title), "en"))
                  }
                  ORDER BY(?movie)
                  """) #get every predicate and object about the uri
            ketqua ="<div class='row'>" #<thead><th>Tên Film</th><th>Film</th><th>Diễn viên</th></thead><tbody>"
            for x, y, z in results.result:
                #ketqua += "<tr><td>"+ str(x) +"</td><td>"+ str(y) +"</td><td>"+ str(z) +"</td></tr>"
                ketqua += "<div class='col-md-4'><div class='card'><img src='/static/images/tenfilm.png' class='card-img-top' alt='...'><div class='card-body'><div class='contentHeader'>"+ str(x) +"</div><div class='div_content'>Phim: <a href='" + str(y) + "'>"+ str(y) +"</a><br/>Diễn viên: <a href='" + str(z) + "'>"+ str(z) +"</a></div></div></div></div>"
            #ketqua += "</tbody>"
            ketqua += "</div>"
            resp = make_response(ketqua)
            resp.headers['Content-Type'] = "application/json"
            return resp
        if(loaitruyvan == "country"):
               results1 = g.query("""
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
                  select ?quocgia ?movie ?film_title
                  where{
                    ?movie a owl-me:Movie;
                    owl-me:has_Name  ?film_title;
                    owl-me:made_in ?quocgia.
                    filter( regex(lcase(str(str(?quocgia))), lcase(str('"""+keywords+ """')) ))
                    FILTER(langMatches(lang(?film_title), "en"))
                    }
                  ORDER BY(?movie)
                  """) #get every predicate and object about the uri
               ketqua1 ="<div class='row'>" #<thead><th>Quốc gia</th><th>Film</th><th>Tên Film</th></thead><tbody>"
               for z, y, x in results1.result:
                  #ketqua1 += "<div class='contentHeader'>"+ str(x1) +"</div><div class='div_content'>Phim: <a href='" + str(y1) + "'>"+ str(y1) +"</a><br/>Diễn viên: <a href='" + str(z1) + "'>"+ str(z1) +"</a></div>"
                  ketqua1 += "<div class='col-md-4'><div class='card'><img src='/static/images/quocgia.png' class='card-img-top' alt='...'><div class='card-body'><div class='contentHeader'>"+  str(x) +"</div><div class='div_content'>Tên phim: <a href='" +  str(y) + "'>"+  str(y) +"</a><br/>Quốc gia: <a href='" +  str(z) + "'>"+  str(z) +"</a></div></div></div></div>"
               ketqua1 += "</div>"
               resp = make_response(ketqua1)
               resp.headers['Content-Type'] = "application/json"
               return resp
        if(loaitruyvan == "producer"):
            results2 = g.query("""
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
                  select ?producer ?movie ?film_title
                  where{
                  ?movie a owl-me:Movie;
                  owl-me:has_Name  ?film_title;
                  owl-me:has_Producer  ?producer.
                  filter( regex(lcase(str(str(?producer))), lcase(str('"""+keywords+ """')) ))
                  FILTER(langMatches(lang(?film_title), 'en'))
                  }
                  ORDER BY(?movie)
                  """) #get every predicate and object about the uri
            ketqua2 ="<div class='row'>"#<thead><th>Nhà sản xuất</th><th>Film</th><th>Tên phim</th></thead><tbody>"
            for y, z,x in results2.result:
                #ketqua2 += "<tr><td>"+ str(x2) +"</td><td>"+ str(y2) +"</td><td>"+ str(z2) +"</td></tr>"
                ketqua2 += "<div class='col-md-4'><div class='card'><img src='/static/images/nhasanxuat.png' class='card-img-top' alt='...'><div class='card-body'><div class='contentHeader'>"+ str(x) +"</div><div class='div_content'>Nhà sản xuất: <a href='" + str(y) + "'>"+ str(y) +"</a><br/>Tên phim: <a href='" + str(z) + "'>"+ str(z) +"</a></div></div></div></div>"
            ketqua2 += "</div>"
            resp = make_response(ketqua2)
            resp.headers['Content-Type'] = "application/json"
            return resp

        if(loaitruyvan == "actor"):
            results3 = g.query("""
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
                  select ?film_title ?movie ?actor
                  where{
                    ?movie a owl-me:Movie;
                    owl-me:has_Name  ?film_title.
                    ?actor a owl-me:Actor.
                    ?movie owl-me:has_Actor  ?actor.
                    filter( regex(lcase(str(str(?actor))), lcase(str('"""+keywords+ """')) ))
                    FILTER(langMatches(lang(?film_title), "en"))
                  }
                  ORDER BY(?movie)
                  """) #get every predicate and object about the uri
            ketqua3 ="<div class='row'>"#<thead><th>Tên Film</th><th>Film</th><th>Diễn viên</th><thead><tbody>"
            for x, y, z in results3.result:
                #ketqua3 += "<tr><td>"+ str(x3) +"</td><td>"+ str(z3) +"</td><td>"+ str(y3) +"</td></tr>"
                ketqua3 += "<div class='col-md-4'><div class='card'><img src='/static/images/dienvien.png' class='card-img-top' alt='...'><div class='card-body'><div class='contentHeader'>"+ str(x) +"</div><div class='div_content'>Tên phim: <a href='" + str(y) + "'>"+ str(y) +"</a><br/>Diễn viên: <a href='" + str(z) + "'>"+ str(z) +"</a></div></div></div></div>"
            ketqua3 += "</div>"
            resp = make_response(ketqua3)
            resp.headers['Content-Type'] = "application/json"
            return resp
        if(loaitruyvan == "year"):
            results4 = g.query("""
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
                  select ?namsanxuat ?film_title ?movie
                  where{
                    ?movie a owl-me:Movie;
                    owl-me:has_Name  ?film_title;
                    owl-me:has_Start  ?namsanxuat.
                    filter( regex(lcase(str(?namsanxuat)), lcase(str('"""+keywords+ """')) ))
                    FILTER(langMatches(lang(?film_title), "en"))
                  }
                  ORDER BY(?movie)
                  """) #get every predicate and object about the uri
            ketqua4 ="<div class='row'>"#<thead><th>Năm sản xuất</th><th>Tên Film</th><th>Film</th><thead><tbody>"
            for y, x, z in results4.result:
                #ketqua4 += "<tr><td>"+ str(x4) +"</td><td>"+ str(y4) +"</td><td>"+ str(z4) +"</td></tr>"
                ketqua4 += "<div class='col-md-4'><div class='card'><img src='/static/images/namsanxuat.png' class='card-img-top' alt='...'><div class='card-body'><div class='contentHeader'>"+ str(x) +"</div><div class='div_content'>Năm sản xuất: <a href='" + str(y) + "'>"+ str(y) +"</a><br/>Tên phim: <a href='" + str(z) + "'>"+ str(z) +"</a></div></div></div></div>"
            ketqua4 += "</div>"
            resp = make_response(ketqua4)
            resp.headers['Content-Type'] = "application/json"
            return resp


if __name__ == '__main__':
  app.run(debug=True)