

## codeforce.999E Reachability from the Capita(dfs+强连通分量)


##### 比赛链接：[传送门](https://codeforces.com/problemset/problem/999/E)


##### 题意：


​ 给出一个有向图，n个顶点，m条边，现在给出一个源点S，问最少添加多少条有向边才能使顶点S可以到达其他所有顶点。

##### 思路：


​ 我们dfs出刚开始dfs可以到达的所有顶点，然后对于剩下的顶点，我们将剩下顶点构建成的图强连通分量缩点( 对有环的情况处理)，然后形成一个拓扑图，我们只有计算处缩点后度数为0的点的个数即可（让S连接度数为0的点即可）

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=1e5+10;
vector<int> g[N];
vector<int> tg[N];
int book[N];
void dfs(int u)
{
    book[u]=true;
    for(int v:g[u]){
        if(!book[v]) dfs(v);
    }
}
int dfn[N],S[N],top,low[N],ins[N],tol;
int color[N],cgt;
void tarjin(int u)
{
    dfn[u]=low[u]=++tol;
    S[top++]=u;
    ins[u]=1;
    for(int i=0;i<g[u].size();++i)
    {
        int v=g[u][i];
        if(book[v]) continue;
        if(!dfn[v])
        {
            tarjin(v);
            low[u]=min(low[u],low[v]);
        }
        else if(ins[v]){
            low[u]=min(low[u],dfn[v]);
        }
    }
    if(low[u]==dfn[u])
    {
        int v;
        ++cgt;
        do{
            v=S[top-1];
            top--;
            ins[v]=0;
            color[v]=cgt;
        }
        while(v!=u);
    }
}
void getall(int n)
{
    fill(dfn,dfn+1+n,0);
    fill(ins,ins+1+n,0);
    tol=cgt=top=0;
    for(int i=1;i<=n;++i){
        if(book[i]) continue;
        if(!dfn[i]) tarjin(i);
    }
}
int ind[N];
int main()
{
    int n,m,s;
    scanf("%d%d%d",&n,&m,&s);
    for(int i=1;i<=m;++i)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        g[a].push_back(b);
    }
    dfs(s);
    getall(n);
    fill(ind,ind+cgt+1,0);
    for(int u=1;u<=n;++u){
        for(int v:g[u]){
            if(book[u]||book[v]) continue;
            int a=color[u],b=color[v];
            if(a!=b)
                ind[b]++;
        }
    }
    int ans=0;
    for(int i=1;i<=cgt;++i)
        if(ind[i]==0) ans++;
    printf("%d\n",ans);
    return 0;
}

