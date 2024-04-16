

### LOJ-1284 Lights inside 3D Grid（期望，二次项公式奇数项求和）


##### 题目链接：[传送门](https://vjudge.net/problem/LightOJ-1284)


##### 题目：


在尺寸为$X*Y*Z$的长方体中每个位置都有一个灯泡，初始没有亮，每次随机取两个点$(x1,y1,z1)$,$(x2,y2,z2)$。让所有满足$x\in[x1,x2],y\in[y1,y2],z\in[z1,z2]$，的点的灯泡状态反转，问 $k$ 次操作后灯泡亮的个数期望值是多少？

##### 思路：


看到数据感觉枚举每个坐标比较实际，对于点$(x,y,z)$，我们用$g(x,y,z)$表示一次中命中点$(x,y,z)$的概率，$f(x,y,z)$表示一次没有点$(x,y,z)$的概率，所以$f(x,y,z)+g(x,y,z)=1.0$。

在$x\in[x1,x2],y\in[y1,y2],z\in[z1,z2]​$时该点才会被命中， 容易看出在维度$x​$被命中的概率为$1-\frac{(x-1)^2+(X-x)^2}{X^2}​$

，故$g(x,y,z)=(1-\frac{(x-1)^2+(X-x)^2}{X^2})*(1-\frac{(y-1)^2+(Y-y)^2}{Y^2})*(1-\frac{(z-1)^2+(Z-z)^2}{Z^2})​$ 。

设$a=f(x,y,z),b=g(x,y,z)​$，所以$k​$次后位置$(x,y,z)​$灯泡亮的概率为：

$$p=C_{k}^{1}*a^1*b^{k-1}+C_{k}^{3}*a^3*b^{k-3}+C_{k}^{5}*a^5*b^{k-5}...​$$



即$(a+b)^k$二项式张展开的奇数项的和，想起来怎么求了吗？

将奇数项的和设为$S1$,偶数项的和设为$S0$。

有$S0+S1=1$

接下来我们令$a'=-a$,那么$(a'+b)^k=(-a+b)^k=-S0+S1$

有这两个方程我们就能联立解出$S1$，即二次项展开的奇数项的和，即灯泡$(x,y,z)$经过 k 次后被命中的概率。

期望$E=\sum_p p*val$，就可以求出经过k次操作后所有灯泡中亮期望个数。

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const double eps=1e-5;
double g[110][110][110];
double getp(int k,int n)
{
    double m=((k-1)*(k-1)+(n-k)*(n-k))/(1.0*n*n);
    return 1.0-m;
}
int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int X,Y,Z,k;
        scanf("%d%d%d%d",&X,&Y,&Z,&k);
        double ans=0.0;
        for(int a=1; a<=X; ++a)
        {
            double pa=getp(a,X);
            for(int b=1; b<=Y; ++b)
            {
                double pb=getp(b,Y);
                for(int c=1; c<=Z; ++c)
                {
                    double pc=getp(c,Z);
                    g[a][b][c]=pa*pb*pc;
                    double gg=g[a][b][c];
                    double m=pow(1-2*gg,k);
                    ans+=(1-m)/2.0;
                }
            }
        }
        printf("Case %d: %.8f\n",++cas,ans);
    }
}

```


