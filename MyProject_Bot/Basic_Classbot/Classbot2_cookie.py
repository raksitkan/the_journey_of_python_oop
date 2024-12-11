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
        
        if locations:
            height = self.temp_img.shape[0]  # ความสูงของภาพเทมเพลต
            width = self.temp_img.shape[1]  # ความกว้างของภาพเทมเพลต
            for loc in locations:
                bottomright = (loc[0] + width, loc[1] + height)  # คำนวณตำแหน่งมุมล่างขวาของกรอบ
                cv.rectangle(self.main_img, loc, bottomright, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)  # วาดกรอบสี่เหลี่ยม
                ### Put text ###
                font = cv.FONT_HERSHEY_COMPLEX
                position = (loc[0] + 10, loc[1] - 10)  # ตำแหน่งข้อความ
                fontsize = 0.35
                color = (0, 255, 0)
                cv.putText(self.main_img, "jelly", position, font, fontsize, color, thickness=2)  # ใส่ข้อความ "jelly"
            # แสดงภาพ
            cv.imshow("cookie", self.main_img)  # แสดงภาพที่มีกรอบและข้อความ
            cv.waitKey(0)  # รอให้ผู้ใช้กดปุ่มก่อนปิดหน้าต่าง
            cv.destroyAllWindows()  # ปิดหน้าต่างทั้งหมด

mybot = Classbot('img/cookie_run.jpg','img/cookie_temp.jpg')
mybot.search()