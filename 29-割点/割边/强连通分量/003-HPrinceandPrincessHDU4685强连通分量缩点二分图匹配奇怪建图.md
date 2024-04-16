

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


