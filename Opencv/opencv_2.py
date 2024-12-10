#ตรวจจับดวงตาและใบหน้าใน video
import cv2
import numpy as np
#ค้าหาสีในภาพและลบสีอื่นออก
# import cv2
# import numpy as np

# while True :
#     img = cv2.imread("Opencv\image\m&m.jpeg")
#     img = cv2.resize(img,(400,400))
#     #BGR
#     upper = np.array([156,227,166])#ช่วงสีเข้ม B,G,R
#     lower = np.array([1, 155, 50])#ช่วงสีอ่อน B,G,R
#     mask = cv2.inRange(img,lower,upper)#ค้าหาช่วงสีในรูปภาพ ระหว่าง ช่วงสีอ่อน - สีเข้ม
#     if cv2.waitKey(0) & 0xFF == ord("e"):
#         break
#     cv2.imshow("original",img)
#     cv2.imshow("Mask",mask)
    
# cv2.destroyAllWindows()

#นำสีไปแปะใน mask
# import cv2
# import numpy as np

# while True :
#     img = cv2.imread("Opencv\image\m&m.jpeg")
#     img = cv2.resize(img,(400,400))
#     #BGR
#     upper = np.array([156,227,166])#ช่วงสีเข้ม B,G,R
#     lower = np.array([1, 155, 50])#ช่วงสีอ่อน B,G,R
#     mask = cv2.inRange(img,lower,upper)#ค้าหาช่วงสีในรูปภาพ ระหว่าง ช่วงสีอ่อน - สีเข้ม
#     #นำสีต้นแบบไปแทนที่พื้นที่สีขาว
#     result = cv2.bitwise_and(img,img,mask=mask)
#     if cv2.waitKey(0) & 0xFF == ord("e"):
#         break
#     cv2.imshow("original",img)
#     cv2.imshow("Mask",mask)
#     cv2.imshow("result",result)
    
# cv2.destroyAllWindows()

#ตรวจจับใบหน้า
# import cv2
# import numpy as np
# img = cv2.imread("Opencv\image\jenna.jpg")
# img = cv2.resize(img,(800,800))

# #อ่านไฟล์สำหรับแยก classification
# face_cascade = cv2.CascadeClassifier("Opencv\Detect\haarcascade_frontalface_default.xml")
# #convert img to gray img
# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #classification face
# scaleFactor = 1.1 # ค่าเริ่มต้น
# minNeighbors = 4 # ค่าตรวจสอบ grayscale
# face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbors)
# #แสดงตำแหน่งใบหน้า
# #x,y จุดเริ่มต้น
# #w,h จุดสุดท้าย
# for (x,y,w,h) in face_detect:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)


# cv2.imshow("original",img)
# # cv2.imshow("result",gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#ตรวจจับใบหน้าใน video
# import cv2
# import numpy as np
# # open video
# cap = cv2.VideoCapture("Opencv\image\Johnnydepp.mp4")
# #อ่านไฟล์สำหรับแยก classification
# face_cascade = cv2.CascadeClassifier("Opencv\Detect\haarcascade_frontalface_default.xml")
# while (cap.isOpened()):
#     chack,frame = cap.read()#รันภาพ frame by frame
#     if chack == True:
#         #convertframe to gray img
#         gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor=1.2,minNeighbors=5e)
#         for (x,y,w,h) in face_detect:
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
#             cv2.imshow("output",frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows

#ตรวจจับดวงตา
# import cv2
# import numpy as np
# img = cv2.imread("Opencv\image\jenna.jpg")
# img = cv2.resize(img,(800,800))

# #อ่านไฟล์สำหรับแยก classification
# face_cascade = cv2.CascadeClassifier("Opencv\Detect\haarcascade_eye_tree_eyeglasses.xml")
# #convert img to gray img
# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #classification face
# scaleFactor = 1.02 # ค่าเริ่มต้น
# minNeighbors = 3 # ค่าตรวจสอบ grayscale
# face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbors)
# #แสดงตำแหน่งใบหน้า
# #x,y จุดเริ่มต้น
# #w,h จุดสุดท้าย
# for (x,y,w,h) in face_detect:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)


# cv2.imshow("original",img)
# # cv2.imshow("result",gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#ตรวจจับดวงตาใน video
# import cv2
# import numpy as np
# # open video
# cap = cv2.VideoCapture("Opencv\image\Johnnydepp.mp4")
# #อ่านไฟล์สำหรับแยก classification
# ery_cascade = cv2.CascadeClassifier("Opencv\Detect\haarcascade_eye_tree_eyeglasses.xml")
# while (cap.isOpened()):
#     chack,frame = cap.read()#รันภาพ frame by frame
#     if chack == True:
#         #convertframe to gray img
#         gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         ery_detect = ery_cascade.detectMultiScale(gray_img,scaleFactor=1.3,minNeighbors=5)
#         for (x,y,w,h) in ery_detect:
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
#             cv2.imshow("output",frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows

#ตรวจจับดวงตาและใบหน้าในรูป
# import cv2
# import numpy as np
# img = cv2.imread("Opencv\image\jenna.jpg")
# img = cv2.resize(img,(800,800))

# #อ่านไฟล์สำหรับแยก classification
# face_cascade = cv2.CascadeClassifier("Opencv\Detect\haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier("Opencv\Detect\haarcascade_eye_tree_eyeglasses.xml")
# #convert img to gray img
# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #classification face
# face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=4)
# eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor=1.02,minNeighbors=4)
# #แสดงตำแหน่งใบหน้า
# #x,y จุดเริ่มต้น
# #w,h จุดสุดท้าย
# for (x,y,w,h) in face_detect:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
#     for (ex,ey,ew,eh) in eye_detect:
#         cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)


# cv2.imshow("original",img)
# # cv2.imshow("result",gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #ตรวจจับดวงตาและใบหน้าใน video
# import cv2
# import numpy as np
# # open video
# cap = cv2.VideoCapture("Opencv\image\Johnnydepp.mp4")
# #อ่านไฟล์สำหรับแยก classification
# eye_cascade = cv2.CascadeClassifier("Opencv\Detect\haarcascade_eye_tree_eyeglasses.xml")
# face_cascade = cv2.CascadeClassifier("Opencv\Detect\haarcascade_frontalface_default.xml")
# while (cap.isOpened()):
#     chack,frame = cap.read()#รันภาพ frame by frame
#     if chack == True:
#         #convertframe to gray_frame
#         gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         eye_detect = eye_cascade.detectMultiScale(gray_frame,scaleFactor=1.3,minNeighbors=5)
#         face_detect = face_cascade.detectMultiScale(gray_frame,scaleFactor=1.2,minNeighbors=5)
#         for (ex,ey,ew,eh) in eye_detect:
#             cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),thickness=5)
#             for (x,y,w,h) in face_detect:
#                 cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=5)
#                 cv2.imshow("output",frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows

#สร้าง TrackBar
img = np.zeros((200,250,3),np.uint8)
cv2.namedWindow("Color Trackbar")
def display(value):
    pass
cv2.createTrackbar("B","Color Trackbar",0,255,display)
cv2.createTrackbar("G","Color Trackbar",0,255,display)
cv2.createTrackbar("R","Color Trackbar",0,255,display)
while True:
    cv2.imshow("Color Trackbar",img)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
    #ดึงค่าจาก TrackBar
    blue = cv2.getTrackbarPos("B","Color Trackbar")
    green = cv2.getTrackbarPos("G","Color Trackbar")
    red = cv2.getTrackbarPos("R","Color Trackbar")
    #แสดงสี
    img[:]=[blue,green,red]

cv2.destroyAllWindows()