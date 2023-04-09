import cv2 #OpenCV tanýmlandý

cam = cv2.VideoCapture(0) #kamera tanýmlandý

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #Face cascade veri seti projeye eklendi
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # Eye cascade veriseti projeye eklendi

while True:
    _,frame = cam.read() # Kamera açýldý ve frame deðiþkenine görseller kayýt edilmeye baþlandý.

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #frame deðikenindeki görseller siyah-beyaz görsellere çevrildi
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #gray deðiþkenindeki görseller üzerinde yüz tanýma yapýyor ve yüzün kordinat deðerlerini döndürüyor.

    for (x,y,w,h) in faces:
        #cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2) # Belirtilen kordinatlar arasýnda kare oluþturuyor ve bu kareyi frame görselleri üzerine çiziyor.
        face_cam = frame[y:y+h,x:x+w]

    #cv2.imshow("Kamera",frame) # frame deðiþkenindeki görseller ekrana gösteriliyor
    #cv2.imshow("Kamera",gray) # gray deðiþkenindeki görseller ekrana gösteriliyor
    cv2.imshow("Kamera",face_cam) # gray deðiþkenindeki görseller ekrana gösteriliyor
    if cv2.waitKey(1)==ord("q"): # 'q' tuþuna basýldýðýnda uygulamadan çýkýþ yapar.
        break;

cam.release()
cv2.destroyAllWindows()