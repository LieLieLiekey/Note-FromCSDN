

### [G - Intervals](https://vjudge.net/problem/POJ-3680)


[POJ - 3680 ](https://vjudge.net/problem/12877/origin)

#### 题意：


​ 求n个区间，从中选取一些区间，使得每个点最多被覆盖k次，使得权值和最大。

#### 分析：


​ 等效问题：选出一些区间，使得区间分成$k k$个区间集合。每个集合里面区间不相交，要求总权值和最大。

网络流将所有端点排序，相邻节点连接一条费用为$0 0$，容量为$i n f inf$的边，对于每个区间$i i$，$a a$到$b b$端点连接一条费用为$− w [ i ] -w[i]$的边。容量为$1 1$。那么求最小费用流，每一个流都代表一个不重叠的区间选取。其权值和等于费用的相反数。

```cpp
#include<queue>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int maxn=500;//顶点数量
const int inf=0x3f3f3f3f;
/*求n个区间，从中选取一些区间，使得每个点最多被覆盖k次
等效问题：选出一些区间，使得区间分成k个集合。每个集合区间不相交，要求容量最大
网络流将所有端点排序，相邻节点连接一条费用为0，容量为inf的边，对于每个区间i，a到b端点连接一条费用为-w[i]的边。容量为1
那么求最小费用流，每一个流都代表一个不重叠的区间选取。其权值等于费用的相反数
*/
struct edge
{
   
    int to,cap,cost,rev;
    edge() {
   }
    edge(int to,int cap,int cost,int rev)
    {
   
        this->to=to,this->cap=cap,this->cost=cost,this->rev=rev```




### [D - Going Home](https://vjudge.net/problem/POJ-2195)POJ - 2195 (最小费用模板题)


### 题意：


给你一个N行M列的地图，其中m代表人 ，H代表房子。每个房子只能容纳一个人，但是每个人走一步都需要耗费一点体力，求在所有人都进入房子的情况下总的耗费体力最小为多少？ 题目保证m的个数和h的个数相同

### 分析：


​ 最小费用最大流模板题。让源点s连接每个m，容量为1；让每个H连接汇点t，容量为1；对于每个$m_i$和$H_i$, 计算出$m_i$和$H_i$的曼哈顿距离，作为$m_i$到$H_i$的费用，$m_i$到$H_i$边的容量为1；

这样求满流的情况下最小费用即可、

```cpp
#include<iostream>
#include<algorithm>
#include<string>
#include<sstream>
#include<set>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<deque>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<functional>
using namespace std;

#define N 250
#define INF 100000000
typedef pair<int, int>P;//first保存最短距离，second保存顶点的编号
const int maxn=250;
struct Edge
{
    int to, cap, cost, rev;//终点，容量（指残量网络中的），费用，反向边编号
    Edge(int t, int c, int cc, int r) :to(t), cap(c), cost(cc), rev(r) {}
};
class MCMF
{
public:
    int V;//顶点数
    vector<Edge>G[N];//图的邻接表
    int h[N];//顶点的势
    int dist[N];//最短距离
    int prevv[N];//最短路中的父结点
    int preve[N];//最短路中的父边
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
    int min_cost_flow(int s, int t, int f)//返回最小费用
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
                if (dist[v]<p.first)continue;//p.first是v入队列时候的值，dist[v]是目前的值，如果目前的更优，扔掉旧值
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
                return res;
            for (int j = 0; j<V; j++)//更新h
                h[j] += dist[j];
            int d = f;
            for (int x = t; x != s; x = prevv[x])
                d = min(d, G[prevv[x]][preve[x]].cap);//从t出发沿着最短路返回s找可改进量
            f -= d;
            res += d*h[t];//h[t]表示最短距离的同时，也代表了这条最短路上的费用之和，乘以流量d即可得到本次增广所需的费用
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

int house[maxn][2],man[maxn][2],htot,mtot;
string grid[maxn];
MCMF kit;
int getDis(int ax,int ay,int bx,int by)
{
    return abs(ax-bx)+abs(ay-by);
}
int main()
{
    int n,m;
    while(cin>>n>>m,n,m)
    {
        for(int i=0; i<n; ++i)
            cin>>grid[i];
        htot=mtot=0;
        for(int i=0; i<n; ++i)
        {
            for(int j=0; j<m; ++j)
            {
                if(grid[i][j]=='H')
                {
                    house[htot][0]=i;
                    house[htot++][1]=j;
                }
                else if(grid[i][j]=='m')
                {
                    man[mtot][0]=i;
                    man[mtot++][1]=j;
                }
            }
        }
        int flow=0,cost=0,soure=htot+mtot,endd=htot+mtot+1;
        kit.init(htot+mtot+2);
        for(int i=0; i<htot; ++i)
        {
            for(int j=0; j<mtot; ++j)
            {
                int w=getDis(house[i][0],house[i][1],man[j][0],man[j][1]);
                kit.addEdge(i,htot+j,1,w);
            }
        }
        for(int i=0; i<htot; ++i)
        {
            kit.addEdge(soure,i,1,0);
        }
        for(int j=0; j<mtot; ++j)
        {
            kit.addEdge(j+htot,endd,1,0);
        }
        cost=kit.min_cost_flow(soure,endd,INF);
        cout<<cost<<endl;
    }
    return 0;
}
```




## 最小费用流


### 大致思路：


​ 在寻找增广路的前提下，只找s到t距离最短的增广路，并沿着这条路进行增广。


本代码采用SPFA进行寻找最短的增广路，如果所有$c o s t cost$为正的，则保证残余流量图中不会出现负环。


为什么不会出现负环？ 如果出现负环，代表这个环有流量，且环中的边都是反向边($c o s t cost$为负的)。且在此之前肯定沿着环的反方向进行增广了(当时肯定是正环) ，但是如果先前在一个正环上进行了一次增广就不会是沿着最短路增广，这与先前每次增广的都是最短路矛盾！故不可能存在负环。


时间复杂度为$O ( ∣ V ∣ ∗ ∣ E ∣ 2 ∗ l o g 2 ∣ V ∣ ) ​ O(|V|*|E|^2*log_2 |V|)​$ 这是上届，一般情况都能过。

其实在增广路进行寻找时 可以用Dijkstra算法优化（引入势的概念）



最小费用流多用于指派问题，比如二分图最小权匹配（二分图的网络流图，费用为权值即可），二分图最大权匹配（把费用变为权的负值即可），还有不重叠边的多路径选取的最小权(最大权)问题。


采用SPFA的寻找最短增广路算法：

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




### [D - Farm Tour](https://vjudge.net/problem/POJ-2135)（最小费用流）


[POJ - 2135](https://vjudge.net/problem/16586/origin)

#### 思路：


​ 问题可以转化为求两条$1 1$到$n n$的路径，使得这两条路径没有重边且费用和最小。而这个问题我们又可以转化为最小费用流问题。对于$u u$到$v v$的费用为$w w$双向边，在图中转化为$u u$到$v v$容量$1 1$费用为$w w$的边和$v v$到$u u$容量为$1 1$，费用为$w w$的边； 求$1 1$到$n n$流量为$2 ​ 2​$

