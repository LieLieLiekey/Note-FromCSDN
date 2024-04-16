

## The Preliminary Contest for ICPC Asia Shenyang 2019赛后部分补题



这里把赛场上自己没写过的题写一下，写过不是自己写的写一下。

PS：E题一直以为是prufer序列计数，四天后重新做题发现题目不要求最后只有一个武器，蛤？这不就是bell数吗？D题树形dp赛场上没有时间写，最后没A…


#### B. Dudu’s maze


难度：中等题


自我感觉这道题题目读懂就好做了，第一次读以为每个怪物房间都有一次“传送门”的机会，然后咋想都想不出来，Google了一下，才明白传送门机会只有一次，那么也就是说只有一次机会碰见怪物并”接着捡糖“


**题意**：

​     给出一个n个节点和m个无向边的图，其中k个节点是“怪物节点”，剩下节点都是”糖果“节点，每个糖果节点里有一个糖果，并且拿到后就没有了。现在你知道这个图的构造，且起始位置为1号节点，且碰见怪物有一次使用”传送门“的机会，如果没有使用“传送门”就必须结束游戏。传送门会把送至怪物节点相邻的某一条遍的节点，每条边的概率是相等的。

    问聪明的自己使用最优策略，你可以获得的期望糖果是多少。

**思路**：

​     可以理解如果经过了一个”糖果“节点，那么可以与这个”糖果“节点相邻的”糖果“节点都可以经过，所以我们可以考虑缩点，使得每个点要么是怪兽节点，要么是连通的“糖果”节点。然后我们遍历与1号“糖果”节点所在的连通块邻接的”怪物“节点。

​     因为每个怪物节点使用一次传送门只能拿到送至的节点所在的"糖果"联通块的糖果，然后就必须结束游戏。所以每个“怪物”节点使用传送门获得的期望价值是 每条边另一个节点所在的”糖果“联通块的节点个数，选择每条边的概率=1/相邻的边的个数。我们就可以算出来每个怪物节点可以获得的期望价值。注意此时1号节点已径没有糖果了。

​     因为我们只能选择一个怪物节点，所以选择期望价值最高的那个+1号节点所在连通块的节点个数即可。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e5+100;
const int inf=0x3f3f3f3f;
vector<int> g[N];
/*
原图dfs缩点一下,建立新图,
*/
int color[N],cnt[N],top;
void dfs(int u,int sign)
{
    color[u]=sign;
    cnt[sign]++;
    for(int v:g[u]){
        if(color[v]) continue;
        dfs(v,sign);
    }
}
int link[N];
double lw[N];
vector<int> rg[N];
void work(int n,int m,int k)
{
    for(int i=1;i<=n;++i){
        if(!color[i]) dfs(i,++top);
    }
    //缩点染色，共top个点,/color[]<=k的都是怪兽
    double ans=cnt[color[1]];
    cnt[color[1]]=0;
    for(int i=1;i<=top;++i){
        rg[i].clear();
        link[i]=0;
    }
    for(int i=1;i<=n;++i){
        for(int v:g[i]){
            if(color[v]==color[i]) continue;
            rg[color[i]].push_back(color[v]);
        }
    }
    int u=color[1];
    for(int v:rg[u]){//取出所有与1连接的怪兽的点
        link[v]=true;
    }
    double maxx=0.0;
    for(int u=1;u<=top;++u){//枚举这些怪兽的点
        if(link[u]==true){
            double val=0;
            int totle=rg[u].size();
            for(int v:rg[u]){//连接v的出现个数
                //如果连接的怪兽，贡献自然为0
                val+=1.0/totle*cnt[v];
            }
            maxx=max(maxx,val);
        }
    }
    printf("%.7f\n",ans+maxx);
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m,k;
        scanf("%d%d%d",&n,&m,&k);
        for(int i=1;i<=n;++i){
            g[i].clear();
            color[i]=cnt[i]=0;
        }
        for(int i=1;i<=m;++i){
            int a,b;
            scanf("%d%d",&a,&b);
            g[a].push_back(b);
            g[b].push_back(a);
        }
        for(int i=1;i<=k;++i){
            int v;
            scanf("%d",&v);
            color[v]=i;
        }
        top=k;
        work(n,m,k);


    }
    return 0;
}
```


​

#### C. Dawn-K’s water


定位：简单题

**题意**：给你n个物品和最少需要买的重量m，并给出n个物品的价值和重量，问最少需要买m重量的的最小花费，如果最小花费下重量有多个，则输出最大的哪个。

**思路**：多重背包,$dp[i]$为刚好购买$i$重量的物品的最小花费。然后从$[m,10000]$遍历取最小值的a和对应的最大b即可。


赛后补题wa了几发，以为重量和买的价值是单调递增的关系。后来才记起来$dp[i]$是恰好买$i$重量物品所花费的最小金币，并没有单调性！！


**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e4+100;
const int inf=0x3f3f3f3f;
ll dp[N],p[1005],c[1005];
ll n,m;
void work()
{
    dp[0]=0;
    ll top=10000;
    for(ll i=1;i<=top;++i) dp[i]=1ll<<62;
    for(ll i=1;i<=n;++i)
        for(ll j=c[i];j<=top;++j){
                dp[j]=min(dp[j],dp[j-c[i]]+p[i]);
    }
    ll a=1ll<<62,b=0;
    for(int i=m;i<=top;++i){
        if(dp[i]<=a) a=dp[i],b=i;
    }
    printf("%lld %lld\n",a,b);
}
int main()
{
    while(~scanf("%lld%lld",&n,&m))
    {
        for(ll i=1;i<=n;++i)
            scanf("%lld%lld",p+i,c+i);
        work();
    }
    return 0;
}
```


