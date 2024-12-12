from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from time import time
from pyautogui import click
# Init title
windows = WindowCapture('Online Whack Em All Arcade Game for Kids: Whack a Mole on the Head With a Hammer and 16 more pages - Personal - Microsoft​ Edge')
looptime = time()

while True:
    # Take screenshot
    screen = windows.screenshot(method="win32")
    
    # Start bot
    bot = Classbot(screen, 'img/mole.jpg')
    points = bot.search(debug=True, text="icon", threshold=0.8)
    for myclick in points:
        click(x=myclick[0],y=myclick[1])
    # กด 'q' เพื่อออก
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
