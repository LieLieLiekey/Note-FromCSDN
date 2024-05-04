# codeforces 1253 E. Antenna Coverage（DP）

#### 题意：

现有一个一维的OX轴，给出n个antenna，每个antenna的属性有$(x_i,r_i)$,代表该antenna 可以覆盖区间$[x_i-r_i,x_i+r_i]$，我们可以花费一个硬币使得某个antenna的 $r$ 增大1，问使区间$[1,m]$都被某个antenna覆盖所需最小花费。$n\in[1,80],m\in[1,2e5],x_i\in [1,m]$,

#### 思路：

因为所有antenna的中心都在$[1,m]$，所以我们在位置0处放一个半径为0的antenna答案不收影响，（因为位置0处的antenna覆盖到位置x，那么x+1位置必定被覆盖了，所以x+1位置必定能花费同样的硬币进行扩展到左边的位置1，我们覆盖位置$[1,x]$所需要的花费不会比之前坏）。我们用$dp[pos]$代表假设位置$pos$已经被覆盖了，那么覆盖$[pos,m]$所需的最小花费。

initial，$dp[m+1]=0$，我们接下来从大到小遍历$pos$,来求出$dp[]$，假设现在要求$dp[pos]$，那么我们枚举所有的电线杆。

- initial，$dp[pos]=1+dp[pos+1]$，代表从x-1位置扩展到x。

- 假设$x_i\ge pos​$，且$x_i-r_i\le pos​$，则$dp[pos]=min(dp[pos],dp[min(x_i+r_i+1,m+1)])​$

- 假设$x_i\ge pos​$，且$x_i-r_i> pos​$，

  则$dp[pos]=min(dp[pos],x_i-r_i-pos+dp[min(2*x_i-pos+1,m+1)])$

- 假设$x_i<pos$，且$x_i+r_i\ge pos$，则$dp[pos]=min(dp[pos],dp[min(x_i+r_i+1,m+1)])$
- 假设$x_i<pos$，且$x_i+r_i< pos$，则不是用这个扩展，因为从x-1处扩展到x的代价不会比这个坏。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e5+10;
const int inf=0x3f3f3f3f;
int dp[N];
int x[85],r[85];
int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1; i<=n; ++i)
    {
        scanf("%d%d",x+i,r+i);
    }
    dp[m+1]=0;
    for(int i=m; i>=1; --i)
    {
        int pos=i;
        dp[i]=1+dp[i+1];
        for(int j=1; j<=n; ++j)
        {
            int _x=x[j],_r=r[j];
            if(_x>=pos)
            {
                if(_x-_r<=pos){
                    dp[i]=min(dp[i],dp[min(m+1,_x+_r+1)]);
                }
                else{
                    dp[i]=min(dp[i],_x-_r-pos+dp[min(m+1,2*_x-pos+1)]);
                }
            }
            else
            {
                if(_x+_r>=pos){
                    dp[i]=min(dp[i],dp[min(m+1,_x+_r+1)]);
                }
            }
        }
    }
    printf("%d\n",dp[1]);
}

```
