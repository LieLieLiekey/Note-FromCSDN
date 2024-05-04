

## 最小费用流问题概述

最小费用流问题是图论中的一个模型，用于找到网络中某些特定条件下的最优流动方式。这些条件包括最小化成本以及满足特定的流量需求。

#### 模型定义

- **图** \(G(V, E)\)：由节点 \(V\) 和边 \(E\) 组成。
- **边属性**：每条边 \( (u, v) \) 有最大容量 \( c_{uv} \) 和单位流动成本 \( cost_{uv} \)。
- **源点 \( s \)** 和 **汇点 \( t \)**：流量从源点 \( s \) 流向汇点 \( t \)。
- **总流量需求 \( D \)**：需要从源点 \( s \) 向汇点 \( t \) 传输的流量。

#### 目标

找到一种流 \( f \)：
- **流量守恒**：对于所有节点（除源点和汇点外），进入的流量等于流出的流量。
- **流量限制**：总流量不超过 \( D \)。
- **成本最小化**：总费用 \( \sum_{(u, v) \in E} cost_{uv} \times flow_{uv} \) 是最小的。

#### 解决方案

最小费用流问题通常采用增广路径算法进行求解，例如：
1. **贝尔曼-福特算法**（Bellman-Ford Algorithm）：适用于包含负权边的情况。
2. **最短路算法**：找到成本最低的路径，然后增加该路径上尽可能多的流量。
3. **最小费用最大流算法**：结合最短路算法和最大流算法迭代求解。

这些方法通过在残余网络中寻找并调整最低成本的流量路径来实现目标，涉及多次迭代和调整
。
#### 增广路概念
在图论和网络流问题中，增广路径（Augmenting Path）是一个非常重要的概念。增广路径指的是从源点到汇点的一条路径，这条路径上的所有边都还有剩余的容量可以用来传递更多的流量。换句话说，增广路径是一条可以通过增加流量以满足某些条件（如最大化总流量或最小化成本）的路径。

增广路径的特点和作用：
剩余容量：增广路径上的每条边都至少有一个单位的剩余容量，这意味着流还可以通过这些边继续增加。
流量调整：在找到一个增广路径后，可以通过这条路径增加流量。具体增加的流量取决于路径上的最小剩余容量（也称为瓶颈容量）。
算法的核心：许多网络流算法（如Edmonds-Karp算法）的核心步骤就是寻找增广路径并通过这些路径增加流量，直到再也找不到新的增广路径为止。

## 大致思路：

​ 在寻找增广路的前提下，只找s到t距离最短的增广路，并沿着这条路进行增广。


> 本代码采用 SPFA 进行寻找最短的增广路，如果所有 cost 为正的，则保证残余流量图中不会出现负环。
>> 为什么不会出现负环？ 如果出现负环，代表这个环有流量，且环中的边都是反向边($c o s t cost$为负的)。且在此之前肯定沿着环的反方向进行增广了(当时肯定是正环) ，但是如果先前在一个正环上进行了一次增广就不会是沿着最短路增广，这与先前每次增广的都是最短路矛盾！故不可能存在负环。


> 时间复杂度为$O(|V|*|E|^2*log_2 |V|)​$ 这是上届，一般情况都能过。
> 其实在增广路进行寻找时 可以用Dijkstra算法优化（引入势的概念）



最小费用流多用于指派问题，比如二分图最小权匹配（二分图的网络流图，费用为权值即可），二分图最大权匹配（把费用变为权的负值即可），还有不重叠边的多路径选取的最小权(最大权)问题。


###  采用 SPFA 的寻找最短增广路算法：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int maxn=220;//顶点数量
const int inf=0x3f3f3f3f;
struct edge{
   
