import sys
import io
import os
# Imports the Google Cloud client library
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

from konlpy.tag import Okt
okt=Okt()


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'C:\Users\sean park\Desktop\python_venv\VisionAPIDemo\project-book-310818-ecc479cf4f22.json'
# Instantiates a client
client = vision_v1.ImageAnnotatorClient()

def title_check(file_name,mask): # file_name이 이미지, mask가 isbn 책 제목

    # The name of the image file to annotate

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    labels = response.text_annotations

    print('Labels:')


    mask='해커스 토익 Hackers Toeic' #isbn 책 제목으로 대체
    mask_noun=okt.nouns(mask)

    for i in mask_noun:
        tmp=i
        for label in labels:
            if label.description==i:
                print('동일')
                return True

    return False
