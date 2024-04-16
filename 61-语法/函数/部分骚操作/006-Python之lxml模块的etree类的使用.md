

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


