from flask import Flask, render_template, request, Response

from extract_book_info import extract_isbn, extract_title, image_parsing
from classify_book import check, evl
import cv2

app = Flask(__name__)


@app.route("/isbn", methods=['GET', 'POST', 'PUT'])
def get_image():
    #isbn = request.args.to_dict()['isbn']
    isbn = '9788961844338'
    print(isbn)
    bookinfo = extract_isbn(isbn)
    print(bookinfo)
    img = image_parsing(bookinfo['thumbnail'])
    cv2.imwrite('static/image/test2.jpeg', img)
    return render_template("result.html", image=bookinfo['thumbnail'])


@app.route("/distinguish", methods=['GET'])
def distinguish():
    canny_a = check('static/image/test2.jpeg')
    canny_b = check("static/image/origin.jepg")
    score, comment = evl(canny_a, canny_b)
    print(score, comment)
    return "test"


if __name__ == "__main__":
    app.run(host="192.168.109.103", port="5000", debug=True)
