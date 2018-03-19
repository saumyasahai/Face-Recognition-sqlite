"""import cv2
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);

while(True):
    ret,img = cam.read();
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows() """


##################################
#                                #
# Code modified by Ritwik Brahma #
#                                #  
#################################


#import OpenCV2 for image processing
import cv2

#start capturing video on webcam
cam = cv2.VideoCapture(0)

#detect face in video stream using Haarcascade Frontal Face 
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#set counter for no. of sample images
i = 0

#variable offset
offset = 50

#Raw input: Enter the id of the user
name = raw_input('Enter your id: ')

#Start looping
while True:
    #Capture a video frame
    ret, im = cam.read()
    #Convert the video frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #Detect face frames in thr captured video frame
    faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    #For each face frame detected loop
    for(x,y,w,h) in faces:
        #increment sample no. by 1
        i=i+1
        #save the captured face image in the datasets folder
        cv2.imwrite("dataSet/face-"+name +'.'+ str(i) + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        #Draw a rectangle around the face image 
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        #Display the video frame with a bounded rectangle on the person
        cv2.imshow('Creating the Dataset',im[y-offset:y+h+offset,x-offset:x+w+offset])
        #Time gap between each image taken is 100ms
        cv2.waitKey(100)
        #If no. of sample images is greater than 20, then stop
    if i>20:
        cam.release()
        cv2.destroyAllWindows()
        break
