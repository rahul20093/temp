import cv2
path ="C:/Users/Rahul/Pictures/wallpapers/oppie.jpg"
img = cv2.imread(path)
rotate = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

imgResized = cv2.resize(rotate,(500,500))
cv2.imshow("Image",imgResized)

