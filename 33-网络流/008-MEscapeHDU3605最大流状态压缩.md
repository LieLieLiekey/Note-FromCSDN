

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


 

