

### H - Imperishable Night


After coding so many days,Mr Acmer wants to have a good [rest.So](http://rest.So) travelling is the best choice!He has decided to visit n cities(he insists on seeing all the cities!And he does not mind which city being his start station because superman can bring him to any city at first but only once.), and of course there are m roads here,following a fee as usual.But Mr Acmer gets bored so easily that he doesn’t want to visit a city more than twice!And he is so mean that he wants to minimize the total fee!He is lazy you [see.So](http://see.So) he turns to you for help.

**Input**

There are several test cases,the first line is two intergers n(1<=n<=10) and m,which means he needs to visit n cities and there are m roads he can choose,then m lines follow,each line will include three intergers a,b and c(1<=a,b<=n),means there is a road between a and b and the cost is of course c.Input to the End Of File.

**Output**

Output the minimum fee that he should pay,or -1 if he can’t find such a route.

**Sample Input**

```bash
2 1
1 2 100
3 2
1 2 40
2 3 50
3 3
1 2 3
1 3 4
2 3 10
```


**Sample Output**

```cpp
100
90
7 
```


### 题意：


现在有n个顶点，有m个边，每个边有相应的权值，要求每个顶点最多经过两次，要求经过n个顶点的权值和最小。如果不能经过n个点，则输出-1

### 分析：


每个顶点可以最多经过两次，$n$个顶点，用3进制数字$s$代表对应的顶点有没有经过，$0$代表没有经过，$1$代表经过一次，$2$代表此状态中该顶点经过$2$次，那么所有情况有$3^n$种，我们让该三进制数的最低位到最高位分别代表顶点$1到n$ ，那么我们要求的就是$3$进制数中$n$个位中状态都非$0$的形成这种状态的最小值。

因为每一个通路可以用一个状态和一个端点表示

所以用$dp[state][v]$代表状态state，且该路径的端点为$v$。这种情况所花费的最小值。

那么求$dp[state][v]$ 只需枚举连接$v$端点的另一个端点即可。

初始化：$dp[state(v)][v]=0$ ，其他都是$inf$，即只有端点v的状态的最小花费为$0$

又因为每种状态的值至于前面的状态有关，所以$for$循环 三进制的值从小到大遍历所有状态即可。最后找出满足条件的最小值即可

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
const int maxn=11;
const int branch=26;
const int inf=0x3f3f3f3f;
const int mod=1e8;
int mm[maxn][maxn];//存放地图
int dp[60000][maxn];
int a[maxn];//存放状态
int n,m;
int quick_pow(int a,int b)
{
    int ans=1;
    while(b)
    {
        if(b&1)
            ans=ans*a;
        a=a*a;
        b>>=1;
    }
    return ans;
}
int Add(int state,int v)//从state中增加v顶点的一次
{
    return state+quick_pow(3,v-1);
}
int Subtract(int state,int v)//从state中减去v顶点的一次数
{
    return state-quick_pow(3,v-1);
}
int getcnt(int state,int v)//得到state中 端点v的出现次数
{
    return (state/quick_pow(3,v-1))%3;
}
int judge(int state)//判断state是否符合条件
{
    for(int i=0;i<n;++i)
    {
        if(state%3==0)
            return 0;
        state/=3;
    }
    return 1;
}
int main()
{
    while(~scanf("%d %d",&n,&m))
    {
        mset(mm,inf);
        int u,v,w;
        for(int i=0;i<m;++i)
        {
            scanf("%d %d %d",&u,&v,&w);
            if(mm[u][v]>w)
                mm[u][v]=mm[v][u]=w;
        }
        /*开始状态转移 dp[state][r]，代表这个状态时statte，且改状态末尾的顶点是r,所花费的最小代价*/
        mset(dp,inf);
        for(int i=1;i<=n;++i)
        {
            dp[Add(0,i)][i]=0;
        }//初始化 刚开始的状态
        int tot=quick_pow(3,n);
        for(int i=0;i<tot;++i)//枚举状态
        {
            for(int j=1;j<=n;++j)//枚举now state
            {
                if(!getcnt(i,j))// out can't rule
                    continue;
                int sss=Subtract(i,j);// out the state
                for(int s=1;s<=n;++s)//enum last v
                {
                    if(!getcnt(sss,s)||mm[s][j]==inf||dp[sss][s]==inf)
                        continue;
                    dp[i][j]=min(dp[i][j],dp[sss][s]+mm[s][j]);
                }
            }
        }
        int minn=inf;
        for(int i=(quick_pow(3,n)-1)/2;i<tot;++i)
        {
            if(judge(i))
            {
                 for(int j=1;j<=n;++j)
                    minn=min(minn,dp[i][j]);
            }

        }
        if(minn==inf)
            printf("-1\n");
        else
            printf("%d\n",minn);
    }
    return 0;
}


```


