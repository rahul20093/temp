import cv2

path = "C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
img =cv2.imread(path)

imgCanny = cv2.Canny(img,200,200)
 
imgResized = cv2.resize(imgCanny, (500,300))
cv2.imshow("Img Canny",imgResized)

