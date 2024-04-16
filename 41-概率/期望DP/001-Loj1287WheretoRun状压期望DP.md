

### Loj-1287 Where to Run（状压期望DP）


##### 题目链接：[LightOJ - 1287 ](https://vjudge.net/problem/26997/origin)


##### 题意：


​ 先给一个n个点m条无向边的图，每条边都有一个权值，顶点编号从0开始，刚开始自己站在0号点，现在要躲避警察的追踪。走的路线有如下限制：

+  离开一个顶点之后就不能回到该顶点 +  如果站在某个顶点u，**剩下的未走的邻接顶点不存在 E J 顶点就停止并被警察抓到**，E J 顶点指如果到该顶点后，满足条件1的情况下可以走完所有未走完的顶点。 如果存在E J顶点，则会进行如下**随机选择**，如果有k个E J顶点，那么有1/(k+1)的概率选择先停留原地5分钟（隐藏）或走剩下的E J 顶点。 +  如果走u到v这条边，则花费的时间为u到v这条边的权值。 


求从 $0$ 号顶点开始出发**躲避警察的时间的期望值**。

数据范围：$n\in[1,15],0\le u,v<n,0< w\le 100$

##### 思路：


​ 我们用$dp[s][u]​$代表经过的顶点状态是 $s​$ ,现在处于节点 $u​$ 的剩下的期望躲避时间，所以我们要求的就是$dp[1][0]​$


期间我一直在想怎么判断剩下的邻接顶点是E J顶点，期间想了各种方法，但都太麻烦且时间复杂度大。

实际上对于状态$(s,u)​$，我们用$cans[s][u]​$代表这个状态下从 $u​$ 开始能否遍历完其他未遍历完的顶点，判断状态$(s,u)​$中$u​$是否为为E J顶点只需判断可选的顶点中是否存在E J 顶点即可


形式化的，我们现在来求$cans[s][u]$，假设有边$(u,v)$，且状态$s$中未经过顶点$v$，那么如果$cans[s|(1<<v)][v]=true$，则$can[s][u]=true$

对于状态转移方程

假设状态$(s,u)​$可选的顶点有 $k​$ 个

+  如果 $k>0$: 对于状态$(s,u)$下u的所有邻接E J顶点$v$，且边权$w$，那么 $dp[s][u]=\frac{1}{k+1}*(dp[s][u]+5)+\frac{1}{k+1}*\sum _k (dp[s|(1<<v)][v]+w)$ $cans[s][u]=true$ +  否则： $dp[s][u]=0$ $cans[s][u]=false$ 


因为$dp$方程中 $s$ 是递增的，所以我们可以按照 $s$ 从大到小遍历，其次遍历$u$ 求$dp[s][u]$和$cans[s][u]$即可，特殊的满状态下$dp[s_{max}][u]=0,cans[s_{max}][u]=true$

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const double eps=1e-5;
typedef pair<int,int> P;
bool cans[1<<16][16];
double dp[1<<16][16];
vector<pair<int,int> > g[16];
int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0; i<=n; ++i) g[i].clear();
        for(int i=1; i<=m; ++i)
        {
            int u,v,w;
            scanf("%d%d%d",&u,&v,&w);
            g[u].push_back(make_pair(v,w));
            g[v].push_back(make_pair(u,w));
        }
        int top=(1<<n)-1;
        for(int s=top; s>=0; --s)
        {
            for(int u=0; u < n; ++u)
            {
                dp[s][u]=0;
                cans[s][u]=false;
                if(s==top)
                {
                    cans[s][u]=true;
                    continue;
                }
                if((s&(1<<u)) == 0) continue;
                int k=0;
                double sum=0.0;
                for(P &p:g[u])
                {
                    int v=p.first,w=p.second;
                    if((s&(1<<v))==0&&cans[s|(1<<v)][v])
                    {
                        k++;
                        sum+=dp[s|(1<<v)][v]+w;
                    }
                }
                if(k > 0)
                {
                    cans[s][u]=true;
                    dp[s][u]=(5.0+sum)/k;
                }

            }
        }
        printf("Case %d: %.8f\n",++cas,dp[1][0]);
    }
    return 0;
}
```


