import cv2

path = "C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

 
imgResized = cv2.resize(imgGray, (500,300))
cv2.imshow("Grayscale",imgResized)


