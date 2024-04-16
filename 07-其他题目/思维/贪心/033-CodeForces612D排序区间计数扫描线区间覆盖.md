

题目链接：[http://codeforces.com/problemset/problem/612/D](http://codeforces.com/problemset/problem/612/D)



题目大意：

给出n条线段，让你算这些线段重合次数大于等于k次的部分



输入： 

第一行：给出两个数n  k      分别表示要输入的线段个数和所需的线段最少重叠次数

接下来n行 每行一个l  r表示线段的左端点和右端点。



解题思路：

至于这道题：区间覆盖问题 ，先把所有线段进行处理

对于每条线段e ，对于**左端点**，将值记下并且标记为0存入结构体数组，**右端点**将 值 记下标记为1存入结构体数组

然后让值从小到大对结构体排序，若值相同将0排在前面（过一会你就知道为什么了）



这样处理后共有2*n个点，定义一个变量cnt记录贡献值

当遇到标记为1时--cnt表示这次之后这点被覆盖了cnt次

遇到标记为0时++cnt；  表示这次之后这点被覆盖了cnt次

当cnt增加到k时就要将这个点作为覆盖k次的左端点，

当cnt减少到k-1时就要把这个点作为覆盖k次结束的右端点



前面提到若值相同将则将标记为0的排在前面，是为了下面这样的数据  

3   2

0 10

0 5

5 10

因为将左端点排在左边 才能将0 5 ，5 10这样的区间看作一个区间（因为cnt是先加后减的）

代码：



```cpp
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<string>
#include<iostream>
#include<cstdlib>
#include<queue>
#define N 1010000
#define INF 0x3f3f3f3f
#define MOD 100007
using namespace std;
struct node
{
    int d,sign;
} e[2*N];
bool cmp(node q,node qq)
{
    if(q.d==qq.d)
        return q.sign<qq.sign;//0   1 ,0在前
    return q.d<qq.d;
}
int ll[N];
int rr[N];
int main()
{
    int cnt,n,k,l,r,le,la;
    scanf("%d %d",&n,&k);
    le=0;
    for(int i=1; i<=n; i++)
    {
        scanf("%d %d",&l,&r);
        e[le].d=l;
        e[le++].sign=0;//左端点
        e[le].d=r;
        e[le++].sign=1;//右端点
    }
    sort(e,e+le,cmp);
    la=0;
    cnt=0;//记录在此点以及之前左端点的出现次数
    for(int i=0; i<le; i++)
    {
        if(!e[i].sign)
        {
            cnt++;
            if(cnt==k)
                ll[la]=e[i].d;
        }
        else
        {
            cnt--;
            if(cnt==(k-1))
               rr[la++]=e[i].d;
        }
    }
    printf("%d\n",la);
    for(int i=0;i<la;i++)
        printf("%d %d\n",ll[i],rr[i]);
}```



