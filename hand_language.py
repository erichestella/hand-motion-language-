#libraries that needed in this code 
import mediapipe as mp
import cv2 

#mediapipe components
mp_drawing_styles = mp.solutions.drawing_styles
mp_drawing = mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

#this is the webcam 
cap = cv2.VideoCapture(0)