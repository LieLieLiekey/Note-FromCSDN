

### [E - Minimum Cost](https://vjudge.net/problem/POJ-2516) POJ - 2516


### 题意：


​ 给你$n、m、k。n$ 。代表需要进货的商店的个数，$m$代表供货商的个数，$k$代表有几种货物。对于每个商店有$k$个属性分别对应$k$中该种货物的需求；对于每个供货商有$k$个属性分别对应该种货物的存储量。下面有$k$个$n*m$的矩阵，对于第$k&#x27;$个矩阵的第$n&#x27;$行第$m&#x27;$列 的值代表货物$k$’从$m&#x27;$到$n$‘的单位花费。

现在让你求所有商店满足所有需求的最下花费，不如不能满足则输出$-1$;

### 分析：


​ 对于每个货物$k$建立一个网络图，源点为$s$，汇点为$t$；第$m$个供货商指向第$n$个商店的容量为$inf$，单位花费为运送费用；源点$s$到供货商$m$容量为对应的库存量，花费为$0$；商店$n$到汇点$t$的容量为货物$k$的需求量，花费为$0$。对于每个$k$求最小花费加起来即可。如果有一种货物k不能满足满流则直接输出$-1$.


我刚开始时是把每个商店$n$和供货商$m$ 变成k个，然后建图求最小花费，但是顶点数最多有5000个，毫无疑问的超时了。


```bash
#include<queue>
#include<vector>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef pair<int, int>P;//first保存最短距离，second保存顶点的编号
const int maxn=5000+100;
const int INF=0x3f3f3f3f;
struct Edge
{
    int to, cap, cost, rev;//终点，容量（指残量网络中的），费用，反向边编号
    Edge(int t, int c, int cc, int r) :to(t), cap(c), cost(cc), rev(r) {}
};
class MCMF
{
public:
    int V;//顶点数
    vector<Edge>G[maxn];//图的邻接表
    int h[maxn];//上一次顶点的最短路s到v的最短路径
    int dist[maxn];//最短距离
    int prevv[maxn];//最短路中的父结点
    int preve[maxn];//最短路中的父边
    void init(int n)
    {
        for(int i=0; i<n; ++i)    G[i].clear();
        V = n;
    }
    void addEdge(int from, int to, int cap, int cost)
    {
        G[from].push_back(Edge( to, cap, cost, G[to].size()));
        G[to].push_back(Edge( from, 0, -cost, G[from].size() - 1 ));
    }
    int minCostMaxFlow(int s, int t, int f)//返回最小费用
    {
        int res = 0;
        fill(h, h + V, 0);
        while (f>0)//f>0时还需要继续增广
        {
            priority_queue<P, vector<P>, greater<P> >q;
            fill(dist, dist + V, INF);//距离初始化为INF
            dist[s] = 0;
            q.push(P(0, s));
            while (!q.empty())
            {
                P p = q.top();
                q.pop();
                int v = p.second;
                if (dist[v]<p.first)    continue;//p.first是v入队列时候的值，dist[v]是目前的值，如果目前的更优，扔掉旧值
                for (int i = 0; i<G[v].size(); i++)
                {
                    Edge&e = G[v][i];
                    if (e.cap>0 && dist[e.to]>dist[v] + e.cost + h[v] - h[e.to])//松弛操作
                    {
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
                        prevv[e.to] = v;//更新父结点
                        preve[e.to] = i;//更新父边编号
                        q.push(P(dist[e.to], e.to));
                    }
                }
            }
            if (dist[t] == INF)//如果dist[t]还是初始时候的INF，那么说明s-t不连通，不能再增广了
                return -1;
            for (int j = 0; j<V; j++)//更新h
                h[j] = dist[j];
            int d = f;
            int sum=0;
            for (int x = t; x != s; x = prevv[x])
            {
                d = min(d, G[prevv[x]][preve[x]].cap);//从t出发沿着最短路返回s找可改进量
                sum+=G[prevv[x]][preve[x]].cost;
            }
            f -= d;
            res += d*sum;//h[t]表示最短距离的同时，也代表了这条最短路上的费用之和，乘以流量d即可得到本次增广所需的费用
            for (int x = t; x != s; x = prevv[x])
            {
                Edge&e = G[prevv[x]][preve[x]];
                e.cap -= d;//修改残量值
                G[x][e.rev].cap += d;
            }
        }
        return res;
    }
};
MCMF kit;
int n,m,k;
int shop[55][55],pro[55][55];
int sellcost[55][55][55];
int getShopv(int nn,int kk)
{
    return m*k+k*(nn-1)+kk;//可以直接代表垫高点标号
}
int getProv(int mm,int kk)
{
    return 0+k*(mm-1)+kk; //pro v的货物k的顶点
}/*
时间复杂度 O(F)*M
分k次  ， 每次复杂度O(F Min)*m  变少
思路：
第k个建立边， 求最大流即可
*/
int main()
{
    while(scanf("%d%d%d",&n,&m,&k),k)
    {
        for(int i=1; i<=n; ++i)
            for(int kk=1; kk<=k; ++kk)//shopi 对于k的进货量
                scanf("%d",&shop[i][kk]);
        for(int i=1; i<=m; ++i)
            for(int kk=1; kk<=k; ++kk)//prom   k的有w个
                scanf("%d",&pro[i][kk]);
        for(int kk=1; kk<=k; ++kk)
            for(int r=1; r<=n; ++r)
                for(int c=1; c<=m; ++c)
                {
//                    int cost;
                    scanf("%d",&sellcost[r][c][kk]);

                }
        int flag=1,ans=0,source,endd;
        int sumflow;
        for(int kk=1;kk<=k;++kk){
            sumflow=0;//物品kk需要的流
            for(int i=1;i<=n;++i)
                sumflow+=shop[i][kk];
            kit.init(n+m+2);
            source=0,endd=n+m+1;
            for(int i=1;i<=n;++i)
                kit.addEdge(m+i,endd,shop[i][kk],0);
            for(int i=1;i<=m;++i)
                kit.addEdge(source,i,pro[i][kk],0);
            for(int i=1;i<=n;++i)
                for(int j=1;j<=m;++j)
                    kit.addEdge(j,m+i,INF,sellcost[i][j][kk]);
            int mid=kit.minCostMaxFlow(source,endd,sumflow);
            if(mid==-1){
                flag=0;
                break;
            }
            ans+=mid;
        }
         /*计算第k个最小花费，并确定是否为满流*/
        if(!flag)
            printf("-1\n");
        else
            printf("%d\n",ans);
    }

    return 0;
}
```


