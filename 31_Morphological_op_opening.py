import cv2
import numpy as np

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

imgResized = cv2.resize(opening, (500,300))
cv2.imshow("opening",imgResized)

