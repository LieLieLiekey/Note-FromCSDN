

### G - Corn Fields


Farmer John has purchased a lush new rectangular pasture composed of *M* by *N* (1 ≤ *M*≤ 12; 1 ≤ *N* ≤ 12) square parcels. He wants to grow some yummy corn for the cows on a number of squares. Regrettably, some of the squares are infertile and can’t be planted. Canny FJ knows that the cows dislike eating close to each other, so when choosing which squares to plant, he avoids choosing squares that are adjacent; no two chosen squares share an edge. He has not yet made the final choice as to which squares to plant.

Being a very open-minded man, Farmer John wants to consider all possible options for how to choose the squares for planting. He is so open-minded that he considers choosing no squares as a valid option! Please help Farmer John determine the number of ways he can choose the squares to plant.

**Input**

Line 1: Two space-separated integers: *M* and *N* Lines 2… *M*+1: Line *i*+1 describes row *i* of the pasture with *N* space-separated integers indicating whether a square is fertile (1 for fertile, 0 for infertile)

**Output**

Line 1: One integer: the number of ways that FJ can choose the squares modulo 100,000,000.

**Sample Input**

```bash
2 3
1 1 1
0 1 0
```


**Sample Output**

```bash
9
```


**Hint**

Number the squares as follows:

```bash
1 2 3
  4  
```


There are four ways to plant only on one squares (1, 2, 3, or 4), three ways to plant on two squares (13, 14, or 34), 1 way to plant on three squares (134), and one way to plant on no squares. 4+3+1+1=9.

### 题意：


牛吃草，给你一个m*n规格的地方，1的地方为草，0的地方为空地，现在要建造围栏，围栏必须建在草上，且围栏不能上下左右相邻。

### 分析：


暴力出所有情况即可，数位dp的入门题，用n位数的二进制代表这一行围栏放的情况，$d[r][state]$为第 r 行状态为state的方法数，计算该方法数的时候 暴力枚举上一行所有的状态，如果状态兼容，则可以有这种状态，上一行状态的方法数即可。

$dp[r][state]表示只考虑前r行兼容，第r行状态为state的方法数，然后dp即可，得到dp[m][state]求和即是答案$

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
const ll  mod=1e8;
int w[15];
ll dp[15][1<<12];
int state[1<<12],tot;
char hhh()
{
    char c=getchar();
    while(c==' '||c=='\n')
        c=getchar();
    return c;
}
int main()
{
    int m,n;
    scanf("%d%d",&m,&n);
    for(int i=1; i<=m; ++i)
    {
        w[i]=0;
        for(int j=0; j<n; ++j)
        {
            w[i]<<=1;
            if(hhh()=='1')
                w[i]+=1;
        }
    }
    tot=0;
    for(int i=0; i<(1<<n); ++i)//预处理出肯定的一行可能的状态
    {
        if(((i<<1)&i)==0)//1 1不能相邻
            state[tot++]=i;
    }
    mset(dp,0);
    for(int i=0; i<tot; ++i)//预处理第一行
    {
        if((state[i]&w[1])==state[i])
            dp[1][i]=1;
    }
    for(int r=2; r<=m; ++r)
    {
        for(int i=0; i<tot; ++i)
        {
            if((state[i]&w[r])==state[i])
            {
                for(int j=0; j<tot; ++j)
                {
                    if(((state[j]&w[r-1])==state[j])&&(state[i]&state[j])==0)
                    {
                        dp[r][i]+=dp[r-1][j];
                    }

                }
                dp[r][i]%=mod;
            }

        }
    }
    ll ans=0;
    for(int i=0;i<tot;++i)
    {
        ans=(ans+dp[m][i])%mod;
    }
    cout<<ans<<endl;
    return 0;

}
```


