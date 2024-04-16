

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