#### D. Fish eating fruit(树形dp+换根)


定位：中上难度

**题意**： 给一个有n个点的树，求所有两点之间的路径权值和，且路径权值和分三类：模3为0，模3为1，模3为2的路径。对于每种路径，输出其种类路径的和。

这道题写了篇博客，因为思路描述比较赘余就不在这里指出了:[博客链接](https://blog.csdn.net/Dch19990825/article/details/100848798)

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const ll N=1e4+20;
const ll mod=1e9+7;
vector<pair<ll,ll> > g[N];
ll dp[N][3];
ll res[N][3];
ll m[3];
ll tol[N][3],rtol[N][3];
ll ccc(ll a)
{
    return (a%mod+mod)%mod;
}
void dfs1(ll u,ll fa)
{
    for(ll i=0; i<3; ++i)
    {
        tol[u][i]=rtol[u][i]=dp[u][i]=res[u][i]=0;
    }
    tol[u][0]=1;
    for(P e:g[u])
    {
        ll v=e.first,w=e.second;
        if(v==fa) continue;
        dfs1(v,u);
        for(ll i=0; i<3; ++i)
        {
            dp[u][(i+w)%3]=ccc(dp[u][(i+w)%3]+dp[v][i]+w*tol[v][i]);
            tol[u][(i+w)%3]+=tol[v][i];
        }
    }
}
void dfs2(ll u,ll fa,ll c)
{
    if(fa!=u) //
    {
        for(ll i=0; i<3; ++i)
        {
            ll p=((i-c)%3+3)%3;
            m[(i+c)%3]=ccc(res[fa][i]-dp[u][p]-c*tol[u][p]+c*(rtol[fa][i]-tol[u][p]));
            rtol[u][(i+c)%3]=tol[u][(i+c)%3]+rtol[fa][i]-tol[u][p];
            res[u][(i+c)%3]=ccc(dp[u][(i+c)%3]+m[(i+c)%3]);
        }
    }
    for(P e:g[u])
    {
        ll v=e.first,w=e.second;
        if(v==fa) continue;
        dfs2(v,u,w);
    }
}
ll sum[3];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n;
    while(cin>>n)
    {
        for(ll i=0; i<n; ++i) g[i].clear();
        for(ll i=0; i<n-1; ++i)
        {
            ll a,b,c;
            cin>>a>>b>>c;
            g[a].push_back({b,c});
            g[b].push_back({a,c});
        }
        dfs1(0,0);
        for(ll i=0; i<3; ++i) res[0][i]=dp[0][i],rtol[0][i]=tol[0][i];
        dfs2(0,0,0);
        sum[0]=sum[1]=sum[2]=0;
        for(ll i=0; i<n; ++i)
        {
            for(ll k=0; k<3; ++k)
                sum[k]=(sum[k]+res[i][k])%mod;
        }
        cout<<sum[0]<<" "<<sum[1]<<" "<<sum[2]<<endl;
    }
    return 0;
}

