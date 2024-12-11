import cv2 as cv
import numpy as np

class Classbot:
    def __init__(self,main_img,temp_img):
        ### Read img ###
        self.main_img = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
    def search(self):
        ### เปรียบเทียบภาพ ###
        result = cv.matchTemplate(self.main_img,self.temp_img,cv.TM_CCOEFF_NORMED)
        _,maxval,_,maxloc = cv.minMaxLoc(result)
        print(maxval)
        print(maxloc)
        ###เช็คค่าว่า หาก ต่าความน่าจะเป็น ของ maxval >= threshold ให้วาดกรอบ
        threshold = 0.5
        if maxval >= threshold:
            topleft = maxloc
            #เช็คความกว้างและสูงของรูป temp_img
            # print(temp_img.shape)
            height = self.temp_img.shape[0]#แทนค่าความสูง
            width = self.temp_img.shape[1]#แทนค่าความกว้าง
            #วาดกรอบ ตำแหน่งซ้ายบน[x] + ค่าความกว้าง & ตำแหน่งล่างขวา[y] + ค่าความสูง
            bottomright = (topleft[0]+width,topleft[1]+height)
            # bottomright = (207+90,146+150)
            cv.rectangle(self.main_img,topleft,bottomright,color=(0,255,0),thickness=2,lineType=cv.LINE_4)
            
            #### Put text ###
            font = cv.FONT_HERSHEY_COMPLEX
            #Position
            position = (topleft[0]+10,topleft[1]-10)
            #fontsize
            fontsize = 0.8
            #color text
            color = (0,255,0)
            cv.putText(self.main_img,"Mark",position,font,fontsize,color,thickness=2)
            ### End Put text ###
            #show img
            cv.imshow("result",self.main_img)
            cv.waitKey(0)
            cv.destroyAllWindows()
        else:
            print("none")
mybot = Classbot('img/top_word_humen.jpg','img/temp.jpg')
mybot.search()