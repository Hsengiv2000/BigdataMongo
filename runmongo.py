import pymongo
import json as js
from flask import json
from flask_restful import Resource, request, reqparse
from bson.json_util import dumps, default
from random import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["kindle"]
metadata = mydb["metadata"]
#for x in metadata.find({"asin":'B0043M6JJW' }):
 #  print(x)
#print(metadata.find_one()["asin"])
#print(myclient.list_database_names())



import flask
app = flask.Flask(__name__)
@app.route('/' )
def  hello_world():
    return 'Hello World'
@app.route('/<key>/<value>')
def customSearch(key,value):
    temp = []
    #return  value

    for x in metadata.find({key:value}):
        temp.append(x)
    print(len(temp))
    default_overview = 'Overview not available.'
    if len(temp)==0:
        return "NOTAVAILABLE####NOTAVAILABLE####NOTAVAILABLE"
    temp =temp[0]

    jsonstring = js.dumps(temp, default=default)
    data = json.loads(jsonstring)
    try:
        image = data['imUrl']
    except:
        image = "NOIMAGE"
    print(data)
    try:
        overview = data['description']
    except:
        overview = "NOOVERVIEW"
    try:
        ab = data['related']['also_bought']
        print(ab)
    except:
        ab = "NOALSOBOUGHT"
    print(image, overview)
    return (image  +"####" + overview+"####"+str(ab))
    #except:
     #   return {"Message": "Failed to retrieve data"}, 500

if __name__ == "__main__":
    app.run(host = '0.0.0.0' , port=3306)
