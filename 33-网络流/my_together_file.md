

## Wi-fi Towers（2009 Google Jam world final D）最大权闭合子图


题目链接：[传送门](https://code.google.com/codejam/contest/311101/dashboard#s=p3)

**题意**：

​ 给定一个无线电塔的网络。对于每座无线电塔，都有一个半径参数，这座无线电塔可以给这个半径范围内的其他无线电塔发送信号，刚开始时无线电塔之间都使用的是古老的协议A进行通信，现在要将某些电塔升级到协议B，升级有个要求：如果电塔a升级到协议B，那么电塔a范围内所有电塔都必须升级到协议B（如果仅仅是某个协议B的电塔a被电塔b覆盖，那么电塔b不用必须升级到协议B）

​ 考虑到升级后的花费和升级后的收益，现我们给每座无线电塔打一个分数（正分表示升级之后收益更多，负分表示升级的花费更多），现要选择一些合适的无线电塔进行升级，使得升级的无线电塔的总分最大。

假设无线电塔的个数为$n$，无线电塔$i$的位置为$(x_i,y_i)$，覆盖半径为$r_i$，分数是$s_i​$.

数据范围：$n\in[1,500],x,y\in[-1000,1000],r\in[1,2000],s\in[-1000,1000]$

**思路**：

​ 所以我们让源点S连向$\mathbf{w}_{\mathbf{i}}\mathbf{\geq 0}$的点i，容量为$\mathbf{w}_{\mathbf{i}}$**；让**$\mathbf{w}_{\mathbf{i}}\mathbf{<0}$**的点i连向汇点T，容量为**$\mathbf{-}\mathbf{w}_{\mathbf{i}}$**；对于原图的边**$\mathbf{(u,v)}$**，让u连向v容量为inf。最终**$\mathbf{\text{su}}\mathbf{m}_{\mathbf{+}}\mathbf{-}​$(S到T的最小割)就是答案。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn=550;
const int inf=0x3f3f3f3f;
struct edge{
int cap,rev,to;
    edge(){};
    edge(int to,int cap,int rev){this->to=to,this->cap=cap,this->rev=rev;}
};
class EK{
public:
    vector<edge> adja[maxn];
    int prevv[maxn],top;
    int preve[maxn];
    void init(int n)
    {
        for(int i=0;i<n;++i)    adja[i].clear();
        top=n;
    }
    void bfs(int s,int t)
    {
        memset(prevv,-1,sizeof(prevv));
        queue<int> mmp;
        mmp.push(s);
        prevv[s]=s;
        while(!mmp.empty()){
            int u=mmp.front();
            mmp.pop();
            for(int i=0;i<adja[u].size();++i){
                edge& e=adja[u][i];
                if(prevv[e.to]==-1&&e.cap>0)
                {
                    prevv[e.to]=u;
                    preve[e.to]=i;
                    mmp.push(e.to);
                }
            }
        }
    }
    void addEdge(int u,int v,int f)
    {
        adja[u].push_back(edge(v,f,adja[v].size()));
        adja[v].push_back(edge(u,0,adja[u].size()-1));
    }
    int maxFlow(int s,int t)
    {
        int flow=0;
        for(;;)
        {
            bfs(s,t);
            if(prevv[t]==-1)
                return flow;
            else
            {
                int minn=inf;
                for(int last=t;prevv[last]!=last;last=prevv[last]){
                    minn=min(minn,adja[prevv[last]][preve[last]].cap);
                }
                flow+=minn;
                for(int last=t;prevv[last]!=last;last=prevv[last]){
                    edge& e=adja[prevv[last]][preve[last]];
                    e.cap-=minn;
                    adja[last][e.rev].cap+=minn;
                }
            }
        }
    }
}ooo;
const int N=505;
int x[N],y[N],r[N],s[N];
int solve(int n)
{
    int S=0,T=n+1,sum=0;
    ooo.init(n+2);
    for(int i=1;i<=n;++i)
    {
        if(s[i]>0){
            sum+=s[i];
            ooo.addEdge(S,i,s[i]);
        }
        else{
            ooo.addEdge(i,T,-s[i]);
        }
    }
    for(int i=1;i<=n;++i)
    {
        for(int j=1;j<=n;++j){
            if(i==j) continue;
            int m=(x[j]-x[i])*(x[j]-x[i])+(y[j]-y[i])*(y[j]-y[i]);
            if(m<=r[i]*r[i]){
                ooo.addEdge(i,j,inf);
            }
        }
    }
    int flow=ooo.maxFlow(S,T);
    return sum-flow;
}
int main()
{
//    freopen("1.in","r",stdin);
//    freopen("1.out","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;++i) scanf("%d%d%d%d",x+i,y+i,r+i,s+i);
        printf("Case #%d: %d\n",++cas,solve(n));
    }
    return 0;
}

