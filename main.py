from flask import Flask, render_template, request, redirect, make_response
import datetime
from orm import model
from orm import ormmanage as manage



# app = Flask(__name__)
# 配置缓存更新时间
# 禁用缓存代码 需要导入datetime模块
# import datetime
# app.send_file_max_age_default = datetime.timelate(seconds=1)
# app.debug = True


@app.route("/")
def index():
    # b1 = model.Book()
    # b1.id = 1
    # b1.name = "小王子"
    # b1.price = 100
    b1 = model.Book(1, '快穿', 20)
    b2 = model.Book(2, '玄幻', 30)
    b3 = model.Book(3, '修仙', 40)
    b4 = model.Book(4, '种田', 50)
    # 判断用户是否登录过

    user = None
    user = request.cookies.get("name")
    if user:
        print("之前已经登陆过")
    else:
        print("之前没有登陆过")

    return render_template("index.html", booklist=[b1, b2, b3, b4], userinfo=user)


@app.route("/news/<int:num>")
def news(num):
    return render_template("news.html", newslist=["汪汪汪独家侦探社", "喵喵喵独家侦探社", "嘿嘿嘿侦探社"])


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # print(username, password)
        # print("收到POST请求，可以提取表单参数了")
        # return "注册成功"

        # 插入用户
        try:
            manage.insertUser(username, password)
            return redirect("/login")
        except:
            redirect("/register")

    elif request.method == "GET":

        # args = request.args
        # name = args.get("username")
        # value1 = args.get("value1")
        # print(name, value1)
        # print("收到GET请求，返回注册页面")
        return render_template("register.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        # print("GET请求，进入登录页面")
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # 查询匹配数据库
        print(username, password)
        # 内容需要查询数据库
        # 第一种不带接口
        # return render_template("/Videolist.html", videolist=['aa', 'bb', 'cc', 'dd'])
        # 第二种 带接口 重定向
        # 自动在URL 发起请求，请求list

        # 为了让响应可以携带头信息，需要构造响应
        # return render_template("/Videolist")
        try:
            result = manage.checkUser(username, password)
            res = make_response(redirect('/Videolist'))
            res.set_cookie('id', username, expires=datetime.datetime.now()+datetime.timedelta(days=7))
            return res
        except:
            return redirect('/login')


@app.route("/quit")
def quit():
    res = make_response(redirect('/'))
    res.delete_cookie("name")
    return res


@app.route("/Videolist", methods=["POST", "GET"])
def Videolist():
    # 新增代码
    user = None
    user = request.cookies.get("name")
    # 内容需要查询数据库
    return render_template("Videolist.html", videolist=['aa', 'bb', 'cc', 'dd'], userinfo = user)


@app.route("/details/<id>")
def details(id):
    print("当前商品为", id)
    user = None
    user = request.cookies.get("name")
    # 从数据库查询商品详情
    return render_template("details.html", details= "这个视频是描述学习的", id=id, userinfo=user)


if __name__ == "__main__":
    app.run()

