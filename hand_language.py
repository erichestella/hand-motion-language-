#libraries that needed in this code 
import mediapipe as mp
import cv2 
import os
import uuid

#mediapipe components
mp_drawing_styles = mp.solutions.drawing_styles
mp_drawing = mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

#this is the webcam 
cap = cv2.VideoCapture(0)

#its code track the hand 
with mp_hands.Hands(min_detection_confidence=0.8, 
                    min_tracking_confidence=0.5) as hands:
     
     #this code will open the webcam 
    while cap.isOpened():

        #this variable represent the image from the webcam
          ret, frame = cap.read()

        #detections of the image
          image= cv2.cvtColor(frame, 
                              cv2.COLOR_BGR2RGB)

        #set flags to {false}
          image.flags.writeable = False

          #detections of the image
          results = hands.process(image)

        #set flag ro {true}
          image.flags.writeable = True 

        #RGB 2 GBR this code converts to each other
          image = cv2.cvtColor(image, 
                               cv2.COLOR_RGB2BGR)

          #detections of the image
          print(results)

          # it performs the lines of the hands 
          if results.multi_hand_landmarks:
             for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

                  #save images
          cv2.imwrite(os.path.join('Pictures taken by the code',
                                   '{}.jpg'.format(uuid.uuid1())), 
                                   image)


#this code create a window for the images
          cv2.imshow('HAND GESTURE (FINAL PROJECT)', 
                     cv2.flip(image, 
                              1))  

#this code performs for closing the window
          if cv2.waitKey(10) & 0xFF == ord('q'):
             break
cap.release()
cv2.destroyAllWindows()


#https://youtu.be/vQZ4IvB07ec?si=CabA7CF5N9apyKGN from Nicholas Renotte (dito ako nagbase sa code niya)

#https://youtu.be/a99p_fAr6e4?si=BXAoI-eBfdHw7DWb from Ivan Goncharov (dito naman, ginaya ko yung coordinates niya or hand land marks)
