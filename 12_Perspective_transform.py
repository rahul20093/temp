import cv2
import numpy as np

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")

rows,cols,_ = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,50],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cols, rows))


imgResized = cv2.resize(dst, (500,300))
cv2.imshow("Transformed Image",imgResized)

