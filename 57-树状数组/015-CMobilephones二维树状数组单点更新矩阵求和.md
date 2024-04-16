

### [C - Mobile phones](https://vjudge.net/problem/POJ-1195)（二维树状数组）


[POJ - 1195 ](https://vjudge.net/problem/17086/origin)

题意：对一个$n ∗ n n*n$的矩阵进行一些操作和查询，操作：单点修改。查询：求子矩阵元素和

思路：

​ 真没想到二维的树状数组是这样的。（真不知道二维线段树应该怎么维护，期待(☆▽☆)！ ）

构建二维树状数组之后我们可以求$i , j i,j$左上角矩阵的和 。求子矩阵可以转化为多个左上角矩阵元素和的加减。


二维树状数组的第二维(也就是行向量代表的节点吧)之间的关系，跟一维向量的 节点之间关系相同。

看博文：[https://blog.csdn.net/chaiwenjun000/article/details/47973737](https://blog.csdn.net/chaiwenjun000/article/details/47973737)


```cpp
#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
```


