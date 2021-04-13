from flask import Flask, render_template, request, url_for
import pyzbar.pyzbar as pyzbar

from flask_restful import Resource,Api,reqparse, abort

import urllib
import requests
import json
import pandas as pd
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
from werkzeug.utils import secure_filename, redirect
import os
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

from app001 import routes



def check(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (500, 500))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (3,3), 0)
    #cv2.imshow("g", blurred_A)
    canny = cv2.Canny(blurred_A, 0, 150)
    return canny


def cannycompare(a,b):
    (score, diff)=compare_ssim(a, b, full=True)
    diff = (diff*255).astype("uint8")
    print(f"Simlarity:{score:.5f}")
    assert score, "못찾음"
    return score

def evl(a,b):
    tmp=cannycompare(a,b)
    return tmp



ca=check('book1.jpg')
cb=check('book2.jpg')

percent_a=0
percent_b=0

print('start')
print(ca.shape)
print(ca.size)

print(cb.shape)
print(cb.size)


#####################################
score=evl(ca,cb)*100

print('score = ', score)

if score>=50:  #compare_ssim 유사도 측정


    #원본 파일 라인
    for i in range(500):
        for j in range(500):
            if ca[i][j] ==255:
                percent_a+=1




    for i in range(500):
        for j in range(500):
            if cb[i][j]==255:
                percent_b+=1



    sub=percent_b-percent_a

    result=(sub/25000)*100
    result=100-result

    print(result,"%")


    if result>=80 and result<100:
        print('A_class')

    elif result >=50 and result<80:
        print('B_class')

    else:
        print('C_class')


    plt.imshow(ca)
    plt.show()



