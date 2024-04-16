

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


