

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


