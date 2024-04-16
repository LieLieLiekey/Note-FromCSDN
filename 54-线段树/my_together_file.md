

## [HihoCoder - 1710 ](https://vjudge.net/problem/1456411/origin)


给定N个整数A1, A2, … AN，小Hi会询问你M个问题。

对于每个问题小Hi给出两个整数L和R(L ≤ R)，请你找出[AL, AL+1, AL+2, … AR]中最长的等差连续子数列，并输出其长度。

例如[2, 3, 5, 7, 9]中最长的等差连续子数列是[3, 5, 7, 9]长度为4。

Input


第一行包含两个整数N和M。

第二行包含N个整数A1, A2, … AN。

以下M行每行包含两个整数L和R，代表一次询问。

对于30%的数据，1 ≤ N, M ≤ 1000

对于100%的数据，1 ≤ N, M ≤ 100000 0 ≤ Ai ≤ 10000000


Output


依次对于每个询问输出一个整数，代表答案。


Sample Input

```bash
6 2  
1 2 3 5 7 9  
2 6  
1 4
```


Sample Output

```bash
4  
3
```


### 思路：


​ 一下这么多查询操作大概就是线段树题吧。这里假设$m a x l [ i ] maxl[i]$ 是第以$i i$个数结尾的$1 1$~$i i$最长连续等差序列长度。

那么求$[ l ， r ] [l，r]$ 中最大连续等差序列长度可以用下列方式来求。


+ 找$[ l ， r ] [l，r]$ 中$m a x l maxl$最大的值并记录其对应的id.
+ 如果$ maxl[id]>(id-l+1)$的 长 度 ， 说 明 该 的长度，说明该$id$的 贡 献 只 能 为 的贡献只能为$(id-l+1)$,然后将该贡献与[id,r]中的最大值比较后取其中最大的即可。
+ 否则$m a x l [ i d ] &lt; = ( i d − l + 1 ) maxl[id]&lt;=(id-l+1)$





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


