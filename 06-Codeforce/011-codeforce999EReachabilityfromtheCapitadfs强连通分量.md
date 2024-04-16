

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


