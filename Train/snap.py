import numpy as np
import cv2

from utils import image_resize

face_cascade        = cv2.CascadeClassifier('third-party/haarcascade_frontalface_alt.xml')
eyes_cascade        = cv2.CascadeClassifier('third-party/frontalEyes35x16.xml')
nose_cascade        = cv2.CascadeClassifier('third-party/Nose18x15.xml')
img                 = cv2.imread("Before.png", -1)
glasses             = cv2.imread("glasses.png", -1)
mustache            = cv2.imread('mustache.png',-1)
gray                = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

faces               = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
for (x, y, w, h) in faces:
    roi_gray    = gray[y:y+h, x:x+h] 
    roi_color   = img[y:y+h, x:x+h]
    #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
for (ex, ey, ew, eh) in eyes:
    #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)
    roi_eyes = roi_gray[ey: ey + eh, ex: ex + ew]
    glasses = image_resize(glasses.copy(), width=ew)

gw, gh, gc = glasses.shape
for i in range(0, gw):
    for j in range(0, gh):
        #print(glasses[i, j]) 
        if glasses[i, j][3] != 0: 
            roi_color[ey + i, ex + j] = glasses[i, j]


nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
for (nx, ny, nw, nh) in nose:
    #cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
    roi_nose = roi_gray[ny: ny + nh, nx: nx + nw]
    mustache = image_resize(mustache.copy(), width=nw)

mw, mh, mc = mustache.shape
for i in range(0, mw):
    for j in range(0, mh):
        #print(glasses[i, j]) 
        if mustache2[i, j][3] != 0: 
            roi_color[ny + int(nh/2.0) + i, nx + j] = mustache[i, j]

    
cv2.imwrite('messigray.png',img)
