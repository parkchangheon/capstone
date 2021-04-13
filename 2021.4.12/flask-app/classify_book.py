#from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim
import cv2
import matplotlib.pyplot as plt


def check(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (500, 500))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (3, 3), 0)
    #cv2.imshow("g", blurred_A)
    canny = cv2.Canny(blurred_A, 0, 150)
    plt.imshow(canny)
    plt.show()
    return canny


def cannycompare(a, b):
    (score, diff) = compare_ssim(a, b, full=True)
    diff = (diff*255).astype("uint8")
    print(f"Simlarity:{score:.5f}")
    assert score, "못찾음"
    return score


def evl(a, b):
    tmp = cannycompare(a, b)
    if(tmp >= 0.55):
        return tmp, '상급'
    elif(0.5 <= tmp <= 0.55):
        return tmp, '중급'
    else:
        return tmp, '하급'
