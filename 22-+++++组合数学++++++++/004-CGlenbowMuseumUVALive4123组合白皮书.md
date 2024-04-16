

### [C - Glenbow Museum](https://cn.vjudge.net/problem/UVALive-4123)


[UVALive - 4123 ](https://cn.vjudge.net/problem/12130/origin)

题意：


​ **对于一个边平行于坐标轴的多边形，我们可以用一个由R或者O组成的序列来描述他，从一个顶点开始按照逆时针顺序走，碰到一个90°的内角记作R；碰到一个270°的内角记作O。这样的序列称为角度序列。**

​ **给定正整数L，有多少个长度为L的角度序列至少可以对应一个星形多边形（即多边形中存在一个点，可以看到多边形边界上的每一个点）？多边形的每条边长度任意。注意一个多边形有多条角度序列与之对应，RRORRR与ORRRRR是不同序列，但可以描述同一个多边形。**


输入描述：


​ **输入包含多组数据，每组数据仅占一行，即角度序列的长度L（1<=L<=1000）输入结束标志（L=0）**


输出描述：


​ **对于每组数据，输出满足条件的角度序列的个数。**


分析：


​ 长度为L的多边形的内角和是一定的，且270°的内角与90°的内角的个数是恒定为L。所以设90°的个数为x个，270°的个数为y个。

$x+y=L$

$90*x+270*x=(L-2)*180$

解得

$x=(l+4)/2$

$y=(l-4)/2$

故可知 90°的序列比270°的多4个，且L必须为偶数，且L >=4

​



**还有那些限制条件呢？**

题目描述的形状由上 下 左 右 四条边，即由4个RR的连续的串， 且OO不能连在一起，最左边是O，最右边是O也不行

那么可以用插空法

1.最左（右）边是O的方法数目 C（x-1，y-1）

2.左右两边有没有O的方法数目 C（x-1，y ）

故答案 

$$ans=C(x-1,y-1)*2+C(x-1,y)$$




```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=10000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
ull l;
int main()
{
    ull ans;
    int kcas=0;
    while(cin>>l,l)
    {
        if(l<=3||l&1)
        {
            ans=0;
        }
        else
        {
            ull x=(l+4)/2;
            ans=(x*(x-1)*(x-2)*(x-3))/24+((x-1)*(x-2)*(x-3)*(x-4))/24;
        }
        printf("Case %d: ",++kcas);
        cout<<ans<<endl;

    }
    return 0;
}
```


