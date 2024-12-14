from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from Classclick import *
from time import time, sleep
import threading
import os
from colorama import Fore, Back, Style, init
# เริ่มต้นใช้งาน colorama
init(autoreset=True)
# เพิ่มตัวควบคุมสถานะ
stop_event = threading.Event()  # ใช้สำหรับหยุดบอท
state = {"current": "MAIN"}  # ใช้ dictionary สำหรับจัดการสถานะ

# Init title
windowsname = "LDPlayer"
windows = WindowCapture(windowsname)
looptime = time()

# Check click hwid
myclick = click(windowsname)
hwid = myclick.gethwid()


def mybot():
    """
    ฟังก์ชันหลักสำหรับการทำงานของบอท
    """

    def click_image(screen, uit, offset=(0, -33), threshold=0.9, sleep_time=3):
        """
        ค้นหาและคลิกตำแหน่งภาพที่ระบุ
        """
        image_path = str(utility[uit])
        bot = Classbot(screen, image_path)
        points = bot.search(debug=False, text="", threshold=threshold)
        if points:
            for pos in points:
                x, y = pos
                sleep(sleep_time)
                myclick.control_click(hwid, x + offset[0], y + offset[1])
                sleep(sleep_time)
        else:
            print(f"No matching points found for {image_path}")

    while not stop_event.is_set():
        # Take screenshot
        screen = windows.screenshot(method="win32")
        # หน้าหลัก
        if state["current"] == "MAIN":
            sleep(3)
            screen = windows.screenshot()
            print("=== Checking Main Screen ===")
            for p_img in people_img:
                bot = Classbot(screen, p_img)
                points = bot.search(debug=False, text="", threshold=0.8)
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
                    myclick.control_click(
                        hwid, 319, 171 - 33
                    )  # -33 เพราะมีการคิดค่า ขอบ title จึงต้องลบ เพื่อให้คลิกในจุดที่ถูกต้อง
                state["current"] = "ROOM"

        # ห้องนอน
        if state["current"] == "ROOM":
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
                points = bot.search(debug=False, text="coin", threshold=0.85)
                if points:
                    for coin in points:
                        print(f"==== เก็บ coin ที่ตำแหน่ง x={coin[0]}, y={coin[1]}====")
                        myclick.control_click(hwid, coin[0], coin[1] - 33)
                    sleep(3)
                    print("====ไม่เจอ coin แล้ว====")
                    sleep(3)
                    print("==== กำลังออกจากห้องนอน ====")
                    click_image(screen, uit=0, threshold=0.9)
                    sleep(3)
                    state["current"] = "GUEST_ROOM"

        if state["current"] == "GUEST_ROOM":
            print("=== เข้าไปเก็บ coin ห้องอาหาร ===")
            sleep(3)
            screen = windows.screenshot()
            bot = Classbot(screen, utility[2])
            points = bot.search(debug=False, text="", threshold=0.8)
            for pos in points:
                myclick.control_click(hwid, pos[0], pos[1] - 33)
            print("=== เข้าห้องไปอาหาร ===")
            sleep(3)
            screen = windows.screenshot()
            for coin in coin_img:
                bot = Classbot(screen, coin)
                points = bot.search(debug=False, text="coin", threshold=0.85)
                if points:
                    for coin in points:
                        print(f"==== เก็บ coin ที่ตำแหน่ง x={coin[0]}, y={coin[1]}====")
                        myclick.control_click(hwid, coin[0], coin[1] - 33)
                        sleep(2)
                    sleep(3)
                    print("====ไม่เจอ coin แล้ว====")
                    sleep(3)

                    print("==== กำลังออกจากห้องอาหาร ====")
                    click_image(screen, uit=0, threshold=0.9)
                    sleep(3)
                    state["current"] = "DINNER"

        if state["current"] == "DINNER":
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
                points = bot.search(debug=False, text="coin", threshold=0.85)
                if points:
                    for coin in points:
                        print(f"==== เก็บ coin ที่ตำแหน่ง x={coin[0]}, y={coin[1]}====")
                        myclick.control_click(hwid, coin[0], coin[1] - 33)
                        sleep(2)
                    sleep(3)
                    print("====ไม่เจอ coin แล้ว====")
                    sleep(3)

                    print("==== กำลังออกจากห้องแขกพิเศษ ====")
                    click_image(screen, uit=4, threshold=0.8)
                    sleep(3)
                    state["current"] = "MAIN"

            # กด 'q' เพื่อออก
            if cv.waitKey(1) == ord("q"):
                cv.destroyAllWindows()
                break


def menu():
    """
    ฟังก์ชันเมนูหลัก
    """
    while True:
        print(Fore.CYAN + "=" * 38)
        print(Fore.GREEN + "===== Resortopia Bot V 0.1 Beta ======")
        print(Fore.CYAN + "=" * 38)
        print(Fore.YELLOW + "1. " + Fore.WHITE + "Start Resortopia Bot")
        print(Fore.YELLOW + "2. " + Fore.WHITE + "Exit")
        choice = input(Fore.YELLOW + "Enter Your Choice: ")

        if choice == "1":
            if not bot_thread.is_alive():
                print(Fore.GREEN + "Starting Bot...")
                stop_event.clear()  # รีเซ็ตสถานะหยุด
                bot_thread.start()
            else:
                print(Fore.RED + "Bot is already running!")

        elif choice == "2":
            print(Fore.GREEN + "Exiting Program...")
            stop_event.set()  # สั่งหยุดบอทหากกำลังทำงาน
            bot_thread.join()
            break

        else:
            print(Fore.RED + "Invalid choice. Try again.")
            os.system("cls")


# กำหนดข้อมูลรูปภาพ
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
    "resort_img/clean.jpg",
    "resort_img/key.jpg",
    "resort_img/q.jpg",
]

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
    "resort_img/coin10.jpg",
    "resort_img/clean.jpg",
    "resort_img/plus.jpg",
    "resort_img/paper.jpg",
    "resort_img/paper2.jpg",
    "resort_img/coin11.jpg",
]

utility = [
    "resort_img/out.jpg",
    "resort_img/room.jpg",
    "resort_img/room2.jpg",
    "resort_img/room3.jpg",
    "resort_img/out2.jpg",
]

# สร้าง Thread สำหรับบอท
bot_thread = threading.Thread(target=mybot)

# เรียกใช้เมนูหลัก
menu()
