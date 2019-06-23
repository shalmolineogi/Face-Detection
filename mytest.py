import face_recognition
import cv2
import numpy as np
import os
from PIL import Image

data=cv2.imread("pics",-1)


my_face_encoding = {"trc":my_face_encoding1,"sarba":my_face_encoding2,"shuva":my_face_encoding3,"Shalmoli":my_face_encoding4}
face_locations = []
face_encodings = []
face_names = []

#taking and encoding the actual data with unknown face:
image = face_recognition.load_image_file("data.jpg")
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

#search for match:
for face_encoding in face_encodings:
    for k,q in my_face_encoding.items():
        x = face_recognition.compare_faces([q], face_encoding,0.5)[0]
        if x:
            face_names.append(k)
            break
    if not(x):
        face_names.append("Unknown")
        
#for making the box around the face:
for (top,right,bottom,left),name in zip(face_locations, face_names):
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#show final image with unknown faces and known faces:
cv2.imshow('image',image)
