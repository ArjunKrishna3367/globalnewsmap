import flask
from flask import request, jsonify
import sqlite3
import pymongo
from bson.json_util import dumps

app = flask.Flask(__name__)
app.config["DEBUG"] = True
client = pymongo.MongoClient("mongodb://akrishna:akrishna@headlinedata-shard-00-00-slopn.mongodb.net:27017,headlinedata-shard-00-01-slopn.mongodb.net:27017,headlinedata-shard-00-02-slopn.mongodb.net:27017/test?ssl=true&replicaSet=HeadlineData-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
posts = db.posts
headlines = []

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Headlines API</h1>
<p>An API for headlines and associated data.</p>'''


@app.route('/headlines/all', methods=['GET'])
def api_all():
    for post in posts.find():
        headlines.append(post)
    return dumps(headlines)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/headlines', methods=['GET'])
def api_filter():
    query_parameters = request.args

    countryCode = query_parameters.get('countrycode')
    headline = query_parameters.get('headline')
    filter = {}

    if countryCode:
        filter["countrycode"] = countryCode
    if headline:
        filter["headline"] = headline

    for post in posts.find(filter):
        headlines.append(post)
    return dumps(headlines)

app.run()
