import cv2


img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

edges = cv2.Canny(img_blur,100,200)

imgResized = cv2.resize(edges, (500,300))

cv2.imshow("Canny Edge Detection",imgResized)
