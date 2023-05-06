import cv2 #OpenCV tanýmlandý.

cam = cv2.VideoCapture(0) #kamera tanýmlandý.

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #Face cascade veri seti projeye eklendi.
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # Eye cascade veriseti projeye eklendi.


while True:
    _,frame = cam.read() # Kamera açýldý ve frame deðiþkenine görseller kayýt edilmeye baþlandý.

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #frame deðikenindeki görseller siyah-beyaz görsellere çevrildi.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #gray deðiþkenindeki görseller üzerinde yüz tanýma yapýyor ve yüzün kordinat deðerlerini döndürüyor.

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2) # Belirtilen kordinatlar arasýnda kare oluþturuyor ve bu kareyi frame görselleri üzerine çiziyor.
        face_cam_r = frame[y:y+int(h/2),x:x+int(w/2)] # frame görsellerini belirtilen kordinatlara göre kýrpýyor. sað göz
        face_cam_l = frame[y:y+int(h/2),x+int(w/2):x+w] # frame görsellerini belirtilen kordinatlara göre kýrpýyor. sol göz
        face_cam_gray_r = gray[y:y+int(h/2),x:x+int(w/2)] # gray görsellerini belirtilen kordinatlara göre kýrpýyor. sað göz
        face_cam_gray_l = gray[y:y+int(h/2),x+int(w/2):x+w] # gray görsellerini belirtilen kordinatlara göre kýrpýyor. sol göz

        #r_eyes = eye_cascade.detectMultiScale(face_cam_gray_r)
        #for(r_eye_x, r_eye_y, r_eye_w, r_eye_h) in r_eyes:
        #    cv2.rectangle(face_cam_r,(r_eye_x, r_eye_y), (r_eye_x + r_eye_w, r_eye_y + r_eye_h),(255,0,0),2)
        #    eye_cam_r = face_cam_r[r_eye_y: r_eye_y + r_eye_h, r_eye_x: r_eye_x + r_eye_w]
        
        l_eyes = eye_cascade.detectMultiScale(face_cam_gray_l)
        for(l_eye_x, l_eye_y, l_eye_w, l_eye_h) in l_eyes:
            cv2.rectangle(face_cam_l,(l_eye_x, l_eye_y), (l_eye_x + l_eye_w, l_eye_y + l_eye_h),(255,0,0),2)
            eye_cam_l = face_cam_l[l_eye_y: l_eye_y + l_eye_h, l_eye_x: l_eye_x + l_eye_w]
            eye_cam_l_gray = face_cam_gray_l[l_eye_y: l_eye_y + l_eye_h, l_eye_x: l_eye_x + l_eye_w]
            rs_eye_cam_l_gray = cv2.resize(eye_cam_l_gray,(1280,720))
            rs_eye_cam_l = cv2.resize(eye_cam_l,(1280,720))
            #rs_eye_cam_l_gray = cv2.cvtColor(rs_eye_cam_l, cv2.COLOR_BGR2GRAY)
            rs_eye_cam_l_gray = cv2.GaussianBlur(rs_eye_cam_l_gray, (7, 7), 0)
            rows,cols, _ = rs_eye_cam_l.shape

            _, threshold = cv2.threshold(rs_eye_cam_l_gray, 20, 255, cv2.THRESH_BINARY_INV)
            contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key= lambda x:cv2.contourArea(x), reverse=True)

            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)

                if x<350:
                     cv2.putText(eye_cam_l, "saga bakiyor",(200,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255), 3, cv2.LINE_AA)
                     print("saga bakiyor")
                if x>700:
                     cv2.putText(eye_cam_l, "sola bakiyor",(200,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255), 3, cv2.LINE_AA)
                     print("sola bakiyor")

                #cv2.drawContours(rs_eye_cam_l, [cnt], -1, (0, 0, 255), 3)
                cv2.rectangle(rs_eye_cam_l, (x,y), (x + w, y + h), (0, 0, 255), 2)
                #cv2.line(rs_eye_cam_l, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
                #cv2.line(rs_eye_cam_l, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
                break
            #print("Boy_l: ", l_eye_h)
            #print("en_l: ", l_eye_w)

    #cv2.imshow("Kamera",frame) # frame deðiþkenindeki görselleri ekrana gösteriliyor.
    #cv2.imshow("Kamera",gray) # gray deðiþkenindeki görselleri ekrana gösteriliyor.
    #cv2.imshow("Kamera",face_cam_gray_l) # face_cam deðiþkenindeki görselleri ekrana gösteriliyor.
    cv2.imshow("Kamera",rs_eye_cam_l) # face_cam deðiþkenindeki görselleri ekrana gösteriliyor.
    #cv2.imshow("Kamera",threshold) # face_cam deðiþkenindeki görselleri ekrana gösteriliyor.
    if cv2.waitKey(1)==ord("q"): # 'q' tuþuna basýldýðýnda uygulamadan çýkýþ yapar.
        break;

cam.release()
cv2.destroyAllWindows()