```




### 网络流之 - 匹配、边覆盖、独立集、顶点覆盖



以下摘抄：[https://blog.sengxian.com/algorithms/networkflow-variants](https://blog.sengxian.com/algorithms/networkflow-variants)


Published on 2015-12-01

在图论中，有以下几个概念，它们之间的关系往往容易弄混淆，这里稍稍证明一下。 先放出概念 - 来自日本人的书。

### 概念


+ 匹配 : 在 $G$中两两没有公共端点的边集合 $M \subseteq E$+ 边覆盖：在 G*G* 中的任意顶点都至少是 F*F* 中某条边的端点的 边集合 $F \subseteq E​$ （边覆盖所有点）+ 独立集：在 G*G* 中两两互不相连的顶点集合 $S \subseteq V​$+ 顶点覆盖：在 G*G* 中的任意边都有至少一个端点属于 S*S* 的顶点集合 $S \subseteq V$ （顶点覆盖所有边）


与之对应的，有最大匹配$ M_{max}​$，最小边覆盖 $F_{min}​$，最大独立集 $S_{max}​$、最小顶点覆盖 $S_{min}​$ 的概念，不过这个应该很好理解。

### 关系


它们之间是满足一些关系的。（废话

#### 最大匹配与最小边覆盖


对于任意无孤立点的图而言

$\vert M_{max} \vert + \vert F_{min} \vert = \vert V \vert​$

用中文描述就是「最大匹配数 + 最小边覆盖数 = 顶点数」

#### 最大独立集与最小顶点覆盖


对于任意图（无所谓联通）而言

$\vert S_{max} \vert + \vert S_{min} \vert = \vert V \vert$

用中文描述就是「最大独立集数 + 最小顶点覆盖数 = 顶点数」。与之前的不同，这里的集合都是针对顶点的集合。

### 求解


借助这些关系，对于有最大匹配与最小边覆盖，最大独立集与最小顶点覆盖，求解出一个就可以求解出另一个。 对于最大匹配问题，二分图可以转化为网络流，一般图则一般用开花树（Edmonds）算法解决。 而对于最大独立集和最小顶点覆盖，却无法高效求解，他们是NP困难的。不过，对于二分图而言：

$\vert M_{max} \vert = \vert S_{min}\vert$

中文描述就是「最大匹配数 = 最小顶点覆盖数」。



### [UVA - 10480 ](https://vjudge.net/problem/41692/origin)


### 题意：


​ 给你一个网络图，开始时候有$n n$，$m m$两个整数，分别代表顶点个数和边的个数。下面$m m$行，每个边有三个整数$u , v , w u,v,w$组成，代表$u u$到 $v v$有一条无向边，费用为$w w$。

现在让你把图破坏某些边，分成两个部分即与$1 1$连接部分的和与$2 2$连接部分，现在让你求破坏费用最小的的的情况下，需要破坏那些边。

### 分析：


​ 最大流最小割定理，$s s$到$t t$的最小割的边就是$s s$到$t t$的最大流的上的关键边.

接下来怎么求残余网络的关键边？

跑一边最大流之后， **让可以与源点$s ​ s​$联通的顶点标记**，接下来遍历所有边，如果该边的一个顶点标记，而另一个顶点未标记，那么这就是其中一个关键边。

### 代码:


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P```




