

### [G - Island Transport](https://vjudge.net/problem/HDU-4280) [HDU - 4280 ](https://vjudge.net/problem/31862/origin)


In the vast waters far far away, there are many islands. People are living on the islands, and all the transport among the islands relies on the ships. 　　You have a transportation company there. Some routes are opened for passengers. Each route is a straight line connecting two different islands, and it is bidirectional. Within an hour, a route can transport a certain number of passengers in one direction. For safety, no two routes are cross or overlap and no routes will pass an island except the departing island and the arriving island. Each island can be treated as a point on the XY plane coordinate system. X coordinate increase from west to east, and Y coordinate increase from south to north. 　　The transport capacity is important to you. Suppose many passengers depart from the westernmost island and would like to arrive at the easternmost island, the maximum number of passengers arrive at the latter within every hour is the transport capacity. Please calculate it.

Input

The first line contains one integer T (1<=T<=20), the number of test cases. 　　Then T test cases follow. The first line of each test case contains two integers N and M (2<=N,M<=100000), the number of islands and the number of routes. Islands are number from 1 to N. 　　Then N lines follow. Each line contain two integers, the X and Y coordinate of an island. The K-th line in the N lines describes the island K. The absolute values of all the coordinates are no more than 100000. 　　Then M lines follow. Each line contains three integers I1, I2 (1<=I1,I2<=N) and C (1<=C<=10000) . It means there is a route connecting island I1 and island I2, and it can transport C passengers in one direction within an hour. 　　It is guaranteed that the routes obey the rules described above. There is only one island is westernmost and only one island is easternmost. No two islands would have the same coordinates. Each island can go to any other island by the routes.

Output

For each test case, output an integer in one line, the transport capacity.

Sample Input

```bash
2
5 7
3 3
3 0
3 1
0 0
4 5
1 3 3
2 3 4
2 4 3
1 5 6
4 5 3
1 4 4
3 4 2
6 7
-1 -1
0 1
0 2
1 0
1 1
2 3
1 2 1
2 3 6
4 5 5
5 6 3
1 4 6
2 5 5
3 6 4
```


Sample Output

```bash
9
6
```


##题意：

​ 给你n个顶点的坐标和m条边，边是双向的有容量，让你求最左边的顶点到最右边的顶点的最大流。

### 思路：


​ 思路超简单，不过Dinc和EK和不优化的ISAP都容易超时。只能用bing神的板子

##### ISAP+BFS初始化+栈优化：


```
#include<string>
#include<cstring>
#include<cstdio>
#include<queue>
#include<iostream>
#define mset(a,b) memset(a,b,sizeof(a))
const int MAXN=100010;
const int MAXM=400010;
const int INF=0x3f3f3f3f;
const int inf=0x3f3f3f3f;
struct Edge
{
    int to,next,cap,flow;
} edge[MAXM];
class ISAP
{
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
    int sap(int start,int end,int N)
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
                for(int i=0;i<top;i++)
                {
                    if(Min>edge[S[i]].cap-edge[S[i]].flow){
                        Min=edge[S[i]].cap-edge[S[i]].flow;
                        inser=i;
                    }
                }
                for(int i=0;i<top;++i){
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
inline int read()
{
    int s=0,w=1;
    char ch=getchar();
    while(ch<'0'||ch>'9')
    {
        if(ch=='-') w=-1;
        ch=getchar();
    }
    while(ch>='0'&&ch<='9') s=s*10+ch-'0',ch=getchar();
    return s*w;
}
ISAP kit;
int main()
{
    int n,m,t;
    scanf("%d",&t);
    while(t--)
    {
        int leftIndex,leftx,rightIndex,rightx;
        leftx=inf,rightx=-1*inf;
        scanf("%d%d",&n,&m);
        for(int i=1; i<=n; ++i)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            if(x<leftx)
            {
                leftx=x;
                leftIndex=i;
            }
            if(x>rightx)
            {
                rightx=x;
                rightIndex=i;
            }
        }
        kit.init();
        for(int i=1; i<=m; ++i)
        {
            int u,v,w;
            scanf("%d%d%d",&u,&v,&w);
            kit.addEdge(u,v,w);
            kit.addEdge(v,u,w);
        }
        int ans=kit.sap(leftIndex,rightIndex,n);
        printf("%d\n",ans);
    }
    return 0;
}

```


