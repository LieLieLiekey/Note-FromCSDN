

## Python正则表达式re的复习


以下有部分参考传智播客的学习资料：

#### 1. 什么是正则表达式



用事先定义好的一些特定字符、及这些特定字符的组合，组成一个**规则字符串**，这个**规则字符串**用来表达对字符串的一种**过滤**逻辑。


#### 2. 正则表达式的常见语法



收藏博客链接：[https://www.cnblogs.com/yyyg/p/5498803.html](https://www.cnblogs.com/yyyg/p/5498803.html)


这里不再赘述。

#### (1).其中贪婪匹配和非贪婪匹配需要重点强调一下


上面提到贪婪匹配和非贪婪匹配请看例子：

```python
import re
#贪婪
ret_greed= re.findall(r'a(\d+)','a23b')
print(ret_greed)
#非贪婪
ret_no_greed= re.findall(r'a(\d+?)','a23b')
print(ret_no_greed)
 
['23']
['2']
```


由于贪婪匹配为尽可能的多匹配所以结果为23 ：

#### (2). 分组与不分组


被括起来的表达式作为一个分组. findall 在有组的情况下只显示组的内容

```python
#不分组下
import re
ret=re.findall("a.*?bc","abcbcd,n",re.S)#在re.s的模式下.号匹配换行符 ，返回匹配列表
print(ret)
```


输出：


[‘abc’]


```python
#分组情况下
import re
MyStr='''
name="Tom",age="18"
name="Hia",age="50"
'''
ret=re.findall(r'name="(.*?)".*?age="(\d+?)"',MyStr)
print(ret)
```


输出：


[(‘Tom’, ‘18’), (‘Hia’, ‘50’)]


#### 3. re模块的常见方法



+  pattern.match（从头找一个） +  pattern.search（找一个） +  pattern.findall（找所有） +  返回一个列表，没有就是空列表 +  `re.findall("\d","chuan1zhi2") >> ["1","2"]` +  pattern.sub（替换） +  `re.sub("\d","_","chuan1zhi2") >> ["chuan_zhi_"]` +  re.compile（编译） +  返回一个模型P，具有和re一样的方法，但是传递的参数不同 +  匹配模式需要传到compile中 
```python
p = re.compile("\d",re.S)
p.findall("chuan1zhi2")
```
 



#### 4. python中原始字符串r的用法



原始字符串定义(raw string)：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符，原始字符串往往针对特殊字符而言。例如`"\n"`的原始字符串就是`"\\n"`

+ 原始字符串的长度


```python
  In [19]: len("\n")
  Out[19]: 1

  In [20]: len(r"\n")
  Out[20]: 2

  In [21]: r"\n"[0]
  Out[21]: '\\'
```


+ 正则中原始字符串的使用


```python
  In [13]: r"a\nb" == "a\\nb"
  Out[13]: True

  In [14]: re.findall("a\nb","a\nb")
  Out[14]: ['a\nb']

  In [15]: re.findall(r"a\nb","a\nb")
  Out[15]: ['a\nb']

  In [16]: re.findall("a\\nb","a\nb")
  Out[16]: ['a\nb']

  In [17]: re.findall("a\\nb","a\\nb")
  Out[17]: []

  In [18]: re.findall(r"a\\nb","a\\nb")
  Out[18]: ['a\\nb']
```



##### 相关项目链接：[Python项目之爬取斗图网所有图片](https://blog.csdn.net/Dch19990825/article/details/83503917)


