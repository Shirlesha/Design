from flask import Flask, render_template, request, redirect, make_response
import datetime
from orm import model1
from orm import ormmanage1


# app = Flask(__name__)
# 配置缓存更新时间

@app.route("/")
def index1():
    g1 = model1.Goods(1, '视频1', 100, 100)
    g2 = model1.Goods(2, '视频2', 200, 200)
    g3 = model1.Goods(3, '视频3', 300, 300)

    # 判断用户是否登录过
    user = None
    user = request.cookies.get("name")
    if user:
        print("之前已经登录过")
    else:
        print("之前没有登录过")
    return render_template("index1.html", goodslist=[g1, g2, g3], userinfo=user)


@app.route("/login1", methods=['POST', 'GET'])
def login1():
    if request.method == "GET":
        return render_template("login1.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # 查询匹配数据库
        #
        #
        #

        # 带接口 重定向
        # 自动在URL 发起请求，请求list

        # 为了让响应可以携带头信息，需要构造响应
        # return render_template("/Goodslist")
        try:
            result = manage.checkUser(username, password)
            res = make_response(redirect('/Goodslist'))
            res.set_cookie('id', username, expires=datetime.datetime.now()+datetime.timedelta(days=7))
            return res
        except:
            return redirect('/login1')





