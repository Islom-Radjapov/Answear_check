from time import sleep
import numpy as np
from PIL import Image
import cv2
from helper_funct import drawRectangle

# read image
image = cv2.imread('orginal.jpg')

# oq-qora ranga otkashish
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# savollar = image[340:340+600, 209:209+117]
# savol_1 = savollar[5:5+25, :]
# savol_2 = savollar[10:10+25, :]
# image_1_1 = image2[:, :30]
# image_1_2 = image2[:, 50:68]
# image_1_3 = image2[:, 68:85]
# image_1_4 = image2[:, 85:]
# gray_image = cv2.bilateralFilter(image2, 11, 17, 17)
# drawRectangle(gray_image,  52, 340, 117, 600 )  # birinchi fan uchun kesib olish
# drawRectangle(gray_image,  209, 340, 117, 600 )

# show results
cv2.imshow("ima", image)
# cv2.imshow("image_1_2", image_1_2)
# cv2.imshow("result", gray_image[340:600+50, 209:117+50])
cv2.waitKey(0)
cv2.destroyAllWindows()