#แสดงผลภาพด้วย matplotlib
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Opencv\image\jenna.jpg")
cv2.imshow("output",img)
#convert BGR to RGB 
img=cv2.cvtColor(img,cv2.COLOR_BGRA2RGB)
plt.imshow(img)
plt.show()

#Thresholding
# gray_img = cv2.imread("Opencv\image\cat.jpg")
# thresh,result1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
# thresh,result2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
# thresh,result3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
# thresh,result4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
# thresh,result5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)
# cv2.imshow("Original",gray_img)
# cv2.imshow("BINARY",result1)
# cv2.imshow("THRESH_BINARY_INV",result2)
# cv2.imshow("THRESH_TRUNC",result3)
# cv2.imshow("THRESH_TOZERO",result4)
# cv2.imshow("THRESH_TOZERO_INV",result5)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#แสดงผลใน matplotlib
# gray_img = cv2.imread("Opencv\image\cat.jpg")
# thresh,result1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
# thresh,result2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
# thresh,result3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
# thresh,result4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
# thresh,result5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)
# list_img = [gray_img,result1,result2,result3,result4,result5]
# tiile = ["Original","BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV"]
# for i in range(len(list_img)):
#     plt.subplot(2,3,i+1)
#     plt.imshow(list_img[i])
#     plt.title(tiile[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

#แปลงภาพสี -> grayscale
# img = cv2.imread("Opencv\image\cat.jpg")
# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# thresh_value = [50,100,130,200,230]

# plt.subplot(231,xticks = [],yticks =[])
# plt.title("Original")
# plt.imshow(gray_img,cmap="gray")

# for i in range(len(thresh_value)):
#     thresh,result = cv2.threshold(gray_img,thresh_value[i],255,cv2.THRESH_BINARY)   
#     plt.subplot(232+i)
#     plt.title("%d"%thresh_value[i])
#     plt.imshow(result,cmap="gray")   
#     plt.xticks([]),plt.yticks([])
# plt.show()

#การปรับค่า Thresholding ด้วย Track bar
# def display(value):
#     pass
# cv2.namedWindow("Output")
# cv2.createTrackbar("value","Output",128,255,display)
# while True :
#     gray_img = img = cv2.imread("Opencv\image\cat.jpg",0)
#     thres_value = cv2.getTrackbarPos("value","Output")
#     thres,result = cv2.threshold(gray_img,thres_value,255,cv2.THRESH_BINARY)
#     if cv2.waitKey(1) &0xFf == ord("e"):
#         break
#     cv2.imshow("Output",result)
# cv2.destroyAllWindows()

#Adaptive Thresholding
#cv2.adaptiveThreshold(gray_img,maxvalue,adaptiveMethod,Thresholdtype,BlockSize,C)
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C
# cv2.ADAPTIVE_THRESH_MEAN_C
# img = cv2.imread("Opencv\image\maps.jpg",0)
# thresh,result = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
# result1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=3,C=1)
# result2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blockSize=3,C=1)
# cv2.imshow("Thresh",result)
# cv2.imshow("Mean",result1)
# cv2.imshow("GAUSSIAN",result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #Adaptive Thresholding เปลี่ยนแปลง blocksize
# img = cv2.imread("Opencv\image\maps.jpg",0)
# #กำหนดขนาด blocksize
# size = [3,5,9,17,33]
# plt.subplot(231,xticks=[],yticks=[])
# plt.imshow(img,cmap="gray")
# for i in range(len(size)):
#     result = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=size[i],C=1)
#     plt.subplot(232+i)
#     plt.title("%d"%size[i])
#     plt.imshow(result,cmap="gray")
#     plt.xticks([]),plt.yticks([])
# plt.show()
