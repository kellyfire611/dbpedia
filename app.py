import os
import pprint
import sys
from flask import Flask, url_for, render_template, request, Response, flash, redirect, abort, send_from_directory, json
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def main():
    message = "Hello world!"
    return render_template('index.html', message = message)

@app.route('/runQuery', methods=['POST'])
def run_query():
    # pprint.pprint(request)
    # sys.exit()

    _graphURI = request.form['inputGraphURI']
    _queryText = request.form['inputQuery']

    pprint.pprint(_graphURI)
    pprint.pprint(_queryText)

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")

    sparql.addDefaultGraph(_graphURI)
    sparql.setQuery(_queryText)

    sparql.setReturnFormat(JSON)
    results = sparql.query()
    
    results = results.convert()
    return json.dumps(results)

if __name__ == "__main__":
    app.run()