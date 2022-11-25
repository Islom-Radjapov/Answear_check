import cv2

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

def drawRectangle(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    pix = cv2.countNonZero(edges)
    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)