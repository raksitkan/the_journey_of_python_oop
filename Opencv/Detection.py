import cv2
import matplotlib.pyplot as plt
import numpy as np
#หาขอบแบบ Sobel
# img = cv2.imread("Opencv\image\coins.png",0)
# #หาขอบแกนแนวนอน  X
# sobelX = cv2.Sobel(img,-1,dx=1,dy=0)
# #หาขอบแกนแนวตั้ง Y
# sobelY = cv2.Sobel(img,-1,dx=0,dy=1)
# #รวม x y
# sobelXY = cv2.bitwise_or(sobelX,sobelY)
# images = [img,sobelX,sobelY,sobelXY]
# titles = ["Original","sobelX","sobelY","sobelXY"]
# # วนลูปแสดงผลภาพ
# for i in range(len(images)):
#     plt.subplot(2, 2, i + 1)
#     plt.imshow(images[i],cmap="gray")  # แปลงภาพ BGR -> RGB
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# # แสดงผลทั้งหมด
# plt.show()

#Laplacian
# img = cv2.imread("Opencv\image\coins.png",0)
# #หาขอบ
# lap = cv2.Laplacian(img,-1)
# cv2.imshow("Original",img)
# cv2.imshow("Laplacian",lap)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #หาขอบภาพ Canny Method ***ได้รับความนิยม***
# img = cv2.imread("Opencv\image\coins.png",0)
# #หาขอบ
# canny = cv2.Canny(img,threshold1=50,threshold2=200)
# cv2.imshow("Original",img)
# cv2.imshow("Canny",canny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#หาเส้นเค้าโครง (Contours)
img = cv2.imread("Opencv\image\cardinal.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh,result =cv2.threshold(gray_img,248,255,cv2.THRESH_BINARY)
#ค้นหาเส้น note สามารถเอา candy มาใส่ได้โดยแทน candy ลง ไปแทน result ใน findContours
contours,hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(0,255,0),thickness=2)
# print(len(contours))
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()