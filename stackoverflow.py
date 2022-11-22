import cv2
import numpy as np

# read image
img = cv2.imread('dtm1.jpg')
h, w = img.shape[:2]

# trim 15 from bottom and 5 from right to remove partial answer and extraneous red
img = img[0:h - 15, 0:w - 5]

# threshold on white color
lower = (225, 225, 225)
upper = (255, 255, 255)
thresh = cv2.inRange(img, lower, upper)
thresh = 255 - thresh

# apply morphology close
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)

# get contours
result = img.copy()
contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours = contours[0] if len(contours) == 2 else contours[1]
print("count:", len(contours))
print('')
i = 1
for cntr in contours:
    M = cv2.moments(cntr)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    cv2.circle(result, (cx, cy), 20, (0, 255, 0), -1)
    pt = (cx, cy)
    print("circle #:", i, "center:", pt)
    i = i + 1

# save results
cv2.imwrite('omr_sheet_thresh2.png', thresh)
cv2.imwrite('omr_sheet_morph2.png', morph)
cv2.imwrite('omr_sheet_result2.png', result)

# show results
cv2.imshow("thresh", thresh)
cv2.imshow("morph", morph)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()