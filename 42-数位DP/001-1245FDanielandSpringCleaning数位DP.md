

## 1245F. Daniel and Spring Cleaning(数位DP)


##### 题目链接：[传送门](https://codeforces.com/problemset/problem/1245/F)


##### 题意：


给出$l,r​$，让求满足$a\in[l,r],b\in[l,r]​$ 且$a⊕b=a+b​$ 的$(a,b)​$对数。

##### 思路：


如果$a⊕b=a+b$ 那么有$a\&b=0$，我们用$f(l,r)$代表满足$a\in[0,l],b\in[0,r]$且满足$a\&b=0$的个数，那么题目等效于求$f(r,r)-f(l-1,r)-f(r,l-1)+f(l-1,l-1)$的值。


这种问题我就没往数位DP上想过。但是用数位DP处理起来真的是太巧妙了。

相似的题目链接：[牛客2019多校pair](https://ac.nowcoder.com/acm/contest/887/H)


因为位运算只与对应的位有关，前后的位无关系，所以我们可以用数位DP来解决这个问题。

为了求$f(l,r)$，我们先让$l,r$进行二进制分解，假设最低位是第1位，最高位为31位（因为 $l,r$ 是在int的数据范围内）。

我们用$dp[k][limt1][limt2]$ 来代表当前满足处理到 $k$ 位，此时 $l$ 和 $r$ 是否是顶位的满足条件的个数。处理到第k位时，前面的必定满足对应的位数**且运算**的值为0。然后我们枚举当前状态下两个数的第k位的所有情况dp即可。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll dp[50][2][2];//dp[k][limt][limt] a&b=0
int ar[50],br[50];//[31...1]  top->down
ll dfs(int k,int limt1,int limt2)
{
    if(k==0)
        return 1;
    if(dp[k][limt1][limt2]!=-1) return dp[k][limt1][limt2];
    int up1=limt1?ar[k]:1;
    int up2=limt2?br[k]:1;
    ll ans=0;
    for(int i=0;i<=up1;++i)
    {
        for(int j=0;j<=up2;++j)
        {
            if((i&j)!=0) continue;
            ans+=dfs(k-1,limt1&&i==up1,limt2&&j==up2);
        }
    }
    return dp[k][limt1][limt2]=ans;
}
ll solve(ll a,ll b)
{
    if(a<0||b<0) return 0;
    mset(dp,-1);
    for(int i=1;i<=31;++i)
    {
        ar[i]=a&1;
        a>>=1;
        br[i]=b&1;
        b>>=1;
    }
    return dfs(31,1,1);
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        ll a,b;
        cin>>a>>b;
        cout<<solve(b,b)-2*solve(a-1,b)+solve(a-1,a-1)<<endl;
    }
    return 0;
}
```


