#coding=utf-8
from flask import Flask,render_template,request     #导入Flask框架，render_template方法来渲染模板,为了返回一个html页面
import MySQLdb as mysql

db = mysql.connect(user='root',passwd='zzk123',host='localhost',db='memory')
db.autocommit(True)
cur = db.cursor()
app = Flask(__name__)    #创建Flask类的实例
import json         #使用json得到数据

@app.route('/')     #路由,route() 装饰器把一个函数绑定到对应的 URL 上
def index():
    return render_template('index.html')
#index()和data()函数返回想要显示在用户浏览器中的信息。一个返回了渲染文件index.html，一个去数据库查数据，返回json，供画图使用

tmp_time = 0
@app.route('/data')     # route()装饰器把一个函数绑定到对应的URL上，路由到对应的url
def data():
    global tmp_time     #第一次tmp_time等于0的时候，查询全部
    if tmp_time>0:
        sql = 'select * from memory where time>%s' % (tmp_time/1000)    #进行增量查询
    else:
        sql = 'select * from memory'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():            #获得查询后的新数据
        arr.append([i[1]*1000,i[0]])    #构造html模版需要的数据类型
    if len(arr)>0:
        tmp_time = arr[-1][0]       #取得新的时间戳
    return json.dumps(arr)          #通过json传递数据

if __name__=='__main__':
	app.run(host='0.0.0.0',port=9393,debug=True)
#用 run() 函数来让应用运行在本地服务器上
#其中 if __name__ == '__main__': 确保服务器只会在该脚本被 Python 解释器直接执行的时候才会运行，而不是作为模块导入的时候。


