import cv2
import numpy as np

image = cv2.imread("C:/Users/Rahul/Pictures/wallpapers/oppie.jpg")
img2 = cv2.imread("C:/Users/Rahul/Downloads/logo.png")
print(image.shape) # Print image shape

imgResized = cv2.resize(image, (500,300))
cv2.imshow("original",imgResized)


imageCopy = image.copy()
cv2.circle(imageCopy, (100, 100), 30, (255, 0, 0), -1)

imgResized = cv2.resize(image, (500,300))
cv2.imshow("image",imgResized)

imgResized = cv2.resize(imageCopy, (500,300))
cv2.imshow("image copy",imgResized)

cropped_image = image[80:280, 150:330]

imgResized = cv2.resize(cropped_image, (500,300))
cv2.imshow("cropped",imgResized)

cv2.imwrite("Cropped Image.jpg", cropped_image)
dst = cv2.addWeighted(image, 0.5, img2, 0.7, 0)
img_arr = np.hstack((image, img2))

imgResized = cv2.resize(img_arr, (500,300))
cv2.imshow("Input Images",imgResized)

imgResized = cv2.resize(dst, (500,300))
cv2.imshow("Blended Image",imgResized)