网络流我习惯采用EK算法

### 思想:


​ 每次从残留网络找出一条增广路，并且沿着这条路增广即可，直至没有增广路

​ 关于网络流的用处：

​ 网络流就像水流一样，求最大的水流速率，很多问题可以转化为网络流模型来解决

+ 二分图匹配( 最少边覆盖)


​ 网络流的做题经验：


求最大消耗量：将产生值的连接到**源点**，消耗值的连接到**汇点**

顶点上有最大容量限制： 插点即可

边上有最小容量限制：（先放一放）假设u到v的最小容量限制为b(e), 那么新增S‘，T’ 让 u到T‘ 流量为b(e),S’到v的流量为b(e) 然后令u到v的容量为c(e)-b(e) 。不过要在S与s，T与t连接之前，先检查S到T的最大容量是否为Sum(e)(让 v到s容量为b(e),)


### 代码：


```cpp
#include<queue>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cstdio>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int maxn=120;
const int inf=0x3f3f3f3f;
struct edge{
int cap,rev,to;//储存 容量、邻接点、反向边
    edge(){};
    edge(int to,int cap,int rev){this->to=to,this->cap=cap,this->rev=rev;}
};
class EK{
public:
    vector<edge> adja[maxn];
    int prevv[maxn],top;
    int preve[maxn];
    void init(int n)
    {
        for(int i=0;i<n;++i)    adja[i].clear();
        top=n;
    }
    void bfs(int s,int t)
    {
        memset(prevv,-1,sizeof(prevv));
        queue<int> mmp;
        mmp.push(s);
        prevv[s]=s;
        while(!mmp.empty()){
            int u=mmp.front();
            mmp.pop();
            for(int i=0;i<adja[u].size();++i){
                edge& e=adja[u][i];
                if(prevv[e.to]==-1&&e.cap>0)
                {
                    prevv[e.to]=u;
                    preve[e.to]=i;
                    mmp.push(e.to);
                }
            }
        }
    }
    void addEdge(int u,int v,int f)
    {
        adja[u].push_back(edge(v,f,adja[v].size()));
        adja[v].push_back(edge(u,0,adja[u].size()-1));
    }
    int maxFlow(int s,int t)
    {
        int flow=0;
        for(;;)
        {
            bfs(s,t);
            if(prevv[t]==-1)
                return flow;
            else
            {
                int minn=inf;
                for(int last=t;prevv[last]!=last;last=prevv[last]){
                    minn=min(minn,adja[prevv[last]][preve[last]].cap);
                }
                flow+=minn;
                for(int last=t;prevv[last]!=last;last=prevv[last]){
                    edge& e=adja[prevv[last]][preve[last]];
                    e.cap-=minn;
                    adja[last][e.rev].cap+=minn;
                }
            }
        }
    }
};
EK kit;

int main()
{
    
}

```


#### 我bing神的模板贼快 ISAP+BSF+栈优化


```cpp
const int MAXN=100010;//点数的最大值  
const int MAXM=400010;//边数的最大值
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
```




### [B - Evacuation](https://vjudge.net/problem/POJ-3057)