    int to,cap,cost,rev;
    edge(){
   }
    edge(int to,int cap,int cost,int rev){
   this->to=to,this->cap=cap,this->cost=cost,this->rev=rev;}
};
class MCMF{
   
public:
    vector<edge> adja[maxn];
    int dis[maxn],prevv[maxn],preve[maxn],top;
    bool inque[maxn];
    void init(int n)
    {
   
        for(int i=0;i<n;++i)    adja[i].clear();
        top=n;
    }
    void addEdge(int u,int v,int f,int cost){
   
        adja[u].push_back(edge(v,f,cost,adja[v].size()));
        adja[v].push_back(edge(u,0,-1*cost,adja[u].size()-1));
    }
    bool spfa(int s,int t){
   
        queue<int> mp;
        mset(dis,inf);
        mset(prevv,-1);
        mset(inque,0);
        mp.push(s),prevv[s]=s,dis[s]=0,inque[s]=true;
        while(!mp.empty()){
   
            int u=mp.front();
            mp.pop();
            inque[u]=false;
            for(int i=0;i<adja[u].size();++i){
   
                edge& e=adja[u][i];
                if(e.cap>0&&dis[e.to]>dis[u]+e.cost){
   
                    dis[e.to]=dis[u]+e.cost;
                    prevv[e.to]=u;
                    preve[e.to]=i;
                    if(!inque[e.to]){
   
                        inque[e.to]=true;
                        mp.push(e.to);
                    }
                }

```


//他的第三个函数也可以这样写，即满足流f的最小花费
```
int minCostMaxFlow(int s,int t,int f) //不能满足流f则返回-1
{
    int cost=0;
    while(f>0)
    {
        spfa(s,t);
        if(dis[t]==inf)
            return -1;
        int d=f;
        for(int v=t; v!=prevv[v]; v=prevv[v]) //找到d
            d=min(d,adja[prevv[v]][preve[v]].cap);
        cost+=d*dis[t];
        f-=d;
        for(int v=t; v!=prevv[v]; v=prevv[v])
        {
            edge &e=adja[prevv[v]][preve[v]];
            e.cap-=d;
            adja[v][e.rev].cap+=d;
        }
    }
    return cost;
}
```


### 采用dijkstra的最短增广路算法：（有时候性能不如SPFA的，可能是因为容器的问题）
**证明**：
1. 每次求最短路时,用$h(v)$作为顶点的势，其$h(v)$ 初始化为0，后来每一回合让$h(v)$等于上一次$dijkstra$来求最短路的$dist(v)$。
2. 让$w'(e)=w(e)+h(u)-h(v)，其中e=u\ to\ v .\ \ \ 且 w'(e)>=0 \ 当e边存在时​$
3. 用 $w'(e)$ 代替 $w(e)$ 以寻找一条 $s$ 到 $t$ 的最短路径


**证明过程中关于我的一些问题以及解释** :

 > 下面关于术语可能不太准确，但能从语言中理解什么意思。（整理时候太过匆忙，请谅解）

 - 在该顶点的势中$h[v]$是上一次 $s$ 到 $v$顶点的最短路，假设第一步中$w'(e)>=0$且更新了$s$到所有顶点的最短路。为什么下一步中下列条件能够满足？

1.图中所有存在的边e都满足这样的情况即$w'(e(u->v))=w(e)+h(u)-h(v)>=0$

1.1. 如果上一次有 e 这条边，那么就不难证明$w'(e)>=0​$
1.2. 如果上一次没 e 这条边，那么  h(v) 和  h(u) 的大小不能直接讨论，但是如果之后这条边出现，那么证明上次$e$在$s$到$t$的最短路径中,即有 $w‘(e)=w'(e)+h(u)-h(v)==0$
1.3. 所以如果上一次$w'(e)>=0$，且经过了s到所有点的最短路径的扫描，那么下次的$w'(e)>=0$  (如果边$e​$ 出现的话)

2.为什么$w'(e)$对应的图中s到t的最短路径一定是残余网络中$s$到$t$的最短路径？
2.1 在$w'(e)$对应的图中，$s$到$t$的任何路径$w'(s-> v)+w'(v->u)+w'(u->t)=w(s->v)+w(v->u)+w(u->t)-h(t)$

2.2 表示为对应w'(e)中相应的图的最短路减去t点的势， 故两个图的最短路等价。

>### 注意事项：
>
>​	如果第一次就存在负边，那么第一步用SPFA求出s到所有点的最短路径即可。其余步骤相同。
>
>​	如果存在负圈就用bellman-ford算法找出负圈并在负圈上尽量增广把负圈消去 (消去其中一条边即可)

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef pair<int, int>P;//first保存最短距离，second保存顶点的编号
const int maxn=250;
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
    int min_cost_flow(int s, int t, int f)//返满足流f的最小费用  不能满足返回-1
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
            for (int x = t; x != s; x = prevv[x]){
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

```
