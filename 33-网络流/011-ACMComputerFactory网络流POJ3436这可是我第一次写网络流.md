

### [ACM Computer Factory](https://vjudge.net/problem/POJ-3436)（网络流 POJ 3436，这可是我第一次写网络流）


### 题意：


```bash
有n台机器，每台机器有一个输入规则和输出规则 和一个最大生产速率，且每个输出和输出的属性有q个。
```


且对于机器的输入规则状态0代表没有，1代表必须有，2代表无所谓，输出规则的状态只有0 和1。现在让你求怎么样才能让流水线生产出最终产品的速率最大。

### 分析：


​ 这是一个网络流的模型，我们可以把机器作为节点, 然后设置一个超级源点$beg$，让所有输入为0 0 0 0 0(2也行)连接到超级源点$beg$，权值设为$inf$， 再设置一个超级汇点，让所有输入1 1 1 1 1的连接到超级汇点$end$ 权值设为$inf$。然后遍历所有机器，如果$a$可以到$b$ ,则设置一条边(权值后面再讨论)。不过可能要注意下面几个问题

+ 每个机器的最大生产速率是一定的。如果$a$可以到$b$，那么$a$到$b$的权值怎么决定呢？ 
  
+ 解决方案：插点法。对于第$i$个节点**新建一个节点**(这里是$i+n$)作为**中转点**，如果$i$到$i+n$的权值为第$i$个机器的速率，且所有$i$可以到达的点，替换成$i+n$节点到达(权值设置为$inf$或者$i$点的速率)。
 + 然后网络流模型即可解决。


### 代码：(EK算法+邻接表实现)


```
#include<bits/stdc++.h>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=120;
const int inf=0x7fffffff;
struct Edge
{
    int to;
    bool is_have;//是否有这个边 在初始的流浪网络中
};
struct Machine{
    int a[15],b[15],cap;
}machin[100];
int p,n;
class EdmondsKarp
{
    /*要求输入：顶点数和边即可*/
public:
    int flow;
    vector<Edge> adja[maxn];/*邻接表遍历边*/
    int cap[maxn][maxn];/*存取容量*/
    int pre[maxn];
    int dismin[maxn];
    int tot;
    /*输入顶点的个数 添加边*/
    void Init(int n)//初始化
    {
        for(int i=0; i<n; ++i) //边从1=0开始标号
            adja[i].clear();
        mset(cap,0);
        tot=n;
    }
    void AddEdge(int u,int v,int c)//又该边
    {
        /* 两个方向加上边 不给过属性不同，*/
        Edge nowe;
        cap[u][v]=c;
        cap[v][u]=0;
        nowe.to=v;
        nowe.is_have=1;//原图中有这边
        adja[u].push_back(nowe);
        nowe.to=u;
        nowe.is_have=0;//原图中没有这边
        adja[v].push_back(nowe);
    }
    int MaxFlow(int s,int t)
    {
        queue<int> mmp;

        flow=0;
        for(;;)
        {
            for(int i=0; i<tot; ++i)
            {
                 pre[i]=-1;
                 dismin[i]=inf;//s到i的最短路的流量最小值
            }
            pre[s]=0;//等于u
            mmp.push(s);
            while(!mmp.empty())
            {
                int nowu=mmp.front();
                mmp.pop();
                for(int i=0; i<adja[nowu].size(); ++i)
                {
                    int nowv=adja[nowu][i].to;
                    if(pre[nowv]==-1&&cap[nowu][nowv]>0)
                    {
                        pre[nowv]=nowu;
                        mmp.push(nowv);
                        dismin[nowv]=min(dismin[nowu],cap[nowu][nowv]);
                    }
                }
            }
            if(pre[t]==-1)
                return flow;
            /*有一条增广路径  顺着这条增广路径一直把边的容量改变*/
            flow+=dismin[t];
            int lastu,now;
            now=t;
            while(now!=s)
            {
                lastu=pre[now];
                cap[lastu][now]-=dismin[t];
                cap[now][lastu]+=dismin[t];
                now=lastu;
            }
        }
    }
};
EdmondsKarp kit;
bool judge(int i,int j)//i能否到j
{
    for(int t=0;t<p;++t)
    {
        if(machin[j].a[t]!=2&&machin[i].b[t]!=machin[j].a[t])
        {
            return 0;
        }
    }
    return 1;
}
bool IsBeginOut(int i)//看需要的输入是不是全为0
{
    for(int j=0;j<p;++j)
    {
        if(machin[i].a[j]==1)
            return false;
    }
    return true;
}
bool IsArrivedIn(int i)
{
    for(int j=0;j<p;++j)
    {
        if(machin[i].b[j]!=1)
            return false;
    }    return true;
}
int main()
{
    scanf("%d%d",&p,&n);
    kit.Init(2*n+2);
    for(int i=1;i<=n;++i)
    {
        scanf("%d",&machin[i].cap);
        for(int j=0;j<p;++j)
            scanf("%d",machin[i].a+j);
        for(int j=0;j<p;++j)
            scanf("%d",machin[i].b+j);
        kit.AddEdge(i,i+n,machin[i].cap);
        if(IsBeginOut(i))
            kit.AddEdge(0,i,machin[i].cap);
        if(IsArrivedIn(i))
        {
            kit.AddEdge(i+n,2*n+1,machin[i].cap);
        }

    }
    for(int i=1;i<=n;++i)
    {
        for(int j=1;j<=n;++j)
        {
            if(i==j)
                continue;
            if(judge(i,j))
                kit.AddEdge(i+n,j,inf);
        }
    }
    int res=kit.MaxFlow(0,2*n+1);
    int tot=0;
    for(int i=n+1;i<=2*n;++i)
    {
        for(int j=0;j<kit.adja[i].size();++j)
        {
            int v=kit.adja[i][j].to;
            if(kit.adja[i][j].is_have=true&&v>=1&&v<=n&&i!=v+n&&kit.cap[v][i]>0)
                tot++;
        }
    }
    printf("%d %d\n",res,tot);
    for(int i=n+1;i<=2*n;++i)
    {
        for(int j=0;j<kit.adja[i].size();++j)
        {
            int v=kit.adja[i][j].to;
            if(kit.adja[i][j].is_have=true&&v>=1&&v<=n&&i!=v+n&&kit.cap[v][i]>0)
               printf("%d %d %d\n",i-n,v,kit.cap[v][i]);
        }
    }
    return 0;
}

```


