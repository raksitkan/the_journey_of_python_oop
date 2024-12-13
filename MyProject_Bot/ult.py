from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from Classclick import *
from time import time,sleep
from ult import *
class ImageClicker:
    def __init__(self, hwid, utility):
        """
        คลาสสำหรับค้นหาและคลิกภาพบนหน้าจอ
        :param hwid: Handle ของหน้าต่างเกม
        :param utility: รายการของเส้นทางรูปภาพ
        """
        self.hwid = hwid
        self.utility = utility

    def click_image(self, screen, uit, offset=(0, -33), threshold=0.9, sleep_time=3):
        """
        ค้นหาและคลิกตำแหน่งภาพบนหน้าจอ
        :param screen: ภาพหน้าจอหลัก
        :param uit: ดัชนีของภาพใน `utility`
        :param offset: การปรับพิกัดการคลิก (ค่าเริ่มต้น: (0, -33))
        :param threshold: ค่าความคล้ายขั้นต่ำ (ค่าเริ่มต้น: 0.9)
        :param sleep_time: เวลารอหลังจากคลิก (ค่าเริ่มต้น: 3 วินาที)
        """
        try:
            # ตรวจสอบดัชนีที่ส่งมา
            if uit < 0 or uit >= len(self.utility):
                raise ValueError(f"Invalid index {uit}. Must be between 0 and {len(self.utility)-1}.")

            # โหลดภาพเทมเพลต
            image_path = str(self.utility[uit])
            bot = Classbot(screen, image_path)

            # ค้นหาภาพ
            points = bot.search(debug=False, text="", threshold=threshold)
            if points:
                for pos in points:
                    print(f"==== Found Image: {image_path} ====")
                    time.sleep(sleep_time)
                    x, y = pos
                    # คลิกตำแหน่งปรับแต่งด้วย offset
                    myclick.control_click(self.hwid, x + offset[0], y + offset[1])
                    print(f"Clicked at ({x + offset[0]}, {y + offset[1]})")
                    time.sleep(sleep_time)
            else:
                print(f"No matching points found for {image_path}")

        except Exception as e:
            print(f"Error in click_image: {e}")