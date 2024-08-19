import cv2

img = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

sobely = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, 5)

imgResized = cv2.resize(sobely, (500,300))
cv2.imshow("Sobel Y",imgResized)

cv2.waitKey(0)
