

### [C - Dual Core CPU](https://vjudge.net/problem/POJ-3469)(最小割，ISAP实现)


[POJ - 3469 ](https://vjudge.net/problem/16358/origin)

#### 题意：


​ 一个双核CPU上运行N个模块，每个模块在两个核上运行的费用分别为Ai和Bi。

同时，有M对模块需要进行数据交换，如果这两个模块不在同一个核上运行需要额外花费。

求运行N个模块的最小费用。

#### 分析：


​ 挑战书上有一句说的好。 “ 用最小费用将对象划分为两个集合的问题，常常可以转化为最小割后顺利解决 ”。

在这里，我们可以将之转化为最小割的问题；图中的顶点有源点$S$，汇点$T$，和所有模块的顶点$V$；我们想让这个图分成两个部分，**源点S可以到达的点的集合**和**可以到达汇点T的点的集合**。

下面就是建图，怎么才能将最小花费转化为图的最小割的费用。

+  让$S$与所有顶点$V$连接，容量为$A_i$。代表模块V在核A上的代价 +  让所有顶点$V$与$T$连接，容量为$B_i$。代表模块V在核B$上的代价 +  对于每种组合，模块$u$与模块$v$组合在不同cpu$上的代价为$cap$，我们让顶点$u$与顶点$v$连接一条双向边，容量为cap。 


然后我们求图的最小割，其值也就是最大流。


我们可以想想一下为什么等效最小割，如果两个顶点$u$，$v$分开后在同一个集合内，如果有$u$，$v$的组合，那么改边一定不会被割开。当然如果两个顶点$u$,$v$分开后不在一个集合，如果有$u$,$v$的组合，那么必定有$s$到$u$，$u$到$v$，$v$到$t$的一个边，即该边需要割开才能使两个顶点在不同的集合内。这样就符合题意了，即不在一个cpu上需要对于模块组合需要花费对应的代价。

​ 等效性证明： 题目中任何一个分配的方案，在建图中都对应一个割图，且费用相等。而任何一个割图也都对应一个分配方案，所以求小费用的分配方案即求最小割。

所以我们求的最小割一定是题目所求的解。


```cpp
#include<queue>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int maxn=2e4+100;
const int maxm=5e5+20;
const int MAXN=2e4+100;;//点数的最大值
const int MAXM=1e6+20;//边数的最大值
const int INF=0x3f3f3f3f;
const int inf=0x3f3f3f3f;
struct Edge
{
    int to,next,cap,flow;
} edge[MAXM];
class ISAP
{
//输入参数:起点、终点、点的总数
//点的编号没有影响，只输入点的总数
public:
    int tol;
    int head[MAXN];
    int gap[MAXN],dep[MAXN],cur[MAXN];
    void init()
    {
        tol=0;
        mset(head,-1);
    }
    void addEdge(int u,int v,int w,int rw=0)
    {
        edge[tol].to=v,edge[tol].cap=w,edge[tol].next=head[u];
        edge[tol].flow=0,head[u]=tol++;
        edge[tol].to=u,edge[tol].cap=rw,edge[tol].next=head[v];
        edge[tol].flow=0,head[v]=tol++;
    }
    int Q[MAXN];
    void BFS(int start,int end)
    {
        mset(dep,-1),mset(gap,0);
        gap[0]=1;
        int front=0,rear=0;
        dep[end]=0;
        Q[rear++]=end;
        while(front!=rear)
        {
            int u=Q[front++];
            for(int i=head[u]; i!=-1; i=edge[i].next)
            {
                int v=edge[i].to;
                if(dep[v]!=-1)  continue;
                Q[rear++]=v;
                dep[v]=dep[u]+1;
                gap[dep[v]]++;
            }
        }
    }
    int S[MAXN];
    int sap(int start,int end,int N)//只输入源点和汇点的编号   和顶点个数
    {
        BFS(start,end);
        memcpy(cur,head,sizeof(head));
        int top=0,u=start,ans=0;
        while(dep[start]<N)
        {
            if(u==end)
            {
                int Min=INF;
                int inser;
                for(int i=0; i<top; i++)
                {
                    if(Min>edge[S[i]].cap-edge[S[i]].flow)
                    {
                        Min=edge[S[i]].cap-edge[S[i]].flow;
                        inser=i;
                    }
                }
                for(int i=0; i<top; ++i)
                {
                    edge[S[i]].flow+=Min;
                    edge[S[i]^1].flow-=Min;
                }
                ans+=Min;
                top=inser;
                u=edge[S[top]^1].to;
                continue;
            }
            bool flag=false;
            int v;
            for(int i=cur[u]; i!=-1; i=edge[i].next)
            {
                v= edge[i].to;
                if(edge[i].cap-edge[i].flow&&dep[v]+1==dep[u])
                {
                    flag=true;
                    cur[u]=i;
                    break;
                }
            }
            if(flag)
            {
                S[top++]=cur[u];
                u=v;
                continue;
            }
            int Min= N;
            for(int i=head[u]; i!=-1; i=edge[i].next)
            {
                if(edge[i].cap-edge[i].flow&&dep[edge[i].to]<Min)
                {
                    Min=dep[edge[i].to];
                    cur[u]=i;
                }
            }
            gap[dep[u]]--;
            if(!gap[dep[u]])    return ans;
            dep[u]=Min+1;
            gap[dep[u]]++;
            if(u!=start) u=edge[S[--top]^1].to;
        }
        return ans;
    }
};
ISAP kit;
int main(){
    int n,m,a,b;
    /*
    n个顶点1~n   m条边
    s到顶点，顶点到t， 容量分别为a，b
    边开成双向的
    */
    scanf("%d%d",&n,&m);
    kit.init();
    int source=0,endd=n+1;
    for(int i=1;i<=n;++i){
        scanf("%d %d",&a,&b);
        kit.addEdge(source,i,a);
        kit.addEdge(i,endd,b);
    }
    for(int i=1;i<=m;++i){
        int u,v,cap;
        scanf("%d%d%d",&u,&v,&cap);
        kit.addEdge(u,v,cap);
        kit.addEdge(v,u,cap);
    }
    int ans=kit.sap(source,endd,n+2);
    printf("%d\n",ans);
    return 0;
}

```


