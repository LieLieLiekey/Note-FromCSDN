

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

