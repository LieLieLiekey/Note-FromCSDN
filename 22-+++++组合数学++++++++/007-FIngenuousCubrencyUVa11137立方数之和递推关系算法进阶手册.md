

### [F - Ingenuous Cubrency](https://vjudge.net/problem/UVA-11137)


[UVA - 11137 ](https://vjudge.net/problem/19454/origin)

**题目描述** ：


​ 立方数之和。输入正整数n( n<=10000) ，求将n写成若干个正整数的立方和有多少种方法。

比如21有3种写法：21=13+13 …+13=23+13+13…13=23+23+13…13 。

77有22种写法，9999有440 022 018 293中写法。


**多组输入** ：


​ 每组输入一个n.


**输出描述** ：


​ 输出有多少种方法.


**分析** ：

​ 可以用多重背包写，也可以建立多段图（后者时间复杂度高），


多重背包

dp（i，j）表示最多不超过i，立方和为j的方法数目

初始状态：dp（0，0）=1

递推关系：dp （i，j）=dp（i-1，j）+dp（i，j - i*i*i*i ） (i>=1)


多段图：


初始状态：dp （0，0）=1

状态转移：对于每个dp（i，j） for k=0 to j+k*i*i*i<=maxn: dp（i，j+k*i*i*i）+=dp（i，j）

表示i，j这个状态可以加上一个i3 或者加上多个i3 转移到 i+1这个状态中


代码1：

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=10000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
ll dp[26][maxn+10];
void Preprocess()
{
    mset(dp,0ll);
    dp[0][0]=1;
    for(int i=1; i<=21; ++i) //最大不超过i
    {
        for(int j=0; j<=maxn; ++j) //递推关系  实际从dp[i-1]行求dp[i]行
        {
            dp[i][j]=dp[i-1][j];
            if(j-i*i*i>=0)
              dp[i][j]+=dp[i][j-i*i*i];
        }
    }
}
int main()
{
    int n;
    Preprocess();
    while(~scanf("%d",&n))
    {
        cout<<dp[21][n]<<endl;
    }
}
```


代码2：

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=10000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
ll dp[26][maxn+10];
void Preprocess()
{
    mset(dp,0);
    dp[0][0]=1;
    for(int i=1; i<=21; ++i)
    {
        for(int j=0; j<=maxn; ++j) //从 i-1  j状态转移
        {
            for(int a=0; j+a*i*i*i<=maxn; ++a)
            {

                dp[i][j+a*i*i*i]+=dp[i-1][j];
            }
        }
    }
}
int main()
{
    int n;
    Preprocess();
    while(~scanf("%d",&n))
    {
        cout<<dp[21][n]<<endl;
    }
}

```


