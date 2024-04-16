

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


