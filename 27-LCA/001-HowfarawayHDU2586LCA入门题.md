## How far away ？ HDU - 2586(LCA入门题)



####  题目:[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=4547)


思路见注释


#### 代码 :

```cpp
/*
求树上无向图的两点简单路径距离距离
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
const int DEG=20;
vector<P> g[N];//v,w=(first,second)
int fa[N][DEG+1],deg[N];
int dis[N][DEG+1];//dis[u][i]为u到2^i个祖先的路径和
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
int n,m;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int T;
    cin>>T;
    while(T--)
    {
        int q;
        cin>>n>>q;
        for(int i=1;i<=n;++i) g[i].clear();
        for(int i=1;i<n;++i)
        {
            int u,v,w;
            cin>>u>>v>>w;
            g[u].push_back({v,w});
            g[v].push_back({u,w});
        }
        bfs(1);
        while(q--)
        {
            int a,b;
            cin>>a>>b;
            cout<<LCAds(a,b)<<endl;
        }
    }
    return 0;
}
```