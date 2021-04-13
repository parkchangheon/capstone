from kakao_api import searchByIsbn, searchByTitle
import cv2
import numpy as np
import json
import requests


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
