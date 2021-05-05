import cv2
import numpy as np

def check(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (256, 256))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (5,5), 0)
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

G_x = np.array([[-1,1]])
G_y = np.array([[-1],[1]])

edge_x=cv2.filter2D(img,-1,G_x)
edge_y=cv2.filter2D(img,-1,G_y)

cv2.imshow('Edge_x',edge_x)
cv2.imshow('Edge_y',edge_y)

cv2.waitKey()



# percent_a=0
# percent_b=0

# #원본 파일 라인
# for i in range(16):
#     for j in range(16):
#         if ca[i][j] ==255:
#             percent_a+=1

# for i in range(16):
#     for j in range(16):
#         if cb[i][j]==255:
#             percent_b+=1


# print('percent_a : ', percent_a)
# print('percent_b : ', percent_b)

# rate_a=(percent_a/20880)*100  # 실제 노이즈 있는 이미지의 전체 대비 흰색 비율
# rate_b=(percent_b/20880)*100  # 실제 원본 이미지의 전체 대비 흰색 비율
# print('rate_a',rate_a)
# print('rate_b',rate_b)

# real_result=rate_a-rate_b
# real_result=100-real_result
# print('real_result ', real_result)

# sub=percent_a-percent_b #흰색간 개수 차이 계산후
# print('sub : ', sub)

# result=(sub/percent_b)*100  # 이것을 원본에 대비한 비율로 계산을 하여 
# result=100-result
# print('result = ',result)
# # 실제 비율 vs 원본에 대비한 비율로 계산하여 차이나는 비율의 정도? 로 등급을 산정 

# # print(result,"%") # 결과값


# if result>=70 and result<100:
#     print('A_class')
#     # return 'A'

# elif result >=40 and result<70:
#     print('B_class')
#     # return 'B'

# else:
#     print('C_class')
#     # return 'C'

