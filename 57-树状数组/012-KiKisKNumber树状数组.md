

### [ KiKi’s K-Number](https://vjudge.net/problem/HDU-2852)  (树状数组)


[HDU - 2852 ](https://vjudge.net/problem/17358/origin)

**题意：**

题意：题目给定三种操作: 0 x 表示把x插入容器 ; 1 x 表示删除一个x如果没有x则输出 No Elment! ; 2 a k 表示比a大的数中的第k大的数 如果没有输出No Find!

**思路：**

​ 树状数组维护元素出现次数前缀和即可。操作0即修改；操作1先查询x是否存在，如果存在删除一个即可。操作2可以用二分逐渐逼近答案。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
const int MAX=100000;
int bt[MAXN];
int lowbit(int k)
{
   
    return k&-k;
}
void modify(int k,int val)
{
   
    while(k<=MAX)
    {
   
        bt[k]```


