import numpy as np
import cv2

def adaptive_threshold(imgfile):
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    r = 900.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 900)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    blur = cv2.GaussianBlur(img, (5,5), 0) #주변 픽셀의 평균값을 대입함으로서 이미지를 흐릿하게 만든다. 2번째 인자는 주변 픽셀의 크기 크면 클수록 정도가 커진다.
    #이진화를 하기전 blur 효과를 줌으로서 noise를 제거
    result_with_blur = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)

    return result_with_blur



def compare(a,b):
    percent_a=0
    percent_b=0

    score=evl(ca,cb)*100
    print(score)
    # print('score = ', score) # compare ssim 판독기


    #원본 파일 라인
    for i in range(174):
        for j in range(120):
            if ca[i][j] ==255:
                percent_a+=1

    for i in range(174):
        for j in range(120):
            if cb[i][j]==255:
                percent_b+=1


        print('percent_a : ', percent_a)
        print('percent_b : ', percent_b)

        rate_a=(percent_a/20880)*100  # 실제 노이즈 있는 이미지의 전체 대비 흰색 비율
        rate_b=(percent_b/20880)*100  # 실제 원본 이미지의 전체 대비 흰색 비율
        



if __name__ == "__main__":
    camera= adaptive_threshold("test1.jpg")
    original=adaptive_threshold("test2.jpeg")
    

    print(camera)
    print(original)

