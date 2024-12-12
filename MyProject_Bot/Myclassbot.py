import cv2 as cv
import numpy as np

class Classbot:
    def __init__(self, main_img, temp_img):
        """
        main_img: ภาพหลักที่ต้องการค้นหา (เช่น ภาพจากหน้าจอ)
        temp_img: ชื่อไฟล์ของภาพเทมเพลตที่ต้องการค้นหา
        """
        self.main_img = main_img  # ภาพหลัก
        self.temp_img = cv.imread(temp_img, cv.IMREAD_ANYCOLOR)  # โหลดภาพเทมเพลต
        if self.temp_img is None:
            raise Exception(f"Template image '{temp_img}' not found!")

    def search(self, threshold=0.8, debug=False, text=""):
        """
        ค้นหาตำแหน่งของภาพเทมเพลตในภาพหลัก
        threshold: ค่าความคล้ายขั้นต่ำ (ค่า 0.8 = 80%)
        debug: หาก True จะวาดกรอบและแสดงภาพในหน้าต่าง
        text: ข้อความที่ต้องการแสดงบนกรอบที่พบ
        """
        # คำนวณการจับคู่ภาพ
        result = cv.matchTemplate(self.main_img, self.temp_img, cv.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)  # หาตำแหน่งที่ค่าความคล้าย >= threshold
        locations = list(zip(*locations[::-1]))  # แปลงตำแหน่ง (y, x) เป็น (x, y)
        height, width = self.temp_img.shape[:2]  # ดึงขนาดของภาพเทมเพลต
        rectangles = []  # เก็บตำแหน่งของกรอบสี่เหลี่ยม

        # สร้างกรอบสี่เหลี่ยมสำหรับทุกตำแหน่งที่พบ
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), width, height]
            rectangles.append(rect)
            rectangles.append(rect)  # เพิ่มซ้ำเพื่อให้ groupRectangles ทำงานได้ดีขึ้น
        rectangles, _ = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)  # รวมกรอบซ้อนกัน

        points = []  # เก็บพิกัดของจุดกลางของกรอบที่พบ
        for (x, y, w, h) in rectangles:
            # คำนวณพิกัดมุมและจุดศูนย์กลาง
            centerx = x + int(w / 2)
            centery = y + int(h / 2)
            points.append((centerx, centery))

            # วาดกรอบและข้อความหาก debug=True
            if debug:
                topleft = (x, y)
                bottomright = (x + w, y + h)
                cv.rectangle(self.main_img, topleft, bottomright, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
                cv.drawMarker(self.main_img, (centerx, centery), color=(255, 0, 145), markerSize=30, markerType=cv.MARKER_CROSS, thickness=1)
                font = cv.FONT_HERSHEY_COMPLEX
                position = (x + 10, y - 10)
                cv.putText(self.main_img, text, position, font, 0.35, (0, 255, 0), thickness=1)

        # แสดงภาพผลลัพธ์แบบเรียลไทม์เฉพาะเมื่อ debug=True
        if debug:
            cv.imshow("Real-Time Detection", self.main_img)
        else:
            cv.imshow("Real-Time Detection", self.main_img)
        # คืนค่าพิกัดของจุดที่พบทั้งหมด
        return points
