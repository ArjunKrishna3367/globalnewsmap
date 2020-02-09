import requests
import json
import time
import pprint
import pymongo as pymongo
from GlobalRelevance import getscores



# Number of Articles to Scrape
numberOfArticles = 100

# URL to Scrape
url = "https://in.reuters.com/assets/jsonWireNews?limit=" + str(numberOfArticles)

# Create MongoDB
if __name__ == '__main__':
    client = pymongo.MongoClient(
        "mongodb://akrishna:akrishna@headlinedata-shard-00-00-slopn.mongodb.net:27017,headlinedata-shard-00-01-slopn.mongodb.net:27017,headlinedata-shard-00-02-slopn.mongodb.net:27017/test?ssl=true&replicaSet=HeadlineData-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.test
    collection = db.test_collection
    print(db)
    posts = db.posts
    # posts.delete_many({})



request1 = requests.get(url)
dataPage = request1.content

# Parse JSON
parsed_json = (json.loads(dataPage))
for i in range(0, numberOfArticles):
    headline = parsed_json['headlines'][i]['headline']
    dateMillis = parsed_json['headlines'][i]['dateMillis']
    url = str('https://in.reuters.com/') + parsed_json['headlines'][i]['url']
    countries, relevant, relevance, objectivity = getscores(headline)
    # Push to MongoDB
    post = {"headline": headline,
            "dataMillis": dateMillis,
            # "url": url
            "countries": countries,
            "relevant": relevant,
            "rel_score": relevance,
            "obj_score": objectivity
    }
    # posts = db.posts_test
    try:
        post_id = posts.insert_one(post).inserted_id
    except:
        print('duplicate')

    # print(pprint.pprint(posts.find_one()))
    # print(pprint.pprint(posts.find_one({"_id": post_id})))
    # print(post_id)
