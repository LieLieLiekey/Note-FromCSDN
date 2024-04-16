

Every day, farmer Ion (this is a Romanian name) takes out all his horses, so they may run and play. When they are done, farmer Ion has to take all the horses back to the stables. In order to do this, he places them in a straight line and they follow him to the stables. Because they are very tired, farmer Ion decides that he doesn't want to make the horses move more than they should. So he develops this algorithm: he places the 1st P 1 horses in the first stable, the next P2 in the 2nd stable and so on. Moreover, he doesn't want any of the K stables he owns to be empty, and no horse must be left outside. Now you should know that farmer Ion only has black or white horses, which don't really get along too well. If there are i black horses and j white horses in one stable, then the coefficient of unhappiness of that stable is i*j. The total coefficient of unhappiness is the sum of the coefficients of unhappiness of every of the K stables. Determine a way to place the N horses into the K stables, so that the total coefficient of unhappiness is minimized.

Input

On the 1st line there are 2 numbers: **N** (1 ≤ N ≤ 500) and **K** (1 ≤ K ≤ N). On the next N lines there are N numbers. The i-th of these lines contains the color of the i-th horse in the sequence: 1 means that the horse is black, 0 means that the horse is white.

Output

You should only output a single number, which is the minimum possible value for the total coefficient of unhappiness.

Example

    
inputoutput 
```
6 3
1
1
0
1
0
1
```
  
```
2
```
 
  

 

**题意**：

有n匹马，k个马厩，让n匹马有顺序的进入马厩。

共有两种不同毛色的马用0 1表示，其中不同毛色的马在一起会有不满意度产生，值为两种马的数量乘积。

怎样一种进去方式使得总不满意度最小。

**大致意思**：

n匹马排着队，用k-1个隔板让他们分成k个区域，每个区域最少有一匹马，给你这个顺序的马的颜色，求出最小不满意度之和。

代码：

```cpp
/*动态规划解法
dp[i][j]表示前j的马放进i个马厩的最小不满意度
unfun(i,j)为i到j的不满意度
1.归纳条款(递推关系)
dp[i][j]=[i,j]之间的一个t，dp[i][j]=(for t->[i,j])min(dp[i-1][t-1]+unfun(t,j))
2.基础条款(初始条件,即为了使i=1时成立)
dp[0][0]=0 ,dp[0][j]=INF;


枚举所有i，找出j找出dp[k][n]==ans
*/
#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<cstdlib>
#include<queue>
using namespace std;
typedef long long ll;
const int maxn=550;
const int INF=0x3f3f3f3f;
int a[maxn],b[maxn],dp[maxn][maxn];
int unfun(int i,int j)//i j的不满意度，保证i<=j
{
    if(i>j)
        return INF;
    return (a[j]-a[i-1])*(b[j]-b[i-1]);
}
int main()
{
    int n,k,val;
    while(~scanf("%d %d",&n,&k))
    {
        a[0]=b[0]=0;
        for(int i=1; i<=n; i++)
        {
            scanf("%d",&val);
            a[i]=a[i-1];
            b[i]=b[i-1];
            if(val)
                b[i]++;
            else
                a[i]++;
        }
        dp[0][0]=0;
        for(int i=1; i<=n; i++)
            dp[0][i]=INF;
        for(int i=1; i<=k; i++)
            for(int j=i; j<=n; j++)
            {
                int minn=INF;
                for(int t=i; t<=j; t++)//t的意思为t之前的马在i-1个槽子内
                {
                    int to=dp[i-1][t-1]+unfun(t,j);//
                    minn=min(minn,to);

                }//找出所有可能求出i  j的最小值为dp[i][j]
                dp[i][j]=minn;
            }
        printf("%d\n",dp[k][n]);
    }
    return 0;
}```


 

