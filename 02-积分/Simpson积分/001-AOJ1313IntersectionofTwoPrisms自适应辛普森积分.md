

## AOJ1313 Intersection of Two Prisms（自适应辛普森积分）


##### 题目链接：[传送门](https://onlinejudge.u-aizu.ac.jp/problems/1313)


##### 思路：



SImpson积分了解：[传送门](https://phqghume.github.io/2018/05/19/%E8%87%AA%E9%80%82%E5%BA%94%E8%BE%9B%E6%99%AE%E6%A3%AE%E6%B3%95/)


我们可以将x轴分割为数个小区间的形式，然后对每个小区间进行计算相交的体积，然后将结果相加即可，对于棱平行于z轴的棱柱P1，在$[x,x+dx]$处分割的长方体为$x'\in[x,x+dx],y'\in[y1,y2],z'\in [-\infty,+\infty]$ 。对于棱柱P2，在x处分割的长方体为$x'\in[x,x+dx],y'\in [-\infty,+\infty],z'\in[z1,z2]$。所以相交的体积为$dx*(z2-z1)*(y2-y1)$.

因为多边形在x处的截距的长度随着x的增加在顶点处不连续，即不可导，所以不能一次全部定积分。

但我们可以分段统计，对于区间$[x1,x2]​$ 如果在两个多边形中都不存在断点，即区间$[x1,x2]​$分别是两多边形的某条边的x的范围，我们就可以定积分求出他们的积分。

这个很简单，我们只需把两个多边形的顶点的X全部存起来，从小到大排序，那么挨着的两个X代表的区间绝对是连续的，可以看出P1的底面在x处的截距y是关于x的线性函数，所以他们的乘积$f(x)=(z2-z1)*(y2-y1)​$是个二次函数，所以$\int _{x1}^{x2} f(x)*dx​$ 可以用Simpson积分计算。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn=550;
const int inf=0x3f3f3f3f;
int _m,_n;//第一个是m多边形,第二个是n多边形
int X1[105],Y1[105],X2[105],Z2[105];//下标从0开始
double width(int X[],int Y[],int n,double x)//对于n个点的多边形(x,y)
{
    double down=1e8,up=-1e8;
    for(int i=0;i<n;++i)
    {
        int x1=X[i],y1=Y[i],x2=X[(i+1)%n],y2=Y[(i+1)%n];
        if(x1>x2){
            swap(x1,x2);swap(y1,y2);
        }
        if(x>=x1&&x<=x2){
            double y=y1+(x-x1)*(y2*1.0-y1)/(x2-x1);
            down=min(down,y);
            up=max(up,y);
        }
    }
    return max(0.0,up-down);
}
double f(double x)
{
    return width(X1,Y1,_m,x)*width(X2,Z2,_n,x);
}
double simpson(double a,double b)//要求a<b
{
    double c=(a+b)/2.0;
    return (b-a)/6.0*(f(a)+4*f(c)+f(b));
}
vector<int> sx;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    while(cin>>_m>>_n)
    {
        if(_m==0&&_n==0) return 0;
        sx.clear();
        for(int i=0;i<_m;++i){
            cin>>X1[i]>>Y1[i];
            sx.push_back(X1[i]);
        }
        for(int i=0;i<_n;++i){
            cin>>X2[i]>>Z2[i];
            sx.push_back(X2[i]);
        }
        sort(sx.begin(),sx.end());
        int min1=*min_element(X1,X1+_m),max1=*max_element(X1,X1+_m);
        int min2=*min_element(X2,X2+_n),max2=*max_element(X2,X2+_n);
        double res=0;
        for(int i=0;i+1<sx.size();++i)
        {
            int a=sx[i],b=sx[i+1];
            if(a>=min1&&a<=max1&&a>=min2&&a<=max2&&b>=min1&&b<=max1&&b>=min2&&b<=max2)
            {
                res+=simpson(a*1.0,b*1.0);
            }
        }
        cout<<fixed<<setprecision(10)<<res<<endl;
    }
}
```


