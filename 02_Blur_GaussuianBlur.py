import cv2

path = "C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(31,31),100)

imgResized = cv2.resize(imgBlur, (500,300))
cv2.imshow("Img Blur",imgResized)

