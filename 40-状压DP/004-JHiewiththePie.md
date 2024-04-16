

### J - Hie with the Pie


The Pizazz Pizzeria prides itself in delivering pizzas to its customers as fast as possible. Unfortunately, due to cutbacks, they can afford to hire only one driver to do the deliveries. He will wait for 1 or more (up to 10) orders to be processed before he starts any deliveries. Needless to say, he would like to take the shortest route in delivering these goodies and returning to the pizzeria, even if it means passing the same location(s) or the pizzeria more than once on the way. He has commissioned you to write a program to help him.

**Input**

Input will consist of multiple test cases. The first line will contain a single integer *n* indicating the number of orders to deliver, where 1 ≤ *n* ≤ 10. After this will be *n* + 1 lines each containing *n* + 1 integers indicating the times to travel between the pizzeria (numbered 0) and the *n* locations (numbers 1 to *n*). The *j*th value on the *i*th line indicates the time to go directly from location *i* to location *j* without visiting any other locations along the way. Note that there may be quicker ways to go from *i* to *j* via other locations, due to different speed limits, traffic lights, etc. Also, the time values may not be symmetric, i.e., the time to go directly from location *i* to *j* may not be the same as the time to go directly from location *j* to *i*. An input value of *n* = 0 will terminate input.

**Output**

For each test case, you should output a single number indicating the minimum time to deliver all of the pizzas and return to the pizzeria.

**Sample Input**


3 0 1 10 10 1 0 1 2 10 1 0 10 10 2 10 0 0


**Sample Output**


8


### 题意：


从0端点到n个端点送外卖，存在一条路径，使得从0开始经过n个端点后回到0端点，所走的最短距离是多少，每个顶点可以走多次。

### 思路：


$用dp[state][j],二进制代表以0为端点，走state的状态，到j的最短距离是多少,其中state对应的二进制为1代表回路中经过该端点$

枚举前继状态，从端点c过来，暴力找出最小值即可，不过在前继状态加上c到j的距离时，需要floyd计算任意两点的最短路径

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
const int maxn=15;
const int branch=26;
const int inf=0x3f3f3f3f;
const int mod=1e8;
int mm[maxn][maxn];
int dp[1<<11][maxn];//dp[i][j] 代表状态i下 ，0到j的最短距离是多少。对应位为1代表图中有他（不带端点）
int main()
{
    int n;
    while(~scanf("%d",&n)&&n)
    {
        for(int i=0;i<=n;++i)
            for(int j=0;j<=n;++j)
                scanf("%d",mm[i]+j);
        for(int k=0;k<=n;++k)
            for(int i=0;i<=n;++i)
                for(int j=0;j<=n;++j)
                    if(mm[i][j]>mm[i][k]+mm[k][j])
                        mm[i][j]=mm[i][k]+mm[k][j];
        //初始化0 状态i下0到点i的最短距离
        mset(dp,inf);
        for(int i=0;i<=n;++i)
        {
            dp[1<<(i)][i]=mm[0][i];
        }
        int tot=1<<(n+1);
        for(int i=0;i<tot;++i)
        {
            for(int v=0;v<=n;++v)
            {
                if((i&(1<<v))==0)//v在这个状态中 必须存在
                    continue;
                for(int s=0;s<=n;++s)
                {
                    if((i&(1<<s))==0)//从s点到这个状态，那么s点必须在i梭子啊状态中，s不能为起始点（这也是初始化的原因吧）
                        continue;
                    //dp[i][s]过来或者dp[i^(1<<v)][s]过来  花费都为m[s][v]
                    int val=min(dp[i][s],dp[i^(1<<v)][s])+mm[s][v];
                    if(val<dp[i][v])
                        dp[i][v]=val;
                }
            }
        }
        cout<<dp[tot-1][0]<<endl;
    }
    return 0;
}
```


