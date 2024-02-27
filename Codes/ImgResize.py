"""_summary_
A simple program to resize image in Python.
"""

# Importing necessary libs:
import cv2
import matplotlib.pyplot


def image_resize(desired_height, desired_width):
    # Getting the image path
    path = "D:\FIT\Junior Year\Official classes\SPRING 2024\Image Processing (IPR)\IPR_Assignment 1\Speakers'_Corner,_Singapore_20220218_081547.jpg"

    # Reading the image
    img = cv2.imread(path)
    resized_img= cv2.resize(img, (desired_height, desired_width), fx = 0.1, fy = 0.1)
    
    cv2.imshow("Test",resized_img)
    cv2.waitKey()
    
    
    
   
