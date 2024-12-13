#ฟีเจอร์สำหรับเล่นเกม Magic Tiles อัตโนมัติ
from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from pyautogui import click
from time import time,sleep
from magicdata import magicdata
import keyboard
# Init title
windows = WindowCapture('LDPlayer')
looptime = time()
sleep(3)
print("game start")
while True:
    #take sceenshot
    sceen = windows.screenshot(method="win32")
    ##start bot##
    search = Classbot(sceen)
    ##สีดำ sum แล้วไม่น่าเกิน 50
    for location in magicdata:
        result = search.getcolor(location['loc'][0], location['loc'][1],"0x000000")
        if result[1] <= 100 or result[0]:
            keyboard.press(location['key'])
            print(location['output'])
        else:
            keyboard.release(location['key'])    
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
