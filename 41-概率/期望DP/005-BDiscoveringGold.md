

### B - Discovering Gold


You are in a cave, a long cave! The cave can be represented by a **1 x N** grid. Each cell of the cave can contain any amount of gold.

Initially you are in position **1**. Now each turn you throw a perfect **6** sided dice. If you get **X** in the dice after throwing, you add **X** to your position and collect all the gold from the new position. If your new position is outside the cave, then you keep throwing again until you get a suitable result. When you reach the **Nth** position you stop your journey. Now you are given the information about the cave, you have to find out the **expected** number of gold you can collect using the given procedure.

**Input**

Input starts with an integer **T (****≤ 100)**, denoting the number of test cases.

Each case contains a blank line and an integer **N (1 ≤ N ≤ 100)** denoting the dimension of the cave. The next line contains **N** space separated integers. The **ith** integer of this line denotes the amount of gold you will get if you come to the **ith** cell. You may safely assume that all the given integers will be non-negative and no integer will be greater than **1000**.

**Output**

For each case, print the case number and the expected number of gold you will collect. Errors less than **10-6** will be ignored.

**Sample Input**


3

1

101

2

10 3

3

3 6 9


**Sample Output**


Case 1: 101.0000000000

Case 2: 13.000

Case 3: 15


### 题意：


有n个格子，编号分别是1~N,每个格子下面有黄金，每到一个格子就掷骰子，掷到的点数就是你下一次跳跃的距离，骰子的有6面，点数分别为1~6,每次掷的点数是等概率的，如果你掷色子使你跳到第N格外面，则重新掷骰子。问到达n点的所获得黄金的期望是多少？

### 分析：



$不能简单的用DP[i]代表1到i的期望$ 如果对之有疑问请看下面，否则建议跳过

$用dp[n]代表1到n点所获的期望的话，则不能单纯的让前置位置的期望加上该点的黄金再乘以的到该状态的概率.$



对于$dp[j]$,$j$的每个前置顶点$i$加进来的期望为$dp[j]+=(w[1~to~i]+val[i\ to\ j ])*P(1\ to\ i)*P(i\ to \ j)$

$而P(1\ to\ i)!=1$ ,$因为1去的方向最终点不全在i点，即所有可能的最终点不在i出，$


$用dp[i]代表i到n点的期望，那么dp[i]的求法:$

$dp[i]=\sum _{j}(val[i]+dp[j])*P(i\ to\ j)​$

$注意\ P(i\ to\ j)的求法即可$

```cpp
#include<cstdio>
#include<algorithm>
using namespace std;
const int maxn=1e2+10;
int val[maxn];
double dp[maxn];
int main()
{
    int t,n,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;++i)
            scanf("%d",val+i);
        dp[n]=val[n];
        int tot=0;
        for(int i=n-1;i>0;--i)
        {
            tot=min(i+6,n)-i;//可供选择的个数
            dp[i]=val[i];
            for(int j=i+tot;j>i;--j)
                dp[i]+=1.0/tot*dp[j];
        }
        printf("Case %d: %.6f\n",++cas,dp[1]);
    }
}

```


##如果用DP[i]表示1到i的期望，则代码这样写

```cpp
include<cstdio>
#include<algorithm>
using namespace std;
const int maxn=1e2+10;
int val[maxn];
double dp[maxn];
double pp[maxn];
int main()
{
    int t,n,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;++i)
            scanf("%d",val+i);
        int tot;
        dp[1]=val[1];
        pp[1]=1;
        for(int i=2;i<=n;++i)
        {
            dp[i]=0;
            pp[i]=0;
            for(int j=max(i-6,1);j<i;j++)
            {
                 tot=min(j+6,n)-j;
                 dp[i]+=(dp[j]+val[i]*pp[j])*1.0/tot;
                 pp[i]+=pp[j]*1.0/tot;
            }
        }
        printf("Case %d: %.6f\n",++cas,dp[n]);
    }
    return 0;
}
```


