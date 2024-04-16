

## 2019CCPC哈尔滨Artful Paintings（二分+差分约束）


题目链接：[传送门](https://codeforces.com/gym/102394/problem/A)

思路：


这题现场赛的时候TLE了，赛后才发现spfa可以剪枝，而且还缺少一约束。


我们假设答案是k，那么k+1也可行，所以可行性具有单调性。设函数S( i )为前 i 个cube画的个数。

那么有约束


+ $1 ≥ S ( i ) − S ( i − 1 ) ≥ 0 1\ge S(i)-S(i-1)\ge0$
+ 对于第一种条件，$S ( r ) − S ( l − 1 ) ≥ k S(r)-S(l-1)\ge k$
+ 对于第二种条件，$S ( n ) − S ( r ) + S ( l − 1 ) ≥ k S(n)-S(r)+S(l-1)\ge k$



因为对于第二种条件， $S ($



## 百度之星初赛第三场B题-最短路2（魔改dijstra）


**题目：**

小 A 是社团里的工具人，有一天他的朋友给了他一个 $n n$ 个点，$m m$ 条边的正权连通无向图，要他计算所有点两两之间的最短路。

作为一个工具人，小 A 熟练掌握着 floyd 算法，设 $w [ i ] [ j ] ​ w[i][j]​$*为原图中$ (i,j)​$ 之间的权值最小的边的权值，若没有边则 $w [ i ] [ j ] = ​ w[i][j]=​$无穷大。特别地，若 $i = j ​ i=j​$，则 $w [ i ] [ j ] = 0 ​ w[i][j]=0​$

Floyd 的 C++ 实现如下：

```
for(int k=1;k<=p;k++)
for(int i=1;i<=n;i++)
for(int j=1;j<=n;j++)
    w[i][j]=min(w[i][j],w[i][k]+w[k][j]);
```


当$ p=n$时，该代码就是我们所熟知的 $f l o y d floyd$，然而小 A 为了让代码跑的更快点，所以想减少 $p p$ 的值。

令 $D i , j D_{i,j}$为最小的非负整数 $x x$,满足当$ p=x$时，点 $i i$与点 $j j$之间的最短路被正确计算了。

现在你需要求 $∑ i = 1 n ∑ j = 1 n D i , j \sum_{i=1}^{n}\sum_{j=1}^{n}D_{i,j}$



## P3953 逛公园


**题目：**[传送门](https://www.luogu.org/problem/P3953)

**思路：**

​ 定义⼀条路径 (X…Y) 的冗余度为它的长度减去 X…Y 的最短路长度，那么这题就是求1到N的冗余度小于k的路径的条数。我们定义$d p [ i ] [ j ] dp[i][j]$ 代表1到 i 的冗余度等于 j 的路径的条数。对于一条有u到v的边表示为W(u,v)，我们定义函数$p ( u , v ) = w ( u , v ) + d i s [ u ] + d i t [ v ] − d i s [ T ] p(u,v)=w(u,v)+dis[u]+dit[v]-dis[T]$ 。那么$d p [ v ] [ j ] = S U M ( d p [ u ] [ j − p ( u , v ) ] ) dp[v][j]=SUM(dp[u][j-p(u,v)])$ ,这个函数的意义是S到T的路径中走(u,v)这条边浪费的长度。其中 u 是后驱为v的边的前驱顶点，边权为w。

​ 这题我们主要注意两点，第一点即零环无解，第二点是确定DP顺序，使得DP顺序是DP图的一个拓扑序(满足无后效性)。

​ 第一点因为数据量较大，我们可以考虑把所有0边都提出来，判断是否存在环即可。

​ 第二点我们可以根据先从小到大枚举冗余度k，在排除第一点的条件下，因为冗余度为0的路径不可能是一个环，对于冗余度不为0的边，我们不用管(因为我们是枚举是k从大到小)，对于浪费度为0的边(这些边只可能是到v的最短路上的边，非零边和零边)，在最短路上的边我们可以根据dis值从小到大来确定dp顶点顺序。对于dis值相等且这两个顶点有一个冗余度为0的边，即零边。我们需要额外的用另一种方法确定他们的dp顺序，我们可以在前面第一点的时候求零的顶点拓扑序列设为id，这样的话得到了零边的更新方式。

​ So



## 差分约束&最短路


##### 什么是差分约束


​ 如果一个系统由n个变量和m个约束条件组成，形成m个形如ai-aj≤k的不等式(i,j∈[1,n],k为常数),则称其为差分约束系统(system of difference constraints)。亦即，差分约束系统是求解关于一组变量的特殊不等式组的方法。

求解差分约束系统，可以转化成图论的单源最短路径（或最长路径）问题。


例子：参考[http://tsreaper.is-programmer.com/posts/180182](http://tsreaper.is-programmer.com/posts/180182)

来考虑这个不等式：a-b ≤ c。

我们知道，对于最短路，有这样的不等式：dis(u) ≤ dis(v) + len(v,u) （v,u是由一条长度为len(v,u)的有向边连接的两个点，dis(v)与dis(u)表示起点到达v或u的最短路）。

变形得：dis(u) - dis(v) ≤ len(v,u)，与a-b ≤ c是不是非常相似？

所以，对于形如a-b ≤ c的不等式，我们可以从点b向点a连接一条长度为c的边。这样，我们就可以把不等式转换为图。


##### 求满足条件的最大值该如何建图？求满足条件的最小值呢？


差分约束求最大值时需要将不等式化为<=的格式，因为这样的不等式满足图论中最短路的性质，所以接下来用最短路来求。求最小值需要将不等式化为>=的格式，因为这样的不等式满足图论中最长路的性质，所以接下来用最长路来求。

##### 差分约束解的存在性


**最长路为什么正环代表该约束条件下无解？**

最长路中不等式是>=的形式。

加入现在有a->b为$w_1 $， b − &gt; a 为 ，b-&gt;a为$w_2$, 这 是 一 个 正 环 ， 即 满 足 , 这是一个正环，即满足$w_1+w_2>0$， 把 边 转 化 为 不 等 式 就 是 ，把边转化为不等式就是$b>=a+w_1,a>=b+w_2$ ，整理一下就是$0 &gt; = w 1 + w 2 0&gt;=w_1+w_2$



## POJ - 1364 (差分约束)


**题意：**

​ 给出一个数字序列 S={a1,a2,…an}，它有 m 个子序列 Si={a[si], a[si+1], a[si+2], … a[si+ni]}，现在给出 m 个限制条件：第 i 个子序列的和 < ki 或 第 i 个子序列的和 > ki

**思路：**

​ 标准的差分约束，用$S i S_i$表示$a 1 + a 2 . . . + a i a_1+a_2...+a_i$



## HDU - 3592（差分约束）


**题意：**

n个人编号分别是1…n在排队，排队顺序与序号相同。现在有x个喜欢关系和y个厌恶关系

对于每一个喜欢关系 ：a b c 代表编号a和编号c之间的距离需要<=c

对于每一个厌恶关系：a b c 代表编号a和编号c之间的距离需要>=c

问在能否满足条件，如果满足条件求1~n之间的最大距离，如果距离无限大输出-2

**分析:**

假设$d[i]$为编号为$i$的成员距离队首的距离。

那么根据题意我们有下列约束条件

+ 喜欢关系a b c需要 $d[b]-d[a]&lt;=c$+ 厌恶关系a b c需要$d[b]-d[a]&gt;=c$+ 相邻之间距离大于1,$d[i]-d[i-1]&gt;=1$+ 队首距离为0，$d[1]=1$


因为求最大，我们我们最短路求满足差分约束下的源点1到n的最小距离即可

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const  int inf=0x3f3f3f3f;
struct Edge{
int to,w;
Edge(){}
Edge(int to,int w):to(to),w(w){}
};
int dis[1005],in[1005];//距离
vector<Edge> adja[1005];//邻接表
bool book[1005];//标记是否够在队列
bool spfa(int s,int n)//源点为s,共有n个点,求最短路
{//有负环返回true，无负环返回false
    queue<int> qe;
    mset(dis,inf);
    mset(in,0);mset(book,0);
    dis[s]=0;
    qe.push(s);book[s]=true;
    while(!qe.empty())
    {
        int u=qe.front();qe.pop();
        in[u]++;book[u]=false;
        if(in[u]>n) return true;
        for(Edge &e:adja[u])
        {
            int v=e.to,w=e.w;
            if(dis[v]>dis[u]+w){
                dis[v]=dis[u]+w;
                if(!book[v]){
                    book[v]=true;
                    qe.push(v);
                }
            }
        }
    }
    return false;
}
int T[1005];
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        int n,x,y;
        cin>>n>>x>>y;
        for(int i=0;i<=n;++i) adja[i].clear();
        for(int i=0;i<x;++i)
        {
            int a,b,c;
            cin>>a>>b>>c;
            adja[a].push_back(Edge(b,c));
        }
        for(int i=0;i<y;++i)
        {
            int a,b,c;
            cin>>a>>b>>c;
            adja[b].push_back(Edge(a,-c));
        }
        for(int i=2;i<=n;++i) adja[i].push_back(Edge(1,0));
        for(int i=2;i<=n;++i) adja[i].push_back(Edge(i-1,-1));
        if(!spfa(1,n))
        {
            cout<<"-1"<<endl;
        }
        else{
            if(dis[n]==inf)
                cout<<"-2"<<endl;
            else
                cout<<dis[n]<<endl;
        }

    }
    return 0;

}

```




## POJ - 1716 差分约束


**题意：**

给出n个区间，现在要你找出一个点集，使得这n个区间都至少有2个元素在这个点集里面，问这个点集最少有几个点

第一行一个整数n。 接下来n行，每行两个整数a,b,表示区间的左端点和右端点，被空格隔开。 所有输入数据的范围[0,10000]

输出集合最小的大小，满足区间都至少有两个点在集合中。

**思路：**

我们用$d [ i ] d[i]$代表0~i中存在点的个数。

那么d数组满足下列约束条件


+ 对于每个区间 a b，我们有$d [ b ] − d [ a − 1 ] &gt; = 2 d[b]-d[a-1]&gt;=2$
+ 每个位置要求 $d [ i ] &gt; = 0 d[i]&gt;=0$
+ 相邻位置要求$0 &lt; = d [ i ] − d [ i − 1 ] &lt; = 1 0&lt;=d[i]-d[i-1]&lt;=1$





## HDU 1688 Sightseeing（DP，统计最短路和次短路的个数）


##### **题目：**


​ [https://cn.vjudge.net/problem/30153/origin](https://cn.vjudge.net/problem/30153/origin)

##### 题意：


​ 给定一个图，源点s和汇点t，统计s到t的最短路的个数和最短路长度+1的路的个数

##### 思路：


如果只是统计s到t的最短路的个数可以用*Dijkstra*+dp解决。但是这里最短路长度+1的路的个数怎么计数呢？

​ 我们可以先把问题转化为求**最短路的个数** ，并且如果**次短路=最短路+1**，那么再加上次短路的个数。这与原问题是等效的。

**那么怎么找次短路并且求出次短路的个数呢？**

​ 其实找次短路的过程和*Dijkstra*找最短路是相似的。*Dijkstra*的证明是什么？ 每次找到一个未确定的当前距离最小的顶点，然后松弛，这个就是确认的最短的。这里添加了次短路,有什么相同的？

前者：最短路的前驱一定是最短路

后者：次短路的前驱一定是：最短路+长边，或次短路+短边

**我们有没有得到一个解法？**

​ *Dijkstra*是每次找到一个未确定的当前最短的顶点，然后松弛。

那我们这里把次短路的顶点也加上去，每次找到一个未确定的当前距离最小的顶点，这个顶点可能是最短路的顶点，也可能是次短路的顶点。总之我们找到它，并标记这个状态已经确认了，就像*Dijkstra*算法中确认后这个就不可能再次更新了。注意这里的状态是指(顶点，最短路/次短路)

**接下来就是松弛操作,怎么松弛呢？**

​ **最短路状态**中我们只需松弛相邻的边，**更新最短路和次短路**；**次短路状态**中松弛相邻的边，**更新次短路。**

这个过程我们用优先队列来优化：

代码：

```cpp
/*
这里mark=0代表最短路,mark=1代表次短路
*/
#include<iostream>
#include<cstring>
#include<string>
#include<cstdlib>
#include<queue>
#include<stack>
//#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const  int inf=0x3f3f3f3f;
struct Edge{
int to,w;
Edge(){}
Edge(int to,int w):to(to),w(w){}
};
struct Node{
int d,u,mark;
Node(){}
Node(int d,int u,int mark):d(d),u(u),mark(mark){}
bool operator < (const Node & b) const
{
    return d>b.d;
}
};
priority_queue<Node> qe;
int dis[1100][2],dp[1100][2];
vector<Edge> adja[1005];
void dijstr(int s,int n)
{
    while(!qe.empty()) qe.pop();
    mset(dis,inf);mset(dp,0);dis[s][0]=0;
    dp[s][0]=1;
    qe.push(Node(0,s,0));
    while(!qe.empty())
    {
        Node  node=qe.top();qe.pop();
        int u=node.u,mark=node.mark;
        if(node.d>dis[u][mark]) continue;//当前信息已经过时,删去(新的信息已经更新过了)
        for(Edge &e:adja[u])
        {
            int v=e.to,w=e.w;
            //比最短路更短  更新最短路和次短路
            if(dis[u][mark]+w<dis[v][0])
            {
                //次短路最短路
                dis[v][1]=dis[v][0];
                dp[v][1]=dp[v][0];//更新路径条数信息
                dis[v][0]=dis[u][mark]+w;
                dp[v][0]=dp[u][mark];//更新路径条数信息
                qe.push(Node(dis[v][0],v,0));//最新信息,加入堆
                qe.push(Node(dis[v][1],v,1));//最新信息,加入堆
            }
            else if(dis[u][mark]+w==dis[v][0])//与最短路相同
            {
                dp[v][0]+=dp[u][mark];//更新路径条数信息
            }
            else if(dis[u][mark]+w < dis[v][1])//比最短路长比次路短，更新次短路.这个状态其实只有mark=1可以进来
            {
                dis[v][1]=dis[u][mark]+w;
                dp[v][1]=dp[u][mark];//更新路径条数信息
                qe.push(Node(dis[v][1],v,1));//最新信息,堆
            }
            else if(dis[u][mark]+w == dis[v][1])//与次短路相等.这个状态其实只有mark=1可以进来
            {
                dp[v][1]+=dp[u][mark];//更新路径条数信息
            }
        }
    }
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        for(int i=1;i<=n;++i) adja[i].clear();
        for(int i=0;i<m;++i){
            int u,v,w;
            cin>>u>>v>>w;
            adja[u].push_back({v,w});
        }
        int s,t;
        cin>>s>>t;
        dijstr(s,n);
        int ans=0;
        ans=dp[t][0];
        if(dis[t][1]==dis[t][0]+1) ans+=dp[t][1];
        cout<<ans<<endl;
    }
    return 0;
}
```




解释在代码里，（题中找突破点，就可以有思路了）

 

*N* (1 ≤ *N* ≤ 100) cows, conveniently numbered 1..*N*, are participating in a programming contest. As we all know, some cows code better than others. Each cow has a certain constant skill rating that is unique among the competitors.

The contest is conducted in several head-to-head rounds, each between two cows. If cow *A* has a greater skill level than cow *B* (1 ≤ *A* ≤ *N*; 1 ≤ *B* ≤ *N*; *A* ≠ *B*), then cow *A* will always beat cow *B*.

Farmer John is trying to rank the cows by skill level. Given a list the results of *M* (1 ≤ *M* ≤ 4,500) two-cow rounds, determine the number of cows whose ranks can be precisely determined from the results. It is guaranteed that the results of the rounds will not be contradictory.

Input

* Line 1: Two space-separated integers: *N* and *M* * Lines 2..*M*+1: Each line contains two space-separated integers that describe the competitors and results (the first integer, *A*, is the winner) of a single round of competition: *A* and *B*

Output

* Line 1: A single integer representing the number of cows whose ranks can be determined 　

Sample Input

```
5 5
4 3
4 2
3 2
1 2
2 5
```


Sample Output

```
2```


 

 

 

 

 

```cpp
/*s u意思为对应编号的牛
若s能打败u就令map[s][u]=1，否则map[s][u]=负无穷（可以理解为路不通）
初始化：map数组所有都为负无穷 map[i][i]=0
输入数据  s u证明s能打败u 令map[s][u]=1
那么所有数据输入完成后就构成一个图，在这个图中只看s到u的路径      
若存在一条路使得这条路所有权值之和>0 证明s能打败u（等于0表明这是
同一个牛）（并且s->u有路与u->s有路 不能同时存在，否则就有歧义了） 

那么我们选s到u的路径肯定选能确定s与u关系即map[s][u]>=0,
这样我们用floyd来找所有两个牛之间的最长”路径“，若这个最长路径>=0 表明s能击败u 即s u关系确定
如果两个牛的关系确定就有map[s][u]>=0成立 或者map[u][s]>=0成立,


一个牛的等级确定也就说明这条牛与其他所有牛的强弱关系都确定了,即这个牛与其他所有牛都存在上面的关系，

这样遍历n个牛就可以知道有几个牛的等级确定。


此代码时间复杂度：o{(n^3)(Floyd)+n*(2n)(遍历关系)}
*/

#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
#define N 100
#define INF -99999999
using namespace std;
int map[N+10][N+10];
int main()
{
    int n,m,a,b,cnt,sign;//floyd//找最长路径
    scanf("%d %d",&n,&m);
    for(int i=1; i<=n; i++) //init map
        for(int j=1; j<=n; j++)
            map[i][j]=INF;
    for(int i=1; i<=n; i++)
        map[i][i]=0;
    for(int i=1; i<=m; i++)
    {
        scanf("%d %d",&a,&b);//a b的关系确定
        map[a][b]=1;
    }
    for(int k=1; k<=n; k++) //通过第K个刷新最长的
        for(int i=1; i<=n; i++)
            for(int j=1; j<=n; j++)
            {
                if(map[i][k]+map[k][j]>map[i][j])
                   map[i][j]=map[i][k]+map[k][j];
            }
    cnt=0;
    for(int i=1;i<=n;i++)
    {
        sign=0;
        for(int j=1;j<=n;j++)
        {
            if(map[i][j]>=0||map[j][i]>=0)
            {
                 sign++;
                 continue;
            }
            break;
        }
        if(sign==n)
            cnt++;
    }
    printf("%d\n",cnt);
}
```


 

 



 

题目：

You have just moved from a quiet Waterloo neighbourhood to a big, noisy city. Instead of getting to ride your bike to school every day, you now get to walk and take the subway. Because you don't want to be late for class, you want to know how long it will take you to get to school. You walk at a speed of 10 km/h. The subway travels at 40 km/h. Assume that you are lucky, and whenever you arrive at a subway station, a train is there that you can board immediately. You may get on and off the subway any number of times, and you may switch between different subway lines if you wish. All subway lines go in both directions.

Input

Input consists of the x,y coordinates of your home and your school, followed by specifications of several subway lines. Each subway line consists of the non-negative integer x,y coordinates of each stop on the line, in order. You may assume the subway runs in a straight line between adjacent stops, and the coordinates represent an integral number of metres. Each line has at least two stops. The end of each subway line is followed by the dummy coordinate pair -1,-1. In total there are at most 200 subway stops in the city.

Output

Output is the number of minutes it will take you to get to school, rounded to the nearest minute, taking the fastest route.

Sample Input

```
0 0 10000 1000
0 200 5000 200 7000 200 -1 -1 
2000 600 5000 600 10000 600 -1 -1```


Sample Output

```
21```


 

 

 

 

题目大意：

先输入两个点的坐标是self and School的坐标

然后输入一系列的坐标，其中以-1 -1结尾的表示之前的坐标是在一个地铁线上，地铁的运行速度是40km/h.

坑点：

1.输入数据是距离单位是m，让你求的时间的单位是分钟。而题中的速度是km/h，所以需要转化一下

2.在同一地铁线上，两个地铁站不能直接建造“地铁线路”，因为这两点的地铁线路可能是折线（到另一个地铁站必须按照地铁的线路去），当然两个地铁站之间可以选择步行到达。

3.最扯淡的也就是数据的输入方式。看完输入就搜博客去了,,ԾㅂԾ,,

 

题解：

将所有坐标都编上号1~n 其在同一条线路上的地铁都将坐标用一个相同的特征元素标记（那么不同地铁线上的特种元素标记的值肯定不同），然后求任意两个点坐标直接通过所用的时间，最后用dijkstra求1->2的最短时间即可（数据要四舍五入）。

 

 

```cpp
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
#define N 250
#define INF 0x7fffffff
using namespace std;
const double vb=10.0*1000/60.0;//Step   速度  m/分钟
const double vs=40.0*1000/60.0;//Subway 速度  m/分钟
double map[N][N],dis[N];//从i到j所用的时间
int book[N];
struct node {
    int  x,y,k;//K为特征元素
}point[N]; //把位置看成点 //结构体下标就是点的编号
double _distant(double x1,double y1,double x2,double y2)
{
    x1=x1-x2;
    y1=y1-y2;
    return sqrt(x1*x1+y1*y1);
}
void dijkstra(int n)
{
    int t=n-1,u;
    double mid,minn;
    while(t--)
    {
        minn=INF;
        for(int i=1;i<=n;i++)
        {
            if((!book[i])&&dis[i]<minn)
            {
                minn=dis[i];
                u=i;
            }
        }
        book[u]=1;
        if(u==2)
            return ;
        for(int i=1;i<=n;i++)
        {
            mid=dis[u]+map[u][i];
            if(mid<dis[i])
                dis[i]=mid;
        }
    }
}
int main()
{
    int cnt=1,k=1;//k表示不同的种类数//同一种类的是在同一线路上
    double mid;
    scanf("%d %d",&point[cnt].x,&point[cnt].y);
    point[cnt++].k=k++;
    scanf("%d %d",&point[cnt].x,&point[cnt].y);
    point[cnt++].k=k++;
    while(~scanf("%d %d",&point[cnt].x,&point[cnt].y))//   cnt=3   k=3
    {
        point[cnt++].k=k;
        while((scanf("%d %d",&point[cnt].x,&point[cnt].y))&&point[cnt].x!=-1)
            point[cnt++].k=k;
        k++;
//        if(k==5)
//            break;
    }//共cnt-1个点  其k相同的就是在同一线路上的 从一开始编号的
    cnt--;
//    printf("cnt=%d\n",cnt);
    for(int i=1;i<=cnt;i++)
        for(int j=1;j<=cnt;j++)
            map[i][j]=INF;
    for(int i=1;i<=cnt;i++)
            map[i][i]=0;
    for(int i=1;i<=cnt;i++)
    {
        for(int j=i+1;j<=cnt;j++)//求编号为i的到编号为J的时间
        {
            mid=_distant(point[i].x,point[i].y,point[j].x,point[j].y);
            if(point[i].k==point[j].k&&(j==i+1))//一条地铁线上且相邻的点
                mid=mid/vs;
            else
                mid=mid/vb;
            if(mid<map[i][j])
                map[i][j]=map[j][i]=mid;
        }
    }
//用于测试数据查看map内数据
/*
    for(int i=0;i<=cnt;i++)
        printf("%5d  ",i);
    printf("\n");
    for(int i=1;i<=cnt;i++)
    {
        printf("%5d  ",i);
        for(int j=1;j<=cnt;j++)
        {
            printf("%5.1lf  ",map[i][j]);
        }
         printf("\n");
    }
*/
     for(int i=1;i<=cnt;i++)//记录1到其他点的时间
        dis[i]=map[1][i];
      book[1]=1;
      dijkstra(cnt);
//      for(int i=1;i<=cnt;i++)
//          printf("dis[%d]=%.2lf\n",i,dis[i]);
      printf("%.0lf\n",dis[2]);
}```


参考博客：[https://www.cnblogs.com/Sunshine-tcf/p/5752027.html](https://www.cnblogs.com/Sunshine-tcf/p/5752027.html)

 



 

年轻的探险家来到了一个印第安部落里。在那里他和酋长的女儿相爱了，于是便向酋长去求亲。酋长要他用10000个金币作为聘礼才答应把女儿嫁给他。探险家拿不出这么多金币，便请求酋长降低要求。酋长说："嗯，如果你能够替我弄到大祭司的皮袄，我可以只要8000金币。如果你能够弄来他的水晶球，那么只要5000金币就行了。"探险家就跑到大祭司那里，向他要求皮袄或水晶球，大祭司要他用金币来换，或者替他弄来其他的东西，他可以降低价格。探险家于是又跑到其他地方，其他人也提出了类似的要求，或者直接用金币换，或者找到其他东西就可以降低价格。不过探险家没必要用多样东西去换一样东西，因为不会得到更低的价格。探险家现在很需要你的帮忙，让他用最少的金币娶到自己的心上人。另外他要告诉你的是，在这个部落里，等级观念十分森严。地位差距超过一定限制的两个人之间不会进行任何形式的直接接触，包括交易。他是一个外来人，所以可以不受这些限制。但是如果他和某个地位较低的人进行了交易，地位较高的的人不会再和他交易，他们认为这样等于是间接接触，反过来也一样。因此你需要在考虑所有的情况以后给他提供一个最好的方案。 为了方便起见，我们把所有的物品从1开始进行编号，酋长的允诺也看作一个物品，并且编号总是1。每个物品都有对应的价格P，主人的地位等级L，以及一系列的替代品Ti和该替代品所对应的"优惠"Vi。如果两人地位等级差距超过了M，就不能"间接交易"。你必须根据这些数据来计算出探险家最少需要多少金币才能娶到酋长的女儿。

Input

输入第一行是两个整数M，N（1 <= N <= 100），依次表示地位等级差距限制和物品的总数。接下来按照编号从小到大依次给出了N个物品的描述。每个物品的描述开头是三个非负整数P、L、X（X < N），依次表示该物品的价格、主人的地位等级和替代品总数。接下来X行每行包括两个整数T和V，分别表示替代品的编号和"优惠价格"。

Output

输出最少需要的金币数。

Sample Input

```
1 4
10000 3 2
2 8000
3 5000
1000 2 1
4 200
3000 2 1
4 200
50 2 0
```


Sample Output

```
5250```


 

 

题目中文的这都不解释了(￣▽￣)"。

 

 

分析：输入数据，假设你想要u，可以用v来换u但是还得多加钱数为money，那么就建立一条边v->u，边上的权为money

数量。

那么这条边的意思就是用v再加上money才能换到u。

又因为每个物品都有自己的编号，所以建立一系列这样的边从而形成一个图。（等级的限制问题一会就说）

 

 

我再加入一个“超级源点“（这是其他人说的，但是挺超级的）x ，设其编号为0

x->u的边权为u的价钱，那么重新生成的这个图。我们求0到1的最短路径即可。（等级限制的问题呢？，别急下面就说）

 

 

```cpp
/*

题中  不同等级之间交易限制的问题，是个难处理的地方。
为了方便处理可以枚举每种可能性，然后从中找出答案
每次枚举编号中的其中一个，假设它为0->1最短路中等级最低
的一个人物v，那么在找最短路上，必须保证交易的过程中
每个的等级都可以与v交易，且等级都大于v(前面说了v等级最低)，否则不能交易（INF）
然后求0->1（0作为超级源点）的最短路径-----（这个交易过
程中满足题目要求）

又因为在答案的最短路中一定存在最低等级的人物v，使这条
交易线上的都满足这样的关系，那么从枚举的最短路径中选出最小的就
是我们要的答案
*/

#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<math.h>//
#define N 110
#define INF 0x3fffffff
using namespace std;
int map[N][N],dis[N],rankk[N],book[N],m;//对应编号的等级
bool check(int a)//a->b等级之间能否交易//把超级源点0的等级比作此次最短路路径的最低等级
{
    if(rankk[a]<rankk[0]||(rankk[a]>rankk[0]+m))
        return 0;
    return 1;
}
void dijkstra(int n)
{
    int t=n;
    int minn,u,mid;
    while(t--)
    {
        minn=INF;
        for(int i=0;i<=n;i++)
        {
            if(!book[i]&&dis[i]<minn)
            {
                minn=dis[i];
                u=i;
            }
        }
        book[u]=1;
        if(!u)
            return ;
        for(int i=0;i<=n;i++)
        {
            if(!check(i))
              continue;
            mid=dis[u]+map[i][u];
            if(mid<dis[i])
                dis[i]=mid;
        }
    }
}
int main()
{
    int n,money,rr,tt,num,ans;
    scanf("%d %d",&m,&n);//共n个物品
    for(int i=0;i<=n;i++)
        for(int j=i+1;j<=n;j++)
           map[i][j]=map[j][i]=INF;
    for(int i=1;i<=n;i++)//表示这个物品的编号，
    {
        scanf("%d %d %d",&money,&rr,&tt);
        map[0][i]=money;//超级源点
        rankk[i]=rr;//第i的物品拥有者的等级是rr
        while(tt--)
        {
            scanf("%d %d",&num,&money);
            map[num][i]=money;
        }
    }
   ans=INF;
   for(int k=1;k<=n;k++)
   {
       rankk[0]=rankk[k];
       if(!check(1))//容易忽略的点... 当1与此人物的等级不能满足交易关系时，表明此次交易就不可能会成功，continue
         continue;
       for(int i=0;i<=n;i++)//update
       {
           book[i]=0;
           if(check(i))
            dis[i]=map[i][1];
           else
            dis[i]=INF;
       }
       dis[1]=0;
       book[1]=1;
       dijkstra(n);
       ans=dis[0]<ans?dis[0]:ans;
   }
    printf("%d\n",ans);
}
```


  

参考博客:[https://www.cnblogs.com/yinzm/p/5937219.html](https://www.cnblogs.com/yinzm/p/5937219.html)



此博文不具体给出其算法的代码，只对其中算法进行分并且给予证明

PS：这些算法我不用证明都是它是正确的（上世纪的数学家看着这些都不用证明，为啥，很简单的），但是我坚持重新证明一遍实际是为了加深印象，并且理解其中的道理和思想，这样在以后的运用中才能灵活运用，当然证明这些算法也



**算法一：Floyd 算法，也是传说中的只用五行就可以解决的多源最短路径问题**

采用邻接矩阵来储存图，时间复杂度为O（n^3），能解决含正权，负权的最短路径，不能解决含有负**环**的最短路径（负环也没有最短路径）



```cpp
for(k=1;k<=n;k++)
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
            if(e[i][j]>e[i][k]+e[k][j])
                 e[i][j]=e[i][k]+e[k][j];```








**当k=1时进行一个嵌套的for循环求出来的是任意两点之间只允许经过点1的最短路径，这个都可以理解吧。**

**(**￣▽￣)"

**当k=2时，经过一个if else的判断最终求出来的是任意两个顶点之间只允许经过1 2号顶点的最短路径。**

这时候可能有人说在进行 if      else 之后判断的是i->j通过2号顶点路径后路径能否缩小，那么如果i->j还能通过1号顶点再次缩小路径，那还能体现出来吗？

好的下面咱们来证明

假设咱们判断过之后i->j之间通过2号顶点可以缩小路径，此时i与j的路径为i->2->j，假设还可以通过1号顶点缩小路径（也就是上面所说的情况）

此时1号顶点肯定在i->j之间，也就是i->2或2->j之间 ，**而咱们在第一次for循环之后的意义上面已经说过了，即任意两点可以经过1号顶点后更新的最短路径**，那么回过来即i->2之间或者2->j之间若可以经过1号顶点在缩短路径，那么铁定在第一次循环后就已经在i->2或2->j之间添加1号顶点了，所以上面的担心是多余的(●'◡'●)

当k=2的循环结束后，得到的意义便是任意两个顶点只允许经过1 2号顶点的最短路径

</



**待更新..........**

题目：

In the age of television, not many people attend theater performances. Antique Comedians of Malidinesia are aware of this fact. They want to propagate theater and, most of all, Antique Comedies. They have printed invitation cards with all the necessary information and with the programme. A lot of students were hired to distribute these invitations among the people. Each student volunteer has assigned exactly one bus stop and he or she stays there the whole day and gives invitation to people travelling by bus. A special course was taken where students learned how to influence people and what is the difference between influencing and robbery. The transport system is very special: all lines are unidirectional and connect exactly two stops. Buses leave the originating stop with passangers each half an hour. After reaching the destination stop they return empty to the originating stop, where they wait until the next full half an hour, e.g. X:00 or X:30, where 'X' denotes the hour. The fee for transport between two stops is given by special tables and is payable on the spot. The lines are planned in such a way, that each round trip (i.e. a journey starting and finishing at the same stop) passes through a Central Checkpoint Stop (CCS) where each passenger has to pass a thorough check including body scan. All the ACM student members leave the CCS each morning. Each volunteer is to move to one predetermined stop to invite passengers. There are as many volunteers as stops. At the end of the day, all students travel back to CCS. You are to write a computer program that helps ACM to minimize the amount of money to pay every day for the transport of their employees.

Input

The input consists of N cases. The first line of the input contains only positive integer N. Then follow the cases. Each case begins with a line containing exactly two integers P and Q, 1 <= P,Q <= 1000000. P is the number of stops including CCS and Q the number of bus lines. Then there are Q lines, each describing one bus line. Each of the lines contains exactly three numbers - the originating stop, the destination stop and the price. The CCS is designated by number 1. Prices are positive integers the sum of which is smaller than 1000000000. You can also assume it is always possible to get from any stop to any other stop.

Output

For each case, print one line containing the minimum amount of money to be paid each day by ACM for the travel costs of its volunteers.

Sample Input

```
2
2 2
1 2 13
2 1 33
4 6
1 2 10
2 1 60
1 3 20
3 4 10
2 4 5
4 1 50```


Sample Output

```
46
210```


 

推荐博客：[https://www.cnblogs.com/liuxin13/p/4656746.html](https://www.cnblogs.com/liuxin13/p/4656746.html)

 

 

```cpp
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
#include<queue>
#define N 1000000
#define INF 0x03ffffffffffffff;
using namespace std;
struct node{
    int u,v,w,next;
}e[N+10];
int head[N+10],book[N+10];
long long dis[N+10],sum[N+10];//book表示该顶点有没有进入队列
void Add(int u,int v,int w,int k)//将特征元素为u的连接到一条链上，并且将对应结构体数据改为从u松弛的
{
    e[k].u=u;
    e[k].v=v;
    e[k].w=w;
    e[k].next=head[u];
    head[u]=k;
}
void spfa_quick()
{
    int u,k;//u松弛  k实现链表
    long long mid;
    queue<int>mmp;
    mmp.push(1);//将松弛点加入队列
    book[1]=1;
    while(!mmp.empty())
    {
        u=mmp.front();
        k=head[u];
        while(k!=-1)//遍历链上的数据//k为此时链上的下标
        {
            mid=dis[e[k].u]+e[k].w;
            if(mid<dis[e[k].v])
            {
                dis[e[k].v]=mid;
                if(!book[e[k].v])
                {
                    mmp.push(e[k].v);
                    book[e[k].v]=1;
                }
            }
            k=e[k].next;
        }
        mmp.pop();
        book[u]=0;
    }
}
int main()
{
    int t,n,m,u,v,w;
    long long ans;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&n,&m);
        for(int i=1;i<=n;i++)//
            head[i]=-1;
        for(int i=1;i<=m;i++)
        {
            scanf("%d %d %d",&u,&v,&w);
            Add(u,v,w,i);
        }
        for(int i=1;i<=n;i++)
        {
            dis[i]=INF;
            book[i]=0;
        }
        dis[1]=0;
        spfa_quick();
        for(int i=1;i<=n;i++)//存下去的路径 初始化head  初始化DIS
        {
//            printf("1->i dis[%d]=%d\n",i,dis[i]);
            sum[i]=dis[i];
            dis[i]=INF;
            head[i]=-1;
        }
        dis[1]=0;
        for(int i=1;i<=m;i++)//填上表
            Add(e[i].v,e[i].u,e[i].w,i);
//        printf("atter.....\n");
        spfa_quick();
        for(int i=1;i<=n;i++)//此时就计算好总路径1到i的来回路径最小和
        {
//            printf("i->1  dis[%d]=%d\n",i,dis[i]);
             sum[i]+=dis[i];
        }
        ans=0;
        for(int i=2;i<=n;i++)
            ans+=sum[i];
        printf("%lld\n",ans);
    }
}
```


 

 

