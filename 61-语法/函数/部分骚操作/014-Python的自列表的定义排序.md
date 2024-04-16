

## Python的自列表的定义排序


因是c++Acmer，故经常用到自定义排序

#### 第一种方法：对小于号进行重载



因为所有比较都可通过小于号的结果进行推导


```python
class Dch:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def __str__(self):
        return "first={},second={}".format(self.first,self.second)
    def __lt__(self, other):
        if (self.first == other.first):
            return int(self.second < other.second)
        return int(self.first < other.first)
    # isinstance(100,int)
aa=Dch(1,2)
bb=Dch(100,1)
cc=Dch(50,50)
dd=Dch(30,-1)
ee=Dch(1,20)
Mylist=[aa,bb,cc,dd,ee]
Mylist=sorted(Mylist)#sorted函数返回对list排序的结果，默认是稳定的归并排序
for i in range(len(Mylist)):
    print(Mylist[i])
```


列表也有内置函数sort，这是官方的解释


`sort`(***, *key=None*, *reverse=False*)

此方法会对列表进行原地排序，只使用 `<` 来进行各项间比较。 异常不会被屏蔽 —— 如果有任何比较操作失败，整个排序操作将失败（而列表可能会处于被部分修改的状态）。

[`sort()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort) 接受两个仅限以关键字形式传入的参数 ([仅限关键字参数](https://docs.python.org/zh-cn/3/glossary.html#keyword-only-parameter)):

…



first=1,second=2 first=1,second=20 first=30,second=-1 first=50,second=50 first=100,second=1


#### 第二种用sort的key参数和lambda表达式


可以参考python的官网文档：[https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort)

```python
class pair:
    def  __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __lt__(self, other):
        if self.x==other.x:
            return self.y<other.y
        return self.x-self.y
    def __str__(self):
        return "%d,%d"% (self.x,self.y)
me=[]
me.append(pair(3,4))
me.append(pair(1,3))
me.append(pair(-1,-1))
me.sort(key=lambda x:(x.y))
for i in me:
    print(i)
#输出：
#-1,-1
#1,3
#3,4
```




#### 深入使用sort的key参数


**如果我们用lambda表达式进行指定key关键词排序时遇见c++ 这样的pair要求的排序** (第一个关键词从小到大排序，如果相同则按第二个关键词从小到大排序)**该怎么做呢？** lambda表达式的结果可返回一个元组，按照对元素为元组的数组排序则默认字典序排序。

```python
class pair:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "{}  {}".format(self.x,self.y)
if __name__ == '__main__':
    mmp=[]
    mmp.append(pair(1,2))
    mmp.append(pair(0, 2))
    mmp.append(pair(4, 5))
    mmp.append(pair(7, 8))
    mmp.append(pair(4, 3))
    mmp.sort(key=lambda me:(me.x,me.y))#这样就会按照元组的字典序进行排序
    for i in mmp:
        print(i)
'''
输出
0  2
1  2
4  3
4  5
7  8
'''
#

```


