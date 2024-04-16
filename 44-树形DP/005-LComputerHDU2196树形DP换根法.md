

### L - Computer(HDU2196 ，树形DP，换根法)


##### 题目 :[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=2196)


思路见注释

##### 代码 :


```cpp
*
换根法dp:
先把无根树化为有根树
第一遍dfs,对于顶点u,求u的子树到u的最大和次大距离
第二遍dfs,将树化为顶点u为根,求u的子树到u的最大距离和次大距离
    对于u的最大距离就是u的答案res[u],而u的次大距离是用来儿子换根的时候进行状态转移
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const ll N=1e4+10;
const ll mod=1e9+7;
vector<P> g[N];
int dp[N][2];//u的最大值与次大值
int pos[N][2];//u的最大值与次大值的位置
int res[N];
void dfs1(int u,int fa)
{
    for(P &p:g[u])
    {
        int v=p.first,w=p.second;
        if(v==fa) continue;
        dfs1(v,u);
        if(dp[v][0]+w>dp[u][0]){
            dp[u][1]=dp[u][0];
            pos[u][1]=pos[u][0];
            dp[u][0]=dp[v][0]+w;
            pos[u][0]=v;
        }
        else if(dp[v][0]+w>dp[u][1]){
            dp[u][1]=dp[v][0]+w;
            pos[u][1]=v;
        }
    }
//    printf("u:%d,dp[0]:%d,pos[0]:%d,dp[1]:%d,pos[1]:%d\n",u,dp[u][0],pos[u][0],dp[u][1],pos[u][1]);
}
void dfs2(int u,int fa,int w)
{
    int other=0;
    if(fa!=u)//再次换根为u，更新最大和次大
    {
         if(pos[fa][0]!=u)//other代表从父亲到该根的最大与次大
            other=dp[fa][0]+w;
         else
            other=dp[fa][1]+w;
         if(other>dp[u][0]){
            pos[u][1]=pos[u][0];
            dp[u][1]=dp[u][0];
            pos[u][0]=fa;
            dp[u][0]=other;
         }
         else if(other>dp[u][1])
         {
             pos[u][1]=fa;
             dp[u][1]=other;
         }
    }
    res[u]=dp[u][0];
    for(P &p:g[u])
    {
        int v=p.first;
        if(v==fa) continue;
        dfs2(v,u,p.second);
    }
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int n;
    while(cin>>n)
    {
        for(int i=1;i<=n;++i) g[i].clear();
        for(int i=2;i<=n;++i){
            int w,v;
            cin>>v>>w;
            g[i].push_back({v,w});
            g[v].push_back({i,w});
        }
        mset(dp,0);
        mset(pos,0);mset(res,0);
        dfs1(1,1);
        dfs2(1,1,0);
        for(int i=1;i<=n;++i){
            cout<<res[i]<<endl;
        }
    }
}
```


