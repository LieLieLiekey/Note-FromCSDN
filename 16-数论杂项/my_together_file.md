

## bzoj4428 [Nwerc2015]Debugging（数论+记忆化搜索）



说下做这个题的初衷，这题第一次见是在2018年在一份pdf上看到的，当时不会，怎么理解都不懂，然后就在2019-9-15的上海网络赛上见到了数据增强后的原题，由于看完题解还是不会，寻思着补一下小范围数据的原题吧。

PS：发现UOJ这个新大陆。


#### 题目链接：[传送门](https://darkbzoj.tk/problem/4428)


#### 题意：


​ 有一个n行代码的程序存在一个bug，现在要定位这个bug，可以在 $i$ 行末尾加$print$语句，运行后你可以看出bug在第 $i$ 行下面，还是第$i$ 行上面(包括第$i$行)，但是运行一个程序需要$r$分钟，加一个$print$语句需要$p$分钟。问在最坏的情况下，最少多少时间能定位到这个bug。

#### 思路：


我们用$dp[i]​$表示长度为$i​$行的bug需要的最少时间。所以我们可以枚举这次运行时添加的$print​$语句，设为$j​$,那么$dp[i]=min(dp[\lceil \frac{n}{j+1} \rceil]+j*p+r),j\in[1,n-1]​$。

考虑到$\lceil\frac{n}{k}\rceil$只有$O(\sqrt n)$种值，我们可以优化下直接取所有不同取值，对于每种取值取$k$最小的。

怎么取$\lceil\frac{n}{k}\rceil$的所有取值呢？其实列个映射关系就看出来其中的奥妙了

+ 令$i=n$+ 令$last=\lceil\frac{n}{\lceil \frac{n}{i} \rceil}\rceil​$+ 那么$j=\lceil\frac{n}{last}\rceil$ 是一个解+ 令$i=last-1$，如果$i>0$返回第二步


至于这道题，dp过程中注意到$\frac{n}{k}​$的分目不能等于$1​$，然后用记忆化搜索优化即可，据某博客说时间复杂度为$O(n^{\frac{3}{4}})​$

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e6+20;
const int inf=0x3f3f3f3f;
ll f[N],r,p;
ll cdiv(ll a,ll b)
{
    return (a+b-1)/b;
}
ll dfs(ll n)
{
    if(n==1) return 0;
    if(f[n]) return f[n];
    ll ans=1ll << 62;
    for(ll i=n,last;i > 1 ; i=last-1)//不能取到自身
    {
        last=cdiv(n,cdiv(n,i));
        ll j=cdiv(n,last);
        ans=min(ans,dfs(j)+(last-1)*p+r);
    }
    return f[n]=ans;
}
int main()
{
    ll n;
    cin>>n>>r>>p;
    cout<<dfs(n)<<endl;
}

