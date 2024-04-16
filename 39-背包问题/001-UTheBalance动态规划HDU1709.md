

### U - The Balance


**Now you are asked to measure a dose of medicine with a balance and a number of weights. Certainly it is not always achievable. So you should find out the qualities which cannot be measured from the range [1,S]. S is the total quality of all the weights.**

**Input**

The input consists of multiple test cases, and each case begins with a single positive integer N (1<=N<=100) on a line by itself indicating the number of weights you have. Followed by N integers Ai (1<=i<=N), indicating the quality of each weight where 1<=Ai<=100.

**Output**

For each input set, you should first print a line specifying the number of qualities which cannot be measured. Then print another line which consists all the irrealizable qualities if the number is not zero.

**Sample Input**

```bash
3
1 2 4
3
9 2 1
```


**Sample Output**

```bash
0
2
4 5
```


题意：

给你n个砝码，sum是n个砝码的重量之和，在此区间[1,sum]有多少个重量不能用天平称出来，输出个数，并输出这些不能称出来的质量

分析：

dp[i][j]表示只用前i个砝码称出 j 这个质量的方案数目

因为第i个砝码可以选择不放，也可以选择放一侧，或者对立的一侧

所以

$$dp[i][j]=dp[i-1][j]+dp[i-1][j-val[i]]+dp[i-1][j+val[i]]+dp[i-1][val[i]-j]$$



```cpp
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<stack>
#include<vector>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=2e4+10;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
int dp[130][maxn],vis[130];
int n,maxx;
int mmp[maxn],top;
void solve()
{
    mset(dp,0);
    dp[0][0]=1;
    for(int i=1;i<=n;++i)//可以使用第i中硬币下
    {
        for(int j=0;j<=maxx;++j)
        {
            dp[i][j]=dp[i-1][j];
            if(j>=vis[i])//加上去
                dp[i][j]+=dp[i-1][j-vis[i]];
            dp[i][j]+=dp[i-1][j+vis[i]];//把这个硬币放在对面
            if(vis[i]-j>=0)//把这个硬币放在对面
                dp[i][j]+=dp[i-1][vis[i]-j];
        }
    }
    top=0;
    for(int i=1;i<=maxx;++i)
        if(!dp[n][i])
           mmp[top++]=i;
    printf("%d\n",top);
    for(int i=0;i<top;++i)
        printf("%d%c",mmp[i],(i==top-1)?'\n':' ');
}
int main()
{
    while(~scanf("%d",&n))
    {
        maxx=0;
        for(int i=1;i<=n;++i)
        {
            scanf("%d",vis+i);
            maxx+=vis[i];
        }
        solve();
    }
    return 0;
}
```