[POJ - 3057 ](https://vjudge.net/problem/23765/origin)

#### 题意：


​ 墙壁“X”，空区域（都是人）“.”， 门“D”。

人向门移动通过时视为逃脱，门每秒能出去一个人，人可以上下左右移动，墙阻止移动。

求最优移动方案下，最后一个人逃脱的最短时间。如果有人无法安全逃脱（比如被墙围困住），则输出“impossible”。

#### 思路：


​ **大致思路：**

​ 可以巧妙的建图来转化这个问题，我们来建立一个二分图，左边节点是人，右边节点为 (时间,门)的元组。如果该人可以在该时间到这个门，那么就有一条人 到元组的边，然后求可以使得所以人都匹配情况下的最小时间$t$。

​ **具体实现思路：**

​ $bfs​$出每个人与所有门的最短距离$minDis[peo][door]​$ （代码中使用 $mindis[px][py][dx][dy]​$ 来表示）。

建立二分图：**左边节点为人,右边节点为 (时间,门)的元组** ；对于每一个时间$t$，如果有$minDis[peo][door]&gt;=t$的 都有 $people$到$(door,t)$权值为$1$的边；

然后每次增加时间$t$，并且添加新的关于$(door,t)$的元组，并连接上可以连接到的人，然后求新增加的匹配数目，直到匹配数目大于$people$的个数即可；又因为时间$t$最大为$n$，所以超过$n$就是无解了。

注：


二分时间$T$ 会超时，所以这里采用的是在原来的时间$t$的基础上，每次将$t$加$1$，直到所有人都被匹配即可。


### 代码：


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
const int maxn=3e4+10;
const int inf=0x3f3f3f3f;

struct edge
{
    int to,rev,cap;
    edge() {}
    edge(int to,int cap,int rev):to(to),rev(rev),cap(cap) {}
};
class EK
{
public:
    vector<edge> adja[maxn];
    int prevv[maxn],preve[maxn],top;
    void init(int n)
    {
        for(int i=0; i<n; ++i) adja[i].clear();
        top=n;
    }
    void addEdge(int u,int v,int cap)
    {
        adja[u].push_back(edge(v,cap,adja[v].size()));
        adja[v].push_back(edge(u,0,adja[u].size()-1));
    }
    void bfs(int s,int t)
    {
        queue<int> mmp;
        mset(prevv,-1);
        prevv[s]=s;
        mmp.push(s);
        while(!mmp.empty())
        {
            int u=mmp.front();
            mmp.pop();
            for(int i=0; i<adja[u].size(); ++i)
            {
                edge &e=adja[u][i];
                if(e.cap>0&&prevv[e.to]==-1)
                {
                    prevv[e.to]=u;
                    preve[e.to]=i;
                    mmp.push(e.to);
                }
            }
        }
    }
    int maxFlow(int s,int t)//多次使用的网络流
    {
        int flow=0;
        for(;;)
        {
            bfs(s,t);
            if(prevv[t]==-1)
                return flow;
            int minn=inf;
            for(int v=t; v!=prevv[v]; v=prevv[v])
            {
                minn=min(minn,adja[prevv[v]][preve[v]].cap);
            }
            flow+=minn;
            for(int v=t; v!=prevv[v]; v=prevv[v])
            {
                edge &e=adja[prevv[v]][preve[v]];
                e.cap-=minn;
                adja[v][e.rev].cap+=minn;
            }
        }

    }
};
EK kit;
int X,Y;
vector<P> peo;
vector<P> door;
int minDis[18][18][18][18];
char files[18][18];
/*
bfs出每个人与所有门的最短距离 mindis[px][py][dx][dy]
 建立二分图：    左边人,右边(时间,门)的元组  ，且minDis[peo][door]>=t的       peo到(door,t)都有权值为1的边
每次增加时间t，并且添加新的关于(door,t)的元组，并连接上可以连接到的人，然后求新增加的匹配数目，直到匹配数目大于people的个数即可。
又因为时间t最大为n，所以超过n就是无解了
*/
int dir[4][2]= {-1,0,1,0,0,-1,0,1};
struct node
{
    int x,y,s;
    node() {}
    node(int x,int y,int s):x(x),y(y),s(s) {}
};
void bfs(int x,int y)//x y坐标与其他门的距离{
{
    queue<node>mmp;
    mmp.push(node(x,y,0));
    while(!mmp.empty())
    {
        node p=mmp.front();
        mmp.pop();
        if(files[p.x][p.y]=='D')
        {
            minDis[x][y][p.x][p.y]=p.s;
            continue;
        }
        for(int i=0; i<4; ++i)
        {
            int xx=p.x+dir[i][0];
            int yy=p.y+dir[i][1];
            if(xx>=0&&xx<X&&yy>=0&&yy<Y&&files[xx][yy]!='X'&&minDis[x][y][xx][yy]==-1)
            {
                //门或者空地,不能从门道门
                minDis[x][y][xx][yy]=0;
                mmp.push(node(xx,yy,p.s+1));
            }
        }
    }
}
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        mset(minDis,-1);
        peo.clear();
        door.clear();
        scanf("%d%d",&X,&Y);
        for(int i=0; i<X; ++i)
            scanf("%s",files[i]);
        for(int i=0; i<X; ++i)
        {
            for(int j=0; j<Y; ++j)
            {
                if(files[i][j]=='.')
                {
                    peo.push_back({i,j});
                    bfs(i,j);
                }
                else if(files[i][j]=='D')
                {
                    door.push_back({i,j});
                }
            }
        }
        if(peo.size()==0)
        {
            printf("0\n");
            continue;
        }
        int flow=0,ans=-1,n=X*Y;
        int dtot=door.size(),ptot=peo.size();
        kit.init(dtot*n+ptot+2);
        int endd=dtot*n+ptot+1,source=0;
        for(int i=1; i<=ptot; ++i) kit.addEdge(source,dtot*n+i,1); //源点到peo的距离
        for(int d=1; d<=dtot; ++d) //(t,door) 到endd的距离
        {
            for(int k=1; k<=n; ++k)
                kit.addEdge(dtot*(k-1)+d,endd,1);
        }
        /*
        随后每次增加时间 并且增加时间对应的一些边
        */
        for(int t=1; t<=X*Y; ++t)
        {
            for(int p=0; p<ptot; ++p)
            {
                for(int d=0; d<dtot; ++d)
                {
                    if(minDis[peo[p].first][peo[p].second][door[d].first][door[d].second]==-1)
                        continue;
                    if(minDis[peo[p].first][peo[p].second][door[d].first][door[d].second]<=t)
                        kit.addEdge(dtot*n+p+1,dtot*(t-1)+d+1,1);
                }
            }
            flow+=kit.maxFlow(source,endd);
            if(flow>=ptot){
                ans=t;
                break;
            }
        }
        if(ans==-1)
        {
            printf("impossible\n");
        }
        else
            printf("%d\n",ans);
    }
    return 0;
}
```




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




### 题意：


      有n个人，m个星球，下面有n行，每行有m个数字，0或1。如果第 i 行第k 个数字为0代表第i 个人不适合生活在星球k，否则适合生活在星球k。每个星球有可以容纳的人数，能否将所有人都转移星球。

 

### 分析：


     最大流，普通的建图很容易想出来，但是n是个10w左右的数（就连ISAP也过不了），我们可以考虑将生活的m个星球的状态作为一个节点，第i 为1代表这个节点的人可以到第i个星球。这样就可以把节点转化为最多1024个。然后建图即可

 

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn=2100;
const int inf=0x3f3f3f3f;
const ll mod=1e9+7;
/* 找出最左边的岛和最优边的岛 求最大流即可*/
struct edge
{
    int to,cap,rev;//rev 代表反向边在 to的第几个边
    edge() {}
    edge(int to,int cap, int rev)
    {
        this->to=to,this->cap=cap,this->rev=rev;
    }
};
inline int rd()
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
class EK
{
public:
    vector<edge> adja[maxn];
    int prevv[maxn],top,preve[maxn];
    void init(int n)
    {
        for(int i=0; i<n; ++i)    adja[i].clear();
        top=n;
    }
    void addEdge(int u,int v,int cap)
    {
        adja[u].push_back(edge(v,cap,adja[v].size()));
        adja[v].push_back(edge(u,0,adja[u].size()-1));
    }
    void bfs(int s,int t)
    {
        queue<int>mp;
        mset(prevv,-1);
        prevv[s]=s,mp.push(s);
        while(!mp.empty())
        {
            int u=mp.front();
            mp.pop();
            for(int i=0; i<adja[u].size(); ++i)
            {
                edge& e=adja[u][i];
                if(e.cap>0&&prevv[e.to]==-1)
                {
                    prevv[e.to]=u;
                    preve[e.to]=i;
                    mp.push(e.to);
                }
            }
        }
    }
    int maxFlow(int s,int t)
    {
        int flow=0;
        for(;;)
        {
            bfs(s,t);
            if(prevv[t]==-1)
                return flow;
            int minn=inf;
            for(int v=t; v!=prevv[v]; v=prevv[v])
            {
                minn=min(minn,adja[prevv[v]][preve[v]].cap);
            }
            flow+=minn;
            for(int v=t; v!=prevv[v]; v=prevv[v])
            {
                edge& e=adja[prevv[v]][preve[v]];
                e.cap-=minn;
                adja[v][e.rev].cap+=minn;
            }
        }
    }
};
EK kit;
int state[2050];
int main()
{
    int n,m;
    while(~scanf("%d%d",&n,&m))
    {
        kit.init((1<<m)+m+2);
        mset(state,0);
        int source=(1<<m)+m+1,endd=(1<<m)+m+2,val;
        for(int i=1; i<=n; ++i)
        {
            int s=0;
            for(int j=1; j<=m; ++j)
            {
                val=rd();
                s<<=1,s+=val;//前面的是小的行求  底位是第m个行求
            }
            state[s]++;
        }
        int top=(1<<m);
        for(int i=0; i<top; ++i)
        {
            kit.addEdge(source,i,state[i]);
            val=i;
            if(state[i]==0) continue;
            for(int k=0; k<m; ++k)
            {
                if((val>>k)&1)
                {
                    kit.addEdge(i,top+m-k,inf);
                }
            }
        }
        for(int i=1; i<=m; ++i)
        {
            val=rd();
            kit.addEdge(top+i,endd,val);
        }
        int sum=kit.maxFlow(source,endd);
        if(sum==n)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}```


 



