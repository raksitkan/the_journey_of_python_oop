#Motion Detection
# import cv2
# cap = cv2.VideoCapture("Opencv\image\Walking.mp4")
# check , frame1 = cap.read()#อ่าน2เฟรมเพื่อหาผลต่างเพื่อเช็คว่าวัตถุนั้นเคลื่อนที่
# check , frame2 = cap.read()#จากนั้นนำไปใส่ใน modtiondiff
# while (cap.isOpened()):

#     if check == True:
#         motion_diff = cv2.absdiff(frame1,frame2)
#         gray_video = cv2.cvtColor(motion_diff,cv2.COLOR_BGR2GRAY)
#         blur = cv2.GaussianBlur(gray_video,(5,5),0)
#         thresh,result = cv2.threshold(gray_video,30,255,cv2.THRESH_BINARY)
#         dilation = cv2.dilate(result,None,iterations=3)#iterations(ทำซ้ำ)
#         contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#         cv2.drawContours(frame1,contours,-1,(0,255,0),thickness=2)
#         cv2.imshow("Output",frame1)
#         frame1=frame2
#         check,frame2 = cap.read()
#         if cv2.waitKey(1)&0xFF==ord("e"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows()

#Motion Tracker
import cv2
cap = cv2.VideoCapture("Opencv\image\Walking.mp4")
check , frame1 = cap.read()#อ่าน2เฟรมเพื่อหาผลต่างเพื่อเช็คว่าวัตถุนั้นเคลื่อนที่
check , frame2 = cap.read()#จากนั้นนำไปใส่ใน modtiondiff
while (cap.isOpened()):

    if check == True:
        motion_diff = cv2.absdiff(frame1,frame2)
        gray_video = cv2.cvtColor(motion_diff,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray_video,(5,5),0)
        thresh,result = cv2.threshold(gray_video,30,255,cv2.THRESH_BINARY)
        dilation = cv2.dilate(result,None,iterations=3)#iterations(ทำซ้ำ)
        contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)        
        
        #วาดกล่องสีเหลียม
        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)
            #กำหนดขอบเขตกล่อง
            if cv2.contourArea(contour)<2500:
                continue
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("Output",frame1)
        frame1=frame2
        check,frame2 = cap.read()
        
        if cv2.waitKey(1)&0xFF==ord("e"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
