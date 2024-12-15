from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from time import time

# Init title
windows = WindowCapture('LDPlayer')
looptime = time()

while True:
    # Take screenshot
    screen = windows.screenshot(method="win32")
    
    # Start bot
    bot = Classbot(screen, 'img/test.jpg')
    points = bot.search(debug=1, text="icon", threshold=0.8)
    
    # กด 'q' เพื่อออก
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
