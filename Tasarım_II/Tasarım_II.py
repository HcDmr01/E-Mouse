import cv2

cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    _,frame = cam.read()

    cv2.imshow("Kamera",frame)
    if cv2.waitKey(1)==ord("q"):
        break;

cam.release()
cv2.destroyAllWindows()