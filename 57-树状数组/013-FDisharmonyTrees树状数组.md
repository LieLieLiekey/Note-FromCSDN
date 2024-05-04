## [F - Disharmony Trees](https://vjudge.net/problem/HDU-3015)

 

[HDU - 3015 ](https://vjudge.net/problem/17589/origin)

#### **题意：**

​	对于n棵树，给出所在位置和高度，根据给出的规则算出每棵树的位置等级$xlev$和高度等级$hlev$

然后，定义f=两树之间的位置的那估计的绝对值，s=两树中最小的高度等级，求所有树之间f*s和。

#### 思路：



​	预处理把所有的树重新构造距离和高度熟属性，我们让所有树按照树的高度从高到低排序，那么每次求当前这个树与前面每个树的 Disharmony Value 即可，因为高度是从高到低，所以与前面每颗数计算的min(H1,H2)都为自己的高度。且求Disharmony Value操作可以优化到logn级别，假设前面的树的距离为aX，高度为aH，当前树的距离为X，高度为H，那么$abs(aX-X)*min(aH,H)=abs(aX-X)*H$

- 如果$aX>=X$  ： $abs(aX-X)*H=aX*H-X*H​$
- 否则：$abs(aX-X)*H=X*H-aX*H$

那么我们可以**统计当前所有的树满足$x>=X$ 的所有**距离和** 以及**个数**，以及当前满足$x<X$的所有**距离和** 以及**个数** 即可。然后加到答案上。

即用树状数组维护区间个数个区间和即可。



```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
ll MAX=1e5+1;
ll sx[MAXN],sh[MAXN];//数据的等级
ll X[MAXN],H[MAXN];//数据
ll n;
struct Node
{
    ll x,h;
} node[MAXN];
bool cmp(Node a,Node b)
{
    return a.h<b.h;
}
ll getxth(ll x)
{
    ll th=lower_bound(X,X+1+n,x)-X;
    return sx[th];
}
ll gethth(ll h)
{
    ll th=lower_bound(H,H+1+n,h)-H;
    return sh[th];
}
ll btt[MAXN],bts[MAXN];//对应节点出现的个数  和出现的X的和
ll book[MAXN],SUM,TOT;
ll lowbit(ll k)
{
    return k&-k;
}
void modify(ll k)
{
    ll val=k;
    while(k<=MAX)
    {
        btt[k]++;
        bts[k]+=val;
        k+=lowbit(k);
    }
}
pair<ll,ll> getinfo(ll k)//1~k 的个数为tot，他们的和为sum
{
    ll tot=0,sum=0;
    while(k>0)
    {
        tot+=btt[k];
        sum+=bts[k];
        k-=lowbit(k);
    }
    return make_pair(tot,sum);
}
void calc(ll l,ll r,ll &tot,ll &sum)
{
    pair<ll,ll> PA,PB;
    PB=getinfo(r);
    PA=getinfo(l-1);
    tot=PB.first-PA.first;
    sum=PB.second-PA.second;
}
int main()
{
    while(~scanf("%lld",&n))
    {
        X[0]=H[0]=0;
        sx[0]=sh[0]=0;
        MAX=-1;
        for(ll i=1; i<=n; ++i)
        {
            scanf("%lld%lld",X+i,H+i);
            node[i].x=X[i];
            node[i].h=H[i];
        }
        sort(X,X+n+1);
        sort(H,H+n+1);
        sort(node+1,node+1+n,cmp);
        for(ll i=1; i<=n; ++i)
        {
            if(X[i]==X[i-1])
                sx[i]=sx[i-1];
            else
                sx[i]=i;
            if(H[i]==H[i-1])
                sh[i]=sh[i-1];
            else
                sh[i]=i;
            MAX=max(MAX,sx[i]);
        }
        mset(btt,0);
        mset(bts,0);
        mset(book,0);
        ll ans=0;
        SUM=TOT=0;
        for(ll i=n; i>=1; --i) //h从大到小遍历, 找到当前比他小 和比他大的个数
        {
            ll xlev=getxth(node[i].x),hlev=gethth(node[i].h);
            TOT++;
            SUM+=xlev;
            modify(xlev);
            ll lstot,lssum,uptot,upsum;
            calc(1,xlev,lstot,lssum);
            uptot=TOT-lstot;
            upsum=SUM-lssum;
            ll mid=((lstot-uptot)*xlev+upsum-lssum)*hlev;
            ans+=((lstot-uptot)*xlev+upsum-lssum)*hlev;
        }
        printf("%lld\n",ans);
    }
    return 0;
}

```
