from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from time import time
from pyautogui import click
# Init title
#https://www.crazygames.com/game/duck-hunt
windows = WindowCapture('Duck Hunt 🕹️ Play on CrazyGames and 15 more pages - Personal - Microsoft​ Edge')
looptime = time()
myduckdata = {
    'duck1':'img/duck_1.jpg',
    'duck2':'img/duck_2.jpg',
    'duck3':'img/duck_3.jpg',
    'duck4':'img/duck_4.jpg'
}
while True:
    # Take screenshot
    screen = windows.screenshot(method="win32")
    for name,path_img in myduckdata.items():
        print(name,path_img)
        # Start bot
        bot = Classbot(screen,path_img)
        points = bot.search(debug=True, text=name, threshold=0.8)
        # Click
        for myclick in points:
            click(x=myclick[0],y=myclick[1])
    # กด 'q' เพื่อออก
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
