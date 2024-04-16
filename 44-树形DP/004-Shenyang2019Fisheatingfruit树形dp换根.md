

### Shenyang 2019 Fish eating fruit (树形dp+换根)


#### 题目链接：[传送门](https://nanti.jisuanke.com/t/41403)


### 题意：


​ 给一个有n个点的树，求所有两点之间的路径权值和，且路径权值和分三类：模3为0，模3为1，模3为2的路径。对于每种路径，输出其种类路径的和。

### 思路 ：


​ 不难想到树形dp+换根可以解决这个问题。

​ 我们首先把节点 0 定为根进行第一遍dfs，对于u节点，记录当前以u为根**子树上的节点到根节点u的路径和模3为 i 的节点个数和该种类的所有路径和**，我们有以下dp方程，假设u的儿子为v，边权为w，那么

初始化：$tol[u][0]=1,tol[u][1]=tol[u][2]=0,dp[u][0]=dp[u][1]=dp[u][2]=0​$

转移方程：$tol[u][(i+w)\%3]+=tol[v][i]，dp[u][(i+w)\%3]=dp[v][i]+w*tol[v][i]$

​ 此时所有节点到节点0的三种路径的和已经计算出来。接下里我们换根来求节点u为根的三种路径和的节点个数并把答案存到$res[u][i]​$和$rtol[u][i]​$上。假设u的父亲是fa，边权为c，此时$res[fa][i]​$和$rtol[fa][i]​$已经求出，那么我们对fa先删除u子树对他的贡献，然后再合并到u上从而求出$res[u][i]​$和$rtol[u][i]​$。以下是改转移的核心代码：

```cpp
//求出res[u][i]和rtol[u][i]
for(ll i=0; i<3; ++i)//枚举fa的每个i，删除其中u对他的贡献
{
    ll p=((i-c)%3+3)%3;//u的p贡献到fa的i
    m[(i+c)%3]=res[fa][i]-dp[u][p]-c*tol[u][p]+c*(rtol[fa][i]-tol[u][p]);
    rtol[u][(i+c)%3]=tol[u][(i+c)%3]+rtol[fa][i]-tol[u][p];
    res[u][(i+c)%3]=dp[u][(i+c)%3]+m[(i+c)%3];
}
```



需要注意的地方太多了，写这种东西一定要搞清楚状态转移！


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


