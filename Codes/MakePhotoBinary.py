# Importing the necessary libraries

import random                       # To randomly set a threshold
import cv2                          # To read image
import matplotlib.pyplot as plt     # To display images in semi-GUI fashion
import os                           # To get the current directory (to save the photo)
from PIL import Image               # To save
import numpy

"""
The function to load an image and convert it to greyscale
"""
def loadGrayScale():
    # Image path
    img_path = r"D:\FIT\Junior Year\Official classes\SPRING 2024\Image Processing (IPR)\IPR_PythonFile\Tut2\Exercises\taylor-swift-eras-tour-081023-3-3411bb8115944906a22fa9d1b7239d13.jpg"

    # Convert image to greyscale
    black_and_white_img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)

    # Return the greyscale image
    return black_and_white_img

"""
The function to display the greyscale image
"""
def displayBlackAndWhite(black_and_white_img):
    plt.imshow(black_and_white_img,cmap='gray')

    # Display title and show the photo
    plt.title("Greyscale Image")
    plt.show()

"""
The function to set global threshold
"""
def globalThreshold(black_and_white_img):
    # The threshold value can be adjusted
    # Here we pick the average of 0 and 255:
    thresholdValue = numpy.average([0,255])

    # Convert the image into binary image
    _, binaryImage = cv2.threshold(black_and_white_img, thresholdValue, 255, cv2.THRESH_BINARY)

    # Return the binary image
    return binaryImage

"""
The function to display the binary image
"""
def showImageUsingMathPlot(binaryImage):
    plt.imshow(binaryImage,cmap="grey")

    # Display the title and show the photo
    plt.title("Binary Image")
    plt.show()

"""
Invoking functions
"""

# Call the loadGreyScale method and display greyscale image
black_and_white_img = loadGrayScale()
displayBlackAndWhite(black_and_white_img)

# Call the globalThreshold method and display binary image
binaryImageDisplay = globalThreshold(black_and_white_img)
showImageUsingMathPlot(binaryImageDisplay)

