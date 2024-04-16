

#### zzuli2520: 大小接近的点对（CCPC河南省省赛） 离线处理+DFS遍历树+树状数组


### 思路：


​ 我们可以利用$DFS$序，统计子树中与该节点权值相差为$k$的个数，这个范围是一个区间。

$DFS$序遍历树，进入一个节点的时候记录符合条件的个数记作$cntf$，然后树状数组添加该节点信息，$DFS$遍历儿子即可。(注意，遍历过程中不撤销节点信息)

离开该节点时记录符合条件的个数记作$cntb$。那么$cntb-cntf$ 就是该节点与子树符合条件的个数。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll maxn=1e5+10;
ll MAX=1e5+5;
ll X[maxn],sa[maxn],XX[maxn];
ll Sum[maxn],bt[maxn],tot;
vector<ll> adja[maxn];
ll n,K;
ll lowbit(ll k)
{
    return k&-k;
}
void modify(ll k)
{
    while(k<=MAX)
    {
        bt[k]+=1;
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
void dfs(ll u)
{
    ll l,r;
    l=lower_bound(XX,XX+tot,X[u]-K)-XX;
    r=upper_bound(XX,XX+tot,X[u]+K)-XX-1;
    ll cntf=getsum(r)-getsum(l-1);
    modify(sa[u]);
    ll sum=0;
    for(ll i=0;i<adja[u].size();++i)
    {
        ll v=adja[u][i];
        dfs(v);
        sum+=Sum[v];
    }
    ll cntb=getsum(r)-getsum(l-1);
    Sum[u]=sum+cntb-cntf;
}
int main()
{
    scanf("%lld%lld",&n,&K);
    XX[0]=0;
    for(ll i=1;i<=n;++i)
        scanf("%lld",&X[i]),XX[i]=X[i];
    for(ll i=2;i<=n;++i)
    {
        ll fa;
        scanf("%lld",&fa);
        adja[fa].push_back(i);
    }
    sort(XX,XX+1+n);
    tot=unique(XX,XX+1+n)-XX;
    MAX=tot;
    for(ll i=1;i<=n;++i)
        sa[i]=lower_bound(XX,XX+tot,X[i])-XX;
    dfs(1);
    for(ll i=1;i<=n;++i)
        printf("%lld\n",Sum[i]);
    return 0;
}

```


