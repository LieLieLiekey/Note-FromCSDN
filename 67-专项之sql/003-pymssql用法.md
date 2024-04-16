

## pymssql用法



因为CSDN博客设置私密就不会再博客分类内看到，所以这篇文章只能设为公开的了。


conn是连接数据库后的hand

cursor是hand的游标 ，用于提交数据库的查询等信息

连接数据库

```python
    conn=pymssql.connect(host="127.0.0.1", #连接数据库
                         user="sa",
                         password="123",
                         database="stuManage",
                         charset="utf8")
```


执行查询语句并获得结果

```python
sql="select * from course"
cursor.execute(sql)#执行sql语句
rs=cursor.fetchall()#取结果
```


执行其他sql语句

```python
sql=''' drop table dch
        ''' 
cursor.execute(sql)
conn.commit()#提交创建信息
```


捕捉操作

```python
try:
	createTable(cursor)# 创建表dch
	# conn.commit()#提交创建信息
except pymssql.OperationalError as e :#捕捉操作异常
	print(e)
#捕捉所有异常
except Exception as e:
    print(e)
```


用表格打印查询结果

```python
sql="select * from course"
cursor.execute(sql)#执行sql语句
table=from_db_cursor(cursor)#直接使用PrettyTable的成员函数即可
print(table)


#也可以这样
table=PrettyTable(["课程号","课程名称","学号"])
rs=cursor.fetchall()#取结果
for i in rs:
    table.add_row(i)
```


类的静态成员变量和类成员函数

```python
class dch:
    dch_name=""  #这是类属性
	@classmethod
    def query(self):
        print("this class methon")
        
```


获取当前时间

```python
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#输出：2019-06-02 23:24:22
```


获取两时间之间有多少天

```python
ans=(datetime.datetime(2020,1,13,12,0,0) - datetime.datetime(2019,1,13,12,0,0)).total_seconds()/(24*60*60)
# 输出：365.0
```


