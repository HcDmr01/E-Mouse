import cv2

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()

    cv2.imshow("Kamera",frame)
    if cv2.waitKey(1)==ord("q"):
        break;

cam.release()
cv2.destroyAllWindows()