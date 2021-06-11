from flask import Flask,jsonify,request 
from flask_restful import Api, Resource
import bcrypt
from pymongo import MongoClient 
import requests
import subprocess
import json
import tensorflow as tf
import numpy as np






app = Flask(__name__)
api = Api(app)






#Mongo DataBase
client = MongoClient("mongodb://db:27017")
db = client.ImageRecognition
users = db['users']


#Load Model
model = tf.keras.models.load_model('./monkey_model.h5')

#predict function
def predict_monkey(url):
  monkeys = ["mantled_howler ","patas_monkey","bald_uakari","japanese_macaque","pygmy_marmoset ",
                      "white_headed_capuchin","silvery_marmoset","common_squirrel_monkey","black_headed_night_monkey",
                      "nilgiri_langur"]
  response = requests.get(url)

  file = open("monkey1", "wb")
  file.write(response.content)
  file.close()
  img = tf.keras.preprocessing.image.load_img("monkey1", target_size=(244, 244))

  img_array = tf.keras.preprocessing.image.img_to_array(img)
  img_array = img_array/255.
  img_array = tf.expand_dims(img_array, 0) 

  predictions = model.predict(img_array)
  score = tf.nn.softmax(predictions[0])
  
  return monkeys[np.argmax(score)]

'''
example
predict_monkey("https://i.pinimg.com/originals/ea/1d/74/ea1d74d74a061086efb6cf5cb8bd6576.jpg")'''




class Predict(Resource):
    def post(self):
        data= request.get_json()
        url = data['url']
        prediction = predict_monkey(url)

        
        return jsonify({"statues":200,"type":prediction})








api.add_resource(Predict,"/predict")


if __name__=='__main__':
    app.run(host='0.0.0.0')