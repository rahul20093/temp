import cv2
import numpy as np

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg", cv2.IMREAD_GRAYSCALE)

dx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1)

edges = cv2.magnitude(dx, dy)

thresh = 100

edges[edges < thresh] = 0
edges[edges >= thresh] = 255

imgResized = cv2.resize(edges, (500,300))
cv2.imshow("Edges",imgResized)
