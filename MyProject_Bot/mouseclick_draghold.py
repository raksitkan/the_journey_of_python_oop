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
    myclick.click_and_hold(hwid,(364, 209))
    sleep(.5)
    myclick.drag_and_drop(hwid,(364, 209),(69, 754))
    
    myclick.click_hold_and_move(hwid,(291, 291),(281, 839),20)
    