```


#### E. Gugugu’s upgrade schemes


定位：性质题


这道题是赛后补题的


**题意**：n个元素的集合划分方法是有多少个，模p输出。

**思路**：bell数+Touchard同余。

Touchard同余就是若p为质数，且$B_n$是第n个贝尔数，那么$B_{p+n}=B_n+B_{n+1} (mod ~~p)$

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e3+10;
const int inf=0x3f3f3f3f;
ll C[N][N],f[1000005],p;
void init(int n)//求0~n的贝尔数
{
    C[0][0]=1;
    for(int i=1;i<=n;++i){
        C[i][0]=C[i][i]=1;
        for(int j=1;j<i;++j) C[i][j]=(C[i-1][j]+C[i-1][j-1])%p;
    }
    f[0]=1;
    for(int i=1;i<=n;++i){
        f[i]=0;
        for(int j=0;j<i;++j)
            f[i]=(f[i]+C[i-1][j]*f[i-1-j])%p;
    }
}
ll dfs(ll n)
{
    if(f[n]!=-1) return f[n];
    ll ans=(dfs(n-p)+dfs(n-p+1))%p;
    return f[n]=ans;
}
int main()
{
    ll T,n;
    cin>>T;
    while(T--)
    {
        cin>>n>>p;
        for(ll i=1;i<=n;++i) f[i]=-1;
        init(p);
        cout<<dfs(n)<<endl;
    }
    return 0;
}

```


#### F. Honk’s pool


定位：中下难度


这题赛场上自己A过


**题意** ：给出一个长度为n的序列，每天可以将序列中最小的一个数+1，最大的一个数-1，问k天之后序列中最大与最小值的差是多少？

**思路**：模拟一下，看k天后最小值最大能到多少，最大值最小能到多少，如果交叉了就判断和是否能被4整除，可以则输出0，否则输出1。没有交叉则输出上面两个值的差

**代码**：

```cpp
include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=5e5+20;
ll w[N];
ll n,K;
ll getlv()
{
    ll k=K,c=1;
    for(ll i=1; i<n; ++i) //第 i 个的个数
    {
        ll d=w[i+1]-w[i];
        if(d*c<=k)
        {
            k-=d*c;
            c+=1;
        }
        else
        {
            ll m=k/c;
            return w[i]+m;
        }
    }
    return w[n];
}
ll getrv()
{
    ll k=K,c=1;
    for(ll i=n; i>1; --i) //第 i 个的个数
    {
        ll d=w[i]-w[i-1];
        if(d*c<=k)
        {
            k-=d*c;
            c+=1;
        }
        else
        {
            ll m=k/c;
            return w[i]-m;
        }
    }
    return w[1];
}
int main()
{

    while(~scanf("%lld%lld",&n,&K))
    {
        ll sum=0;
        for(ll i=1; i<=n; ++i)
        {
            scanf("%lld",w+i);
            sum+=w[i];
        }
        sort(w+1,w+1+n);
        ll a=getlv(),b=getrv();
        if(a<b)
        {
            printf("%lld\n",b-a);
        }
        else
        {
            if(sum%n==0)
            {
                printf("0\n");
            }
            else
            {
                printf("1\n");
            }
        }

    }
    return 0;
}
```


#### H. Texas hold’em Poker


定位：难

**题意**：

**思路**：

K. Guanguan’s Happy water


这道题正解是高斯消元+矩阵快速幂，线性BM给过了，不知道数据有多水


