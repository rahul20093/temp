import cv2

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

sobelx = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, 5)

imgResized = cv2.resize(sobelx, (500,300))

cv2.imshow("Sobel X",imgResized)
