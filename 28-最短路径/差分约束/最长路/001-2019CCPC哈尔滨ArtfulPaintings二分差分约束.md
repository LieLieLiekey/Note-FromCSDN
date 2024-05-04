# 2019CCPC哈尔滨Artful Paintings（二分+差分约束）

题目链接：[传送门](<https://codeforces.com/gym/102394/problem/A>)

思路：

> 这题现场赛的时候TLE了，赛后才发现spfa可以剪枝，而且还缺少一约束。

我们假设答案是k，那么k+1也可行，所以可行性具有单调性。设函数S( i )为前 i 个cube画的个数。

那么有约束

- $1\ge S(i)-S(i-1)\ge0$
- 对于第一种条件，$S(r)-S(l-1)\ge k$
- 对于第二种条件，$S(n)-S(r)+S(l-1)\ge k$

因为对于第二种条件， $S(n)$的值不确定，所以不能直接建立差分约束图。但是因为可行性对于$S(n)$的值有单调性，所以我们二分$S(n)$ 的值，就能用差分约束系统来check 的可行性，从而求出$S(n)$的最小值。

但是要注意的是，假设此时令$S(n)=w$，然后检查可行性的时，需要增加约束$S(n)=w$。另外没有剪纸的差分约束是会TLE的(根据图的性质进行剪纸)，但是建图（建最短图的话）后我们发现所有点都有到0有一条费用为0的路径，所以一旦存在某个u 使得 $dis[u]<0$，那么必定有负环。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=3e3+10;
const int inf=0x3f3f3f3f;
struct Node
{
    int l,r,k;
} q1[N],q2[N];
int n,k1,k2;
int dis[N],in[N];//距离
struct Edge{
    int to,w;
    Edge() {};
    Edge(int to,int w):to(to),w(w) {}
};
vector<Edge> g[N];//邻接表
bool book[N];//标记是否够在队列
bool spfa(int s,int n)//源点为s,共有(0..n)n个点,求最短路
{
    //有负环返回true，无负环返回false
    queue<int> qe;
    fill(dis,dis+n,inf);
    fill(in,in+n,0);
    fill(book,book+n,false);
    dis[s]=0;
    qe.push(s);
    book[s]=true;
    while(!qe.empty())
    {
        int u=qe.front();
        qe.pop();
        in[u]++;
        book[u]=false;
        if(dis[u] < 0 ) return true;
        if(in[u] > n) return true;
        for(Edge &e:g[u])
        {
            int v=e.to,w=e.w;
            if(dis[v]>dis[u]+w)
            {
                dis[v]=dis[u]+w;
                if(!book[v])
                {
                    book[v]=true;
                    qe.push(v);
                }
            }
        }
    }
//    puts("no circle");
    return false;
}
bool check(int mv)//无环返回true
{
//    printf("mv:%d\n",mv);
    for(int i=0; i<=n; ++i) g[i].clear();
    for(int i=1; i<=k1; ++i)
    {
        int u=q1[i].r,v=q1[i].l-1,w=-q1[i].k;
        g[u].push_back(Edge(v,w));
    }
    for(int i=1;i<=n;++i){
         g[i].push_back(Edge(i-1,0));
         g[i-1].push_back(Edge(i,1));
    }
    for(int i=1; i<=k2; ++i)
    {
        int u=q2[i].l-1,v=q2[i].r,w=mv-q2[i].k;
        g[u].push_back(Edge(v,w));
    }
    g[0].push_back(Edge(n,mv));
    g[n].push_back(Edge(0,-mv));
    return !spfa(0,n+1);
}
int main()
{
    int T;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&n,&k1,&k2);
        for(int i=1; i<=k1; ++i)
            scanf("%d%d%d",&q1[i].l,&q1[i].r,&q1[i].k);
        for(int i=1; i<=k2; ++i)
            scanf("%d%d%d",&q2[i].l,&q2[i].r,&q2[i].k);
        int ans=-1,l=0,r=n;
        while(l<=r)
        {
            int m=(l+r)/2;
            if(check(m))
            {
                ans=m;
                r=m-1;
            }
            else
                l=m+1;
        }
        printf("%d\n",ans);
    }
}
```
