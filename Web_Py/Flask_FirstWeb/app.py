from flask import Flask, request, render_template, redirect, url_for, jsonify, json # 載入 flask


# 創建一個 app 的物件 並加入 Flask 這應用物件,將__name__ 作為引述傳入 Flask 類別 初始化時 傳入的 __name__ 參數，代表當前模組的名稱
app = Flask(__name__)
# 創建route ~/ GET or ~/hello
@app.route("/")
@app.route("/hello")
def hello():
    return "Hello,World!"
# URL 也可以成為函式接收的參數 String ~/data/appInfo/<string> GET
@app.route("/data/appinfo/<name>", methods = ["Get"])
def queryDataMessageByName(name):
    print("type(name) : ", type(name))
    return 'String => {}'.format(name)
# URL 也可以成為函式接收的參數 Int  ~/data/appInfo/id/5 GET
@app.route('/data/appInfo/id/<int:id>', methods = ['GET'])
def queryDataMessageById(id):
    print("type(id) : ", type(id))
    return 'int => {}'.format(id)
# 使用 Jinja2 的模板引擎 簡單的網頁格式 ~/text
@app.route('/text')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'
# # 創建 templates 資料夾，html 檔案放置於此
# 做網頁渲染 ~/home
@app.route('/home')
def home():
    return render_template('home.html')
# API 附帶參數 第二個參數可以附帶資料內容
@app.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask !")
# API 字典型態與頁面條件式 : @app.route('/page/app')
@app.route('/page/app')
def pageAppInfo():
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)
# API : 字典型態與頁面迴圈
@app.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('page.html', data=data)
# 前端開發的javascript與css 必須放在static資料夾才會生效
@app.route('/static')
def staticPage():
    return render_template('static.html')

# 使用Form表單進行資料傳輸
@app.route('/form')
def formPage():
    return render_template('form.html')
#  表單 Forms表單
@app.route('/submit', methods=['POST', 'GET'])
def formSubmit():
    if request.method == 'POST':
        user = request.form['user']
        print("post : user => ",user)
        return redirect(url_for('success', name=user, action="post"))
    else:
        user = request.args.get('user')
        print("get : user => ", user)
        return redirect(url_for('success', name=user, action="get"))
# 成功葉面
@app.route('/success/<action>/<name>')
def success(name, action):
    return '{} : Welcome {} ~ !!!'.format(action, name)
# 使用jQuery ajax 做資料傳遞
@app.route('/data')
def webapi():
    return render_template('data.html')
# 回傳結果
@app.route('/data/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        with open('static/data/message.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)  # 直接回傳 data 也可以，都是 json 格式
@app.route('/data/message', methods=['POST'])
def setDataMessage():
    if request.method == "POST":
        data = {
            'appInfo': {
                'id': request.form['app_id'],
                'name': request.form['app_name'],
                'version': request.form['app_version'],
                'author': request.form['app_author'],
                'remark': request.form['app_remark']
            }
        }
        print(type(data))
        with open('static/data/input.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)