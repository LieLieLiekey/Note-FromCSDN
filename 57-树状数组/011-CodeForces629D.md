

### H - Babaei and Birthday Cake CodeForces - 629D


[https://vjudge.net/contest/301590#problem/H](https://vjudge.net/contest/301590#problem/H)

题意：

​ 有n个蛋糕，从1编号到n，现在用这些蛋糕制作一个大蛋糕，要求编号大的蛋糕必须放在编号小的蛋糕上面，且上面的蛋糕的体积必须严格大于下面蛋糕的体积，问能制作出的大蛋糕的最大体积

思路：

​ 每次找出面积比他小的堆起来的最大蛋糕面积即可。找的过程可以将所有面积离散化，然后用树状数组查找（线段树，map都可以实现）。

​ 且面积之间的累加和比较可以用$h*r*r$ 来表示。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
const ll MAX=100000;
const ll inf=0x3f3f3f3f;
const double PI=acos(-1);
ll n;
ll sa[MAXN],X[MAXN];//离散化后的sa  原来的X
ll XX[MAXN],dp[MAXN],bt[MAXN];
ll lowbit(ll k)
{
    return k&-k;
}
void modify(ll k,ll val)
{
    while(k<=MAX)
    {
        bt[k]=max(bt[k],val);
        k+=lowbit(k);
    }
}
ll getmax(ll k)
{
    ll ans=0;
    while(k>0)
    {
        ans=max(ans,bt[k]);
        k-=lowbit(k);
    }
    return ans;
}
int main()
{
    ll n,r,h;
    scanf("%lld",&n);
    XX[0]=X[0]=sa[0]=dp[0]=0;
    for(ll i=1;i<=n;++i)
    {
        scanf("%lld%lld",&r,&h);
        X[i]=h*r*r;
        XX[i]=X[i];
    }
    sort(XX,XX+1+n);
    ll tot=unique(XX,XX+1+n)-XX;
    for(ll i=1;i<=n;++i)
        sa[i]=lower_bound(XX,XX+tot,X[i])-XX;
    for(ll i=1;i<=n;++i){
        dp[i]=X[i]+getmax(sa[i]-1);
        modify(sa[i],dp[i]);
    }
    ll maxx=0;
    for(ll i=1;i<=n;++i)
    {
        maxx=max(maxx,dp[i]);
    }
    printf("%.10f\n",double(maxx)*PI);
    return 0;
}

```


