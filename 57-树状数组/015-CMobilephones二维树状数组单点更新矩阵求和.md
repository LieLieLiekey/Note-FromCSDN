## [C - Mobile phones](https://vjudge.net/problem/POJ-1195)（二维树状数组）

 

[POJ - 1195 ](https://vjudge.net/problem/17086/origin)

题意：对一个$n*n$的矩阵进行一些操作和查询，操作：单点修改。查询：求子矩阵元素和

思路：

​	真没想到二维的树状数组是这样的。（真不知道二维线段树应该怎么维护，期待(☆▽☆)！  ）

构建二维树状数组之后我们可以求$i,j$左上角矩阵的和 。求子矩阵可以转化为多个左上角矩阵元素和的加减。

> 二维树状数组的第二维(也就是行向量代表的节点吧)之间的关系，跟一维向量的 节点之间关系相同。
>
> 看博文：<https://blog.csdn.net/chaiwenjun000/article/details/47973737>



```cpp
#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1050;
const ll MAX=1025;
ll bt[MAXN][MAXN];
ll lowbit(ll k)
{
    return k&-k;
}
ll getsum(ll de,ll k)//高度为de，的第k个元素左上角和
{
    ll ans=0;
    for(;de>0;de-=lowbit(de))
        for(int kk=k;kk>0;kk-=lowbit(kk))
            ans+=bt[de][kk];
    return ans;
}
void modify(ll de,ll k,ll val)
{
    for(;de<=MAX;de+=lowbit(de))
        for(int kk=k;kk<=MAX;kk+=lowbit(kk))
           bt[de][kk]+=val;;
}
ll calc(int l,int w,int r,int h)
{
    ll ans=getsum(h,r)-getsum(w-1,r)-getsum(h,l-1)+getsum(w-1,l-1);
    return ans;
}
int main(){
    ll n,cm;
    scanf("%lld %lld",&cm,&n);
    while(scanf("%lld",&cm),cm!=3)
    {
        if(cm==1)
        {
            ll x,y,val;
            scanf("%lld%lld%lld",&x,&y,&val);
            ++x,++y;
            modify(y,x,val);
        }
        else
        {
            ll l,r,w,h;
            scanf("%lld%lld%lld%lld",&l,&w,&r,&h);
            ++l,++w,++r,++h;
            printf("%lld\n",calc(l,w,r,h));
        }//
    }
}
```
