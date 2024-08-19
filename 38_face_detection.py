import cv2

img = cv2.imread("C:/Users/Rahul/OneDrive/Desktop/work/opencv/pic.png")



face_cascade = cv2.CascadeClassifier("C:/Users/Rahul/Downloads/facedet.xml")

faces = face_cascade.detectMultiScale(img, 1.1,5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

imgRes = cv2.resize(img, (500,300))
cv2.imshow("Eyes Detected",imgRes)
