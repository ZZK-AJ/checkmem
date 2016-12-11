#coding=utf-8
import time    
import MySQLdb as mysql  #导入mysql数据库模块

db = mysql.connect(user="root",passwd="zzk123",db="memory",host="localhost")  #连接数据库
db.autocommit(True)  #自动commit
cur = db.cursor()   #获得数据库游标

def getMem():
	with open('/proc/meminfo') as f:     #linux下全部都是文件，内存信息也是在这个文件中的
		total = int(f.readline().split()[1])        #首先readline方法读取一行，使用split方法分割取出第二个值，默认空格分割
		free = int(f.readline().split()[1])         #使用int()函数把他们变成数字
		available = int(f.readline().split()[1])
		buffers = int(f.readline().split()[1])
		cache = int(f.readline().split()[1])
	memuse = total-free-buffers-cache  #计算使用了多少内存
	t = int(time.time())		#获得时间戳
	sql = 'insert into memory (memory,time) value (%s,%s)'%(int(memuse)/1024,t)		#插入的sql语句
	cur.execute(sql)		#使用游标，execute方法执行SQL语句
	print int(memuse)/1024
	print 'ok'

while True:
	time.sleep(3)
	getMem()


