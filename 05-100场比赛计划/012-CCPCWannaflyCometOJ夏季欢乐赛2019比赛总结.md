

## CCPC－Wannafly & Comet OJ 夏季欢乐赛（2019）比赛总结


##### 总结：


​ 这场比赛不太顺心，B，I水题 10分钟内A了。A题推公式用double写卡了1个小时，换成其他暴力也错了，赛后补题与AC代码对比发现一个语句的与想象中的不一样，但是现在还不知道为什么。C题阶乘没想到4!!爆int，一直以为会有个公式，真是大意了导致卡了1个小时。D题是线段树+扫描线，不熟悉主动放弃。G题想到了每类取前5个然后暴搜，但是算错时间复杂度了以为会超时就没写，不过5分钟之后想到状压dp就给A了。H题分配学号，思路也是比较顺利，不过代码写完之后有诸多bug（写错语句这种低级错误），导致比赛结束后也没A出来，赛后才直到一个变量没有赋新值，就这样浪费了一个多小时。

​ 总的来的这场比赛小错误犯的太多了，打代码的时候应该再用点心，初始化、语句写错等低级错误不用犯了。

##### 比赛链接：[传送门](https://www.cometoj.com/contest/59)


##### 题解：


**A题完全k叉树**

解决方案：满层的与根的距离*2+残缺层的最左边节点与上一层的距离+最右边的节点是否可以可以让答案更远。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int inf=0x3f3f3f3f;
const double eps=1e-9;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    ll n, k,ans=0;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        if(k==1ll){
            cout<<n-1ll<<endl;
            continue;
        }
        ll d=0ll,det=1ll,fsum=1ll;
        while(true)
        {
            if(det*k+fsum>n) break;
            d++;
            det*=k;
            fsum+=det;
        }
        ans=d*2;
        if(n-fsum>0ll) ans++;
        if(n-fsum>det) ans++;
        cout<<ans<<endl;

    }
    return 0;
}
```


**B题距离产生美**

解决方案：贪心

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll A[100005];
int main()
{
    int n;
    ll k;
    ios::sync_with_stdio(false);cin.tie(0);
    cin>>n>>k;
    ll ppp=1e18+10;
    for(int i=0;i<n;++i) cin>>A[i];
    int ans=0;
    for(int i=1;i<n;++i)
    {
        if(abs(A[i]-A[i-1])<k){
            ans++;
            A[i]=ppp;
        }
    }
    cout<<ans<<endl;
    return 0;
}
```


**C题烤面包片**

