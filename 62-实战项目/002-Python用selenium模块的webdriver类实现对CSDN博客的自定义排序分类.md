

## Python 用selenium模块的webdriver类实现对CSDN博客的自定义排序分类



下面分几个步骤 1.安装Chrome驱动器，需要安装对应浏览器版本的 网址:[https://npm.taobao.org/mirrors/chromedriver](https://npm.taobao.org/mirrors/chromedriver)

2.获得并**保存**登陆后**个人列表**的信息

3.**自己**对**保存的个人列表**进行一个**排序**，并**保存文件**

4.根据保存的文件和当前博客的分类顺序进行模拟点击，完成排序过程。


### 1. 安装Chorme驱动器


​ 这里我查看了自己Chrome浏览器的版本，我在此安装的版本为: 72.0.3626.69/

​ 在程序中用selenium模块的webdriver进行一个Chrome驱动器的实现

​

```python
    login_url = "https://passport.csdn.net/login"
    driver = webdriver.Chrome(executable_path=r'C:\Users\12495\Desktop\chromedriver.exe')
```


### 2.获得登陆后保存的个人列表信息


​ 这里分两个步骤

```bash
>1.登陆到个人分类页面 login函数
>
>2.保存数据 SaveListInfo
```


```python
from selenium import webdriver #selenium的webdriver类的功能
import requests
import time
from lxml import etree
def login(AccountNumbers,Passworld):
    login_url = "https://passport.csdn.net/login"
    driver = webdriver.Chrome(executable_path=r'C:\Users\12495\Desktop\chromedriver.exe')
    # 1.用该浏览器打开页面
    driver.get(login_url)
    time.sleep(1)
    # 2.向对应id的表格发送信息
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/ul/li[1]/a').click()
    driver.find_element_by_id("all").send_keys(AccountNumbers)
    driver.find_element_by_id("password-number").send_keys(Passworld)
    driver.find_element_by_xpath(r'//*[@id="app"]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button').click()
    time.sleep(3)
    SortUrl = 'https://mp.csdn.net/category/list'
    driver.get(SortUrl)
    try:
        driver.find_element_by_id("btnStart").click()
    except:
        print("Login Fail！")
        exit(1)
    time.sleep(1)
    return driver

def SaveListInfo(HtmlCode):#保存当前sort的信息保存
    Xpath = r'//li[@ class="d-flex align-items-center"]'
    element=etree.HTML(HtmlCode)
    ElementList=element.xpath(Xpath)
    with open("ListInfo.txt","w",encoding="utf-8") as fp:
        for i in range(len(ElementList)):
            element=ElementList[i]
            element=etree.HTML(etree.tostring(element))
            fp.write("{}  {} {}\n".format(i,element.xpath(r'//input/@value')[0],element.xpath('//@data-id')[0]))
            
if __name__ == '__main__':
    AccountNumbers=input("请输入账号:")
    Password=input("请输入密码:")
    driver=login(AccountNumbers,Password)#第一步 得到一个当前页面的list Chrome 驱动
    SaveListInfo(driver.page_source)#第二步  保存数据
    time.sleep(5)
    driver.quit()
```


### 3.用保存的文件 自定义排序


```bash
在上一步的程序中得到一个ListInfo.txt文件  里面每行是一个分类的：顺序  名称  编号
```


​ 然后自己粘贴复制一轮乱搞，把信息排个序就行，像下面这样 ，（其实只要把id号按规定的排个序就行，名称只是个幌子，为了看清除）

```bash
>35 ------------------------动态规划--... 8057180
>36 【动态规划dp】 7495677
>37 【区间DP】 7671892
>38 状压dp 8633336
>39 数位DP 8597046
>40 期望/概率dp 8642191
>41 ------------------------图论----... 8057155
>42 【最短路径】 7425656
>43 【最小生成树】 7433840
>44 【并查集】 7799073
>45 【欧拉回路】 7732919
```


### 4.开始模拟浏览器进行分类处理


算法实现很简单：


现在对应该所处位置第 i 个 进行模拟点击

1.读取现在第i个分类所处的位置

2.计算位置差，从而点击多少次。


```python
'''
程序需要：
1.登陆页面信息 程序提示输入
2.想要达到的ShoudleList.txt文件 第二步和第三步手动处理后的文件  （只要id号对应即可

'''
from selenium import webdriver #selenium的webdriver类的功能
import requests
import time
from lxml import etree
import os
def GetCookies(driver):#获得此时浏览器的cookies 是字典形式
    CookiesList = driver.get_cookies()
    # print(CookiesList)
    # 6.把cookies的name和value提取出来，作为键值对
    cookies = {}
    for i in CookiesList:
        cookies[i["name"]] = i["value"]
    return cookies
def SaveListInfo(HtmlCode):#保存当前sort的信息保存
    Xpath = r'//li[@ class="d-flex align-items-center"]'
    element=etree.HTML(HtmlCode)
    ElementList=element.xpath(Xpath)
    with open("ListInfo.txt","w",encoding="utf-8") as fp:
        for i in range(len(ElementList)):
            element=ElementList[i]
            element=etree.HTML(etree.tostring(element))
            fp.write("{} {} {}\n".format(i,element.xpath(r'//input/@value')[0],element.xpath('//@data-id')[0]))
def IdToUp(driver,id,times):
    for i in range(times):
        driver.find_element_by_xpath('//li[@ data-id="{}"]/div/button[ @data-type="up"]'.format(id)).click()
        time.sleep(0.5)
def IdToDown(driver,id,times):
    for i in range(times):
        driver.find_element_by_xpath('//li[@ data-id="{}"]/div/button[ @data-type="down"]'.format(id)).click()
        time.sleep(0.5)
def login(AccountNumbers,Passworld):
    login_url = "https://passport.csdn.net/login"
    driver = webdriver.Chrome(executable_path=r'C:\Users\12495\Desktop\chromedriver.exe')
    # 1.用该浏览器打开页面
    driver.get(login_url)
    time.sleep(1)
    # 2.向对应id的表格发送信息
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/ul/li[1]/a').click()
    driver.find_element_by_id("all").send_keys(AccountNumbers)
    driver.find_element_by_id("password-number").send_keys(Passworld)
    driver.find_element_by_xpath(r'//*[@id="app"]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button').click()
    time.sleep(20)
    SortUrl = 'https://mp.csdn.net/category/list'
    driver.get(SortUrl)
    try:
        driver.find_element_by_id("btnStart").click()
    except:
        print("Login Fail！")
        exit(1)
    time.sleep(1)
    return driver
def GetCurrentSortMap(HtmlCode):
    Xpath = r'//li[@ class="d-flex align-items-center"]'
    element=etree.HTML(HtmlCode)
    ElementList=element.xpath(Xpath)
    CurrentSortMap={}
    for i in range(len(ElementList)):#把每个element的 id:顺序(从0开始)
        element=ElementList[i]
        element=etree.HTML(etree.tostring(element))
        CurrentSortMap[element.xpath('//@data-id')[0]]=i
    return CurrentSortMap
def Init():
    EndSortList=[]#表示按照顺序排序之后的编号顺序
    with open("ShoudleList.txt","r",encoding="utf-8") as fp:
        while True:
            line=fp.readline()
            if not line:
                break
            EndSortList.append(line.split(" ")[-1][:-1])
    return EndSortList#标号从0开始
if __name__ == '__main__':

    EndSortList = Init() #排序后应该的id顺序
    AccountNumbers=input("请输入账号:")
    Password=input("请输入密码:")
    driver=login(AccountNumbers,Password)#得到一个当前页面的list Chrome 驱动
    for i in range(len(EndSortList)):#从应该的顺序从低到高 依次完成
        NeedSortId=EndSortList[i]
        CurrentSortMap=GetCurrentSortMap(driver.page_source)
        NowNumbers=CurrentSortMap[NeedSortId]
        if(NowNumbers>i):
            IdToUp(driver,NeedSortId,NowNumbers-i)
    SaveListInfo(driver.page_source)
    # IdToUp(driver,"8642191",22)
    time.sleep(5)
    driver.quit()

```


