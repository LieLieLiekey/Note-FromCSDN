

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


