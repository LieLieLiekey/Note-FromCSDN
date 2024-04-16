

### HDU - 1561树形依赖背包


**题目：** [传送门](http://acm.hdu.edu.cn/showproblem.php?pid=1561)

思路见代码注释. **代码：**

```cpp
/*
对于每个节点u,要么有唯一的父亲fa,要么没有父亲,自形一颗树
所以按照题目给的要求该图是一个森林.
我们考虑将森林中的每一颗树的根连接到超级根root.那么形成的图是一个以超级根
为根的树,题目也转化为从该树上取m+1个节点,使得价值最大,取u节点必须先取父亲节点.
这就是树形依赖背包的问题了
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e4+10;
const int mod=1e9+7;
int w[305];
vector<int> g[305];
int dp[305][305];
int n,m;
void dfs(int u)
{
    for(int v:g[u])
    {
        dfs(v);
        /*因为要求该儿子中要么只取一个，要么不取, 所以我们必须先枚举背包容量从大到小,其次枚举儿子的容量大小*/
        for(int s=m;s>=1;--s)//枚举背包容量从大到小
        {
            for(int a=1;a<=s;++a){//其次枚举儿子容量
                dp[u][s]=max(dp[u][s],dp[u][s-a]+dp[v][a]);
            }
        }
    }
    dp[u][0]=0;
    for(int i=m;i>=1;--i)
        dp[u][i]=dp[u][i-1]+w[u];

}
int solve()
{
    dfs(0);
    return dp[0][m];
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    while(cin>>n>>m,n)
    {
        for(int i=0;i<=n;++i) g[i].clear();
        for(int i=1;i<=n;++i){
            int fa,ww;
            cin>>fa>>ww;
            w[i]=ww;
            g[fa].push_back(i);
        }
        ++m;//0这个节点额外的且是必须取的,所以m要+1
        mset(dp,0);
        cout<<solve()<<endl;
    }
    return 0;
}
```




### K - Strategic game POJ - 1463（简单树形DP）


##### 题目:[传送门]()


思路见注释

##### 代码 :


```cpp
/*
树的最小顶点覆盖
dp[u][0]代表当前以u为根的子树,u不选所需的最小花费
dp[u][1]代表当前以u为根的子树,u选的最小所需花费
dp[u][1]=1+sum(min(dp[son][0],dp[son][1]))
dp[u][0]=sum(dp[son][1])
*/
#include<stdio.h>
#include<iostream>
#include<vector>
#include<string.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=2e3+10;
int dp[N][2];
vector<int> g[N];
void dfs(int u,int fa)
{
    dp[u][1]=1;
    dp[u][0]=0;
    for(int i=0;i<g[u].size();++i){
        int v=g[u][i];
        if(v==fa) continue;
        dfs(v,u);
        dp[u][1]+=min(dp[v][0],dp[v][1]);
        dp[u][0]+=dp[v][1];
    }
}
int solve(int n)
{
    dfs(0,0);
    return min(dp[0][0],dp[0][1]);
}
int main()
{
//    ios::sync_with_stdio(false);cin.tie(0);
    int n;
    while(~scanf("%d",&n))
    {
        for(int i=0;i<n;++i) g[i].clear();
        for(int i=0;i<n;++i){
            int u,k,v;
            scanf("%d:(%d)",&u,&k);
            for(int j=0;j<k;++j){
                scanf("%d",&v);
                g[u].push_back(v);
                g[v].push_back(u);
            }
        }
        cout<<solve(n)<<endl;
    }
}
```




### J - Anniversary party POJ - 2342(简单树形DP）


##### 题目:[传送门]()


思路见注释

##### 代码 :


```cpp
/*
简单树形dp.
考虑dp[node][0/1],代表以node在选与不选的情况下,以u为根的子树的最大价值
dp[node][0]=sum(max(dp[v][0],dp[v][1]))
dp[node][1]=sum(dp[v][0])
*/
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=1e4+10;
const int inf=0x3f3f3f3f;
int in[N],w[N],dp[N][2];
vector<int> g[N];
int ans;
void dfs(int u)
{
    int sum0=0,sum1=0;
    for(int i=0;i<g[u].size();++i){
        int v=g[u][i];
        dfs(v);
        sum0+=max(dp[v][1],dp[v][0]);
        sum1+=dp[v][0];
    }
    dp[u][0]=sum0;
    dp[u][1]=sum1+=w[u];
}
int solve(int n)
{
    int root=0;
    for(int i=1;i<=n;++i) if(in[i]==0){root=i;break;}
    ans=-inf;
    dfs(root);
    return max(dp[root][0],dp[root][1]);
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    while(cin>>n,n)
    {
        for(int i=1; i<=n; ++i)
        {
            cin>>w[i];
            dp[i][1]=dp[i][0]=-inf;
            in[i]=0;
        }
        for(int i=1; i<n; ++i)
        {
            int fa,v;
            cin>>v>>fa;
            g[fa].push_back(v);
            in[v]++;
        }
        cout<<solve(n)<<endl;
    }
    return  0;
}
```




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




### L - Computer(HDU2196 ，树形DP，换根法)


##### 题目 :[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=2196)


思路见注释

##### 代码 :


```cpp
*
换根法dp:
先把无根树化为有根树
第一遍dfs,对于顶点u,求u的子树到u的最大和次大距离
第二遍dfs,将树化为顶点u为根,求u的子树到u的最大距离和次大距离
    对于u的最大距离就是u的答案res[u],而u的次大距离是用来儿子换根的时候进行状态转移
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const ll N=1e4+10;
const ll mod=1e9+7;
vector<P> g[N];
int dp[N][2];//u的最大值与次大值
int pos[N][2];//u的最大值与次大值的位置
int res[N];
void dfs1(int u,int fa)
{
    for(P &p:g[u])
    {
        int v=p.first,w=p.second;
        if(v==fa) continue;
        dfs1(v,u);
        if(dp[v][0]+w>dp[u][0]){
            dp[u][1]=dp[u][0];
            pos[u][1]=pos[u][0];
            dp[u][0]=dp[v][0]+w;
            pos[u][0]=v;
        }
        else if(dp[v][0]+w>dp[u][1]){
            dp[u][1]=dp[v][0]+w;
            pos[u][1]=v;
        }
    }
//    printf("u:%d,dp[0]:%d,pos[0]:%d,dp[1]:%d,pos[1]:%d\n",u,dp[u][0],pos[u][0],dp[u][1],pos[u][1]);
}
void dfs2(int u,int fa,int w)
{
    int other=0;
    if(fa!=u)//再次换根为u，更新最大和次大
    {
         if(pos[fa][0]!=u)//other代表从父亲到该根的最大与次大
            other=dp[fa][0]+w;
         else
            other=dp[fa][1]+w;
         if(other>dp[u][0]){
            pos[u][1]=pos[u][0];
            dp[u][1]=dp[u][0];
            pos[u][0]=fa;
            dp[u][0]=other;
         }
         else if(other>dp[u][1])
         {
             pos[u][1]=fa;
             dp[u][1]=other;
         }
    }
    res[u]=dp[u][0];
    for(P &p:g[u])
    {
        int v=p.first;
        if(v==fa) continue;
        dfs2(v,u,p.second);
    }
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int n;
    while(cin>>n)
    {
        for(int i=1;i<=n;++i) g[i].clear();
        for(int i=2;i<=n;++i){
            int w,v;
            cin>>v>>w;
            g[i].push_back({v,w});
            g[v].push_back({i,w});
        }
        mset(dp,0);
        mset(pos,0);mset(res,0);
        dfs1(1,1);
        dfs2(1,1,0);
        for(int i=1;i<=n;++i){
            cout<<res[i]<<endl;
        }
    }
}
```


