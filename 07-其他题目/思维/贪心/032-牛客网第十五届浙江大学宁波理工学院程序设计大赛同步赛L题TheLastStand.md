

## 牛客网第十五届浙江大学宁波理工学院程序设计大赛（同步赛）


[The Last Stand](https://ac.nowcoder.com/acm/contest/303/L)

题意不在描述

分析：

简单dp

​ dp[i]表示经过第i个点时候的最大能量（不选）

那么

$dp[i]=max(dp[j]+val[j]+(pos[i]-pos[j])*delta[j]), 0&lt;=j&lt;i$

初始令

val[0]=h,delta[0]=0;dp[0]=h

求dp[n+1]即可

```cpp
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<map>
#include<vector>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e3+10;
const int branch=26;
const int inf=0x3f3f3f3f;
ll pos[maxn],val[maxn],delta[maxn];
ll dp[maxn];
int main()
{
    int n,ans,h,t,pp,m,vv,dd;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d %d",&n,&m,&h);
        mset(dp,0);
        for(int i=1; i<=n; ++i)
            scanf("%lld %lld %lld",pos+i,val+i,delta+i);
        pos[0]=0;
        val[0]=0;
        delta[0]=0;
        dp[0]=h;
        pos[n+1]=m;
        val[n+1]=0;
        delta[n+1]=0;
        for(int i=0; i<=n+1; ++i)
        {
            for(int j=0; j<i; ++j)
            {
                if(dp[j]+val[j]>0)//走到这个点之前选择的是j这个点
                {
                    dp[i]=max(dp[i],dp[j]+(pos[i]-pos[j])*delta[j]+val[j]);
                }

            }
        }

        printf("%lld\n",dp[n+1]);
    }
    return 0;
}
```


