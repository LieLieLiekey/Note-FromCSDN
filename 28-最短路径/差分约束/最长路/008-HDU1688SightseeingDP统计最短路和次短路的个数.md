

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


