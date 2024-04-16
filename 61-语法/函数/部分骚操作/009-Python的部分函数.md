

## Python的部分函数


+  pprint函数 效果：输出更直观，对列表和字典的嵌套效果较为明显 
```python
#普通print输出
d1={"name":"Tom","age":19}
mylist=[]
for i in range(5):
    mylist.append(d1.copy())
print(mylist)
```
 输出：


[{‘name’: ‘Tom’, ‘age’: 19}, {‘name’: ‘Tom’, ‘age’: 19}, {‘name’: ‘Tom’, ‘age’: 19}, {‘name’: ‘Tom’, ‘age’: 19}, {‘name’: ‘Tom’, ‘age’: 19}]
 
##### **使用pprint输出**
 导入函数： 
```python
#使用pprint输出
#函数为内置函数直接导入即可
from pprint import pprint

```
 输出：


[{‘age’: 19, ‘name’: ‘Tom’}, {‘age’: 19, ‘name’: ‘Tom’}, {‘age’: 19, ‘name’: ‘Tom’}, {‘age’: 19, ‘name’: ‘Tom’}, {‘age’: 19, ‘name’: ‘Tom’}]
 +  deepcopy函数 **c++中直接对类或数组赋值**可造成**浅拷贝效果**，在python中列表，字典，集合等的直接赋值都是浅拷贝。深拷贝可调用deepcopy函数 **这是浅拷贝的一个例子** 
```python
MyList=[[1],[2],[3]]
RetList=MyList
for i in RetList:
    i.append(100)
print("RetList:",RetList)
print("Mylist:",MyList)
#输出：
#RetList: [[1, 100], [2, 100], [3, 100]]
#Mylist: [[1, 100], [2, 100], [3, 100]]

```
 **deepcopy函数接受参数为任意数据类型，返回该参数的拷贝，是深拷贝** 导入函数： 
```python
#函数为内置函数直接导入即可
from copy import deepcopy
MyList=[[1],[2],[3]]
RetList=deepcopy(MyList)#深度拷贝不会受到影响
for i in RetList:
    i.append(100)
print("RetList:",RetList)
print("Mylist:",MyList)
```
 输出：


RetList: [[1, 100], [2, 100], [3, 100]] Mylist: [[1], [2], [3]]
 


