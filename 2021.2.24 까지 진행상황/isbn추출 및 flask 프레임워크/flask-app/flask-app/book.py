from flask import Flask, render_template, request

import urllib
import requests
import json
import pandas as pd
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
#from skimage.measure import compare_ssim


def search(title):
    api_key = "6e86171d42e3de80275a5239293e6c93"  # REST api key
    # Kakao API URL (ISBN기반 검색)
    url = "https://dapi.kakao.com/v3/search/book?target=isbn"
    query = "&query=" + urllib.parse.quote(title)
    request = urllib.request.Request(url+query)
    # api key 헤더 추가
    request.add_header("Authorization", "KakaoAK "+api_key)

    response = urllib.request.urlopen(request)
    status_code = response.getcode()

    if status_code == 200:  # 200 OK
        return response.read().decode('utf-8')
    else:  # 예외 ? .. 음
        return status_code


def extract(isbn):
    res = search(isbn)
    tmp = json.loads(res)
    doc = tmp['documents']
    # return doc[0]['thumbnail']
    return doc[0]


def image_parsing(url):
    image_nparray = np.asarray(
        bytearray(requests.get(url).content), dtype=np.uint8)
    image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    #cv2.imshow('Image from url', image)
    # cv2.waitKey(0)
    return image

######################


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('searchForm.html')

# 입력받은 ISBN을 쿼리로 하여 API호출
# API로부터 필요 데이터 받아옴
# 이미지는 데이터 파싱 후 리소스 폴더에 저장
@app.route('/book', methods=['GET', 'POST'])
def getBookInfoAndRendering():
    if request.method == 'POST':
        isbn = request.form
        # 9788996991342 - 미움받을 용기
        # 9791190313186 - 지적 대화를 위한 넓고 얕은 지식 1
        # 9788935305292 - 파이썬을 사용한 프로그래밍 입문
        bookinfo = extract(isbn['isbn'])  # ISBN으로 책 검색, 이미지 URL 추출
        test_image = image_parsing(bookinfo['thumbnail'])  # 이미지 URL 파싱
        cv2.imwrite('static/image/test2.jpeg', test_image)  # 파싱된 이미지URL 파일로 저장

        return render_template("result.html", title=bookinfo['title'], image=bookinfo['thumbnail'], contents=bookinfo['contents'])

'''
이게 웹캠 띄우는 부분인데 잘 안됨 .. 해결좀 ...
'''
@app.route('/scan')
def scanningISBN():

    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if success:
            cv2.imshow('cam', frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
