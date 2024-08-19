import cv2
path ="C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
src = cv2.imread(path)
image = cv2.rotate(src, cv2.ROTATE_180)

imgResized = cv2.resize(image, (500,300))
cv2.imshow("Image",imgResized)
cv2.waitKey(0)
