

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
Mylist=sorted(Mylist)
for i in range(len(Mylist)):
    print(Mylist[i])
```


输出：


first=1,second=2 first=1,second=20 first=30,second=-1 first=50,second=50 first=100,second=1


## 其他的暂时没实践过哦


