

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