放个**非正解的线性BM**递推，正解有机会在写吧。

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef vector<long long> VI;
typedef long long ll;
const ll mod=1e9+7;
ll powmod(ll a,ll b)
{
    ll res=1;
    a%=mod;
    assert(b>=0);
    for(; b; b>>=1)
    {
        if(b&1)res=res*a%mod;
        a=a*a%mod;
    }
    return res;
}
namespace linear_seq
{
#define rep(i,a,n) for (long long i=a;i<n;i++)
#define pb push_back
#define SZ(x) ((long long)(x).size())
const long long N=10010;
ll res[N],base[N],_c[N],_md[N];

vector<long long> Md;
void mul(ll *a,ll *b,long long k)
{
    rep(i,0,k+k) _c[i]=0;
    rep(i,0,k) if (a[i]) rep(j,0,k)
        _c[i+j]=(_c[i+j]+a[i]*b[j])%mod;
    for (long long i=k+k-1; i>=k; i--) if (_c[i])
            rep(j,0,SZ(Md)) _c[i-k+Md[j]]=(_c[i-k+Md[j]]-_c[i]*_md[Md[j]])%mod;
    rep(i,0,k) a[i]=_c[i];
}
long long solve(ll n,VI a,VI b)
{
    // a 系数 b 初值 b[n+1]=a[0]*b[n]+...
    //        printf("%d\n",SZ(b));
    ll ans=0,pnt=0;
    long long k=SZ(a);
    assert(SZ(a)==SZ(b));
    rep(i,0,k) _md[k-1-i]=-a[i];
    _md[k]=1;
    Md.clear();
    rep(i,0,k) if (_md[i]!=0) Md.push_back(i);
    rep(i,0,k) res[i]=base[i]=0;
    res[0]=1;
    while ((1ll<<pnt)<=n) pnt++;
    for (long long p=pnt; p>=0; p--)
    {
        mul(res,res,k);
        if ((n>>p)&1)
        {
            for (long long i=k-1; i>=0; i--) res[i+1]=res[i];
            res[0]=0;
            rep(j,0,SZ(Md)) res[Md[j]]=(res[Md[j]]-res[k]*_md[Md[j]])%mod;
        }
    }
    rep(i,0,k) ans=(ans+res[i]*b[i])%mod;
    if (ans<0) ans+=mod;
    return ans;
}
VI BM(VI s)
{
    VI C(1,1),B(1,1);
    long long L=0,m=1,b=1;
    rep(n,0,SZ(s))
    {
        ll d=0;
        rep(i,0,L+1) d=(d+(ll)C[i]*s[n-i])%mod;
        if (d==0) ++m;
        else if (2*L<=n)
        {
            VI T=C;
            ll c=mod-d*powmod(b,mod-2)%mod;
            while (SZ(C)<SZ(B)+m) C.pb(0);
            rep(i,0,SZ(B)) C[i+m]=(C[i+m]+c*B[i])%mod;
            L=n+1-L;
            B=T;
            b=d;
            m=1;
        }
        else
        {
            ll c=mod-d*powmod(b,mod-2)%mod;
            while (SZ(C)<SZ(B)+m) C.pb(0);
            rep(i,0,SZ(B)) C[i+m]=(C[i+m]+c*B[i])%mod;
            ++m;
        }
    }
    return C;
}
long long gao(VI a,ll n)
{
    VI c=BM(a);
    c.erase(c.begin());
    rep(i,0,SZ(c)) c[i]=(mod-c[i])%mod;
    return solve(n,c,VI(a.begin(),a.begin()+SZ(c)));
}
};
long long k,n,f[220],sum[220];
vector<long long>  v;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        for(int i=1;i<=2*k;++i) cin>>f[i];
        if(k==1){
            cout<<(f[1]*(n%mod))%mod<<endl;
            continue;
        }
        sum[0]=0;
        for(int i=1;i<=2*k;++i) sum[i]=(sum[i-1]+f[i])%mod;
        v.clear();
        for(int i=1;i<=2*k;++i) v.push_back(sum[i]);
        cout<<linear_seq::gao(v,n-1)<<endl;
    }
    return 0;
}
```


