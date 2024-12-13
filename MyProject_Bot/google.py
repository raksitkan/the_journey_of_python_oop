from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from time import time
from Classclick import *
from time import time,sleep
# Init title
windowsname = 'Click speed test - CPS Test Online and 9 more pages - Personal - Microsoft​ Edge'
windows = WindowCapture(windowsname)
looptime = time()
##check click hwid
myclick = click(windowsname)
hwid = myclick.getchromeid()
print(f"HWID: {hwid}")
while True:
    # Take screenshot
    screen = windows.screenshot(method="win32")
    
    # Start bot
    bot = Classbot(screen, 'img/click_temp.jpg')
    points = bot.search(debug=0, text="icon", threshold=0.7)
    sleep(0.001)
    for pos in points:
        print(pos[0],pos[1])
        myclick.control_click(hwid,pos[0],pos[1])
        
    # กด 'q' เพื่อออก
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
