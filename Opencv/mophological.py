import cv2
import matplotlib.pyplot as plt
import numpy as np
# img = cv2.imread("Opencv\image\CoinNoise.png",0)
# thresh,result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
# titles = ["Original","THRESH"]
# images = [img,result]
# for i in range(len(images)):
#     plt.subplot(1,2,i+1)
#     plt.imshow(images[i],cmap="gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

# #กรองข้อมูล
# img = cv2.imread("Opencv\image\CoinNoise.png",0)
# thresh,result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
# #กรองข้อมูล
# kernel = np.ones((2,2),np.uint8)#ขนาด,ชนิดข้อมูล
# #ขยายภาพ
# dilation = cv2.dilate(result,kernel,iterations=2)#iterations(ทำซ้ำ)
# #plot
# titles = ["Original","THRESH","DILATION"]
# images = [img,result,dilation]
# for i in range(len(images)):
#     plt.subplot(1,3,i+1)
#     plt.imshow(images[i],cmap="gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

# #การกร่อนภาพ Erosion
# img = cv2.imread("Opencv\image\CoinNoise.png",0)
# thresh,result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
# #กรองข้อมูล
# kernel = np.ones((2,2),np.uint8)#ขนาด,ชนิดข้อมูล
# #การขยายภาพ
# dilation = cv2.dilate(result,kernel,iterations=2)#iterations(ทำซ้ำ)
# #การกร่อนภาพ
# erosion = cv2.erode(result,kernel,iterations=7)
# #plot
# titles = ["Original","THRESH","DILATION","EROSION"]
# images = [img,result,dilation,erosion]
# for i in range(len(images)):
#     plt.subplot(2,2,i+1)
#     plt.imshow(images[i],cmap="gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

# #นำ การขยายภาพ และ การกร่อนภาพ Erosion มาใช่ร่วมกัน
# img = cv2.imread("Opencv\image\CoinNoise.png",0)
# thresh,result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
# #กรองข้อมูล
# kernel = np.ones((2,2),np.uint8)#ขนาด,ชนิดข้อมูล
# #การขยายภาพ
# dilation = cv2.dilate(result,kernel,iterations=2)#iterations(ทำซ้ำ)
# # mix การขยายภาพ การกร่อนภาพ
# dilation_erosion = cv2.erode(dilation,kernel,iterations=7)
# #plot
# titles = ["Original","THRESH","DILATION","DILATION_EROSION"]
# images = [img,result,dilation,dilation_erosion]
# for i in range(len(images)):
#     plt.subplot(2,2,i+1)
#     plt.imshow(images[i],cmap="gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

# #การใช้คำสั่ง opening
# img = cv2.imread("Opencv\image\CoinNoise.png",0)
# thresh,result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
# #กรองข้อมูล
# kernel = np.ones((2,2),np.uint8)#ขนาด,ชนิดข้อมูล
# #การขยายภาพ
# dilation = cv2.dilate(result,kernel,iterations=2)#iterations(ทำซ้ำ)
# #การกร่อนภาพ
# dilation_erosion = cv2.erode(dilation,kernel,iterations=7)
# #opening
# opening = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,kernel,iterations=7)
# #plot
# titles = ["Original","THRESH","DILATION","EROSION","OPENING"]
# images = [img,result,dilation,dilation_erosion,opening]
# for i in range(len(images)):
#     plt.subplot(2,3,i+1)
#     plt.imshow(images[i],cmap="gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

# #การใช้คำสั่ง colosing
img = cv2.imread("Opencv\image\CoinNoise.png",0)
thresh,result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
#กรองข้อมูล
kernel = np.ones((2,2),np.uint8)#ขนาด,ชนิดข้อมูล
#การขยายภาพ
dilation = cv2.dilate(result,kernel,iterations=2)#iterations(ทำซ้ำ)
#การกร่อนภาพ
dilation_erosion = cv2.erode(dilation,kernel,iterations=7)
#opening
opening = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,kernel,iterations=7)
#closing
closing = cv2.morphologyEx(result,cv2.MORPH_CLOSE,kernel,iterations=7)
#plot
titles = ["Original","THRESH","DILATION","EROSION","OPENING","CLOSING"]
images = [img,result,dilation,dilation_erosion,opening,closing]
for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()