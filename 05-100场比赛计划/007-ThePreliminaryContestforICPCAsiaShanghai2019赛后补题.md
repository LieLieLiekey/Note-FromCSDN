

## The Preliminary Contest for ICPC Asia Shanghai 2019 赛后补题


#### 比赛链接:[传送门](https://www.jisuanke.com/contest/3003?view=challenges)



这次比赛过程中大部分都是队友A的，所以这里补一下自己没有A到的题和没A的题。

这次又出到了Bell 数的相关知识，跟昨天的网络赛有相似的题但是还没时间补。尽快把不会的知识点补全。

增加了退背包的思想。

G题hash字符串还未补


#### B：Light bulbs


定位：简单题

**题意**：t组输入，有一排长度为n的灯泡，初始状态都是关闭，接下来m次操作，每次操作使得区间$[l,r]$ 灯泡状态反转，问最后有多少个灯泡开着的。$t\in[1,1000],n\in(1,1e6),m\in[1,1000]$

**思路**：这是明显的区间异或，我们可以将区间异或变成异或差分的形式。这样每组时间复杂度为$O(n)$，但是t组却超时了，我们注意到m很小，所以我们处理出所有变化的点，然后排序统计答案即可。每组的时间复杂度为$O(mlogm)$。

**代码**：

```cpp
#include <bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef pair<int,int> P;
const int N=1e6+20;
int sq[N];
int main()
{
    int n,m,t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        int top=0;
        for(int i=1;i<=m;++i){
            int l,r;
            scanf("%d%d",&l,&r);
            l++,r++;
            sq[top++]=l;
            sq[top++]=r+1;
        }
        sort(sq,sq+top);
        int ans=0,pe=0,last=1;
        for(int i=0;i<top;++i){
            if(pe&1)    ans+=sq[i]-last;
            last=sq[i];
            pe^=1;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
}
```


#### D：Counting Sequences I


定位：中等偏难

**题意**：给出一个n，求满足条件$a_1+a_2+a_3...+a_n=a_1*a_2*a_3...*a_n$的序列的个数。

**思路**：我们可以看出来序列的顺序改变不影响等式成立，并且模拟几下可以看出来总有$n-2$个1，一个2，一个n的序列满足条件，并且当次大的数增大1时，最大的数减小速度快，所以我们可以推断出这个序列的和不超过$2*n$，并且不考虑位置的情况下，满足条件的序列数目应该很少，所以我们可以暴力搜索+大剪枝。然后对于每一个序列计算该序列考虑位置的组合数即可


只要知道前面的信息，那么随意剪枝就行。

这题因为check快速幂的一个小错误，检测a^b是否大于k，应该先让b/2，再判断a是否在于k。找了1h30min的bug…


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const ll N=3000+20;
const ll mod=1e9+7;
ll qpow(ll a,ll b,ll m)
{
    ll ans=1;
    while(b)
    {
        if(b&1) ans=ans*a%m;
        a=a*a%m;
        b>>=1;
    }
    return ans;
}
int ok;
ll ckpow(ll a,ll b,ll limt)
{
    ll ans=1;
    while(b)
    {
        if(b&1)
        {
            ans=ans*a;
            if(ans>limt)
                return -1;
        }
        b>>=1;
        a=a*a;
        if(b!=0&&a>limt)
            return -1;

    }
    return ans;
}
ll inv(ll a)
{
    return qpow(a,mod-2,mod);
}
ll f[N],g[N];//i!,i!逆元
void init()
{
    f[0]=1;
    for(ll i=1; i<=3000; ++i) f[i]=(f[i-1]*i)%mod;
    for(ll i=1; i<=3000; ++i)
    {
        g[i]=inv(f[i]);
    }
}
ll calc(ll w[],ll n)
{
    ll ans=f[n];
    map<ll,ll> mmp;
    for(ll i=1; i<=n; ++i) mmp[w[i]]++;
    for(P p:mmp)
    {
        ans=ans*g[p.second]%mod;;
    }
    return ans;
}
ll s[3005],res,n;
void dfs(ll ps,ll pt,ll limt,ll k)
{

    if(pt > 2*n) return ;
    if(pt > ps &&limt > 1) return ;
    if((n-k+1)*limt + ps> 2*n) return ;//数列和优化
    ll si=ckpow(limt,n-k+1,2*n);
    if(limt>1 &&si==-1) return ;//数列乘积优化
    if(limt>1&& si*pt>2*n) return ;//数列乘积优化

    if(k > n){
        if(ps==pt){
            res=(res+calc(s,n))%mod;
        }

        return ;
    }
    for(ll i=limt;i<=n;++i){
        int si=ckpow(i,n-k,2*n);
        if(si==-1||si*i*pt>2*n) return ;
        s[k]=i;
        dfs(ps+i,pt*i,i,k+1);
    }
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    init();
    ll t;
    cin>>t;
    while(t--)
    {
        cin>>n;
        res=0;
        dfs(0,1,1,1);
        cout<<res<<endl;
    }
    return 0;
}

