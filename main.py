#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------
# Google App Engine Demo
# Playing with Flask in Python
# GET returns number-th position in the container 
# POST appends to the container
# ----------------------------------------------

#START

import os.path
import numpy as np
import cv2
import json
from flask import Flask,request,Response
import uuid
import face_recognition




#function for face compare
def facecompare(img_original,img_capyure):
   #known_image = face_recognition.load_image_file("abhishek.jpeg")
   unknown_image = face_recognition.load_image_file("abhishekk.jpeg")
   biden_encoding = face_recognition.face_encodings(img_original)[0]
   unknown_encoding = face_recognition.face_encodings(img_capyure)[0]
   results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
   data = (results[0])

   return json.dumps(str(data))
  
  

# Api
app = Flask(__name__)

#route http post to this method 
#@app.route('/api/upload', method("POST"))
@app.route('/api/upload',methods=['GET', 'POST'])
def upload():
    # retrive image from client
    img_original = cv2.imdecode(np.frombuffer(request.files['image'].read(),np.uint8),cv2.IMREAD_UNCHANGED)
    img_capyure = cv2.imdecode(np.frombuffer(request.files['image1'].read(),np.uint8),cv2.IMREAD_UNCHANGED)
    # process image
    data_compare = facecompare(img_original,img_capyure)
   
    print("data");
    #response
    return Response(response=data_compare,status=200,mimetype="application/json")

if __name__ == '__main__':
	app.run(debug=True)

