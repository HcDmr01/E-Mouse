import cv2 #OpenCV tanımlandı.

cam = cv2.VideoCapture(0) #kamera tanımlandı.

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #Face cascade veri seti projeye eklendi.
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # Eye cascade veriseti projeye eklendi.

while True:
    _,frame = cam.read() # Kamera açıldı ve frame değişkenine görseller kayıt edilmeye başlandı.

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #frame değikenindeki görseller siyah-beyaz görsellere çevrildi.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #gray değişkenindeki görseller üzerinde yüz tanıma yapıyor ve yüzün kordinat değerlerini döndürüyor.

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2) # Belirtilen kordinatlar arasında kare oluşturuyor ve bu kareyi frame görselleri üzerine çiziyor.
        face_cam = frame[y:y+h-50,x:x+w] # frame görsellerini belirtilen kordinatlara göre kırpıyor.
        face_cam_gray = gray[y:y+h,x:x+w] # gray görsellerini belirtilen kordinatlara göre kırpıyor.

        eyes = eye_cascade.detectMultiScale(face_cam_gray)
        for(eye_x, eye_y, eye_w, eye_h) in eyes:
            cv2.rectangle(face_cam,(eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h),(255,0,0),2)
            eye_cam = face_cam[eye_y: eye_y + eye_h, eye_x: eye_x + eye_w]

    cv2.imshow("Kamera",frame) # frame değişkenindeki görselleri ekrana gösteriliyor.
    #cv2.imshow("Kamera",gray) # gray değişkenindeki görselleri ekrana gösteriliyor.
    #cv2.imshow("Kamera",face_cam) # face_cam değişkenindeki görselleri ekrana gösteriliyor.
    #cv2.imshow("Kamera",eye_cam) # face_cam değişkenindeki görselleri ekrana gösteriliyor.
    if cv2.waitKey(1)==ord("q"): # 'q' tuşuna basıldığında uygulamadan çıkış yapar.
        break;

cam.release()
cv2.destroyAllWindows()