解决方案：n>=4的话，n!!的值一定大于mod，结果是0，其他情况暴力求解

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll calc(ll a)
{
    ll ans=1;
    for(ll i=a; i; --i)
    {
        ans=ans*i;
    }
    return ans;
}
ll calc(ll a,ll mod)
{
    if(a>=mod) return 0;
    ll ans=1;
    for(ll i=a;i;--i)
    {
        ans=ans*i%mod;
        if(!ans) return 0;
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n,mod;
    cin>>n>>mod;
    if(n>=4){
        cout<<0<<endl;
    }
    else if(n==1||n==0)
    {
        cout<<1%mod<<endl;
    }
    else {
        ll ans=calc(n);
        ans=calc(ans);
        ans=calc(ans,mod);
        cout<<ans%mod<<endl;
    }
    return 0;

}
```


**D题茶颜悦色**

解决方案：线段树+扫描线不会，数据结构靠队友，没时间了只能后来再补了

**E飞行棋**

还没看题概率dp，先放这，有时间再补吧

**F题三元组**

解决方案：考虑$a_i+a_j&lt;=b_i+b_j​$ 时候，公式化成$2*a_i-b_i+2*a_j+b_j&lt;=0​$,

否则$a_i+a_j &gt;b_i+b_j$ 时候公式化为$2*b_i-a_i+2*b_j+a_j&lt;=0$,考虑到这两种情况不会同时出现，我们可以分类统计。

先按照第一种情况按$2*a_i-b_i$的值从到大排序，假如对于i，其符合条件的的最远的下标为p[i],那么对于i+1,符合条件的最远的下标在[i+1,p[i]]中，即p[i]不会增大，所以我们可以O(n)双指针来计算对于每个 i 符合条件的最远的下标为 p[i]。然后统计贡献值即可

第二种情况将$a_i$和$b_i$交换然后再按第一种情况统计贡献值即可

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
vector<P> comb;
map<int,int> mmp;
const ll mod=1e9+7;
struct Node{
ll a,b,c;
bool operator <(const Node & other)const {
    return (2*a-b)<(other.a*2-other.b);
}
};
Node tup[100005];
ll presum[100005];
ll getlr(ll l,ll r)
{
    if(r<l) return 0ll;
    return (presum[r]-presum[l-1])%mod;
}
ll solve(ll n)//1到n统计个数
{
    ll ans=0,p=0,r;
    ll last=tup[1].a*2-tup[1].b;
    for(ll i=1;i<=n;++i){
        ll now=tup[i].a*2-tup[i].b;
        if(last+now<=0)
            p++,r=i;
    }
    ans+=tup[1].c*getlr(1,p);
    ans%=mod;
    for(ll i=2;i<=n;++i)
    {
         last=tup[i].a*2-tup[i].b;
         while(p>=i&&(last+tup[p].a*2-tup[p].b>0)) p--;
         ans+=(tup[i].c*getlr(i,p))%mod;
         ans%=mod;
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll n;
    cin>>n;
    for(ll i=1;i<=n;++i){
        cin>>tup[i].a>>tup[i].b>>tup[i].c;
    }
    sort(tup+1,tup+n+1);
    for(ll i=1;i<=n;++i){
        presum[i]=presum[i-1]+tup[i].c;
    }
    ll ans=0;
    ans +=solve(n);
    for(ll i=1;i<=n;++i) swap(tup[i].a,tup[i].b);
    sort(tup+1,tup+n+1);
    for(ll i=1;i<=n;++i){
        presum[i]=presum[i-1]+tup[i].c;
    }
    ans+=solve(n);
    ans%=mod;
    cout<<ans<<endl;
    return 0;
}

```


**G篮球校赛**

解决方案：可以考虑将每类的前5名放在一起去重之后爆搜答案。也考虑考虑状压dp，$dp[i][s]$ 代表前i个人，位置的状态的s的最大价值，然后对于第i 个人的每个状态考虑自己上不上场即可。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll A[100005][35];
ll dp[100005][35];
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll n;
    cin>>n;
    for(ll i=1;i<=n;++i){
        for(ll j=0;j<5;++j) cin>>A[i][j];
    }
    ll top=1<<5;
    for(ll i=1;i<=n;++i)
    {
        for(ll s=0;s<top;++s){
            dp[i][s]=dp[i-1][s];
            for(ll j=0;j<5;++j){
                ll ns=1<<j;
                if(!(s&ns)) continue;
                dp[i][s]=max(dp[i][s],dp[i-1][s^ns]+A[i][j]);
            }
        }
    }
    cout<<dp[n][top-1]<<endl;
    return 0;

}

```


**H题分配学号**

解决方案：考虑统计出现的所有学号和出现的次数，然后用rem来表示前面待选的有多个少个，详情看代码。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
vector<P> comb;
map<ll,ll> mmp;
const ll mod=1e9+7;
ll calc(ll a,ll b)//计算阶乘A(a,b)
{
    ll ans=1;
    for(ll k=0;k<b;++k)
        ans=ans*(a-k)%mod;
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll n;
    cin>>n;
    for(ll i=0;i<n;++i){
        ll x;
        cin>>x;
        mmp[x]+=1;
    }
    ll lap=-1,lan=-1,rem=0,nwp,nwn;//lap为上一个元素的元号，lan表示上一个元素有多少个，rem表示前面未选位置的的个数
    for(P p:mmp)
    {
        nwp=p.first;
        nwn=p.second;
        if(lap!=-1){
            ll dx=nwp-lap;
            if(rem>dx)//前面未选的的个数大于与前面的学号和该学号间距，放不完，只能放dx个
            {
                comb.push_back({rem,dx});//存放A(rem,dx)
                rem-=dx;rem+=nwn;
            }
            else//前面未选的的个数小于与前面的学号和该学号间距，可以放rem个
            {
                 comb.push_back({rem,rem});
                 rem=nwn;
            }
            lap=nwp;
            lan=nwn;
        }
        else{
            rem=nwn;
            lap=nwp;
            lan=nwn;
        }
    }
    comb.push_back({rem,rem});

    ll ans=1;
    for(P &p:comb){
        ans=ans*calc(p.first,p.second)%mod;
    }
    cout<<ans<<endl;
    return 0;
}
```


**I题Gree的心房**

解决方案：水题

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll A[100005];
int main()
{
    ios::sync_with_stdio(false);
    ll n,m,k;
    ll ans=0;
    cin>>n>>m>>k;
    n--;m--;
    if(k>m*n) ans=-1;
    else ans=n+m;
    cout<<ans<<endl;
    return 0;

}
```


