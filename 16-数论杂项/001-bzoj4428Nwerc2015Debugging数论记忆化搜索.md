

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

