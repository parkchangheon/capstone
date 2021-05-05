import cv2
import numpy as np

def check(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (256, 256))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (3,3), 0)
    #cv2.imshow("g", blurred_A)
    canny = cv2.Canny(blurred_A, 0, 150)
    return canny

def check_ca(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (256, 256))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (7,7), 0)
    #cv2.imshow("g", blurred_A)
    canny = cv2.Canny(blurred_A, 0, 150)
    return canny



# img = check_ca('test1.jpg')
# img = check('test2.jpeg')

# img = check_ca('test5.png')
img = check('test6.png')

G_x = np.array([[1,0],[0,-1]])
G_y = np.array([[0,1],[-1,0]])

edge_x=cv2.filter2D(img,-1,G_x)
edge_y=cv2.filter2D(img,-1,G_y)

cv2.imshow('Edge_x',edge_x)
cv2.imshow('Edge_y',edge_y)

cv2.waitKey()
