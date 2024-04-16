

## 900D. Unusual Sequences（莫比乌斯反演）


##### 题目链接：[传送门](https://codeforces.com/contest/900/problem/D)


##### 题意：


给出 $x$ 和 $y$ ,求序列形如 $a_1,a_2..a_n$ 满足 $gcd(a_1,a_2...a_n)=1$ 且 $\sum_{i=1}^na_i=y$ 的序列的个数。( $n$ 没有约束)

#### 思路：


令$b_i=a_i$，我们很容易知道问题可以转化为$\sum_{i=1}^{n} b_i=\frac{y}{x},gcd(b_1,b_2...b_n)=1$。

我们用$f(n)$ 表示序列和为 $n$ , $gcd(b_1,b_2...b_n)=1$的序列的个数。$g(n)$表示序列和为 $n$ 的序列的个数。

对于$g(n)​$，我们用隔板法可知,$g(n)=C_{n-1}^{0}+C_{n-1}^{1}...+C_{n-1}^{n-1}=2^{n-1}​$，且序列的所有可能的 $gcd​$ 都是 $n​$ 的约数，所以



$$g(n)=\sum_{d|n}f(n/d)​$$



我们用莫比乌斯反演可将之转化为



$$f(n)=\sum_{d|n}mu(d)*g(n/d)$$



所以我们只需筛出n的所有约数的莫比乌斯函数，然后遍历求出$f(n)$即可

代码：

```cpp
#include<bits/stdc++.h>
#define mse(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e5+10;
const ll mod=1e9+7;
//把n的约束的莫比乌斯反演反演函数的值使用map的形式返回.O(sqrt(n))
map<int,int> moebius(int n)
{
    map<int,int> res;
    vector<int> primes;
    for(int i=2; i*i<=n; ++i)
    {
        if(n%i==0)
        {
            primes.push_back(i);
            while(n%i==0) n/=i;
        }
    }
    if(n!=1) primes.push_back(n);
    int m=primes.size();
    for(int i=0; i< (1<<m) ; ++i)
    {
        int mu=1,d=1;
        for(int j=0; j<m; ++j)
        {
            if(i >>j & 1){
                mu*=-1;
                d*=primes[j];
            }
        }
        res[d]=mu;
    }
    return res;
}
ll qpow(ll a,ll b)
{
    ll ans=1;
    while(b)
    {
        if(b&1)
            ans=ans*a%mod;
        a=a*a%mod;
        b>>=1;
    }
    return ans;
}
int g(ll n)
{
    return (int)qpow(2,n-1);
}
ll f(int n)
{
    map<int,int> mu;
    mu=moebius(n);
    int ans=0;
    for(auto it=mu.begin();it!=mu.end();++it)
    {
        ans += it->second * (g( n / it->first));
        ans=(ans%mod+mod)%mod;
    }
    return ans;
}
int main()
{
    int x,y;
    cin>>x>>y;
    if(y%x!=0)
        cout<<0<<endl;
    else
        cout<<f(y / x)<<endl;
}

```


