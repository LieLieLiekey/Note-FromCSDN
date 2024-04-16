

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
 


