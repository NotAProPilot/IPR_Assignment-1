"""_summary_
A simple program to resize image in Python.
"""

# Importing necessary libs:
import cv2
import matplotlib.pyplot


def resize_size():
    # Get the desired height from user via GUI
    # Surround this block of code around a try - catch invalid number (float, negative integer, not number)
    
    # Starting import GUI now (otherwise it will cause a "circular import error")
    import Codes.ImageResizeActivity.GUI as GUI
    
    desired_height = int(GUI.height.get())
    desired_width = int(GUI.width.get())
    
    
    return desired_height, desired_width
        
    

def image_resize(desired_height, desired_width):
    # Getting the image path
    path = "D:\FIT\Junior Year\Official classes\SPRING 2024\Image Processing (IPR)\IPR_Assignment 1\Speakers'_Corner,_Singapore_20220218_081547.jpg"
    
    # Reading the image
    img = cv2.imread(path)
    
    # Actually resize the image
    resize_img = cv2.resize(img, (desired_height, desired_width), -0.1, -0.1)
    
    # Show the image
    cv2.imshow("Test", resize_img)
    cv2.waitKey()
   
