

## 中国剩余定理


看介绍和解方程：https://baike.baidu.com/item/%E5%AD%99%E5%AD%90%E5%AE%9A%E7%90%86


前提:

$M_{i}$互质


例题：POJ1006 代码：


该代码只能处理模数互质的情况，对于模数不互质的情况，可以依此合并一次同余同余方程来求解。详情看最后kuangbin的模板 过了一年后看自己写的代码感觉好丑而且不使用


```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxn=1e4+10;
ll ExGcd(ll a,ll b,ll &x,ll &y)//求 a b 最大公约数，且得到gcd(a,b)=x*a+y*b;
{
    if(!b)
    {
        x=1;
        y=0;
        return a;
    }
    ll gcd=ExGcd(b,a%b,x,y);
    ll temp,k=a/b;
    temp=x;
    x=y;
    y=temp-k*y;
    return gcd;
}
bool IsOk;
ll calc(ll a,ll c,ll m)
{
    ll x,y;
    ll gcd=ExGcd(a,m,x,y);
    if(c%gcd!=0)
    {
        IsOk=false;
        return 0ll;
    }
    return c/gcd*x%m;
}
/*

前提 mi互质
中国剩余定理
x=a1(mod m1)
x=a2(mod m2)
x=an(mod mn)
设M为m1...mn大的乘积
Mi=M/mi
设ti为Mi关于mi的逆元
则 ans=ai*Mi*ti 时间复杂度为O(n*gcd)
*/
ll aa[maxn],mm[maxn];
ll CRT(int n)//n个方程 返回x的的值
{
    ll Mpro=1;
    for(int i=0; i<n; ++i)
        Mpro*=mm[i];
    ll ans=0;
    for(int i=0; i<n; ++i)
    {
        aa[i]%=mm[i];
        ans+=(aa[i]*calc(Mpro/mm[i],1,mm[i])%Mpro*(Mpro/mm[i]))%Mpro;
    }
    return ans;
}
int main()
{
    ll a,b,c,d;
    mm[0]=23,mm[1]=28,mm[2]=33;
    int cas=0;
    ll ans=0;
    while(cin>>a>>b>>c>>d)
    {
        if(a==-1)
            break;
        aa[0]=a;
        aa[1]=b;
        aa[2]=c;
        ans=CRT(3);
        ll Mpro=23*28*33;
        ans=((ans-d)%Mpro+Mpro)%Mpro;
        cout<<"Case "<<++cas<<": the next triple peak occurs in ";
        cout<<(ans==0?Mpro:ans)<<" days."<<endl;
    }
    return 0;
}



```


#### kuangbin的代码，处理模数不互质的情况。


```cpp
long long extend_gcd(long long a,long long b,long long &x,long long  &y)
{
    if(a == 0 && b == 0)return -1;
    if(b ==0 )
    {
        x = 1;
        y = 0;
        return a;
    }
    long long d = extend_gcd(b,a%b,y,x);
    y -= a/b*x;
    return d;
}
int m[10],a[10];//模数为m,余数为a, X % m = a
bool solve(int &m0,int &a0,int m,int a)
{
    long long y,x;
    int g = extend_gcd(m0,m,x,y);//得到的x是m0/g关于m1/g的逆元
    if( abs(a - a0)%g )return false;
    x *= (a - a0)/g;
    x %= m/g;
    a0 = (x*m0 + a0);
    m0 *= m/g;  //合并方程后的模数是增大的
    a0 %= m0;
    if( a0 < 0 )a0 += m0;
    return true;
}
/*
 * 无解返回false,有解返回true;
 * 解的形式最后为 a0 + m0 * t  (0<=a0<m0)
 */
bool MLES(int &m0,int &a0,int n) //解为  X = a0 + m0 * k
{
    bool flag = true;
    m0 = 1;
    a0 = 0;
    for(int i = 0; i < n; i++)
        if( !solve(m0,a0,m[i],a[i]) )
        {
            flag = false;
            break;
        }
    return flag;
}

```




### 扩展欧几里得算法：


$a x + b y = g c d ( a , b ) ​ ax+by=gcd(a,b)​$ 求出满足条件唯一的x,y的值

$设 ： 设：$


a为r0，b为r1


$r 0 = q 1 ∗ r 1 + r 2 r_{0}=q_{1}*r_{1}+r_{2}$

$r 1 = q 2 ∗ r 2 + r 3 r_{1}=q_{2}*r_{2}+r_{3}$

$r 2 = q 3 ∗ r 3 + r 4 ​ r_{2}=q_{3}*r_{3}+r_{4}​$

$. . . . . . . . . . ..........$



## P4774 [NOI2018]屠龙勇士(exCRT)


题目链接:[传送门](https://www.luogu.org/problem/P4774)

**思路**：

​     首先根据题意我们可以算出来对于每一条龙使用的武器攻击力（这个使用set和upper_bound成员函数很容易实现）。

​     现在我们价假设第 $i ​ i​$ 条龙的生命值为$h [ i ] ​ h[i]​$,恢复能力为$p [ i ] ​ p[i]​$,此时使用的武器攻击力为$g [ i ] ​ g[i]​$, 那么我们攻击次数$x ​ x​$ 需要满足这样的方程式$( h [ i ] − x ∗ g [ i ] ) % p [ i ] = 0 ​ (h[i]-x*g[i])\%p[i]=0​$ ，且$h [ i ] − x ∗ g [ i ] ≤ 0 ​ h[i]-x*g[i]\le 0​$。

​     现在我们有n个方程我们根据所有的第二个限制条件求出来$x x$的最小值。接下来就是对所有的第一个方程求出x的值即可。很容易看出第一个方式即$x ∗ g [ i ] = h [ i ]     (    m o d    p [ i ] ) x*g[i]=h[i] ~~~(~~mod~~p[i])$     我们把等式两边全除以$g [ i ] , h [ i ] , p [ i ] g[i],h[i],p[i]$