```




### I - Caocao’s Bridges HDU - 4738(求边双连通）


##### 题目:[传送门]()


思路见注释

##### 代码 :


```cpp
/*
if 图不连通：ans=0
eles if 无桥：ans=-1
else ans=权值最小的桥==0?1:ans
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=5e4+10;
const int inf=0x3f3f3f3f;
vector<P> cute;
vector<P> g[N];
int low[N],dfn[N],tol,ans;
void tarjan(int u,int fa)
{
    low[u]=dfn[u]=++tol;
    bool infa=false;
    for(P &e:g[u])
    {
        int v=e.first,w=e.second;
        if(v==fa&&infa==false)
        {
            infa=true;
            continue;
        }
        if(!dfn[v])
        {
            tarjan(v,u);
            low[u]=min(low[u],low[v]);
            if(low[v]>low[u]) {
                cute.push_back({u,v});
                ans=min(ans,w);
            }
        }
        else low[u]=min(low[u],dfn[v]);
    }
}
int solve(int n)
{
    tol=0,ans=inf;
    mset(dfn,0);
    int connet_tot=0;
    for(int i=1; i<=n; ++i)
    {
        if(!dfn[i])
        {
            connet_tot++;
            if(connet_tot>1) return 0;
            tarjan(i,i);
        }
    }
    if(ans==inf) return -1;
    return ans==0?1:ans;

}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,m;
    while(cin>>n>>m,n)
    {
        for(int i=1; i<=n; ++i) g[i].clear();
        for(int i=1; i<=m; ++i)
        {
            int u,v,w;
            cin>>u>>v>>w;
            g[u].push_back({v,w});
            g[v].push_back({u,w});
        }
        cout<<solve(n)<<endl;
    }
    return 0;
}
```




### H - Prince and Princess HDU - 4685（强连通分量缩点+二分图匹配+奇怪建图）


##### 题目:[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=4685)


思路见注释

##### 代码 :


```cpp
/*
做法：
1.建图最大匹配
2.增加点,给不能匹配的匹配上
3.再次二分图匹配
4.对于u,匹配的match[u],那么match[u]连接所有对应u喜欢的顶点
5.强连通分量缩点.
6.对于u ,对于喜欢的公主v，如果v和match[u]颜色相同,则对之匹配不影响最终解。
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=1000+100;
vector<int> g[N];
vector<int> ans[N];
int low[N],dfn[N],tol,ins[N],top,S[N],cgt,color[N];
int rdu[N],cdu[N],num[N];
int matchx[N],matchy[N];
bool love[N][N];
bool used[N];//只会标记左边x,是否dfs过
bool dfs(int u,int m)
{
    used[u]=true;
    for(int v=1;v<=m;++v){
        if(!love[u][v]) continue;
        int w=matchy[v];
        if(w<0||(!used[w]&&dfs(w,m))){
            matchx[u]=v;
            matchy[v]=u;
            return true;
        }
    }
    return false;
}
int bipartite_match(int n,int m)
{
    int res=0;
    mset(matchx,-1);mset(matchy,-1);
    for(int i=1;i<=n;++i){
        if(matchx[i]<0){
            mset(used,0);
            if(dfs(i,m)) res++;
        }
    }
    return res;
}
void tarjan(int u,int fa)
{
    low[u]=dfn[u]=++tol;
    ins[u]=1;
    S[top++]=u;
    for(int i=0; i<g[u].size(); ++i)
    {
        int v=g[u][i];
        if(!dfn[v])
        {
            tarjan(v,u);
            low[u]=min(low[u],low[v]);
        }
        else if(ins[v]) low[u]=min(low[u],dfn[v]);
    }
    if(low[u]==dfn[u])
    {
        ++cgt;
        int v;
        do
        {
            v=S[--top];
            ins[v]=0;
            color[v]=cgt;
            num[cgt]++;
        }
        while(v!=u);
    }
}
void solve(int n)
{
    mset(dfn,0);mset(color,0);
    tol=top=cgt=0;
    for(int i=1;i<=n;++i) if(!dfn[i]) tarjan(i,i);
}
int main()
{
    int t,n,m,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        mset(love,0);
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;++i){
            int k,v;
            scanf("%d",&k);
            while(k--)
            {
                scanf("%d",&v);
                love[i][v]=true;
            }
        }
        int tot=bipartite_match(n,m);
//        for(int i=1;i<=n;++i) printf("match: %d - %d\n",i,matchx[i]);
//        cout<<"tot:"<<tot<<endl;
        int top=n+m-tot;
        for(int i=n+1;i<=top;++i){
            for(int j=1;j<=top;++j) love[i][j]=true;
        }
        for(int i=1;i<=top;++i){
            for(int j=m+1;j<=top;++j) love[i][j]=true;
        }
        tot=bipartite_match(top,top);
//         cout<<"tot:"<<tot<<endl;
//        for(int i=1;i<=top;++i) printf("match: %d - %d\n",i,matchx[i]);
        for(int i=1;i<=top;++i) g[i].clear();
        for(int i=1;i<=top;++i){
            int u=matchx[i];
            for(int j=1;j<=top;++j){
                if(love[i][j]&&u!=j)
                {
//                    cout<<"edge:"<<u<<" "<<j<<endl;
                     g[u].push_back(j);
                }
            }
        }
        solve(top);
        for(int i=1;i<=n;++i){
            ans[i].clear();
            for(int j=1;j<=m;++j){
                if(love[i][j]&&color[matchx[i]]==color[j]) ans[i].push_back(j);
            }
        }
        printf("Case #%d:\n",++cas);
        for(int i=1;i<=n;++i){
            printf("%u",ans[i].size());
//            cout<<ans[i].size();
            for(int v:ans[i])
                printf(" %d",v);
//                cout<<" "<<v;
            puts("");
        }
    }
    return 0;
}
```




### G - Strongly connected HDU - 4635（强连通缩点）


##### 题目:[传送门]()


思路见注释

##### 代码 :


```cpp
/*
思路:我们考虑将所有强连通分量缩点后形成的DAG图G进行讨论.
假设缩点后的顶点个数为cgt个.我们让G变为完全图G’,那么形成的完全图G'的边的总数为cgt*(cgt-1),
实际上如果我们考虑缩点前每一个强连通分量也形成完全子图,那么边的总数为n*(n-1).总共增加的边就是n*(n-1)-m
那么原问题就可以转化为:在形成的完全图G'中,我们删掉最少的增加的边,使得剩下的图不连通.那么剩下的增加的边数就是答案.
1.对于缩点后的图G中顶点入度和出度都不为0的顶点u,因为在形成的G'完全图中除了u,其他剩下的顶点都是连通的,所以我们不能
  通过删掉u上增加的边,使得图不连通。
2.对于图G'中入度为0的点u,我们可以删除除u外的顶点到顶点u的边,这样u和剩下的顶点就是两个强连通分量.
3.对于图G'中出度为0的点u,我们可以删除顶点u到除u外的顶点的边,这样u和剩下的顶点就是两个强连通分量.

归纳一下:将连通图分量缩点,统计每个缩点后的点包含的点的个数.对于入度为0或出度为0的点u,我们更新答案ans=max(ans,n*(n-1)-m-(n-num[u])*num[u])
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=1e5+100;
vector<int> g[N];
int low[N],dfn[N],tol,ins[N],top,S[N],cgt,color[N];
int rdu[N],cdu[N],num[N];
void tarjan(int u,int fa)
{
    low[u]=dfn[u]=++tol;
    ins[u]=1;
    S[top++]=u;
    for(int i=0; i<g[u].size(); ++i)
    {
        int v=g[u][i];
        if(!dfn[v])
        {
            tarjan(v,u);
            low[u]=min(low[u],low[v]);
        }
        else if(ins[v]) low[u]=min(low[u],dfn[v]);
    }
    if(low[u]==dfn[u])
    {
        ++cgt;
        int v;
        do
        {
            v=S[--top];
            ins[v]=0;
            color[v]=cgt;
            num[cgt]++;
        }
        while(v!=u);
    }
}
ll solve(int n,int m)
{
    tol=top=cgt=0;
    for(int i=1;i<=n;++i)
        dfn[i]=color[i]=num[i]=0;
    for(int i=1;i<=n;++i) if(!dfn[i]) tarjan(i,i);
    for(int i=1;i<=cgt;++i) rdu[i]=cdu[i]=0;
    if(cgt==1) return -1ll;
    for(int u=1;u<=n;++u){
        for(int v:g[u]){
            if(color[u]!=color[v]){
//                cout<<"u:"<<u<<" v:"<<v<<endl;
//                cout<<" color:"<<color[u]<<" "<<color[v]<<endl;
                cdu[color[u]]++;
                rdu[color[v]]++;
            }
        }
    }
    ll ans=0;
    ll sum=(ll)n*(n-1ll)-m;
    for(int i=1;i<=cgt;++i){
        if(rdu[i]==0||cdu[i]==0){
            ans=max(ans,sum-((ll)n-num[i])*num[i]);
//            cout<<"color:"<<i<<" "<<num[i]<<endl;
        }
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t,cas=0;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        for(int i=1;i<=n;++i) g[i].clear();
        for(int i=1;i<=m;++i){
            int u,v;
            cin>>u>>v;
            g[u].push_back(v);
        }
        cout<<"Case "<<++cas<<": "<<solve(n,m)<<endl;
    }
}
```




## POJ 2942(点双连通分量+无向图判奇环)


##### 题目链接：[传送门](http://poj.org/problem?id=2942)


##### 题意：



来自kuangbin模板


POJ 2942 Knights of the Round Table

亚瑟王要在圆桌上召开骑士会议，为了不引发骑士之间的冲突， 并且能够让会议的议题有令人满意的结果，每次开会前都必须对出席会议的骑士有如下要求： 1、 相互憎恨的两个骑士不能坐在直接相邻的2个位置； 2、 出席会议的骑士数必须是奇数，这是为了让投票表决议题时都能有结果。

注意：1、所给出的憎恨关系一定是双向的，不存在单向憎恨关系。 2、由于是圆桌会议，则每个出席的骑士身边必定刚好有2个骑士。 即每个骑士的座位两边都必定各有一个骑士。 3、一个骑士无法开会，就是说至少有3个骑士才可能开会。

##### 思路：


首先根据给出的互相憎恨的图中得到补图。 然后就相当于找出不能形成奇圈的点。 利用下面两个定理：

（1）如果一个点双连通分量内的某些顶点在一个奇圈中（即点双连通分量含有奇圈）， 那么这个点双连通分量的其他顶点也在某个奇圈中；

（2）如果一个点双连通分量含有奇圈，则他必定不是一个二分图。反过来也成立，这是一个充要条件。

所以本题的做法，就是对补图求点双连通分量。 然后对于求得的点双连通分量，使用染色法判断是不是二分图，不是二分图，这个双连通分量的点是可以存在的


bing神nb


##### 代码：


```cpp
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int N=1e3+10;
bool hate[N][N];
vector<int> g[N];
int dfn[N],tol,low[N],S[N],top,belong[N],block;
bool ins[N];
bool have[N],canjoin[N];//have[i]表示i点是否在当前点双连通分量中
int temp[N];//temp用来储存当前点双联通分量的点,用于记录可以参加会议的骑士
int color[N];
bool dfs(int u,int sg)//二分图交叉染色法
{
   
    if(color[u]==sg) return true;
    if(color[u]```


