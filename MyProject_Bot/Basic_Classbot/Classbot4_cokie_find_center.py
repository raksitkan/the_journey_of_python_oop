#การแก้ไข pos ซ้ำซ้อน
import cv2 as cv
import numpy as np

class Classbot:
    def __init__(self, main_img, temp_img):
        ### Read img ###
        self.main_img = cv.imread(main_img, cv.IMREAD_ANYCOLOR)  # อ่านภาพหลัก
        self.temp_img = cv.imread(temp_img, cv.IMREAD_ANYCOLOR)  # อ่านภาพเทมเพลต
    
    def search(self):
        ### เปรียบเทียบภาพ ###
        result = cv.matchTemplate(self.main_img, self.temp_img, cv.TM_CCOEFF_NORMED)  # หาตำแหน่งที่ภาพเหมือนกัน
        _, maxval, _, maxloc = cv.minMaxLoc(result)  # หาค่าความคล้ายสูงสุดและตำแหน่ง
        threshold = 0.8  # กำหนดค่าความคล้ายขั้นต่ำ
        locations = np.where(result >= threshold)  # หาตำแหน่งที่ค่าความคล้าย >= threshold       
        locations = list(zip(*locations[::-1]))  # แปลงตำแหน่งเป็น list ของพิกัด (x, y)
        
        height = self.temp_img.shape[0]  # ความสูงของภาพเทมเพลต
        width = self.temp_img.shape[1]  # ความกว้างของภาพเทมเพลต
        rectangles = []  # สร้างรายการสำหรับเก็บกรอบสี่เหลี่ยม
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), width, height]  # สร้างกรอบสี่เหลี่ยม (x, y, ความกว้าง, ความสูง)
            rectangles.append(rect)  # เพิ่มกรอบเข้าไปในรายการ
            rectangles.append(rect)  # เพิ่มซ้ำสำหรับการตรวจจับกรอบที่ซ้อนกัน
        rectangles, _ = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)  
        # รวมกรอบที่ซ้อนทับกันให้เป็นกรอบเดียว
        # print(rectangles)  # แสดงผลลัพธ์กรอบที่ถูกจัดกลุ่ม
        # print(f"พบภาพทั้งหมด : {len(rectangles)}")  # แสดงจำนวนกรอบทั้งหมด
        # exit
        point = []
        if len(rectangles):
            for (x,y,w,h) in rectangles:
                # print(x,y,w,h,)
                topleft = (x,y)
                bottomright = (x+w,y+h)
                cv.rectangle(self.main_img, topleft, bottomright, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)  # วาดกรอบสี่เหลี่ยม

                centerx = x + int(w / 2)  # คำนวณตำแหน่ง x ของจุดกลางโดยการบวกครึ่งหนึ่งของความกว้าง (w)
                centery = y + int(h / 2)  # คำนวณตำแหน่ง y ของจุดกลางโดยการบวกครึ่งหนึ่งของความสูง (h)
                # add x y to point for click
                point.append((centerx, centery))  # เพิ่มพิกัดของจุดกลางลงในลิสต์ 'point'
                cv.drawMarker(self.main_img, (centerx, centery), color=(255, 0, 145), markerSize=30, markerType=cv.MARKER_CROSS, thickness=1)  # วาดเครื่องหมายกากบาทที่จุดกลาง

                # print(centerx,centery)
                ### Put text ###
                font = cv.FONT_HERSHEY_COMPLEX
                position = (topleft[0] + 10, topleft[1] - 10)  # ตำแหน่งข้อความ
                fontsize = 0.35
                color = (0, 255, 0)
                cv.putText(self.main_img, "jelly", position, font, fontsize, color, thickness=2)  # ใส่ข้อความ "jelly"
            # แสดงภาพ
            cv.imshow("cookie", self.main_img)  # แสดงภาพที่มีกรอบและข้อความ
            cv.waitKey(0)  # รอให้ผู้ใช้กดปุ่มก่อนปิดหน้าต่าง
            cv.destroyAllWindows()  # ปิดหน้าต่างทั้งหมด
            return(point)
mybot = Classbot('img/cookie_run.jpg','img/cookie_temp.jpg')
mypoint = mybot.search()
for myClick in mypoint:
    print(myClick[0],myClick[1])