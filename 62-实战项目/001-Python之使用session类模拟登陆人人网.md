

## 使用request模块的session类模拟登陆人人网



因为人人网的登陆不需要验证码，故模拟登陆比较简单。


## 思路


####  1. 使用浏览器打开人人网的登陆页面


####  2. 找出登陆时发送post请求的url地址和请求体格式


####  3. 使用session发送post请求获得cookies后，访问所需页面即可


 

 

 

###  1. 使用浏览器打开人人网的登陆页面



![./figures/20190216203459651.png](./figures/20190216203459651.png)


 

###      2. 找出登陆时发送post请求的url地址和请求体格式


 

 

      
![./figures/20190216203705165.png](./figures/20190216203705165.png)


密码框的   id="password"  账号框的id="email "  对应的form表单的action="http://www.renren.com/PLogin.do"

所以   当输入账号和密码点击登陆之后，浏览器会把表单信息发送给"http://www.renren.com/PLogin.do"。

**故我们猜测把该url地址作为post发送请求的地址，然后准备好请求头，请求体的内容是一个字典 key'值分别为"password"和"email"**

 

###  3. 使用session发送post请求获得cookies后，访问所需页面即可



我们知道发送请求的**url地址**和**post请求体**的数据之后就可以模拟浏览器发送请求了


 代码：


注：由于隐私问题，下面的login_info的账号密码信息删了，自己使用时候只需填上自己的账号密码即可


```python
import requests
login_info={"email":"你的账号","password":"你的密码"}
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

url="http://www.renren.com/PLogin.do"
session=requests.session()
session.post(url,headers=headers,data=login_info)#向登陆程序发送post请求 获得登陆后的cookie
#使用session发送post请求返回的页面
profile_url="http://www.renren.com/969664771/profile"#个人主页url
resp=session.get(profile_url,headers=headers)#人人网的个人主页
ProfileHtml=resp.content.decode()#得到登陆后的个人主页html代码

resp=session.get("http://zhibo.renren.com/car/home#nav=0",headers=headers)#进入登陆后的人人网的直播 商城
ZbHtml=resp.content.decode()#得到登陆后的直播商城的html代码
print(ZbHtml)```



在session发送第一个post请求之后，seesion就会记下登陆信息（cookies）接下来只需访问登陆后的数据即可。(有些数据不容易访问) 


