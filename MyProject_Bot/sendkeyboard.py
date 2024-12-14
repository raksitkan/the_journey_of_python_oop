from Windowscapture import *
import cv2 as cv
from Myclassbot import *
from time import time
from time import sleep
from Classclick import *
import os

## init title
windowname = 'LDPlayer'
windows = WindowCapture(windowname)
## check click hwid
myclick = click(windowname)
hwid = myclick.gethwid()

while True:
    myclick.send_input(hwid,"สวัสดีครับ")
    sleep(2)

    
    
