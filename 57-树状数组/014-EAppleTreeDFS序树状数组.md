

### [E - Apple Tree](https://vjudge.net/problem/POJ-3321)


[POJ - 3321 ](https://vjudge.net/problem/10486/origin)

题意：

​ 一颗苹果树，刚开始所有节点都有苹果，有以下两种操作，一种是改变一个节点的状态（有苹果就取走，没苹果就产生一个），一种是询问一个点的子树（包括节点自己）一共有多少个苹果，对于每次询问输出结果

分析：

```bash
重新DFS序给节点标号，那么没个节点的子孙就对应一个连续的区间。那么修改点的状态相当于单点修改，查询操作相当于区间求和，树状数组和线段树都可以写。
```


注：POJ存树图用vector超时

```cpp
#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
const ll MAX=100000;
ll DS[MAXN],L[MAXN],R[MAXN];//顶点u对应的区间为[L,R],u的虚拟节点为DS[u]
ll book[MAXN],tot,ecnt;
ll bt[MAXN],sw[MAXN];
int head[MAXN];
struct Edge{
 int v,to;
}edge[MAXN<<1];
void addEdge(int u,int v,int ed)
{
    edge[ed].v=v;
    edge[ed].to=head[u];
    head[u]=ed;
}
void dfs(ll u)
{
    tot++,book[u]=1;
    DS[u]=tot,L[u]=tot;
    int to=head[u];
    while(to!=-1)
    {
        int v=edge[to].v;
        to=edge[to].to;
        if(book[v]) continue;
        dfs(v);
    }
    R[u]=tot;
}
/*
重现构造搜索序列
*/
ll lowbit(ll k)
{
    return k&-k;
}
void modify(ll k,ll val)
{
    while(k<=MAX){
        bt[k]+=val;
        k+=lowbit(k);
    }
}
ll getsum(ll k)
{
    ll ans=0;
    while(k>0)
    {
        ans+=bt[k];
        k-=lowbit(k);
    }
    return ans;
}
char s[10];
int main(){
    ll n;
    scanf("%lld",&n);
    ecnt=0ll;
    mset(head,-1);
    for(ll i=0;i<n-1;++i){
        ll u,v;
        scanf("%lld%lld",&u,&v);
        addEdge(u,v,ecnt++);
        addEdge(v,u,ecnt++);
    }
    tot=0;
    dfs(1);
    for(ll i=1;i<=n;++i)
        modify(i,1);
    ll q;
    scanf("%lld",&q);
    while(q--)
    {
        scanf("%s",s);
        if(s[0]=='Q'){
            ll u;
            scanf("%lld",&u);
            printf("%lld\n",getsum(R[u])-getsum(L[u]-1));
        }
        else{
            ll u;
            scanf("%lld",&u);
            if(sw[u]==1){
                sw[u]=0;
                modify(DS[u],1);
            }
            else{
                sw[u]=1;
                modify(DS[u],-1);
            }
        }
    }
    return 0;
}

```


