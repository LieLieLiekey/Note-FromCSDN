## Factory HDU - 6115（LCA倍增，求树上简单路径的距离）


####  题目:[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=6115)

这题其实暴力LCA即可


#### 代码 :

```cpp
/*
暴力枚举两公司的所有顶点即可。
    求树上的两点到lca的距离
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
const int DEG=20;
vector<P> g[N];
int fa[N][DEG+1],deg[N];
int dis[N][DEG+1];
void bfs(int root)
{
    queue<int> Q;
    Q.push(root);
    fa[root][0]=root;
    dis[root][0]=0;
    deg[root]=0;
    while(!Q.empty())
    {
        int u=Q.front();
        Q.pop();
        for(int i=1; i<=DEG; ++i) {
            fa[u][i]=fa[fa[u][i-1]][i-1];
            dis[u][i]=dis[u][i-1]+dis[fa[u][i-1]][i-1];
        }
        for(P& e:g[u])
        {
            int v=e.first,w=e.second;
            if(v==fa[u][0]) continue;
            deg[v]=deg[u]+1;
            fa[v][0]=u;
            dis[v][0]=w;
            Q.push(v);
        }
    }
}
int LCAds(int u,int v)
{
    int ans=0;
    if(deg[u]>deg[v]) swap(u,v);
    int tu=u,tv=v;
    for(int det=deg[tv]-deg[tu],i=0; det; ++i)
    {
        if(det&(1<<i))
        {
            ans+=dis[tv][i];
            det-=(1<<i);
            tv=fa[tv][i];
        }
    }
    if(tu==tv) return ans;
    for(int i=DEG; ~i; --i)
    {
        if(fa[tu][i]!=fa[tv][i])
        {
            ans+=dis[tv][i];
            ans+=dis[tu][i];
            tu=fa[tu][i];
            tv=fa[tv][i];
        }
    }
    ans+=dis[tu][0];
    ans+=dis[tv][0];
    return ans;
}
vector<int> work[N];
int n,m;
int getCompanydis(int a,int b)
{
    int ans=inf;
    for(int i:work[a])
    {
        for(int j:work[b])
        {
            ans=min(ans,LCAds(i,j));
        }
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int T;
    cin>>T;
    while(T--)
    {
        cin>>n>>m;
        for(int i=1;i<=n;++i) g[i].clear();
        for(int i=1;i<n;++i)
        {
            int u,v,w;
            cin>>u>>v>>w;
            g[u].push_back({v,w});
            g[v].push_back({u,w});
        }
        for(int i=1;i<=m;++i) work[i].clear();
        for(int i=1;i<=m;++i)
        {
            int k,p;
            cin>>k;
            while(k--)
            {
                cin>>p;
                work[i].push_back(p);
            }
            sort(work[i].begin(),work[i].end());
            work[i].erase(unique(work[i].begin(),work[i].end()),work[i].end());
        }
        bfs(1);
        int q;
        cin>>q;
        while(q--)
        {
            int a,b;
            cin>>a>>b;
            cout<<getCompanydis(a,b)<<endl;
        }
    }
    return 0;
}
```