### [C - A Plug for UNIX](https://vjudge.net/problem/POJ-1087)[POJ - 1087 ](https://vjudge.net/problem/10508/origin)


### 题意：


​ 给你一些插头，和插座。插头和插座分别有不同的型号，只有相同的型号才能配成一对。现在有k个转换器，每种转换器有无限个，但不一定有所有的转换器型号，转换器的作用是：将一个插头转换成另一个插头。现在求你最少有多少个插头不能插到插座上。

### 分析：


​ 只要求最多有多少个插头可以插到插座上即可，那么我们可以采用网络流算法。

+ 让source指向所有插头，权值为1。+ 让所有插座指向汇点End，权值为1。+ 然后根据所有的插头和插座和转换器 set出所有的**插头类型**。+ 让插头指向对应的**插头类型**，权值为1。+ 让**插头类型**指向对应的插座，权值为1.+ 根据转换器，让**插头类型**指向**插头类型**，权值为inf。


然后求source 到End的最大流即可。

**提供一组数据 **

```bash
输入：
2
A
A
2
laptop C
comb D
3
C X
X A
D X
输出：
0

```


### 代码：


```
#include<vector>
#include<queue>
#include<cstdio>
#include<set>
#include<cstring>
#include<string>
#include<algorithm>
#include<iostream>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
const int maxn=710;
const int inf=0x3f3f3f3f;
string seat[110],head[110],Convert[300][2];
int htot,stot,ztot;//插头 插座  转换器
vector<string>headCla;
class EK
{
public:
    vector<int> adja[maxn];//
    int cap[maxn][maxn];
    int dis[maxn],pre[maxn],tot;
    void init(int n)
    {
        for(int i=0; i<n; ++i)
            adja[i].clear();
        mset(cap,0);
        tot=n;
    }
    void addEdge(int s,int t,int f)
    {
        cap[s][t]=f;
        cap[t][s]=0;
        adja[s].push_back(t);
        adja[t].push_back(s);
    }
    void bfs(int s,int t)//广搜一条增广路径
    {
        mset(dis,-1);
        queue<int>mmp;
        mmp.push(s);
        dis[s]=s;
        while(!mmp.empty())
        {
            int u=mmp.front();
            mmp.pop();
            for(int i=0; i<adja[u].size(); ++i)
            {
                int v=adja[u][i];
                if(dis[v]==-1&&cap[u][v]>0)
                {
                    dis[v]=dis[u]+1;
                    pre[v]=u;
                    mmp.push(v);
                }
            }
        }
    }
    int maxFlow(int s,int t)
    {
        int flow=0;
        for(;;)
        {
            bfs(s,t);
            if(dis[t]==-1)
                return flow;
            int last=t,minn=inf;
            while(last!=pre[last])
            {
                minn=min(minn,cap[pre[last]][last]);
                last=pre[last];
            }
            last=t;
            while(last!=pre[last])
            {
                cap[pre[last]][last]-=minn;
                cap[last][pre[last]]+=minn;
                last=pre[last];
            }
            flow+=minn;
        }
    }
};
set<string> Unique;
EK kit;
int main()
{
    int source=0,Endd;
    string name;
    while(~scanf("%d",&stot))
    {
        Unique.clear();
        for(int i=0; i<stot; ++i){
         cin>>seat[i];
         Unique.insert(seat[i]);
        }
        scanf("%d",&htot);
        for(int i=0; i<htot; ++i){
         cin>>name>>head[i];
         Unique.insert(head[i]);
        }
        /*输入插座和插头*/
        sort(seat,seat+stot);
        sort(head,head+htot);
        scanf("%d",&ztot);
        for(int i=0; i<ztot; ++i)
        {
            cin>>Convert[i][0]>>Convert[i][1];
            Unique.insert(Convert[i][0]);
            Unique.insert(Convert[i][1]);
        }
        headCla.clear();
        for(set<string>::iterator it=Unique.begin();it!=Unique.end();++it)   headCla.push_back(*it);
        kit.init(stot+htot+headCla.size()+2);//初始化
        Endd=stot+htot+headCla.size()+1;
        /*插头与插头类型相连*/
        int TotHeadCla=htot+stot;
        int TotHead=stot,Totseat=0;
        for(int i=0; i<htot; ++i)
        {
            int th=lower_bound(headCla.begin(),headCla.end(),head[i])-headCla.begin();
            kit.addEdge(TotHead+i+1,TotHeadCla+th+1,1);
        }
        /*插头类型与插座相连*/
        for(int i=0; i<stot; ++i)
        {
            int th=lower_bound(headCla.begin(),headCla.end(),seat[i])-headCla.begin();
            if(th==headCla.size())
                continue;
            kit.addEdge(TotHeadCla+th+1,Totseat+i+1,1);
        }
        /*插头利用转换器与插头相连*/
        for(int i=0;i<ztot;++i){
            string a=Convert[i][0];
            string b=Convert[i][1];
            int ath,bth;
            ath=lower_bound(headCla.begin(),headCla.end(),a)-headCla.begin();
            bth=lower_bound(headCla.begin(),headCla.end(),b)-headCla.begin();
            if(ath==bth||ath==headCla.size()||bth==headCla.size())
                continue;
            kit.addEdge(TotHeadCla+ath+1,TotHeadCla+bth+1,inf);
        }
        for(int i=1; i<=htot; ++i) //跟插头对着
            kit.addEdge(source,TotHead+i,1);
        for(int i=1; i<=stot; ++i)
            kit.addEdge(Totseat+i,Endd,1);
        int ans=kit.maxFlow(source,Endd);
        printf("%d\n",htot-ans);
    }
    return 0;
}
```




 

