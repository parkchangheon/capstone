#!/usr/bin/env python
# coding: utf-8

# In[107]:


from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
model = VGG16(weights='imagenet', include_top=False)
img_path = 'pic1.png'
img = image.load_img(img_path, target_size=(300, 300))
img_tensor=image.img_to_array(img)
img_tensor=np.expand_dims(img_tensor,axis=0)
img_tensor/=255.

print(img_tensor.shape)


# In[108]:


import matplotlib.pyplot as plt

plt.imshow(img_tensor[0])
plt.show()

print(img_tensor[0])


# In[109]:


from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
model = VGG16(weights='imagenet', include_top=False)
img_path2 = 'pic2.jpg'
img2 = image.load_img(img_path2, target_size=(300, 300))
img_tensor2=image.img_to_array(img2)
img_tensor2=np.expand_dims(img_tensor2,axis=0)
img_tensor2/=255.

print(img_tensor2.shape)


# In[110]:


import matplotlib.pyplot as plt

plt.imshow(img_tensor2[0])
plt.show()

print(img_tensor2[0])


# In[111]:


from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
model = VGG16(weights='imagenet', include_top=False)
img_path3 = 'data4.png'
img3 = image.load_img(img_path3, target_size=(300, 300))
img_tensor3=image.img_to_array(img3)
img_tensor3=np.expand_dims(img_tensor3,axis=0)
img_tensor3/=255.

print(img_tensor3.shape)


# In[112]:


import matplotlib.pyplot as plt

plt.imshow(img_tensor3[0])
plt.show()

print(img_tensor3[0])


# In[118]:


import cv2
def crash(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (500, 500))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (5,5), 0)
    canny = cv2.Canny(blurred_A, 10, 100,3)
    return canny


# In[119]:


res1=crash(img_path)
res2=crash(img_path2)
res3=crash(img_path3)

r1=img_tensor[0]
r2=img_tensor2[0]
r3=img_tensor3[0]


# In[123]:


import matplotlib.pyplot as plt

plt.imshow(r1)
plt.imshow(r2)
plt.imshow(r3)

plt.show()


# In[124]:


from numpy.linalg import norm
import numpy as np

def euclidean_distance(A,B):
    return np.linalg.norm(A-B)

doucument_1=r1
doucument_2=r2
doucument_3=r3

print(euclidean_distance(doucument_1,doucument_2))
print(euclidean_distance(doucument_1,doucument_3))  


# http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791186805091&orderClick=LEA&Kc=

# In[126]:


import dload


# In[127]:


origin=dload.save("http://image.kyobobook.co.kr/images/book/large/091/l9791186805091.jpg")


# In[128]:


origin


# In[130]:



from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import quote_plus
 
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어 입력: ') 
crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))
 
url = baseUrl + quote_plus(plusUrl) # 한글 검색 자동 변환
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img')
 
n = 1
for i in img:
    print(n)
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./images/img' + str(n)+'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
    if n > crawl_num:
        break
    
    


# In[ ]:


import cv2
from skimage.measure import compare_ssim
path_a="C:/Users/Justar/study/testing.jpg"
path_b="C:/Users/Justar/study/test_mybook.jpg"
path_c="C:/Users/Justar/study/test_book.jpg"
path_d="C:/Users/Justar/study/bluetest.png"
path_e="C:/Users/Justar/study/cat.jpg"
path_h="C:/Users/Justar/study/him.png"
path_hb="C:/Users/Justar/study/himb.jpg"
path_hc="C:/Users/Justar/study/himc.png"
path_f="C:/Users/Justar/study/fold.jpg"
imageA = cv2.imread(path_a)
imageB = cv2.imread(path_b)
imageC= cv2.imread(path_d)

def crash(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (500, 500))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (3,3), 0)
    #cv2.imshow("g", blurred_A)
    canny = cv2.Canny(blurred_A, 0, 150)
    return canny


#src_b = cv2.imread(path_b)
#gray_b = cv2.cvtColor(src_b, cv2.COLOR_BGR2GRAY)
#blurred_b = cv2.GaussianBlur(gray_b, (3,3), 0)
#canny_b = cv2.Canny(blurred_b, 100, 255)

#src_c = cv2.imread(path_d)
#gray_c = cv2.cvtColor(src_c, cv2.COLOR_BGR2GRAY)
#blurred_c = cv2.GaussianBlur(gray_c, (3,3), 0)
#canny_c = cv2.Canny(blurred_c, 100, 255)
canny_a=crash(path_c)
canny_b=crash(path_a)
canny_c=crash(path_d)
canny_d=crash(path_b)
canny_e=crash(path_e)
canny_h=crash(path_h)
canny_hb=crash(path_hb)
canny_hc=crash(path_hc)
canny_f=crash(path_f)
#cv2.imshow("standard", canny_a)

#cv2.imshow("crash", canny_b)
#cv2.imshow("cra&print", canny_c)

#cv2.imshow("canny_h", canny_h)
#cv2.imshow("canny_hb", canny_hb)
#cv2.imshow("canny_hc", canny_hc)
cv2.imshow("canny_f", canny_f)
cv2.waitKey(0)
#cv2.destroyAllwindows()

