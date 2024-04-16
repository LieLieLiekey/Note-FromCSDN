

 这里选取的网址是  http://www.doutula.com   目的：爬取其中的图片  并且翻页爬取

首页图片的规则

```
<img src="https://ws3.sinaimg.cn/bmiddle/6af89bc8gw1f8oqmqwpjgj206o05k0ss.jpg" style="margin: 0px auto; min-height: inherit; height: 184.471px; display: block;" data-original="https://ws3.sinaimg.cn/bmiddle/6af89bc8gw1f8oqmqwpjgj206o05k0ss.jpg" alt="不发别走！" class="img-responsive lazy image_dta" data-backup="http://img.doutula.com/production/uploads/image//2016/04/27/20160427715202_Oaoikb.jpg!dta">```


所以正则表达式

```python
ImgUrlList=re.findall(r'<img src=.*?data-original="(.*?.jpg)"',htmltext)```


怎么实现翻页功能呢，因为每一页的链接有规律，So

```python
ToUrl='http://www.doutula.com/article/list/?page='```


**思路就是：**

**1.枚举每个页面 ，用正则表达式获取其中的img的url和img的名字列表**

**2.对于每img根据其urll将之下载至电脑，用requests的get方法需要加上请求头伪装成该信息是浏览器发出的，并且是该网页请求 不然会被屏蔽请求**

 

 

这里有个坑点，其他页面的img标签与首页的规则不同

 

```
<img class="lazy image_dtb img-responsive" src="https://ws2.sinaimg.cn/bmiddle/9150e4e5ly1fvscbyvi9mj206o06ot8n.jpg" data-original="https://ws2.sinaimg.cn/bmiddle/9150e4e5ly1fvscbyvi9mj206o06ot8n.jpg" data-backup="http://img.doutula.com/production/uploads/image//2018/10/11/20181011212059_SCoIQM.jpg!dta" alt="天鸭 - 鸭鸭表情" style="height: 170px; display: block;">```


 所以我把正则表达式改为了

```python
  ImgUrlList=re.findall(r'<img.*?src=.*?data-original="(.*?.jpg)"',htmltext)```


 这样就可以获取每个页面的img信息（包括首页）

```python
import requests
import re
#UA卷则  代表请求由谁发出的
def Getimage(htmltext):#根据html代码   返回 图片url列表和图片名称列表
    ImgUrlList=re.findall(r'<img.*?src=.*?data-original="(.*?.jpg)"',htmltext)#获取img链接并且保证后缀为jpg
    ImgNameList=[]
    for url in ImgUrlList:
        url=url.split('/')
        ImgNameList.append(url[-1])
    return ImgUrlList,ImgNameList
def GetNexthtml(htmltext,url):#根据html代码 和总的url求出下一个next链接
    Nexthtml=re.findall(r'<a class="page-link" href="(/article/list/[?]page=\d+)',htmltext)
    print(Nexthtml)
    if len(Nexthtml)==0:
        raise Exception(u"don't next page  in GetNexthtml Fuction!")
    ToUrl=url+Nexthtml[0]
    return ToUrl
def Saveimg(Imgbit,Imgname):#根据二进制文件  和文件名字获取图片
    with open("imgs/{}".format(Imgname),"wb") as fp:
        fp.write(Imgbit)
RequestHeaders={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    ,'Referer': 'http://www.doutula.com/'
}#前导空格不能有  此时是浏览器发出的
url="http://www.doutula.com"
nowurl=url
response = requests.get(nowurl, headers=RequestHeaders)  # 发起一个请求 得到html
if response.status_code!=200:
    raise  Exception(u"url没有访问权限")
ImgUrlList,ImgNameList=Getimage(response.text)#根据htmltext得到 里面url列表 和名字列表
count=len(ImgUrlList)
print(count)
for i in range(count):
    response=requests.get(ImgUrlList[i],headers=RequestHeaders)#图片的响应头的二进制文件在成员变量content里面
    print(ImgUrlList[i],ImgNameList[i])
    Saveimg(response.content,ImgNameList[i])
ToUrl='http://www.doutula.com/article/list/?page='
for i in range(2,1000):#根据nowurl 得到请求
    nowurl="{}{}".format(ToUrl,str(i))
    print("nowurl:",nowurl)
    response = requests.get(nowurl, headers=RequestHeaders)  # 发起一个请求
    if response.status_code!=200:
        continue
    ImgUrlList,ImgNameList=Getimage(response.text)#根据html得到图片列表
    count=len(ImgUrlList)
    print(count)
    for i in range(count):
        response=requests.get(ImgUrlList[i],headers=RequestHeaders)#图片的响应头的二进制文件在成员变量content里面
        print(ImgUrlList[i],ImgNameList[i])
        Saveimg(response.content,ImgNameList[i])```


 

