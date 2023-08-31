import cv2
fd=cv2.CascadeClassifier(cv2.data.haarcascades+ "haarcascade_frontalface_defualt.xml")
#video read using web cam
vid = cv2.VideoCapture(0)
# mai loop t read andshow image until we break the loop 
while True:
    flag,img = vid.read()
    img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #th,img =cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)

    # if flag  is true then only show image
    if flag:
        faces = fd.detectMultiScale(img,1.1,5)
        for x,y,w,h in faces:
          
        # draw a rectange on image 
           cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color =(255,0,0), thickness=1)
        cv2.imshow("webcam_image",img)
        key=cv2.waitKey(1)
        if key == ord("t"):
            break
    else:
        break
cv2.destroyAllWindows()
vid.release( )

    