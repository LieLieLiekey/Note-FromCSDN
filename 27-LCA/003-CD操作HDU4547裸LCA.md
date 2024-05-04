## CD操作 HDU - 4547（裸LCA）


####  题目:[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=4547)


思路见注释


#### 代码 :

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
const int DEG=20;
vector<int> g[N];
int fa[N][DEG+1],deg[N],du[N];
unordered_map<string,int> mmp;
int tol;
int getid(string s)
{
    if(mmp[s]==0){
        mmp[s]=++tol;
        return tol;
    }
    return mmp[s];
}
void bfs(int root)
{
    queue<int> Q;
    Q.push(root);
    fa[root][0]=root;
    deg[root]=0;
    while(!Q.empty())
    {
        int u=Q.front();
        Q.pop();
        for(int i=1; i<=DEG; ++i) fa[u][i]=fa[fa[u][i-1]][i-1];
        for(int i=0; i<g[u].size(); ++i)
        {
            int v=g[u][i];
            deg[v]=deg[u]+1;
            fa[v][0]=u;
            Q.push(v);
        }
    }
}
int lca(int u,int v)
{
    if(deg[u]>deg[v]) swap(u,v);
    int tu=u,tv=v;
    for(int det=deg[tv]-deg[tu],i=0; det; ++i)
    {
        if(det&(1<<i))
        {
            det-=(1<<i);
            tv=fa[tv][i];
        }
    }
    if(tu==tv) return tu;
    for(int i=DEG; ~i; --i)
    {
        if(fa[tu][i]!=fa[tv][i])
        {
            tu=fa[tu][i];
            tv=fa[tv][i];
        }
    }
    return fa[tu][0];
}
string su,sv;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        int n,q;
        mmp.clear();
        tol=0;
        cin>>n>>q;
        for(int i=1;i<=n;++i) g[i].clear();
        for(int i=1;i<n;++i)
        {
            cin>>su>>sv;
            int u=getid(su);
            int v=getid(sv);
            g[v].push_back(u);
            du[u]++;
        }
        int root;
        for(int i=1;i<=n;++i)
        {
            if(!du[i]) {root=i;break;}
        }
        bfs(root);
        while(q--)
        {
            cin>>su>>sv;
            int u=getid(su);
            int v=getid(sv);
            int ans=0,ooo=lca(u,v);
            ans=deg[u]-deg[ooo];
            if(ooo!=v) ans++;
            cout<<ans<<endl;
        }
    }
    return 0;
}
```