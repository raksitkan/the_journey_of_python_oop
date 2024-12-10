import cv2

# #read img
# img = cv2.imread("Opencv\image\plant.jpg",cv2.IMREAD_GRAYSCALE)
# # cv2.imshow("show",img)
# #resize
# img_resize = cv2.resize(img,(640,640))
# #show
# cv2.imshow("output",img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#open webcam
# cap = cv2.VideoCapture(0)
# while (True):
#     chack,frame = cap.read()
#     cv2.imshow("output",frame)
#     if cv2.waitKey(1) & 0xFF == ord("e"):
#         break
# cap.release()
# cv2.destroyAllWindows

#open video
# cap = cv2.VideoCapture("Opencv\image\Bean Time-Lapse .mp4")
# while (cap.isOpened()):
#     chack,frame = cap.read()#รันภาพ frame by frame
#     if chack == True:
#         cv2.imshow("output",frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows

#open video GRAYSCALE
# cap = cv2.VideoCapture("Opencv\image\Bean Time-Lapse .mp4")
# while (cap.isOpened()):    
#     chack,frame = cap.read()#รันภาพ frame by frame
#     if chack == True:
#         #convert RGB to gray video
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow("output",gray)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows

# #video writer
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# record = cv2.VideoWriter("Opencv\image\output.mp4",fourcc,20.0,(640,480))
# while (cap.isOpened()):    
#     chack,frame = cap.read()#รันภาพ frame by frame
#     if chack == True:
#         cv2.imshow("output",frame)
#         record.write(frame)      
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
# record.release()     
# cap.release()
# cv2.destroyAllWindows

# open video
# cap = cv2.VideoCapture("Opencv\image\output.mp4")
# while (cap.isOpened()):
#     chack,frame = cap.read()#รันภาพ frame by frame
#     if chack == True:
#         cv2.imshow("output",frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows

#สร้างเส้นตรง
# img = cv2.imread("Opencv\image\plant.jpg")

# #resize
# img_resize = cv2.resize(img,(700,700))

# #วาดเส้นตรง
# #line (img, start(x,y) , end (x,y), color(BGR), ความหนา)
# # cv2.line(img_resize,(0,0),(100,200),(255,0,200),10)
# cv2.arrowedLine(img_resize,(0,0),(100,200),(255,0,200),10)

# #show
# cv2.imshow("output",img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#วาดกรอบสีเหลี่ยม
# img = cv2.imread("Opencv\image\plant.jpg")
# #resize
# img_resize = cv2.resize(img,(800,600),interpolation=cv2.INTER_AREA )
# #วาดกรอบสีเหลี่ยม
# #rectangle (img, มุมที่1(มุมบนซ้าย), มุมที่2(มุมล่างขวา) color(BGR), ความหนา)
# cv2.rectangle(img_resize,(100,100),(500,500),(0,0,255),5)
# #show
# cv2.imshow("output",img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#วาดวงกลม
# img = cv2.imread("Opencv\image\plant.jpg")
# #resize
# img_resize = cv2.resize(img,(800,600),interpolation=cv2.INTER_AREA )
# #Circle
# #Circle (img, ตำแหน่งจุดกึ่งกลาง(x,y),รัศมี, color(BGR), ความหนา)
# cv2.circle(img_resize,(200,200),(70),(0,0,255),5)#-1 ถมสีวงกลม
# #show
# cv2.imshow("output",img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#ใส่ข้อความ
# img = cv2.imread("Opencv\image\plant.jpg")
# #resize
# img_resize = cv2.resize(img,(800,600),interpolation=cv2.INTER_AREA )
# #วาดข้อความบนภาพ
# #Circle (img,ข้อความ,พิกัดแสดงข้อความ(x,y),font,ขนาดข้อความ,color(BGR), ความหนา)
# cv2.putText(img_resize,"sakura",(150,545),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),cv2.LINE_4)#-1 ถมสีวงกลม
# #show
# cv2.imshow("output",img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# แสดงวันเวลาในวีดีโอ
# import datetime
# # cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("Opencv\image\Bean Time-Lapse .mp4")
# while (cap.isOpened()):
#     check,frame = cap.read()#รันภาพ frame by frame
#     if check == True: 
#         currentDate = datetime.datetime.now()
#         formatted_date = currentDate.strftime("%Y-%m-%d %H:%M:%S")
#         cv2.putText(frame,formatted_date,(10,40),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),cv2.LINE_4)
#         cv2.imshow("output",frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows

# #แสดงพิกัดด้วย mouse event
# img = cv2.imread("Opencv\image\plant.jpg")
# #resize
# img_resize = cv2.resize(img,(800,600))
# def clickpos(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN :#คลิกซ้าย
#         text = str(x)+","+str(y) #เก็บตำแหน่งคลิกเ
#         cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),cv2.LINE_4)
#         cv2.imshow("output",img)


# #show img #ข้อควรระวัง ชื่อ titel ต้องตรงกันหมด
# cv2.imshow("output",img_resize)
# cv2.setMouseCallback("output",clickpos)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # #ตรวจจับสี mouse event
# img = cv2.imread("Opencv\image\plant.jpg")
# #resize
# img_resize = cv2.resize(img,(800,600))
# def clickpos(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN :#คลิกซ้าย
#         blue = img[y,x,0]
#         green = img[y,x,1]
#         red = img[y,x,2]
#         text = str(blue)+","+str(green)+","+str(red) #เก็บตำแหน่งคลิกเ
#         cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),cv2.LINE_4)
#         cv2.imshow("output",img)


# #show img #ข้อควรระวัง ชื่อ titel ต้องตรงกันหมด
# cv2.imshow("output",img_resize)
# cv2.setMouseCallback("output",clickpos)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #ตรวจจับสี จาก pixel
import numpy as np
img = cv2.imread("Opencv\image\m&m.jpeg")
#resize
img_resize = cv2.resize(img,(800,600))
def clickpos(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :#คลิกซ้าย
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        img_color = np.zeros([244,244,3],np.uint8)
        img_color[:] = [blue,green,red]
        cv2.imshow("Result",img_color)


#show img #ข้อควรระวัง ชื่อ titel ต้องตรงกันหมด
cv2.imshow("output",img_resize)
cv2.setMouseCallback("output",clickpos)
cv2.waitKey(0)
cv2.destroyAllWindows()

#สร้างเส้นเชื่อมโยง
# import numpy as np
# img = cv2.imread("Opencv\image\plant.jpg")
# point = []
# def clickpos(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN :#คลิกซ้าย
#         cv2.circle(img,(x,y),10,(0,0,255,5))
#         point.append((x,y))
        
#         if len(point)>=2:
#             cv2.line(img,point[-2],point[-1],(0,255,0),5)
#             print("point ก่อนหน้า [-1] = ",point[-1])
#             print("point] ล่าสุด [-2] = ",point[-2])
#         cv2.imshow("output",img)


# #show img #ข้อควรระวัง ชื่อ titel ต้องตรงกันหมด
# cv2.imshow("output",img)
# cv2.setMouseCallback("output",clickpos)
# cv2.waitKey(0)
# cv2.destroyAllWindows()