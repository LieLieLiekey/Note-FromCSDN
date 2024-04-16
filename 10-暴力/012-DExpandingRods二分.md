

### D - Expanding Rods


When a thin rod of length L is heated n degrees, it expands to a new length L’=(1+n*C)*L, where C is the coefficient of heat expansion. When a thin rod is mounted on two solid walls and then heated, it expands and takes the shape of a circular segment, the original rod being the chord of the segment.

Your task is to compute the distance by which the center of the rod is displaced.

**Input**

The input contains multiple lines. Each line of input contains three non-negative numbers: the initial lenth of the rod in millimeters, the temperature change in degrees and the coefficient of heat expansion of the material. Input data guarantee that no rod expands by more than one half of its original length. The last line of input contains three negative numbers and it should not be processed.

**Output**

For each line of input, output one line with the displacement of the center of the rod in millimeters with 3 digits of precision.

**Sample Input**

```bash
1000 100 0.0001
15000 10 0.00006
10 0 0.001
-1 -1 -1
```


**Sample Output**

```bash
61.329
225.020
0.000
```


##### 题意：


一个长度为L的铁棒夹在距离为L的墙之间，随着温度的升高，铁棒会膨胀， 在温度n下，铁棒的的长度L‘=（1+n*c）*L ，其中n为常量系数 现在给你L N C，求铁棒的中心距离铁棒两端的高度为多少？其中铁棒弯曲后上方为一个圆形的一部分，且保证膨胀后满足 L’-L<=L/2

##### 分析：


铁棒弯曲后对应的圆的圆心在中线线上，且每一个R，就可以确定一个弧长，枚举R，求出对应的弧长l，不断逼近L，二分即可

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
double L,LL,n,c;
inline double f(double r)//半径对应的弧长
{
    double as=asin(L/(2.0*r));
    return 2.0*as*r;
}
double solve()
{
    double l=L/2.0,r=1e20,mid;//枚举半径R，求出在R下的弧长即可
    while(r-l>wc)
    {
        mid=(l+r)/2.0;
        if(f(mid)<LL)
            r=mid;
        else
            l=mid;
    }
    return (l+r)/2.0;
}
int main()
{
    while(scanf("%lf %lf %lf",&L,&n,&c))
    {
        if(L<0.0||n<0.0||c<0.0)
            break;
        if(n==0.0||c==0.0)
        {
             printf("0.000\n");
             continue;
        }
        LL=(1.0+n*c)*L;
        double ar=solve();//求出半径
        double as=asin(L/(2.0*ar));//求出此时的圆心角的一半
        cout<<fixed<<setprecision(3)<<ar*(1-cos(as))<<endl;
    }
    return 0;
}
```


