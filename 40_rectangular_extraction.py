import cv2

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
x, y = 100, 100
width, height = 500, 350
roi = img[y:y+height, x:x+width]

imgResized = cv2.resize(roi, (500,300))
cv2.imshow("ROI",imgResized)
