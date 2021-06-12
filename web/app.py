from flask import Flask,jsonify,request 
from flask_restful import Api, Resource
import bcrypt
from pymongo import MongoClient 
import requests
import subprocess
import json
import tensorflow as tf
import numpy as np
from flask_cors import CORS, cross_origin
import base64






app = Flask(__name__)
cors =CORS(app,resources={r"/upload":{"origins":"*"}})
app.config['CORS_HEADERS']='Content-Type'










@app.route('/upload',methods=['POST'])
@cross_origin(origin="*",headers=['Content-Type','Authorization'])
def upload_files():
    res = request.files['image']
    print(res.filename)
    res.save('111.png')
    with open("111.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    
    
    
    
    return encoded_string


@app.route('/',methods=['GET'])
def home():
    return "wow"




#api.add_resource(Predict,"/predict")


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
