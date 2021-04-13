from flask import Flask, render_template, request, Response

import urllib
import requests
import json
import pandas as pd
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
from flask import jsonify
import io
import PIL.Image as Image
import matplotlib.pyplot as plt
# from skimage.measure import compare_ssim


def gen_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()
    cv2.destroyAllWindows()


def searchByTitle(title):
    api_key = "-"  # REST api key
    # Kakao API URL (ISBN기반 검색)
    url = "https://dapi.kakao.com/v3/search/book?target=title"
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


def searchByIsbn(isbn):
    api_key = "-"  # REST api key
    # Kakao API URL (ISBN기반 검색)
    url = "https://dapi.kakao.com/v3/search/book?target=isbn"
    query = "&query=" + urllib.parse.quote(isbn)
    request = urllib.request.Request(url+query)
    # api key 헤더 추가
    request.add_header("Authorization", "KakaoAK "+api_key)

    response = urllib.request.urlopen(request)
    status_code = response.getcode()

    if status_code == 200:  # 200 OK
        return response.read().decode('utf-8')
    else:  # 예외 ? .. 음
        return status_code


def extract_isbn(isbn):
    res = searchByIsbn(isbn)
    tmp = json.loads(res)
    doc = tmp['documents']
    # return doc[0]['thumbnail']
    return doc[0]


def extract_title(title):
    res = searchByTitle(title)
    tmp = json.loads(res)
    doc = tmp['documents']
    # return doc[0]['thumbnail']
    return doc[0]


def image_parsing(url):
    image_nparray = np.asarray(
        bytearray(requests.get(url).content), dtype=np.uint8)
    image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
    # cv2.imshow('Image from url', image)
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
@app.route('/book_isbn', methods=['GET', 'POST'])
def getBookInfoAndRenderingByIsbn():
    if request.method == 'GET':
        isbn = request.values
        # 9788996991342 - 미움받을 용기
        # 9791190313186 - 지적 대화를 위한 넓고 얕은 지식 1
        # 9788935305292 - 파이썬을 사용한 프로그래밍 입문
        bookinfo = extract_isbn(isbn['isbn'])  # ISBN으로 책 검색, 이미지 URL 추출
        test_image = image_parsing(bookinfo['thumbnail'])  # 이미지 URL 파싱
        # cv2.imwrite('static/image/test2.jpeg', test_image)  # 파싱된 이미지URL 파일로 저장

        return render_template("result.html", image=bookinfo['thumbnail'])


@app.route('/book_title', methods=['GET', 'POST'])
def getBookInfoAndRenderingByTitle():
    if request.method == 'POST':
        title = request.form
        bookinfo = extract_title(title['title'])
        test_image = image_parsing(bookinfo['thumbnail'])  # 이미지 URL 파싱
        # cv2.imwrite('static/image/test2.jpeg', test_image)  # 파싱된 이미지URL 파일로 저장

        return render_template("result.html", image=bookinfo['thumbnail'])


@app.route("/image", methods=['GET', 'POST'])
def imagetest():
    if request.method == 'GET':
        image_dict = request.args.to_dict()

    elif request.method == 'POST':
        data = str(request.values)
        encoded_img = np.fromstring(data, dtype=np.uint8)
        print(encoded_img)
        img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
        print(img)
    return "test"


@app.route("/image2", methods=['GET', 'POST', 'PUT'])
def imagetest2():
    with open('static/image/testimg.jpeg', 'rb') as f:
        testimg1 = f.read()
    print(len(testimg1))
    encoded_img1 = np.fromstring(bytes(testimg1), dtype=np.uint8)
    print("저장된 테스트 이미지 : ", encoded_img1)
    image = Image.open(io.BytesIO(encoded_img1))

    # encoded_img2 = np.fromstring(file, dtype=np.uint8)
    # print("앰 인벤터에서 넘어온 이미지 : ", encoded_img2)
    # image = Image.open(io.BytesIO(encoded_img2))
    return "test"


@app.route("/isbn", methods=['GET', 'POST', 'PUT'])
def isbntest():
    isbn = request.args.to_dict()['isbn']
    bookinfo = extract_isbn(isbn)
    image = image_parsing(bookinfo['thumbnail'])

    return render_template("result.html", image=bookinfo['thumbnail'])


if __name__ == "__main__":
    app.run(host="-", port="5000", debug=True)
    # app.run(debug=True)
