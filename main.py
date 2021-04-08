import cv2
import numpy as np
import time
import random
from generate_templates import get_templates
from matching import match
from generate_boxes import get_random_boxes
import argparse
import sys


camera_url = 0

cap = cv2.VideoCapture(camera_url)


time.sleep(1)
ret , frame = cap.read()
print(ret)
points = get_random_boxes(500,frame)
print("Boxes Calculated")
temp_images = get_templates(frame , points,20)
print("Templates Generted")
while cap.isOpened():
    frame_available , frame = cap.read()
    if frame_available:
        frame_template = get_templates(frame , points,20)
        index = match(frame_template,temp_images)/2
        if  index < 10 :
            print("Camera Tempered ",index)
            
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    else:
        print("[Error] NO frame Available")


cap.release()
