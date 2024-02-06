#libraries that needed in this code 
import mediapipe as mp
import cv2 

#mediapipe components
mp_drawing_styles = mp.solutions.drawing_styles
mp_drawing = mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

#this is the webcam 
cap = cv2.VideoCapture(0)

#its code track the hand 
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
     
     #this code will open the webcam 
    while cap.isOpened():

        #this variable represent the image from the webcam
          ret, frame = cap.read()

        #detections of the image
          image= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #set flags to {false}
          image.flags.writeable = False

          #detections of the image
          results = hands.process(image)

        #set flag ro {true}
          image.flags.writeable = True 

        #RGB 2 GBR this code converts to each other
          image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

          #detections of the image
          print(results)