###  题意：


      有f 个食物和 d个饮料，现在有n头牛，每头牛有喜欢的食物和饮料。每头牛只吃自己喜欢的饮料和食物，且食物和饮料各吃一个才算满足，问最多能满足多少个牛？

### 分析：


     这是挑战书上的例题，花式建图，下面的图中，f是食物，d是饮料。

      令s到f的权值为1，d到t的权值为1，牛1到牛2的权值为1，喜欢的食物到牛，权值为1，牛到喜欢的饮料权值为1，求最大流即可


![./figures/20190316115428518.png](./figures/20190316115428518.png)


 以上图片来自[https://amoshyc.github.io/ojsolution-build/poj/p3281.html](https://amoshyc.github.io/ojsolution-build/poj/p3281.html).

 

代码：

```cpp
#include<vector>
#include<queue>
#include<cstdio>
#include<cstring>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
const int maxn=1100;
const int inf=0x3f3f3f3f;
class EK
{
public:
    vector<int> adja[maxn];
    int cap[maxn][maxn];
    int dis[maxn],pre[maxn],tot;
    void init(int n)
    {
        for(int i=0; i<n; ++i)
            adja[i].clear();
        mset(cap,0);
        tot=n;
    }
    void addEdge(int s,int t,int f)
    {
        cap[s][t]=f;
        cap[t][s]=0;
        adja[s].push_back(t);
        adja[t].push_back(s);
    }
    void bfs(int s,int t)//广搜一条增广路径
    {
        mset(dis,-1);
        queue<int>mmp;
        mmp.push(s);
        dis[s]=s;
        while(!mmp.empty())
        {
            int u=mmp.front();
            mmp.pop();
            for(int i=0; i<adja[u].size(); ++i)
            {
                int v=adja[u][i];
                if(dis[v]==-1&&cap[u][v]>0)
                {
                    dis[v]=dis[u]+1;
                    pre[v]=u;
                    mmp.push(v);
                }
            }
        }
    }
    int maxFlow(int s,int t)
    {
        int flow=0;
        for(;;)
        {
            bfs(s,t);
            if(dis[t]==-1)
                return flow;
            int last=t,minn=inf;
            while(last!=pre[last])
            {
                minn=min(minn,cap[pre[last]][last]);
                last=pre[last];
            }
            last=t;
            while(last!=pre[last])
            {
                cap[pre[last]][last]-=minn;
                cap[last][pre[last]]+=minn;
                last=pre[last];
            }
            flow+=minn;
        }
    }
};
int main()
{
    int N, F,D;
    scanf("%d %d %d",&N,&F,&D);
    EK kit;
    kit.init(2*N+F+D+2);// s=0   t=2*N+F+D+1
    for(int i=1; i<=N; ++i) // i ->N+i
    {
        kit.addEdge(i,i+N,1);
        int ftot,dtot,val;
        scanf("%d %d",&ftot,&dtot);
        for(int j=1; j<=ftot; ++j) //2*N+j
        {
            scanf("%d",&val);
            kit.addEdge(2*N+val,i,1);
        }
        for(int j=1; j<=dtot; ++j) //2*N+F+j
        {
            scanf("%d",&val);
            kit.addEdge(N+i,2*N+F+val,1);
        }
    }
    for(int i=1; i<=F; ++i) kit.addEdge(0,2*N+i,1);
    for(int i=1; i<=D; ++i) kit.addEdge(2*N+F+i,2*N+F+D+1,1);
    printf("%d\n",kit.maxFlow(0,2*N+F+D+1));

    return 0;
}
```


 



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


