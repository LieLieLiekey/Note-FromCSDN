

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


