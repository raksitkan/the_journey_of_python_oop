import cv2 as cv
import numpy as np
### Read img ###
main_img = cv.imread('img/top_word_humen.jpg',cv.IMREAD_ANYCOLOR)
temp_img = cv.imread('img/temp.jpg',cv.IMREAD_ANYCOLOR)
### End Read ###
### เปรียบเทียบภาพ ###
result = cv.matchTemplate(main_img,temp_img,cv.TM_CCOEFF_NORMED)

###หาพิกัดของภาพ main_img ที่ตรงกับ temp_img
_,maxval,_,maxloc = cv.minMaxLoc(result)
print(maxval)
print(maxloc)
###เช็คค่าว่า หาก ต่าความน่าจะเป็น ของ maxval >= threshold ให้วาดกรอบ
threshold = 0.9
if maxval >= threshold:
    topleft = maxloc
    #เช็คความกว้างและสูงของรูป temp_img
    # print(temp_img.shape)
    height = temp_img.shape[0]#แทนค่าความสูง
    width = temp_img.shape[1]#แทนค่าความกว้าง
    #วาดกรอบ ตำแหน่งซ้ายบน[x] + ค่าความกว้าง & ตำแหน่งล่างขวา[y] + ค่าความสูง
    bottomright = (topleft[0]+width,topleft[1]+height)
    # bottomright = (207+90,146+150)
    cv.rectangle(main_img,topleft,bottomright,color=(0,255,0),thickness=2,lineType=cv.LINE_4)
    
    #### Put text ###
    font = cv.FONT_HERSHEY_COMPLEX
    #Position
    position = (topleft[0]+10,topleft[1]-10)
    #fontsize
    fontsize = 0.8
    #color text
    color = (0,255,0)
    cv.putText(main_img,"Mark",position,font,fontsize,color,thickness=2)
    ### End Put text ###
    #show img
    cv.imshow("result",main_img)
    cv.waitKey(0)
    cv.destroyAllWindows()