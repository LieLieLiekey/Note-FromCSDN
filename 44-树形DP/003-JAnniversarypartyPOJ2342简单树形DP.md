

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


