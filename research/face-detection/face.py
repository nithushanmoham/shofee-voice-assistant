import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _ret, img = cap.read()

    if _ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow('img', img)
            
        k = cv2.waitKey(1) & 0xff
        if k==27:
                break
    
cap.release()