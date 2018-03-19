

# Import OpenCV2 for image processing
# Import os for file path
import cv2,os
import subprocess

# Import numpy for matrix calculation
import numpy as np

# Import Python Image Library (PIL)
from PIL import Image

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.createLBPHFaceRecognizer()
cascadePath = "haarcascade_frontalface_default.xml"

# Using prebuilt frontal face training model, for face detection
faceCascade = cv2.CascadeClassifier(cascadePath);

# Path for retrieval of images
path = 'dataSet'

# Create method to get the images and label data
def get_images_and_labels(path):

     # Get all file path
     image_paths = [os.path.join(path, f) for f in os.listdir(path)]

     # initialize images array that contains the face samples
     images = []
     
     # initialize labels array that will contain the ids/label nos. that are assigned to the images
     labels = []

     # Loop for each of image file paths
     for image_path in image_paths:
          
         # Read the image and convert to grayscale
         image_pil = Image.open(image_path).convert('L')
         
         # Convert the PIL image  into numpy array
         image_numpy = np.array(image_pil, 'uint8')

         # Get the label number of the image
         labelno = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))

         #label=int(''.join(str(ord(c)) for c in nbr))
         print labelno

         # Get a single face from the training images
         faces = faceCascade.detectMultiScale(image_numpy)

         # If face is detected, append the face sample to images array and the label to labels array

         # For each face  
         for (x, y, w, h) in faces:

             # Appending face samples 
             images.append(image_numpy[y: y + h, x: x + w])

             #Appending label nos.
             labels.append(labelno)
             
             cv2.imshow("Adding faces to traning set...", image_numpy[y: y + h, x: x + w])

             cv2.waitKey(10)

     # return the images list and labels list
     return images, labels

#Get the faces and the label nos.
images, labels = get_images_and_labels(path)

#Show the final image
cv2.imshow('test',images[0])

cv2.waitKey(1)

# Train the model using the faces and IDs
recognizer.train(images, np.array(labels))

# Save the model into trainer.yml
recognizer.save('trainer/trainer.yml')

#Close existing windows
cv2.destroyAllWindows()

subprocess.Popen("detector.py",shell =True)
