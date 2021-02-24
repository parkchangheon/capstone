from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello world!!'

# 라우팅
@app.route('/test')
def test1():
    return 'test!'

# 동적 URL 라우팅
@app.route("/test/<param>")
def test2(param):
    return f'Test - {param}'

# HTML  렌더링
@app.route('/test3')
def test3():
    return '''
    <h1>Hello!!</h1>
    <p>안녕하세용</p>
    '''

# 템플리 렌더링 (Jinja2 템플릿)
# templates폴더 이하 html파일을 랜더링
@app.route('/jinja2')
def jinja():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)  # debug=True : 변경감지


'''
Note

서버실행 : python app.py

'''
