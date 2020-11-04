"""
Install OpenCV:
Write the following into the command prompt:
    pip install opencv-python
    pip install opencv-contrib-python (OPTIONAL)
"""

"""
Read a colored image
Convert it to GrayScale
Save it as JPEG.

functions: cv2.cvtColor(), cv2.imwrite()
"""

import cv2 # import OpenCV
import numpy as np # import Numpy

# reading an image
img_bgr = cv2.imread("lenna.png") # bgr (colored)
img_gray = cv2.imread("lenna.png", cv2.IMREAD_GRAYSCALE) # grayscale

# Grayscale
# showing an image in a windows
cv2.imshow("Colored Image", img_bgr) 
cv2.waitKey() # pausing the windows until a key is pressed

# Colored
# showing an image in a windows
cv2.imshow("Grayscale Image", img_gray) 
cv2.waitKey() # pausing the windows until a key is pressed

# Drawing a line on the image
color = (0,255,0) # green
cv2.line(img_bgr, (0,0),(0,150),color,15)
cv2.imshow("Line on Image", img_bgr)
cv2.waitKey()

# Drawing a rectangle on the image
cv2.rectangle(img_bgr,(15,25),(200,150), color,5)
cv2.imshow("Rectangle on Image", img_bgr)
cv2.waitKey()

# write text on the image
# use: cv2.putText()
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_bgr, 'Hello_Testing', (110,60), font, 2, (200,255,0), 2)

"""
TASK: Read a colored image.
separate B G R channels and show them.
The resulting images will be in shade of gray. What if we want to display these
images with colors? 
"""

red_img = img_bgr
red_img[:,:,0] = 0 # setting Blue channel to zero
red_img[:,:,1] = 0 # setting Green channel to zero
cv2.imshow("red channel only", red_img)
cv2.waitKey()

# printing the pixel values of the image
# print(img)