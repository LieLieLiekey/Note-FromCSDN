

## 思路


### 1. 要获得怎么样的数据


#### 2. 找到数据来源


#### 3. 模拟浏览器发送请求获得数据


#### 4. 处理数据，保存数据


### 第一步：



在这里数据**是豆瓣top250中高于指定分数的电影信息**

**信息有：名称，评分，格言**


### 第二步：



数据在网页html中，这里我使用xpath语法分析htm代码提取数据即可

当然也有其它方法比如：找出页面请求的数据包，抓包分析，找出数据来源


 首页的url=[https://movie.douban.com/top250](https://movie.douban.com/top250)

第二页的url为=[https://movie.douban.com/top250?start=25](https://movie.douban.com/top250?start=25)

故猜测第k页的url只需start为25*(k-1)

所以我们枚举url，提取有效的数据。

### 第三步：


获得网页源码是一般是发送get请求。故


+ 制定请求头
+ 找到url
+ 模拟浏览器发送数据



```python
def GetHelpfulElement(Html,s```


