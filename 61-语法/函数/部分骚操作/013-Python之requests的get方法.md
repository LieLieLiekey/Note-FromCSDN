

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
 


