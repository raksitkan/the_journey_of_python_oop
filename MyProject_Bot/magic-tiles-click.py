#ฟีเจอร์สำหรับเล่นเกม Magic Tiles อัตโนมัติ
from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from Classclick import *
from time import time,sleep
from magicdata import magicdata
import keyboard
# Init title
windowname = 'LDPlayer'
windows = WindowCapture(windowname)
looptime = time()
# sleep(3)
# print("game start")
##check click hwid
myclick = click(windowname)
hwid = myclick.gethwid()
print(f"HWID: {hwid}")
# while True:
#     #take sceenshot
#     sceen = windows.screenshot(method="win32")
#     ##start bot##
#     search = Classbot(sceen)
#     ##สีดำ sum แล้วไม่น่าเกิน 50
#     for location in magicdata:
#         # ตรวจสอบสีที่ตำแหน่ง
#         result = search.getcolor(location['loc'][0], location['loc'][1], "0x000000")
        
#         if result[1] <= 50 or result[0]:  # ปรับค่าผลรวมสีที่เหมาะสม
#             # ปรับพิกัดให้สัมพันธ์กับหน้าต่างเกม
#             x_adjusted = location['loc'][0]
#             y_adjusted = location['loc'][1]

            
#             # คลิกที่ตำแหน่งที่ปรับแล้ว
#             myclick.control_click(hwid, x_adjusted, y_adjusted)


    
    # if cv.waitKey(1) == ord('q'):
    #     cv.destroyAllWindows()
    #     break
# import cv2 as cv

# วาดกรอบรอบพิกัดที่กำหนด
def draw_debug_boxes(screen, magicdata):
    for location in magicdata:
        x, y = location['loc']  # พิกัดที่กำหนด
        color = (0, 255, 0)  # สีเขียวสำหรับกรอบ
        thickness = 2  # ความหนาของกรอบ
        size = 10  # ขนาดกรอบ (ครึ่งหนึ่งของความกว้างและสูง)

        # คำนวณมุมบนซ้ายและล่างขวาของกรอบ
        topleft = (x - size, y - size)
        bottomright = (x + size, y + size)

        # วาดกรอบ
        cv.rectangle(screen, topleft, bottomright, color, thickness)

        # เพิ่มข้อความตำแหน่ง
        text = f"({x}, {y})"
        cv.putText(screen, text, (x + 10, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)

# ตัวอย่างการใช้งาน
# สมมุติว่า `screen` คือภาพที่จับมาจากหน้าจอ
# และ `magicdata` คือข้อมูลพิกัด
# magicdata = [
#     {'loc': (52+20, 757), 'key': 'A'},
#     {'loc': (165+30,757), 'key': 'S'},
#     {'loc': (278+60,757), 'key': 'D'},
#     {'loc': (388+90,757), 'key': 'F'}
# ]
while True:
    screen = windows.screenshot(method="win32")  # จับภาพหน้าจอ
    draw_debug_boxes(screen, magicdata)  # วาดกรอบบนภาพ
    cv.imshow("Debug with Boxes", screen)  # แสดงภาพ


    # แสดงผลภาพ
    cv.imshow("Debug with Boxes", screen)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