```


数据增强的题目链接：[传送门](https://nanti.jisuanke.com/t/41419)



## 关于向上取整和向下取整知识整理


向下取整函数$f ( x ) = ⌊ x ⌋ f(x)=\lfloor x\rfloor$ 是单调递增的 ，向上取整函数$f ( x ) = ⌈ x ⌉ f(x)=\lceil x\rceil$也是单调递增的。

对任意整数n，



$$⌈ n 2 ⌉ + ⌊ n 2 ⌋ = n \lceil \frac{n}{2}\rceil+\lfloor \frac{n}{2}\rfloor=n$$





$$⌈ n b ⌉ = ⌊ n + b − 1 b ⌋ ​ \lceil \frac{n}{b}\rceil=\lfloor \frac{n+b-1}{b}\rfloor​$$



对任意 **实数**$x ≥ 0 x\ge0$和**整数**$a , b > 0 a,b>0$



$$⌈ ⌈ x / a ⌉ b ⌉ = ⌈ x a b ⌉ ​ \lceil \frac{\lceil x/a\rceil}{b}\rceil=\lceil \frac{x}{ab} \rceil​$$





## P2480 [SDOI2010]古代猪文（lucas定理）


**题目链接**:[传送门](https://www.luogu.org/problem/P2480#submit)

**思路**： 题目其实就是求$G^{\sum_{d|n}C(n,d)} \%999911659​$的值，因为999911659是素数，我们我们可以用欧拉定理缩小幂次让原方程变为$G^{\sum_{d|n}C(n,d)\%(999911658)} \%999911659​$，但是n太大，求幂次中的$\sum_{d|n}C(n,d)\%999911658​$的值就不太现实，所以我们可以考虑将999911658分解素因子$2, 3,4679,35617​$的乘积，然后分别求$\sum_{d|n}C(n,d)\%2​$， $\sum_{d|n}C(n,d)\%3​$， $\sum_{d|n}C(n,d)\%4679​$， $\sum_{d|n}C(n,d)\%35617​$。然后用CRT合并即可。

现在问题转化为大组合数取余小质数，此时我们可以使用$lucas​$定理：



$$C(a,b)\%p=C(a\%p,b\%p)*C(a/p,b/p)\%p$$



就可以求出来了。

不过需要额外特判$G$是$999911659$的倍数的情况。

**代码**：

```bash
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e5+100;
const int inf=0x3f3f3f3f;
ll fac[N],tf;//因子
void dps_fac(ll n)//分解n的所有因子
{
    tf=0;
    for(int i=1;i*i<=n;++i){
        if(n%i==0){
            fac[tf++]=i;
            if(n/i!=i) fac[tf++]=n/i;
        }
    }
}
ll pf[20],tp;//素因子
void dps_p(ll n)//分解n的素因子
{
    tp=0;
    for(ll i=2;i*i<=n;++i){
        while(n%i==0){
            pf[tp++]=i;
            n/=i;
        }
    }
    if(n!=1) pf[tp++]=n;
}
ll qpow(ll a,ll b,ll p)
{
    if( a <= 0) return 0;
    ll ans=1;
    while(b)
    {
        if(b&1) ans=ans*a%p;
        a=a*a%p;
        b>>=1;
    }
    return ans;
}
ll f[40005];//n!%mod
void init(ll mod)
{
    f[0]=1;
    for(int i=1;i<=36000;++i) f[i]=(f[i-1]*i)%mod;
}
ll C(ll n,ll m,ll p)//要求:预处理mod p的阶乘f[]
{
    if(n<m) return 0;
    return f[n]*qpow(f[m],p-2,p)%p*qpow(f[n-m],p-2,p)%p;
}
//
ll lucas(ll n,ll m,ll p)//    C(a,b)%c的值
{

    if(n < m) return 0;
    if(!n) return 1;
    return lucas(n/p,m/p,p)*C(n%p,m%p,p)%p;
}
ll inv(ll a,ll p)//要求p是质数
{
    return qpow(a,p-2,p);
}
void CRT(ll w[],ll p[],int n,ll &m,ll &a)
{
    a=0,m=1;
    for(int i=0;i<n;++i) m*=p[i];
    for(int i=0;i<n;++i){
        ll t=m/p[i];
        a=(a+w[i]*t*inv(t,p[i]))%m;
    }
}
ll w[N];
void work(ll n,ll g,ll mod)
{
    //首先n的因子分解,然后mod进行质因子分解,用欧拉降幂先求 指数%(mod-1)
    dps_p(mod-1);
    dps_fac(n);
    for(int i=0;i<tp;++i){//枚举(mod-1)的每个素因子,求出来一份结果
        init(pf[i]);
        ll v=0;
        for(int j=0;j<tf;++j)
            v=(v+lucas(n,fac[j],pf[i]))%pf[i];//求出这个结果
        w[i]=v;
    }
    ll m,a;
    CRT(w,pf,tp,m,a);
    ll ans=qpow(g,a,mod);
    cout<<ans<<endl;
    //剩下用CRT合并
}
int main()
{
    ll n,g,mod=999911659ll;//2  3 4679 35617
    cin>>n>>g;
    if(g%mod==0){
        cout<<0<<endl;
        return 0;
    }
    work(n,g,mod);
    return 0;
}

```