```


#### J：Stone game


定位：中等偏难

**题意**：给出n个石头，每个石头的价值为$a_i$，求有多少种取法使得，取的石头价值和大于等于未取的石头价值和，且满足从拿到的石头中任意减去一个石头的价值使得 剩下的价值小于等于未取的石头价值和。$n\in[1,300],a_i\in[1,500]$

**思路**：01退背包思想，然后枚举最小值计算满足其题意的解的个数即可。

我们首先将物品从小到大排序，先计算出01背包满足总价值为 $j$ 的取法个数。然后退去物品$a_1$求出满足总价值为 $j$ 的取法个数，满足条件的价值是一个区间$[(sum+1)/2-a_i,(sum-a_i)/2]$，统计其种类数即可。接下来就是枚举$a_2$是所取集合中最小的物品，此时我们只需要将$a_1,a_2​$从背包中退去即可，然后模仿上面统计即可。以此类推一直到$a_n$。


比赛中只有想到用$dp[i][j]$为集合中最小值为 $i$ ,集合元素和为$j$的方法数，但时间复杂度不允许。

也是第一次碰到这种退背包的思想。与此同时还有多重背包的退背包。


**代码**:

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=300+20;
const int mod=1e9+7;
int dp[305*505],w[305];
int main()
{
    int t,n,ans,sum;
    scanf("%d",&t);
    while(t--)
    {
        ans=sum=0;
        scanf("%d",&n);
        dp[0]=1;
        for(int i=1;i<=n;++i) {
            scanf("%d",&w[i]);
        }
        sort(w+1,w+n+1);
        for(int i=1;i<=n;++i){
            sum+=w[i];
            for(int j=sum;j>=w[i];--j){
                    dp[j]=(dp[j]+dp[j-w[i]])%mod;
            }
        }
        for(int i=1;i<=n;++i)
        {
            for(int j=w[i];j<=sum;++j) dp[j]=(dp[j]-dp[j-w[i]]+mod)%mod;
            int down=max((sum+1)/2 - w[i],0),up=(sum-w[i])/2;

            for(int j=down;j<=up;++j){
                ans=(ans+dp[j])%mod;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
```


#### L：Digit sum


定位：简单题

**题意**：给出n和b，求$[1,n]$所有的数在b进制下的数位和。$n\in [1,1e6],b\in[2,10]$

**思路**：我们只要算出每位的每个数对答案的贡献即可。算贡献的方法：假设n在b进制表示为$a_ka_{k-1}a_{k-2}...a_0​$。

那么对于下标为$i$，其所有情况的贡献为$pre[i]*\sum _{i=0} ^{b-1}*b^i+\sum _{i=0} ^{a_i-1}*b^i+a_i*(suf[i]+1)$ 。其中$pre[i]$等于$a_ka_{k-1}...a_{i+1}$，$suf[i]$表示为$a_{i-1}...a_0$。

当然也可以数位dp。

```cpp
#include <bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll num[45],pre[45],suf[45];
ll init(ll n,ll b)
{
    ll nn=n;
    ll top=0;
    do{
        num[top++]=n%b;
        n/=b;
    }
    while(n);
    suf[0]=0;
    ll m=1;
    for(ll i=1;i<top;++i){
        suf[i]=suf[i-1]+m*num[i-1];
        m*=b;
    }
    m=nn;
    for(ll i=0;i<top;++i){
        m/=b;
        pre[i]=m;
    }
    return top;
}
ll qpow(ll a,ll b)
{
    ll ans=1;
    while(b)
    {
        if(b&1) ans=ans*a;
        a=a*a;
        b>>=1;
    }
    return ans;
}
ll work(ll n,ll b)
{
    ll top=init(n,b);
    ll ans=0;
    for(ll i=top-1;i>=0;--i)
    {
        ll m=0;
        m+=pre[i]*((b-1)*b)/2*qpow(b,i);
        if(num[i]!=0){
            m+=qpow(b,i)*((num[i]-1)*num[i])/2;
        }
        m+=num[i]*(suf[i]+1);
        ans+=m;
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    ll t,cas=0;
    cin>>t;
    while(t--)
    {
        ll n,b;
        cin>>n>>b;
        cout<<"Case #"<<++cas<<": "<<work(n,b)<<endl;
    }
    return 0;
}

```


