from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from Classclick import *
from time import time, sleep

# Init title
windowsname = "LDPlayer"
windows = WindowCapture(windowsname)
looptime = time()
##check click hwid
myclick = click(windowsname)
hwid = myclick.gethwid()

# people_img
people_img = [
    "resort_img/h1.jpg",
    "resort_img/h2.jpg",
    "resort_img/h3.jpg",
    "resort_img/h4.jpg",
    "resort_img/bus1.jpg",
    "resort_img/h5.jpg",
    "resort_img/h6.jpg",
    "resort_img/h7.jpg",
    "resort_img/h8.jpg",
]
# for p_img in people_img:
#     print(p_img)
coin_img = [
    "resort_img/coin.jpg",
    "resort_img/coin2.jpg",
    "resort_img/coin3.jpg",
    "resort_img/coin4.jpg",
    "resort_img/coin5.jpg",
    "resort_img/coin6.jpg",
    "resort_img/coin7.jpg",
    "resort_img/coin8.jpg",
    "resort_img/coin9.jpg",
]
# for coin in coin_img:
#     print(coin)
utility = [
    "resort_img/out.jpg",
    "resort_img/room.jpg",
    "resort_img/room2.jpg",
    "resort_img/room3.jpg",
    "resort_img/out2.jpg",
]


class ImageClicker:
    def __init__(self, hwid, utility):
        self.hwid = hwid
        self.utility = utility

    def click_image(self, screen, uit, offset=(0, -33), threshold=0.9, sleep_time=3):
        # โหลดภาพเทมเพลต
        screen = windows.screenshot()
        image_path = str(self.utility[uit])
        bot = Classbot(screen, image_path)

        # ค้นหาภาพ
        points = bot.search(debug=False, text="", threshold=threshold)
        if points:
            for pos in points:
                # print(f"==== Found Image: {image_path} ====")
                x, y = pos
                sleep(3)
                # คลิกตำแหน่งปรับแต่งด้วย offset
                myclick.control_click(self.hwid, x + offset[0], y + offset[1])
                # print(f"Clicked at ({x + offset[0]}, {y + offset[1]})")
                sleep(3)
        else:
            print(f"No matching points found for {image_path}")


clicker = ImageClicker(hwid, utility)

energy = False  # ถ้า  energy = False แสดงว่า พลังงานไม่หมด
room = False
gust_room = False
while True:
    # Take screenshot
    screen = windows.screenshot(method="win32")
    # หน้าหลัก
    for p_img in people_img:
        bot = Classbot(screen, p_img)
        points = bot.search(debug=False, text="", threshold=0.9)
        for pos in points:
            myclick.control_click(
                hwid, pos[0], pos[1] - 33
            )  # -33 เพราะมีการคิดค่า ขอบ title จึงต้องลบ เพื่อให้คลิกในจุดที่ถูกต้อง
        # check stamina
        bot = Classbot(screen, "resort_img/stemina_out.jpg")
        points = bot.search(debug=False, text="", threshold=0.9)
        if points:
            for pos in points:
                print("==== พลังานหมดแล้ว ====")
                sleep(3)
                energy = True
                print("==== กำลังคลิกออก ====")
                myclick.control_click(
                    hwid, 319, 171 - 33
                )  # -33 เพราะมีการคิดค่า ขอบ title จึงต้องลบ เพื่อให้คลิกในจุดที่ถูกต้อง
                sleep(3)
            ### ห้องนอน
        if energy == True:
            print("=== เข้าไปเก็บ coin ห้องนอน ===")
            sleep(3)
            screen = windows.screenshot()
            bot = Classbot(screen, utility[1])
            points = bot.search(debug=False, text="", threshold=0.8)
            for pos in points:
                myclick.control_click(hwid, pos[0], pos[1] - 33)
            print("=== เข้าไปห้องนอน ===")
            sleep(3)
            screen = windows.screenshot()
            for coin in coin_img:
                bot = Classbot(screen, coin)
                points = bot.search(debug=False, text="coin", threshold=0.7)
                if points:
                    for coin in points:
                        print(f"==== เก็บ coin ที่ตำแหน่ง x={coin[0]}, y={coin[1]}====")
                        myclick.control_click(hwid, coin[0], coin[1] - 33)
                        # sleep(2)
                    screen = windows.screenshot()
                    sleep(3)
                    print("====ไม่เจอ coin แล้ว====")
                    sleep(3)

                    print("==== กำลังออกจากห้องนอน ====")
                    clicker.click_image(screen, uit=0, threshold=0.85)
                    sleep(3)
                    energy = False
                    room = True
                    print("==== ออกจากห้องนอนแล้ว ====")

        if room == True:
            print("=== เข้าไปเก็บ coin อาหาร ===")
            sleep(3)
            screen = windows.screenshot()
            bot = Classbot(screen, utility[2])
            points = bot.search(debug=False, text="", threshold=0.8)
            for pos in points:
                myclick.control_click(hwid, pos[0], pos[1] - 33)
            print("=== เข้าไปอาหาร ===")
            sleep(3)
            screen = windows.screenshot()
            for coin in coin_img:
                bot = Classbot(screen, coin)
                points = bot.search(debug=False, text="coin", threshold=0.7)
                if points:
                    for coin in points:
                        print(f"==== เก็บ coin ที่ตำแหน่ง x={coin[0]}, y={coin[1]}====")
                        myclick.control_click(hwid, coin[0], coin[1] - 33)
                        sleep(2)
                    screen = windows.screenshot()
                    sleep(3)
                    print("====ไม่เจอ coin แล้ว====")
                    sleep(3)

                    print("==== กำลังออกจากห้องอาหาร ====")
                    clicker.click_image(screen, uit=0, threshold=0.85)
                    sleep(3)
                    energy = False
                    room = False
                    gust_room = True
                    print("==== ออกจากห้องอาหาร ====")

        if gust_room == True:
            print("=== เข้าไปเก็บ coin ห้องแขกพิเศษ ===")
            sleep(3)
            screen = windows.screenshot()
            bot = Classbot(screen, utility[3])
            points = bot.search(debug=False, text="", threshold=0.8)
            for pos in points:
                myclick.control_click(hwid, pos[0], pos[1] - 33)
            print("=== เข้าไปห้องแขกพิเศษ===")
            sleep(3)
            screen = windows.screenshot()
            for coin in coin_img:
                bot = Classbot(screen, coin)
                points = bot.search(debug=False, text="coin", threshold=0.7)
                if points:
                    for coin in points:
                        print(f"==== เก็บ coin ที่ตำแหน่ง x={coin[0]}, y={coin[1]}====")
                        myclick.control_click(hwid, coin[0], coin[1] - 33)
                        sleep(2)
                    screen = windows.screenshot()
                    sleep(3)
                    print("====ไม่เจอ coin แล้ว====")
                    sleep(3)

                    print("==== กำลังออกจากห้องแขกพิเศษ ====")
                    clicker.click_image(screen, uit=4, threshold=0.75)
                    sleep(3)
                    energy = False
                    room = False
                    gust_room = False
                    print("==== ออกจากห้องแขกพิเศษ ====")

    # กด 'q' เพื่อออก
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
