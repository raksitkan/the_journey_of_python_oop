from Windowscapture import *
import cv2 as cv
from Myclassbot import *

windows = WindowCapture('LDPlayer')

screen = windows.screenshot(method="pyautogui")
print(screen)
screen = Classbot(screen,'img/test.jpg')
point = screen.search(debug=True,text="icon")

