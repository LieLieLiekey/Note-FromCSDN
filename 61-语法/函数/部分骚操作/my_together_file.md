

## selenium的入门使用


可以参考博客：[https://www.cnblogs.com/feng0815/p/8334144.html](https://www.cnblogs.com/feng0815/p/8334144.html)

```python
from selenium import webdriver #selenium的webdriver类的功能
import time
import os
#0.创建一个浏览器页，使用驱动
driver=webdriver.Chrome(executable_path=r'C:\Users\12495\Desktop\chromedriver.exe')
#1.用该浏览器打开页面
driver.get(r'http://www.baidu.com')
#2.向对应id的表格发送信息
driver.find_element_by_id("kw").send_keys("Python牛逼")
#3.向对应id点击
driver.find_element_by_id("su").click()
#4.获取页面源码
HtmlString=driver.page_source
#5.获取当前浏览器的cookies
CookiesList=driver.get_cookies()
# print(CookiesList)
#6.把cookies的name和value提取出来，作为键值对
cookies={}
for i in CookiesList:
    cookies[i["name"]]=i["value"]
print(cookies)
# time.sleep(3)
# driver.close()
```




## xpath语法


#### 前言：


处理规则数据例如json类数据就就需json模块提取

处理不规则数据例如html代码的数据一般使用正则表达式或者lxml提取。

而lxml模块需要了解xpath语法，故xpath语法及其重要

#### Xpath的节点和语法以及基本使用请参考W3school：[http://www.w3school.com.cn/xpath/xpath_syntax.asp](http://www.w3school.com.cn/xpath/xpath_syntax.asp)


#### 1.什么是xpath


XPath (XML Path Language) 是一门在 HTML\XML 文档中查找信息的**语言**，可用来在 HTML\XML 文档中对**元素和属性进行遍历**。

#### ​2.认识xmL


```
<bookstore>
<book category="COOKING">
  <title lang="en">Everyday Italian</title> 
  <author>Giada De Laurentiis</author> 
  <year>2005</year> 
  <price>30.00</price> 
</book>
<book category="CHILDREN">
  <title lang="en">Harry Potter</title> 
  <author>J K. Rowling</author> 
  <year>2005</year> 
  <price>29.99</price> 
</book>
<book category="WEB">
  <title lang="en">Learning XML</title> 
  <author>Erik T. Ray</author> 
  <year>2003</year> 
  <price>39.95</price> 
</book>
</bookstore>
```


### 3.下面引用W3school中对于xpath的语法，已经是非常常用的！


#### 下面列出了最有用的路径表达式：

表达式描述nodename选取此节点的所有子节点。/从根节点选取。//从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。.选取当前节点。…选取当前节点的父节点。@选取属性。

#### 实例


在下面的表格中，我们已列出了一些路径表达式以及表达式的结果：
路径表达式结果bookstore选取 bookstore 元素的所有子节点。/bookstore选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！bookstore/book选取属于 bookstore 的子元素的所有 book 元素。//book选取所有 book 子元素，而不管它们在文档中的位置。bookstore//book选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。//@lang选取名为 lang 的所有属性。

### 谓语（Predicates）


谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

#### 实例


在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：
路径表达式结果/bookstore/book[1]选取属于 bookstore 子元素的第一个 book 元素。/bookstore/book[last()]选取属于 bookstore 子元素的最后一个 book 元素。/bookstore/book[last()-1]选取属于 bookstore 子元素的倒数第二个 book 元素。/bookstore/book[position()❤️]选取最前面的两个属于 bookstore 元素的子元素的 book 元素。//title[@lang]选取所有拥有名为 lang 的属性的 title 元素。//title[@lang=‘eng’]选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。/bookstore/book[price>35.00]选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。/bookstore/book[price>35.00]/title选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

### 选取未知节点


XPath 通配符可用来选取未知的 XML 元素。
通配符描述*匹配任何元素节点。@*匹配任何属性节点。node()匹配任何类型的节点。

#### 实例


在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：
路径表达式结果/bookstore/*选取 bookstore 元素的所有子元素。//*选取文档中的所有元素。//title[@*]选取所有带有属性的 title 元素。

### 选取若干路径


通过在路径表达式中使用“|”运算符，您可以选取若干个路径。

#### 实例


在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：
路径表达式结果//book/title | //book/price选取 book 元素的所有 title 和 price 元素。//title | //price选取文档中的所有 title 和 price 元素。/bookstore/book/title | //price选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。

##### 


##### 对于Python中xpath的使用请看下一章：




#### Python之使用requests.session进行会话保持



前面使用手动的方式使用cookie，那么有没有更好的方法在requets中处理cookie呢？


requests 提供了一个叫做session类，来实现客户端和服务端的`会话保持`

会话保持有两个内涵：

+ 保存cookie，下一次请求会带上前一次的cookie+ 实现和服务端的长连接，加快请求速度

1. 使用方法

```python
session = requests.session()
response = session.get(url,headers)
```


session实例在请求了一个网站后，对方服务器设置在本地的cookie会保存在session中，下一次再使用session请求对方服务器的时候，会带上前一次的cookie

##### `session对象的方法与requests的方法相同`


下面用Python模拟登陆人人网的例子来练习seesion类的使用：

项目链接：[使用session模拟登陆人人网](https://blog.csdn.net/Dch19990825/article/details/87470615)



## Python的自列表的定义排序


因是c++Acmer，故经常用到自定义排序

#### 第一种方法：对小于号进行重载



因为所有比较都可通过小于号的结果进行推导


```python
class Dch:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def __str__(self):
        return "first={},second={}".format(self.first,self.second)
    def __lt__(self, other):
        if (self.first == other.first):
            return int(self.second < other.second)
        return int(self.first < other.first)
    # isinstance(100,int)
aa=Dch(1,2)
bb=Dch(100,1)
cc=Dch(50,50)
dd=Dch(30,-1)
ee=Dch(1,20)
Mylist=[aa,bb,cc,dd,ee]
Mylist=sorted(Mylist)
for i in range(len(Mylist)):
    print(Mylist[i])
```


输出：


first=1,second=2 first=1,second=20 first=30,second=-1 first=50,second=50 first=100,second=1


## 其他的暂时没实践过哦




## 

   Python学习笔记 
 


**已经有c语言基础**

#### 基础语法规则：


+  
##### 数据类型
 字符串是以单引号’或双引号"括起来的任意文本，比如’abc’，“xyz"等等。请注意，’'或”"本身只是一种表示方式，不是字符串的一部分，如果字符串内部既包含’又包含"怎么办？可以用转义字符\来标识。 Python还允许用r’‘表示’‘内部的字符串默认不转义，即原始字符串 EG： print(r’\\t\’) 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用’’’…’’'的格式表示多行内容，可以自己试试： +  
##### 变量名规则与c语言变量命名规则一致
 +  
##### 强制转换方法
 
```
int()//转化为int
float()
str()//转化为str
chr()//int转化为字符
ord()//得到字符对应的ASSIC码值(含中文字符)
list()//字符串转化为一个列表
```
 +  
##### 基本输入输出
 1.输入函数:str_return=input(str) ​ 解释：str为一个提示信息 ,让用户输入一个一行字符串,直至遇到回车结束 并且把该字符串返回到 ​ str_return. 2.输出函数:print(“name”，500，50.7，u“哈哈哈”) 输出对应的列表 遇见逗号输出空格,结尾输出空行 +  
##### 条件语句
 
```python

if  条件:
    语句
elif 条件:
    语句
else：
    语句
#注意缩进用四个空格     注意冒号

    
```
 +  
##### 循环语句
 
```python
#for循环开头需要
for  a in List:
    语句
#while循环开头需要
while 条件 ：
	语句
#注意缩进用四个空格     注意冒号
```
 +  
##### 定义函数
 
```python
def fuctionname(参数表):
	内容
#注意缩进用四个空格     注意冒号
```
 +  
##### 逻辑符号
 逻辑符号有 and or not ,分别表示 && || ！ +  
##### 用#注释 与c语言的//意思近似
 


#### 学习列表：


+  
##### str的成员函数split
 str.split(char c,int num) 让一个字符串根据c字符切片，成num个字符串 返回一个列表 可以不指定Num 和c(默认空格) 1.如果不指定c 和num 则默认空格 而且可以连续分隔多个空格 2.如果指定c 不指定num 则默认分割数个字符串 否则的话则分割前Num个字符串 剩下的都在在最后一个元素 3.如果指定c ，则不能连续分割开，会产生空串 +  
##### 占位符用来输出函数
 str.format(输出项目列表) 
```python
num1,operator,num2=input('Enter calculation:').split(' ')
num1=int(num1)
num2=int(num2)
if operator =='+':
    print('{}+{}={}'.format(num1,num2,num1+num2))
```
 +  
##### print函数自动换行
 如果要取消的话在最后设定一个输出项 
```bash
print(u‘漂亮’,end='',sep="")
#sep为隔开字符(sperate) end为结束字符
```
 +  
##### range函数
 range(num) 即函数产生一个列表 列表第一个元素从0开始 道num-1结束 共有num个 range(beg,endd) 左开右闭区间 从beg开始 到endd-1结束 共 endd-begg个 range(beg,endd,space)区间 范围为[beg,endd) 从beg开始 增量为space range(num)与range(0,num)与range(0,num,1)相同 +  
##### 字符串的索引和切片
 str[index]//索引 str[beg:endd]//区间 str[beg:endd,space]//区间以及递增量 +  
##### 字符串的去空格函数AND字符串大小写转化函数AND字符串查找函数ANDcount函数
 str.strip()//左右两边去空格 str.lstrip()//左边去空格 str.rstrip()//右边去空格 str.upper()// 将str全部转化为大写 str.lower()//将str全部转化为小写 str.count(str)//返回字符串有多少个str str.isdight()//是否为一个数字 str.isalnum()//是否为一个数字 +  
##### 列表的连接
 str.join(list)//表示用str 把列表list里面的连接起来 +  
##### 列表的函数
 list.sort()//引用排序 list.reverse()//引用反转 list.insert(int sub,val) list.remove(val)//删除val 但是只删除一个 从左到右数的第一个 list.append(val)//追加 list.pop()//弹出一个 可以指定一个下标 list+list //列表的合并 list*num list[index]用索引进行读取 print(list)输出列表 
```python
randlist = ["string",1.234,28]
print(randlist)
#['string', 1.234, 28]
```
 +  
##### 列表的切片
 像字符串的切片相同推广 +  
##### 用for循环产生列表
 例子 
```python
#生成一个平方数列表
MyList=[i*i for i in range(10)]
print(MyList)
#生成一个列表，共有10个元素，每个元素又是一个10的列表  相当于10*10的二维数组
MyList=[[0]*10 for i in range(10)]
print(MyList)
```
 +  
##### 导入内置模块
 import （名称） 例子： import random 导入随机种子的包(产生随机数) 成员函数: random.randrange(beg,end)//返回一个数字 random.choice(list)//从列表中随机选一个 +  
##### 元组
 定义 使用小括号 意义 定义后不可被改变 tup=(9,2,1,3,4,7,3)//元素值都不能变的 +  
##### 内置函数 在Python官网查看
 max()//求列表 或远足的最大值 sorted()//返回排序的结果列表 +  
##### 定义函数传入多个参数
 
```python
# 代表接受多个多个参数  传参进去代表多个参数  变为一个列表
def GetSum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
MyList=[i for i in range(10)]
#加个*列表名(元组名) 代表将其变为多个数
print(GetSum(*MyList))
```
 函数可以返回多个： 
```bash
def mult_divide(num1,num2):
    return (num1*num2),num1/num2
#返回 两个数的乘法结果和除法结果
```
 函数内定义的变量为局部变量： 而global name 可以代表这里的name为外面的name 
```python
def change_name():
    #代表name在外边的
    global name
    name="Tom"
name="Tery"
print(name)
change_name()
print(name)
```
 +  
##### 内置模块之 math
 将math看作一个对象调用内容的方法就行 具体方法请用help(math)或者到官网查看 +  
##### dict字典(dictionary)
 **初始化方法** dictName={key1:val1,key2,val2} dictName={} 代表空字典 **添加方法** ​ dictName.setdefault(key,default)//如果有的话不操作 没有的话设置默认值 并且返回内容值 ​ dictName[key]=val **删除方法** ​ del dictName[key] //没有返回值 没有则报错 **查找方法** ​ dicttName.get(key,default)//有的话返回 没有的话返回默认值 ​ key in dictName : 返回为真则存在 否则Flase **清除容器** ​ dictName.clear()// **返回所有key值** ​ dictName.keys()//列表？ **返回所有内容值** ​ dicttName.values()//列表 +  
##### 内置模块之pprint
 可以打印字典 +  
##### 集合(set)
 **空集合** setname=set() **初始化** setname{name,name,name} **添加:** setname.add() **删除** setname.discard()//删除 没有也不会报错 setname.remove()//待测试 **查找** pass **遍历集合** for val in setname: **集合的 并 交 异或（吧）** 
```python
numbers1={1,2,3,4,5}
numbers2={1,3,4,6}
# 并  交  异或
print(numbers1 | numbers2)
print(numbers1 & numbers2)
print(numbers1 - numbers2)
```
 +  
##### 抛出异常的例子
 
```python
#输出图形
def boxPrint(symbol,width,height):
        # if不符合要求  抛出异常  相当于c++的throw what;
    if len(symbol)!=1:
        raise Exception("Symbol must be a single character")
    if width<=2:
        raise Exception("Width must be greater than 2")
    if height<=2:
        raise Exception("Height must be greater than 2")
    print(symbol*width)
    for i in range(height-2):
        print(symbol," "*(width-2),symbol,sep="")
    print(symbol * width)
for symc,w,h in(('a',10,10),("zz",2,2)):
    try:
        boxPrint(symc,w,h)
    except Exception as err:
        print("NameError:",err)
```
 +  
##### 捕捉异常
 
```python
def spam(divideby):
    try:
        return 42/divideby
    except :
        print(u"除数不能为0")
spam(0)
#不存在文件
try:
    fp=open("date.txt")
except :
    print("The file not exit!")
bad_var="dsaddas"
try:
    var=bad_var
#     自动捕捉错误名称 并且作为字符串赋给e
except NameError as e:
    print(e)
#     如果没有异常 执行否则
else:
    print(var)
#     最后都执行的
finally:
    print("Executing Finally....")
```
 




## Python之lxml模块的etree类的使用


#### 前言：



有关xptah语法可在W3school中查看或者在上一篇博客查看

+ lxml的安装与etree类的导入+ 将html字符串转化为Element对象，且elment对象的方法+ element对象的xptah方法



#### 1.lxml模块的安装


安装方式：在终端cmd下利用pip命令安装即可（保证网络畅通）

`pip install lxml`

#### 2.element对象


element对象是xpath语法的使用对象，element对象可由html字符串转化

+  利用etree.HTML()将html字符串转化为element对象 , 
```python
from lxml import etree
MyStr = '''<meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    '''
HtmlElement = etree.HTML(MyStr) 
print(type(HtmlElement))
#<class 'lxml.etree._Element'>
```
 +  将element对象转化为字符串 etree的tostring方法可以将element转化为二进制类型。故**需要用encoding属性指定编码方法**，否则可能会造成乱码。 **且此方法会使原来不规则的html字符串补全为规则的html** 
```python
HtmlStr=etree.tostring(HtmlElement,encoding="utf-8").decode()
print(HtmlStr)
```
 输出： 
```
<html><head><meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE"/>
    <meta http-equiv="Pragma" content="no-cache"/>
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT"/>
    </head></html>
```
 


#### 3.element对象的xpath方法


利用etree.HTML，将字符串转化为Element对象,Element对象具有xpath的方法,返回结果的列表，能够接受bytes类型的数据和str类型的数据

```python
html = etree.HTML(text) 
ret_list = html.xpath("xpath字符串")
```


+  如果xpath取的*标签的属性*，则返回字符串的列表 
```python
#取MyStr中link标签的href属性
from lxml import etree
MyStr = '''<meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">

    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/bf61b1fa02f564a4a8f809da7c7179b883a56146/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/92c148e64e4f81dc6fad7f3355308ee8cacecd92/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js">
    '''
HtmlElement = etree.HTML(MyStr)
EleList = HtmlElement.xpath("//link/@href")  # 这样匹配列表中的每个元素都是字符串
print(EleList)
```
 输出： 
```
['https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png', 'https://img3.doubanio.com/f/shire/bf61b1fa02f564a4a8f809da7c7179b883a56146/css/douban.css', 'https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css', 'https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css']
```
 +  如果xpath取标签，则返回element元素的列表 
```python
from lxml import etree

MyStr = '''<meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">

    <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img3.doubanio.com/f/shire/bf61b1fa02f564a4a8f809da7c7179b883a56146/css/douban.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
    <link href="https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
    <script type="text/javascript">var _head_start = new Date();</script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/92c148e64e4f81dc6fad7f3355308ee8cacecd92/js/douban.js"></script>
    <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js">
    '''
HtmlElement = etree.HTML(MyStr)
EleList = HtmlElement.xpath("//link[@ href]")  # 这样匹配列表中的每个元素都是element元素
print(EleList)
```
 输出： 
```
[<Element link at 0xb2e7d8>, <Element link at 0xb2e7b0>, <Element link at 0xb2e788>, <Element link at 0xb2e760>]
```
 


##### 4.补充


**lxml的高阶使用：**当提取标签的多种属性时，可以分组提取相应的标签，在对每个标签进行处理即可，这样可防止有些标签没有相应的属性，导致信息列表对应错误

剩下的都是xpath语法的使用了，只需深入了解xpath语法即可

##### 相关项目：[实战-爬取豆瓣评分高于指定值的电影信息](https://blog.csdn.net/Dch19990825/article/details/87726785)




## Python之json模块的使用


**JSON：JavaScript 对象表示法（JavaScript Object Notation）。**

**JSON 是存储和交换文本信息的语法。类似 XML。**

**JSON 比 XML 更小、更快，更易解析。**


W3school链接：[http://www.w3school.com.cn/json/index.asp](http://www.w3school.com.cn/json/index.asp)


在Python中，数据内容可转化为json字符串，json是字符串类型。不过它长这个样子

```python
import json
Mylist=[1,2,3,"nice"]
print(type(json.dumps(Mylist)))
print(json.dumps(Mylist))
```


输出：


<class ‘str’> [1, 2, 3, “nice”]


可见json字符串可以用来储存python的数据信息

JSON 值可以是：

+ 数字（整数或浮点数）+ 字符串（在双引号中）+ 逻辑值（true 或 false）+ 数组（在方括号中）+ 对象（在花括号中）+ null


## Python主要有四个方法，其中dumps和loads方法最常用


```python
#json.dumps 实现python类型转化为json字符串
#indent实现换行和空格
#ensure_ascii=False实现让中文写入的时候保持为中文
json_str = json.dumps(mydict,indent=2,ensure_ascii=False)

#json.loads 实现json字符串转化为python的数据类型
my_dict = json.loads(json_str)


#json.dump 实现把python类型写入类文件对象
with open("temp.txt","w") as f:
    json.dump(mydict,f,ensure_ascii=False,indent=2)

# json.load 实现类文件对象中的json字符串转化为python类型
with open("temp.txt","r") as f:
    my_dict = json.load(f)
```


##### 相关项目链接：[Python之豆瓣华语新歌榜数据提取](https://blog.csdn.net/Dch19990825/article/details/87706172)




## Python正则表达式re的复习


以下有部分参考传智播客的学习资料：

#### 1. 什么是正则表达式



用事先定义好的一些特定字符、及这些特定字符的组合，组成一个**规则字符串**，这个**规则字符串**用来表达对字符串的一种**过滤**逻辑。


#### 2. 正则表达式的常见语法



收藏博客链接：[https://www.cnblogs.com/yyyg/p/5498803.html](https://www.cnblogs.com/yyyg/p/5498803.html)


这里不再赘述。

#### (1).其中贪婪匹配和非贪婪匹配需要重点强调一下


上面提到贪婪匹配和非贪婪匹配请看例子：

```python
import re
#贪婪
ret_greed= re.findall(r'a(\d+)','a23b')
print(ret_greed)
#非贪婪
ret_no_greed= re.findall(r'a(\d+?)','a23b')
print(ret_no_greed)
 
['23']
['2']
```


由于贪婪匹配为尽可能的多匹配所以结果为23 ：

#### (2). 分组与不分组


被括起来的表达式作为一个分组. findall 在有组的情况下只显示组的内容

```python
#不分组下
import re
ret=re.findall("a.*?bc","abcbcd,n",re.S)#在re.s的模式下.号匹配换行符 ，返回匹配列表
print(ret)
```


输出：


[‘abc’]


```python
#分组情况下
import re
MyStr='''
name="Tom",age="18"
name="Hia",age="50"
'''
ret=re.findall(r'name="(.*?)".*?age="(\d+?)"',MyStr)
print(ret)
```


输出：


[(‘Tom’, ‘18’), (‘Hia’, ‘50’)]


#### 3. re模块的常见方法



+  pattern.match（从头找一个） +  pattern.search（找一个） +  pattern.findall（找所有） +  返回一个列表，没有就是空列表 +  `re.findall("\d","chuan1zhi2") >> ["1","2"]` +  pattern.sub（替换） +  `re.sub("\d","_","chuan1zhi2") >> ["chuan_zhi_"]` +  re.compile（编译） +  返回一个模型P，具有和re一样的方法，但是传递的参数不同 +  匹配模式需要传到compile中 
```python
p = re.compile("\d",re.S)
p.findall("chuan1zhi2")
```
 



#### 4. python中原始字符串r的用法



原始字符串定义(raw string)：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符，原始字符串往往针对特殊字符而言。例如`"\n"`的原始字符串就是`"\\n"`

+ 原始字符串的长度


```python
  In [19]: len("\n")
  Out[19]: 1

  In [20]: len(r"\n")
  Out[20]: 2

  In [21]: r"\n"[0]
  Out[21]: '\\'
```


+ 正则中原始字符串的使用


```python
  In [13]: r"a\nb" == "a\\nb"
  Out[13]: True

  In [14]: re.findall("a\nb","a\nb")
  Out[14]: ['a\nb']

  In [15]: re.findall(r"a\nb","a\nb")
  Out[15]: ['a\nb']

  In [16]: re.findall("a\\nb","a\nb")
  Out[16]: ['a\nb']

  In [17]: re.findall("a\\nb","a\\nb")
  Out[17]: []

  In [18]: re.findall(r"a\\nb","a\\nb")
  Out[18]: ['a\\nb']
```



##### 相关项目链接：[Python项目之爬取斗图网所有图片](https://blog.csdn.net/Dch19990825/article/details/83503917)




## Python的部分函数


+  pprint函数 效果：输出更直观，对列表和字典的嵌套效果较为明显 
```python
#普通print输出
d1={"name":"Tom","age":19}
mylist=[]
for i in range(5):
    mylist.append(d1.copy())
print(mylist)
```
 输出：


[{‘name’: ‘Tom’, ‘age’: 19}, {‘name’: ‘Tom’, ‘age’: 19}, {‘name’: ‘Tom’, ‘age’: 19}, {‘name’: ‘Tom’, ‘age’: 19}, {‘name’: ‘Tom’, ‘age’: 19}]
 
##### **使用pprint输出**
 导入函数： 
```python
#使用pprint输出
#函数为内置函数直接导入即可
from pprint import pprint

```
 输出：


[{‘age’: 19, ‘name’: ‘Tom’}, {‘age’: 19, ‘name’: ‘Tom’}, {‘age’: 19, ‘name’: ‘Tom’}, {‘age’: 19, ‘name’: ‘Tom’}, {‘age’: 19, ‘name’: ‘Tom’}]
 +  deepcopy函数 **c++中直接对类或数组赋值**可造成**浅拷贝效果**，在python中列表，字典，集合等的直接赋值都是浅拷贝。深拷贝可调用deepcopy函数 **这是浅拷贝的一个例子** 
```python
MyList=[[1],[2],[3]]
RetList=MyList
for i in RetList:
    i.append(100)
print("RetList:",RetList)
print("Mylist:",MyList)
#输出：
#RetList: [[1, 100], [2, 100], [3, 100]]
#Mylist: [[1, 100], [2, 100], [3, 100]]

```
 **deepcopy函数接受参数为任意数据类型，返回该参数的拷贝，是深拷贝** 导入函数： 
```python
#函数为内置函数直接导入即可
from copy import deepcopy
MyList=[[1],[2],[3]]
RetList=deepcopy(MyList)#深度拷贝不会受到影响
for i in RetList:
    i.append(100)
print("RetList:",RetList)
print("Mylist:",MyList)
```
 输出：


RetList: [[1, 100], [2, 100], [3, 100]] Mylist: [[1], [2], [3]]
 




## 

   Python之判断变量类型isinstance函数 
 


​ Python的 isinstance函数可以判断指定的**变量**和**类型** 是否对应，返回值是bool类型

函数原型：


**isinstance(object, classinfo)**

​ 即 isinstance(变量名，类型)


```python
MyList=[100,20,"hello world"]
MyDict={"name":"Dae"}
MySet={100,20,50}
MyString="hello Python!"
MyInt=50
Myfloat=9.8
print(isinstance(MyList,list))# True
print(isinstance(MyInt,list))#False
print(isinstance(MyString,str))#True
```




#### 1 requests中cookirJar的处理方法



使用request获取的resposne对象，具有cookies属性，能够获取对方服务器设置在本地的cookie，但是如何使用这些cookie呢？

1.1 方法介绍

+ response.cookies是CookieJar类型+ 使用requests.utils.dict_from_cookiejar，能够实现把cookiejar对象转化为字典

1.2 方法展示

```python
import requests

url = "http://www.baidu.com"
#发送请求，获取resposne
response = requests.get(url)
print(type(response.cookies))

#使用方法从cookiejar中提取数据
cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)
```


输出为:

```python
<class 'requests.cookies.RequestsCookieJar'>
{'BDORZ': '27315'}
```

注意：

在前面的requests的session类中，我们不需要处理cookie的任何细节，如果有需要，我们可以使用上述方法来解决



## 

   Python之 requests的post方法 
 


#### post方法与get方法相比多了个请求体，post请求可携带的数据的空间比get请求多。



如果没有安装requests可以在Windows的cmd下面使用 pip命令安装该库

```bash
pip install requests
```



#### 下面列出get请求的部分参数


##### 1. url（请求的url地址，必需）



+ 形式：字符串
+ 意义：作为请求的**url地址**
+ 使用方法：参照get请求一章



##### 2. headers参数（请求头，可选）



+  形式：字典 
+  意义：作为请求的**请求头** 
+  使用方法：参照get请求一章 详情请看项目： 



##### 3. date参数 （请求参数，可选）



+  形式：字典 
+  意义：作为post请求的请求体 
+  使用方法 
```python
```






## 

   Python之 requests的get方法 
 


#### requests是一个简单的请求库，其中的get方法可以像指定服务器发送get请求，该库是外部库，需要手动安装。



如果没有安装requests可以在Windows的cmd下面使用 pip命令安装该库

```bash
pip install requests
```



#### 下面列出get请求的部分参数


##### 1. url（请求的url地址，必需 ）


+  形式：字符串 +  意义：作为请求的**url地址** +  使用方法： 
```python
import  requests
url="http://www.baidu.com"
resp=requests.get(url)#向url对应的服务器发送相应的get请求，获得对应的相应 。
```
 


##### 2. headers参数（请求头，可选）


+  形式：字典 +  意义：作为请求的**请求头** +  使用方法： 
```python
import requests
url=r"https://www.baidu.com/s"
Headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
         }
response=requests.get(url=url,headers=Headers)
```
 详情请看项目： 


##### 3. params参数 （请求参数，可选）


+  形式：字典 +  意义：作为**get请求**的**表格信息**，会被**显式的加到url**中 +  使用方法： 
```python
import requests
url=r"https://www.baidu.com/s"
#以带参数的Get请求，请求对应页面，比如百度搜索 Python，只需
Params={"wd":"Python"}
Headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
response=requests.get(url=url,params=Params,headers=Headers)
print(response.request.url)#输出：https://www.baidu.com/s?wd=Python
```
 详情请看项目： 


##### 4. proxies参数 （代理IP，可选）


+  形式：字典 +  意义：作为用户代理，访问服务器会以**该代理的ip访问服务器**，可掩盖本机ip. +  使用方法 
```python
import requests
#proxies 是伪ip使用代理访问页面
#下面是使用代理访问百度
Headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
         }
#proxies的格式是字典，类型：协议表示+域名+端口
proxies={
    "http":"http://1.192.242.107:9999"
    # "https":"https://192.168.0.1:80"
}
url="https://www.baidu.com"
resp=requests.get(url,headers=Headers,proxies=proxies)
print(resp.content.decode())

```
 


##### 5. verify参数（ssl证书验证，可选）


+  形式：bool类型 +  意义：**ssl证书验证是否跳过**，用于访问有些页面出现证书验证错误的时候 +  使用方法： 
```python
'''
当访问https页面出现证书错误，可以使用verify来取消验证
在get或者post请求的verify参数设置成False
requests.get(url,headers,data,prams,proxies,verify=False)
'''
import requests
url="https://www.12306.cn"
resp=requests.get(url,verify=False)
print(resp.content.decode())
```
 


##### 6. timeout参数 （延迟限制，可选）


+  形式：实数类型 +  意义：通过添加timeout参数，能够保证在指**定秒钟内返回响应**，**否则会报错** +  使用方法： 
```python
'''
超时参数的使用
response = requests.get(url,timeout=3)通过添加timeout参数，能够保证在3秒钟内返回响应，否则会报错
'''
import  requests
proxies={"http":"http://1.192.242.107:9999"}
url="http://www.baidu.com"
try:
    resp=requests.get(url,proxies=proxies,timeout=3)
except :
    print("运行时出错")
```
 


##### 7. cookies参数 （作为cookies，可选）


+  形式：字典 +  意义：使用该参数会**显式将cookies字符串**加入到请求头的cookies中 +  使用方法： 
```bash
#这里不再演示，cookies值本来是键值对，加入到headers中会处理为字符串加入到key对应的值中
```
 




## Python的自列表的定义排序


因是c++Acmer，故经常用到自定义排序

#### 第一种方法：对小于号进行重载



因为所有比较都可通过小于号的结果进行推导


```python
class Dch:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def __str__(self):
        return "first={},second={}".format(self.first,self.second)
    def __lt__(self, other):
        if (self.first == other.first):
            return int(self.second < other.second)
        return int(self.first < other.first)
    # isinstance(100,int)
aa=Dch(1,2)
bb=Dch(100,1)
cc=Dch(50,50)
dd=Dch(30,-1)
ee=Dch(1,20)
Mylist=[aa,bb,cc,dd,ee]
Mylist=sorted(Mylist)#sorted函数返回对list排序的结果，默认是稳定的归并排序
for i in range(len(Mylist)):
    print(Mylist[i])
```


列表也有内置函数sort，这是官方的解释


`sort`(***, *key=None*, *reverse=False*)

此方法会对列表进行原地排序，只使用 `<` 来进行各项间比较。 异常不会被屏蔽 —— 如果有任何比较操作失败，整个排序操作将失败（而列表可能会处于被部分修改的状态）。

[`sort()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort) 接受两个仅限以关键字形式传入的参数 ([仅限关键字参数](https://docs.python.org/zh-cn/3/glossary.html#keyword-only-parameter)):

…



first=1,second=2 first=1,second=20 first=30,second=-1 first=50,second=50 first=100,second=1


#### 第二种用sort的key参数和lambda表达式


可以参考python的官网文档：[https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort)

```python
class pair:
    def  __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __lt__(self, other):
        if self.x==other.x:
            return self.y<other.y
        return self.x-self.y
    def __str__(self):
        return "%d,%d"% (self.x,self.y)
me=[]
me.append(pair(3,4))
me.append(pair(1,3))
me.append(pair(-1,-1))
me.sort(key=lambda x:(x.y))
for i in me:
    print(i)
#输出：
#-1,-1
#1,3
#3,4
```




#### 深入使用sort的key参数


**如果我们用lambda表达式进行指定key关键词排序时遇见c++ 这样的pair要求的排序** (第一个关键词从小到大排序，如果相同则按第二个关键词从小到大排序)**该怎么做呢？** lambda表达式的结果可返回一个元组，按照对元素为元组的数组排序则默认字典序排序。

```python
class pair:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "{}  {}".format(self.x,self.y)
if __name__ == '__main__':
    mmp=[]
    mmp.append(pair(1,2))
    mmp.append(pair(0, 2))
    mmp.append(pair(4, 5))
    mmp.append(pair(7, 8))
    mmp.append(pair(4, 3))
    mmp.sort(key=lambda me:(me.x,me.y))#这样就会按照元组的字典序进行排序
    for i in mmp:
        print(i)
'''
输出
0  2
1  2
4  3
4  5
7  8
'''
#

```


