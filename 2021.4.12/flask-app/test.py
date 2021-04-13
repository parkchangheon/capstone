from flask import Flask, render_template, request, Response


app = Flask(__name__)


@app.route("/test", methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        print(request.)

    return "test"


if __name__ == '__main__':
    app.run(host="192.168.185.103", port="5000", debug=True)
