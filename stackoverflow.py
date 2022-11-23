import cv2
import numpy as np
import csv

def drawRectangle(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    pix = cv2.countNonZero(edges)
    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)

# read image
img = cv2.imread('orginal.jpg')
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

i = 1
for cntr in contours:
    M = cv2.moments(cntr)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    cv2.circle(result, (cx, cy), 20, (0, 255, 0), -1)
    pt = (cx, cy)
    i = i + 1

def callback(foo):
    pass
cv2.namedWindow('parameters')
cv2.createTrackbar('Threshold1', 'parameters', 545, 700, callback)
cv2.createTrackbar('Threshold2', 'parameters', 402, 700, callback)
cv2.createTrackbar('Min pixels', 'parameters', 100, 1500, callback)
cv2.createTrackbar('Max pixels', 'parameters', 323, 1500, callback)

min = cv2.getTrackbarPos('Min pixels', 'parameters')
max = cv2.getTrackbarPos('Max pixels', 'parameters')
lowThreshold = cv2.getTrackbarPos('Threshold1', 'parameters')
highThreshold = cv2.getTrackbarPos('Threshold2', 'parameters')
font = cv2.FONT_HERSHEY_SIMPLEX

with open(r'Cordinates/rais.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)
rois = [[int(float(j)) for j in i] for i in rois]
# for i in range(len(rois)):
drawRectangle(result, 52, 340, 117, 600)

# save results
# cv2.imwrite('omr_sheet_thresh2.png', thresh)
# cv2.imwrite('omr_sheet_morph2.png', morph)
# cv2.imwrite('omr_sheet_result2.png', result)

# show results
cv2.imshow("thresh", thresh)
cv2.waitKey(0)
cv2.imshow("morph", morph)
cv2.waitKey(0)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()