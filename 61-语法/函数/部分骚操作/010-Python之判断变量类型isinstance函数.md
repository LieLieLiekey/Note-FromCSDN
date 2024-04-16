

## 

   Python之判断变量类型isinstance函数 
 


​ Python的 isinstance函数可以判断指定的**变量**和**类型** 是否对应，返回值是bool类型

函数原型：


**isinstance(object, classinfo)**

​ 即 isinstance(变量名，类型)


```python
MyList=[100,20,"hello world"]
MyDict={"name":"Dae"}
MySet={100,20,50}
MyString="hello Python!"
MyInt=50
Myfloat=9.8
print(isinstance(MyList,list))# True
print(isinstance(MyInt,list))#False
print(isinstance(MyString,str))#True
```


