

### [B - Minimum](https://vjudge.net/problem/HihoCoder-1586)


[HihoCoder - 1586 ](https://vjudge.net/problem/1087342/origin)

题意： 一段序列支持两种操作：

+ 1.Output $Min _{x,y∈[l,r]} (ax,ay)$.+ 2.Let $a_x=y$.


思路：

​ 维护区间最大值，最小值即可。假设区间$[l,r]$的中最大值为 $max$和最小值为 $min$ 那么根据其的正负性四种答案有四种可能。

+ max为$+$，min为 $+$. 那么答案$ans=min*min$+ max为$+$，min为 $-$. 那么答案$ans=max*min$+ max为$-$，min为 $+$. 那么答案$ans=max*min$+ max为$-$，min为 $-$. 那么答案$ans=max*max$


代码：（略丑，请不要介意…）

```cpp
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#define mset(a,b) memset(a,b,sizeof(a))
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
using namespace std;
typedef long long ll;
const ll maxn=150000;
const ll inf=0x3f3f3f3f;
/*
线段树维护区间最大值 最小值
1.查询
2.修改 push_up
*/
struct Node{
    ll max,min;
}node[maxn<<2];
ll val[maxn];
void push_up(ll rt){
    node[rt].max=max(node[rt<<1].max,node[rt<<1|1].max);
    node[rt].min=min(node[rt<<1].min,node[rt<<1|1].min);
}
void buliding(ll l,ll r,ll rt)
{
    node[rt].max=-1*inf;
    node[rt].min=inf;
    if(l==r){
        node[rt].max=node[rt].min=val[l];
        return ;
    }
    ll m=(l+r)/2;
    buliding(lson);
    buliding(rson);
    push_up(rt);
}
void inserting(ll id,ll k,ll l,ll r,ll rt)//把id的值变为k
{
    if(l==r&&l==id){
        node[rt].max=node[rt].min=k;
        return ;
    }
    ll m=(l+r)/2;
    if(id<=m)
        inserting(id,k,lson);
    if(id>=m+1)
        inserting(id,k,rson);
    push_up(rt);
}
Node querying(ll L,ll R,ll l,ll r ,ll rt)
{
    if(L<=l&&R>=r){
        return node[rt];
    }
    ll m=(l+r)/2;
    ll maxx=-1*inf,minn=inf;
    if(L<=m){
        Node mid=querying(L,R,lson);
        maxx=max(maxx,mid.max);
        minn=min(minn,mid.min);
    }
    if(R>m){
        Node mid=querying(L,R,rson);
        maxx=max(maxx,mid.max);
        minn=min(minn,mid.min);
    }
    Node ans;ans.max=maxx,ans.min=minn;
    return ans;
}
int main(){
    ll t,n,q,kind,a,b;
    scanf("%lld",&t);
    while(t--){
        scanf("%lld",&n);
        ll top=1<<n;
        for(ll i=0;i<top;++i)
            scanf("%lld",val+i);
        buliding(0,top-1,1);
        scanf("%lld",&q);
        while(q--){
            scanf("%lld%lld%lld",&kind,&a,&b);
            if(kind==1){
                Node mid=querying(a,b,0,top-1,1);
                ll maxx=mid.max;
                ll minn=mid.min;
                ll ans=min(maxx*maxx,min(maxx*minn,minn*minn));
                printf("%lld\n",ans);
            }
            else{
                inserting(a,b,0,top-1,1);
            }
        }
    }
    return 0;
}

```


