import urllib
import requests
import json


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
