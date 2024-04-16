

### LOJ 1265-Snakes and Ladders（期望DP+高斯消元）


##### 题目链接：[传送门]([LightOJ - 1151](https://vjudge.net/problem/26865/origin))



其实这道题并不难，写下这篇博客的目的是纪念这种做法，当期望DP方程的递推关系拓扑图有环时，我们可以用高斯消元的方法去做（因为每一个位置都可以列一个方程，且都线性无关，所以可以用高斯消元解方程）


##### 题意：


有$100$个方格，其中从左到右编号依此为 $1$ 到 $100$，现在我们有一个6个面的骰子，我们每次掷骰子，得到多少点数当前就会跳几个格子，比如我们现在在$1$号格子，点数为 $5$，那么我们就会直接跳到$6$号点。

除了掷骰子外，格子上有 $m$ 个传送关系，表示为$(a,b)$，且 $a\ne b$，传送关系的作用是，如果你到了 $a$ 号点，那么你必须会被传送到 $b$ 号点。

现在我们的初始位置是 $1$ ，且给出$m$个传送关系，问到达位置$100$的掷骰子的期望次数是多少？需要注意的是，如果掷骰子后将要跳跃的位置超过$100$时，需要重新再掷骰子，直到将要跳跃的位置不超过$100$时停止。

##### 思路：


众所周知，期望DP倒着求（容易求）。

我们用$dp[i]$表示 $i$ 号格子到终点掷骰子的期望次数。

+  如果 $i$ 号点有传送且传送到$tp[i]$：$dp[i]=dp[tp[i]]$ +  否则：令$k=(100-i,6)$，$dp[i]=\frac{1}{6}*\sum_{j=1} ^{k}dp[i+j]+\frac{6-k}{6}*dp[i]+1$ 然后化简后得出$dp[i]$的表达式即可。 


因为$tp[i]$ 可能小于 $i$ ，所以我们不能单纯的从后往前$dp$。我们考虑将$dp[i]$设为第 $i$ 个未知数，则可以建立100个有100个未知数的一次方程，然后高斯消元进行求解即可。

**代码**：

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=1e5+10;
const double eps=1e-7;
double g[105][105],ans[105];
bool Gauss(int n)
{
    //A*x=B
    for(int i=1;i<=n;++i)
    {
        int r=i;
        for(int j=i+1;j<=n;++j) if(fabs(g[r][i])<fabs(g[r][j])) r=i;
        if(fabs(g[r][i]) < eps) return false;
        swap(g[i],g[r]);
        double div=g[r][i];
        for(int j=i;j<=n+1;++j) g[i][j]/=div;
        for(int j=i+1;j<=n;++j)
        {
            div=g[j][i];
            for(int p=i;p<=n+1;++p) g[j][p]-=div*g[i][p];
        }
    }
    ans[n]=g[n][n+1];
    for(int i=n-1;i>=1;--i)
    {
        ans[i]=g[i][n+1];
        for(int j=i+1;j<=n;++j) ans[i]-=g[i][j]*ans[j];
    }
    return true;
}
int to[105];//传送关系
int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int m,n=100;
        scanf("%d",&m);
        fill(to+1,to+n+1,0);
        for(int i=1;i<=m;++i)
        {
            int a,b;
            scanf("%d%d",&a,&b);
            to[a]=b;//a可以传送到to[a]
        }
        for(int i=1;i<=n;++i)
            for(int j=1;j<=n+1;++j) g[i][j]=0.0;//初始化高斯消元矩阵
        g[n][n]=1.0;//终点的方程
        g[n][n+1]=0.0;
        for(int i=1;i < n;++i)
        {
            if(to[i])
            {
                g[i][i]=1;
                g[i][to[i]]=-1;
                g[i][n+1]=0.0;
            }
            else
            {
                int k=min(6,100-i);
                g[i][i]=1;
                for(int j=1;j<=k;++j)
                    g[i][i+j]=-1.0/k;
                g[i][n+1]=6.0/k;
            }
        }
        Gauss(n);
        printf("Case %d: %.9f\n",++cas,ans[1]);
    }
    return 0;
}

```


