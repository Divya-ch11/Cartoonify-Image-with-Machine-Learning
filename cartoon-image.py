import cv2
from tkinter.filedialog import *

photo = askopenfilename()
img = cv2.imread(photo)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3) 
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)
#cv2.imshow("edges", edges)

col_img = cv2.bilateralFilter(img, 5, 255, 255)
cartoon = cv2.bitwise_and(col_img, col_img,mask = edges)

cv2.imshow("Image", img)
cv2.imshow("cartoon", cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
