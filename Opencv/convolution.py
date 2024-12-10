#ตัวกรอง convolution filter2D
import cv2
import matplotlib.pyplot as plt
import numpy as np

# # โหลดภาพ
# img = cv2.imread("Opencv/image/noise.png")

# # สร้าง kernel และใช้ฟิลเตอร์
# kernel = np.ones((3, 3), np.float32) / 9

# convo1 = cv2.filter2D(img, -1,np.ones((3, 3), np.float32) / 9)
# convo2 = cv2.filter2D(img, -1,np.ones((5, 5), np.float32) / 25)

# # กำหนดชื่อและภาพสำหรับแสดงผล
# titles = ["ORIGINAL", "CONVOLUTION 3X3","CONVOLUTION 5X5"]
# images = [img, convo1,convo2]

# # วนลูปแสดงผลภาพ
# for i in range(len(images)):
#     plt.subplot(1, 3, i + 1)
#     plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # แปลงภาพ BGR -> RGB
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# # แสดงผลทั้งหมด
# plt.show()

#ตัวกรองค่าเฉลี่ย/เบลอ
# # โหลดภาพ
# img = cv2.imread("Opencv/image/noise.png")

# # สร้าง kernel และใช้ฟิลเตอร์
# kernel = np.ones((3, 3), np.float32) / 9
# #filter2D
# filter2D = cv2.filter2D(img, -1,np.ones((3, 3), np.float32) / 9)
# #blur
# blur = cv2.blur(img,(5,5))
# # กำหนดชื่อและภาพสำหรับแสดงผล
# titles = ["ORIGINAL", "filter2D","BLUR"]
# images = [img, filter2D,blur]

# # วนลูปแสดงผลภาพ
# for i in range(len(images)):
#     plt.subplot(1, 3, i + 1)
#     plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # แปลงภาพ BGR -> RGB
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# # แสดงผลทั้งหมด
# plt.show()

#ตัวกรองค่ามัธยฐาน medianBlur
# โหลดภาพ
# img = cv2.imread("Opencv/image/noise.png")

# # สร้าง kernel และใช้ฟิลเตอร์
# kernel = np.ones((3, 3), np.float32) / 9
# #filter2D
# filter2D = cv2.filter2D(img, -1,np.ones((3, 3), np.float32) / 9)
# #blur
# blur = cv2.blur(img,(5,5))
# #medianBlur
# mblur= cv2.medianBlur(img,5)
# # กำหนดชื่อและภาพสำหรับแสดงผล
# titles = ["ORIGINAL", "filter2D","BLUR","MEDIAN BLUR"]
# images = [img, filter2D,blur,mblur]

# # วนลูปแสดงผลภาพ
# for i in range(len(images)):
#     plt.subplot(2, 2, i + 1)
#     plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # แปลงภาพ BGR -> RGB
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# # แสดงผลทั้งหมด
# plt.show()

#ตัวกรอง Gaussian Filter
# โหลดภาพ
img = cv2.imread("Opencv/image/noise.png")

#filter2D
filter2D = cv2.filter2D(img, -1,np.ones((3, 3), np.float32) / 9)
#blur
blur = cv2.blur(img,(5,5))
#medianBlur
mblur= cv2.medianBlur(img,5)
#Gaussian Filter
gblur = cv2.GaussianBlur(img,(5,5),1)
# กำหนดชื่อและภาพสำหรับแสดงผล
titles = ["ORIGINAL", "filter2D","BLUR","MEDIAN BLUR","Gaussian BLUR"]
images = [img, filter2D,blur,mblur,gblur]

# วนลูปแสดงผลภาพ
for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # แปลงภาพ BGR -> RGB
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# แสดงผลทั้งหมด
plt.show()