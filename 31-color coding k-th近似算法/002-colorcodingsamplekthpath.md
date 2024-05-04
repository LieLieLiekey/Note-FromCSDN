# color coding ，sample k-th path algorithm
<br><br>



#### 什么是color  coding 算法
color coding算法是一种近似算法，主要用来解决找到一个**图的包含k个顶点的简单路径**的**最小(最大)权值路径**。

比如这个问题：

​	给你有n个顶点，m条边的无向图，每无向边条边由u,v,w组成，w为这条边的权值，现在求一个包含k个顶点的简单路径，使得这个路径上所有边的权值和最大。

数据范围：$n<=1e4.m<=1e4,2<=k<=6$


#### 暴力方法：

​	最暴力的方法就是枚举每个顶点$v$作为路径的起点进行dfs，最坏情况下的时间复杂度为$O(n*m)$



#### **我们用color coding解决：**

第一步：首先我们对图中的点随机染色，颜色的种类是k种（为选取的简单路径的顶点个数）。**而该算法要求枚举的路径上的所有顶点均颜色不同。**



第二步：接下来我们进行$dp$，$dp[s][v]$ 代表此时路径颜色集合状态为s，路径终点是$v​$的路径最大权值是多少。

​	对于这个DP,我们先对之进行初始化。把所有的$dp[*][*]$设为无效值(-inf)。然后对于每个顶点v和其颜色color[v]，$dp[1<<color[v]][v]=0]$,

​	然后从小到大枚举状态S，每一个状态$s$下枚举末尾顶点$v$，对于每个v我们其邻接所有边的前驱u，那么$dp[s][v]=max(dp[s][v],[s\ Xor\ (1<<color[v])][u])$ ，且要求且要求$s\&(1<<color[v])!=0$。

第三步：我们枚举顶点v，从$dp[2^k-1][v]$找到最大值即可。

每一次算法执行的时间复杂度为$O(2^k*m)​$。

该算法是近似算法，并且我们枚举到答案的概率为$k!/k^k$。故我们只需要$T*(k^k/k!)$次遍历这个算法，T越大，就越有可能获得到答案那条路径。总的时间复杂度是$O(T*2^k*m)$
   
>参考博客：color coding k-path近似算法：https://blog.csdn.net/u010352695/article/details/40924019?utm_source=blogxgwz5

#### 练习一下：

题目链接：[hdu 6664](<http://acm.hdu.edu.cn/showproblem.php?pid=6664>)

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e4+10;
int n,m,k;
vector<P> g[N];
int color[N],dp[80][N];//s,v
void init(int n)
{
    for(int i=1; i<=n; ++i) color[i]=rand()%k;
}
int solve(int n,int m,int k)
{
    init(n);

    int top=1<<k;
    for(int i=1; i<=n; ++i)
    {
        for(int s=0; s<top; ++s) dp[s][i]=-inf; // 无效值
        dp[1<<color[i]][i]=0;
    }
    for(int s=0; s<top; ++s)
    {
        for(int u=1; u<=n; ++u) //枚举顶点
        {
            if(!(s&(1<<color[u]))) continue;//不符合
//                cout<<"asdasd"<<endl;
            for(P &p:g[u])
            {
                int v=p.first,w=p.second;
                dp[s][u]=max(dp[s][u],dp[s^(1<<color[u])][v]+w);
            }
        }
    }
    int ans=-inf;
    for(int i=1; i<=n; ++i) ans=max(ans,dp[top-1][i]);
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    srand(time(NULL));
    cin>>t;
    while(t--)
    {
        cin>>n>>m>>k;
        for(int i=1; i<=n; ++i) g[i].clear();
        for(int i=0; i<m; ++i)
        {
            int u,v,w;
            cin>>u>>v>>w;
            g[u].push_back({v,w});
            g[v].push_back({u,w});
        }
        int p=300;//随机300次
        int ans=-inf;
        while(p--)
            ans=max(ans,solve(n,m,k));
//        cout<<"ans:"<<ans<<endl;
        if(ans<0)
            cout<<"impossible"<<endl;
        else
            cout<<ans<<endl;
    }
    return 0;
}

```
