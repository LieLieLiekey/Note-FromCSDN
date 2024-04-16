

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


