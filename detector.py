##################################
#                                #
# Code modified by Ritwik Brahma #
#                                #  
################################## 

# Import OpenCV2 for image processing and os for file path
import cv2,os
import sqlite3

# Import numpy for matrices calculations
import numpy as np

#Import image from python image library
from PIL import Image 

#For Object Serialization
import pickle

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.createLBPHFaceRecognizer()

# Load the trained mode
recognizer.load('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the path
path = 'dataSet'

def getProfile(id):
    conn = sqlite3.connect("FaceBase1.db")
    cmd = "SELECT * FROM People WHERE ID="+str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Set the font style
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) 

# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all faces from the video frame
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # For each face in faces
    for(x,y,w,h) in faces:

        # Recognize the face belongs to which ID
        id_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])

        # Create rectangle around the face
        cv2.rectangle(im,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),4)
        # Check the ID if exist 
        profile = getProfile(id_predicted)
        if(profile!=None):
            cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[1]), (x,y+h+60),font, (0,255,0))
            #cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[2]), (x,y+h+60),font, (0,255,0))
            #cv2.cv.PutText(cv2.cv.fromarray(im),str(profile[3]), (x,y+h+90),font, (0,255,0))

        #Display the video frame with bounded rectangle
        cv2.imshow('Recognizer',im)
        
        cv2.waitKey(10)
