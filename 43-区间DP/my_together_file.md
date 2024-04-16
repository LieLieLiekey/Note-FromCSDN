

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


 



## [SCU - 4441 ](https://vjudge.net/problem/184145/origin) 环形dp+树状数组优化


## Necklace


frog has nn gems arranged in a cycle, whose *beautifulness* are a1,a2,…,ana1,a2,…,an. She would like to remove some gems to make them into a *beautiful necklace* without changing their relative order.

Note that a *beautiful necklace* can be divided into 3 consecutive parts X,y,Z where


+ XX consists of gems with non-decreasing *beautifulness*,
+ yy is **the only** *perfect gem*. (A *perfect gem* is a gem whose *beautifulness* equals to 1000010000)
+ ZZ consists of gems with non-increasing *beautifulness*.



Find out the maximum total *beautifulness* of the remaining gems.

### Input


The input consists of multiple tests. For each test:

The first line contains 1 integer n ($1 ≤ n ≤ 1 0 5 1≤n≤10^5$). The second line contains nnintegers a1,a2,…,an a1,a2,…,an. ($0 ≤ a i ≤ 1 0 4 , 1 ≤ n u m b e r   o f   p e r f e c t g e m s ≤ 10 0≤ai≤10^4,1≤number~of~perfect gems≤10$).

### Output


For each test, write 11 integer which denotes the maximum total remaining *beautifulness*.

### Sample Input


```bash
    6
    10000 3 2 4 2 3
    2
    10000 10000
```


### Sample Output


```bash
    10010
    10000
```


### 题意：


N个数构成一个环，现在可以删除一些数，使得这个环可以分成连续的三部分：

X部分：所有数不降

Y部分：仅含一个值为10000的数

Z部分：所有数不增

### 思路：


​ 大体思路就是枚举每个10000的点，再枚举中间的每个端点，求10000右边的非递增序列最大和，求10000左边的非递减序列最大和。但是我们可以把这个数组复制成原来的两倍，那么$i d id$ 的复制品 $i d + n id+n$ 之间的就是环的其他部分，我们可以用树状数组求每个端点从左边开始的非递增序列最大和 **以及** 每个端点从右边开始向左边的非递增序列最大和,时间复杂度为O（nllogn）。最后O(n)枚举分裂点求最大即可

### AC代码：


```cpp
#include<bits/stdc```


