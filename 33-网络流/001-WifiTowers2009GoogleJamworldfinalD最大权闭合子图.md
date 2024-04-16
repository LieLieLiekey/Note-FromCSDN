

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


