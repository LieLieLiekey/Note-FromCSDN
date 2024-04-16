

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


