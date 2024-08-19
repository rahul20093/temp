import cv2

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg",cv2.IMREAD_COLOR)
img = cv2.resize(img,(500,300))

cv2.imshow("image",img)
