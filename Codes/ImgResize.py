"""_summary_
A simple program to resize image in Python.
"""

# Importing necessary libs:
import cv2
import matplotlib.pyplot


def image_resize(desired_height, desired_width, path_from_user):
    # Getting the image path
    path = path_from_user

    # Reading the image
    img = cv2.imread(path)
    resized_img= cv2.resize(img, (desired_height, desired_width), fx = 0.1, fy = 0.1)
    
    cv2.imshow("Test",resized_img)
    cv2.waitKey()
    
    
    
   
