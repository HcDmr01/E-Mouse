import cv2 #OpenCV tan�mland�.

cam = cv2.VideoCapture(0) #kamera tan�mland�.

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #Face cascade veri seti projeye eklendi.
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # Eye cascade veriseti projeye eklendi.

while True:
    _,frame = cam.read() # Kamera a��ld� ve frame de�i�kenine g�rseller kay�t edilmeye ba�land�.

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #frame de�ikenindeki g�rseller siyah-beyaz g�rsellere �evrildi.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #gray de�i�kenindeki g�rseller �zerinde y�z tan�ma yap�yor ve y�z�n kordinat de�erlerini d�nd�r�yor.

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2) # Belirtilen kordinatlar aras�nda kare olu�turuyor ve bu kareyi frame g�rselleri �zerine �iziyor.
        face_cam = frame[y:y+h-50,x:x+w] # frame g�rsellerini belirtilen kordinatlara g�re k�rp�yor.
        face_cam_gray = gray[y:y+h,x:x+w] # gray g�rsellerini belirtilen kordinatlara g�re k�rp�yor.

        eyes = eye_cascade.detectMultiScale(face_cam_gray)
        for(eye_x, eye_y, eye_w, eye_h) in eyes:
            cv2.rectangle(face_cam,(eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h),(255,0,0),2)
            eye_cam = face_cam[eye_y: eye_y + eye_h, eye_x: eye_x + eye_w]

    cv2.imshow("Kamera",frame) # frame de�i�kenindeki g�rselleri ekrana g�steriliyor.
    #cv2.imshow("Kamera",gray) # gray de�i�kenindeki g�rselleri ekrana g�steriliyor.
    #cv2.imshow("Kamera",face_cam) # face_cam de�i�kenindeki g�rselleri ekrana g�steriliyor.
    #cv2.imshow("Kamera",eye_cam) # face_cam de�i�kenindeki g�rselleri ekrana g�steriliyor.
    if cv2.waitKey(1)==ord("q"): # 'q' tu�una bas�ld���nda uygulamadan ��k�� yapar.
        break;

cam.release()
cv2.destroyAllWindows()