

## 2018 CCPC final G.Pastoral Life in Stardew Valley(思路)


题目链接：[传送门](https://codeforces.com/gym/102055/problem/G)


这题一开始只想着对一个求和公式化简，但是用另一个角度来看这个问题就很简单了

题意：给一个n行m列，问有多少种方法使得放两个矩形，且矩形 1 完全包含在矩形 2 内，且边界之隔最小为1.
思路：

对于矩形，因为长宽互不影响，所以问题就化简为**一个长度为n的一维格子，有多少种方法选两个的区间，使得区间1被区间2完全包含且两区间边界相隔至少为1.**

区间1的长度的等于1时，那么就相当于长度为n的一排格子，选3个不同的格子，其种类数即$C_n^3$

区间1的长度大于1时，那么相当于长度为n的一排格子，选4个不同的格子，其种类数为$C_n^4$

所以总的答案就是$(C_n^4+C_n^3)*(C_m^4+C_m^3)$

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll mod=1e9+7;
const int N=1e5+10;
ll f[N],g[N];
ll qpow(ll a,ll b)
{
    ll ans=1;
    while(b)
    {
        if(b&1) ans=ans*a%mod;
        a=a*a%mod;
        b>>=1;
    }
    return ans;
}
void init()
{
    int n=1e5;
    f[0]=1;
    for(ll i=1;i<=n;++i)
        f[i]=f[i-1]*i%mod;
    g[n]=qpow(f[n],mod-2);
    for(ll i=n-1;i>=0;--i)
        g[i]=g[i+1]*(i+1)%mod;
}
ll C(ll a,ll b)
{
    if(a < b) return 0;
    return f[a]*g[b]%mod*g[a-b]%mod;
}
ll calc(ll n)
{
    return (C(n,3)+C(n,4))%mod;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    init();
    int t,cas=0;
    cin>>t;
    while(t--)
    {
        ll n,m;
        cin>>n>>m;
        cout<<"Case "<<++cas<<": "<<calc(n)*calc(m)%mod<<'\n';
    }
    return 0;
}
```


