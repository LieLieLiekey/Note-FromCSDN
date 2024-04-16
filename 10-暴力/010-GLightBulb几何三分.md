

### G - Light Bulb


Compared to wildleopard’s wealthiness, his brother mildleopard is rather poor. His house is narrow and he has only one light bulb in his house. Every night, he is wandering in his incommodious house, thinking of how to earn more money. One day, he found that the length of his shadow was changing from time to time while walking between the light bulb and the wall of his house. A sudden thought ran through his mind and he wanted to know the maximum length of his shadow.

**Input**

The first line of the input contains an integer *T* (*T* <= 100), indicating the number of cases.

Each test case contains three real numbers *H*, *h* and *D* in one line. *H* is the height of the light bulb while *h* is the height of mildleopard. *D* is distance between the light bulb and the wall. All numbers are in range from 10-2 to 103, both inclusive, and *H* - *h* >= 10-2.

**Output**

For each test case, output the maximum length of mildleopard’s shadow in one line, accurate up to three decimal places…

**Sample Input**


3 2 1 0.5 2 0.5 3 4 3 4


**Sample Output**


1.000 0.750 4.000


##### 题意：


[https://vjudge.net/contest/277059#problem/G](https://vjudge.net/contest/277059#problem/G) 对着题中的图看，可以假设人距离灯x米，那么每一个距离都可以利用几何关系得到一个L‘（影子的长度）

当$x=D-(H*D)/H$ 的的时候刚好影子的头部在墙角处，所以，根据几何关系求出来长度f关于x的关系式

$f(x)=x*h/(H-h)...........当x&lt;=D-h*D/H$

$f(x)=D+H-x-D(H-h)/x............当x&gt;=D-h*D/H$

对应第一种情况x的范围是$[0,D-h*D/H]$ 故最大值在端点处取

对应第二种情况x的取值范围为$[D-h*D/H,D]$,求导以后最大值点对应的$x=\sqrt{D*(H-h)}$

如果极值点在该区间则最大值在该点，否则，最大值在两端取。

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
const double wc=1e-6;
const ll MOD=1e9+7;
int t;
double H,h,D;
double f(double x)
{
    return D+H-x-D*(H-h)/x;
}
int main()
{
    double ans;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lf %lf %lf",&H,&h,&D);
        ans=D*h/H;
         double xx=D-(h*D/H);
        double jx=sqrt(D*(H-h));
        if(xx<=jx&&jx<=D)
        {
            ans=max(ans,f(jx));
        }
        else
            ans=max(ans,f(D));
        printf("%.3lf\n",ans);
    }
    return 0;
}
```


