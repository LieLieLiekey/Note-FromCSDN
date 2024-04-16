

### Loj-1287 Where to Run（状压期望DP）


##### 题目链接：[LightOJ - 1287 ](https://vjudge.net/problem/26997/origin)


##### 题意：


​ 先给一个n个点m条无向边的图，每条边都有一个权值，顶点编号从0开始，刚开始自己站在0号点，现在要躲避警察的追踪。走的路线有如下限制：

+  离开一个顶点之后就不能回到该顶点 +  如果站在某个顶点u，**剩下的未走的邻接顶点不存在 E J 顶点就停止并被警察抓到**，E J 顶点指如果到该顶点后，满足条件1的情况下可以走完所有未走完的顶点。 如果存在E J顶点，则会进行如下**随机选择**，如果有k个E J顶点，那么有1/(k+1)的概率选择先停留原地5分钟（隐藏）或走剩下的E J 顶点。 +  如果走u到v这条边，则花费的时间为u到v这条边的权值。 


求从 $0$ 号顶点开始出发**躲避警察的时间的期望值**。

数据范围：$n\in[1,15],0\le u,v<n,0< w\le 100$

##### 思路：


​ 我们用$dp[s][u]​$代表经过的顶点状态是 $s​$ ,现在处于节点 $u​$ 的剩下的期望躲避时间，所以我们要求的就是$dp[1][0]​$


期间我一直在想怎么判断剩下的邻接顶点是E J顶点，期间想了各种方法，但都太麻烦且时间复杂度大。

实际上对于状态$(s,u)​$，我们用$cans[s][u]​$代表这个状态下从 $u​$ 开始能否遍历完其他未遍历完的顶点，判断状态$(s,u)​$中$u​$是否为为E J顶点只需判断可选的顶点中是否存在E J 顶点即可


形式化的，我们现在来求$cans[s][u]$，假设有边$(u,v)$，且状态$s$中未经过顶点$v$，那么如果$cans[s|(1<<v)][v]=true$，则$can[s][u]=true$

对于状态转移方程

假设状态$(s,u)​$可选的顶点有 $k​$ 个

+  如果 $k>0$: 对于状态$(s,u)$下u的所有邻接E J顶点$v$，且边权$w$，那么 $dp[s][u]=\frac{1}{k+1}*(dp[s][u]+5)+\frac{1}{k+1}*\sum _k (dp[s|(1<<v)][v]+w)$ $cans[s][u]=true$ +  否则： $dp[s][u]=0$ $cans[s][u]=false$ 


因为$dp$方程中 $s$ 是递增的，所以我们可以按照 $s$ 从大到小遍历，其次遍历$u$ 求$dp[s][u]$和$cans[s][u]$即可，特殊的满状态下$dp[s_{max}][u]=0,cans[s_{max}][u]=true$

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const double eps=1e-5;
typedef pair<int,int> P;
bool cans[1<<16][16];
double dp[1<<16][16];
vector<pair<int,int> > g[16];
int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0; i<=n; ++i) g[i].clear();
        for(int i=1; i<=m; ++i)
        {
            int u,v,w;
            scanf("%d%d%d",&u,&v,&w);
            g[u].push_back(make_pair(v,w));
            g[v].push_back(make_pair(u,w));
        }
        int top=(1<<n)-1;
        for(int s=top; s>=0; --s)
        {
            for(int u=0; u < n; ++u)
            {
                dp[s][u]=0;
                cans[s][u]=false;
                if(s==top)
                {
                    cans[s][u]=true;
                    continue;
                }
                if((s&(1<<u)) == 0) continue;
                int k=0;
                double sum=0.0;
                for(P &p:g[u])
                {
                    int v=p.first,w=p.second;
                    if((s&(1<<v))==0&&cans[s|(1<<v)][v])
                    {
                        k++;
                        sum+=dp[s|(1<<v)][v]+w;
                    }
                }
                if(k > 0)
                {
                    cans[s][u]=true;
                    dp[s][u]=(5.0+sum)/k;
                }

            }
        }
        printf("Case %d: %.8f\n",++cas,dp[1][0]);
    }
    return 0;
}
```




### LOJ-1284 Lights inside 3D Grid（期望，二次项公式奇数项求和）


##### 题目链接：[传送门](https://vjudge.net/problem/LightOJ-1284)


##### 题目：


在尺寸为$X*Y*Z$的长方体中每个位置都有一个灯泡，初始没有亮，每次随机取两个点$(x1,y1,z1)$,$(x2,y2,z2)$。让所有满足$x\in[x1,x2],y\in[y1,y2],z\in[z1,z2]$，的点的灯泡状态反转，问 $k$ 次操作后灯泡亮的个数期望值是多少？

##### 思路：


看到数据感觉枚举每个坐标比较实际，对于点$(x,y,z)$，我们用$g(x,y,z)$表示一次中命中点$(x,y,z)$的概率，$f(x,y,z)$表示一次没有点$(x,y,z)$的概率，所以$f(x,y,z)+g(x,y,z)=1.0$。

在$x\in[x1,x2],y\in[y1,y2],z\in[z1,z2]​$时该点才会被命中， 容易看出在维度$x​$被命中的概率为$1-\frac{(x-1)^2+(X-x)^2}{X^2}​$

，故$g(x,y,z)=(1-\frac{(x-1)^2+(X-x)^2}{X^2})*(1-\frac{(y-1)^2+(Y-y)^2}{Y^2})*(1-\frac{(z-1)^2+(Z-z)^2}{Z^2})​$ 。

设$a=f(x,y,z),b=g(x,y,z)​$，所以$k​$次后位置$(x,y,z)​$灯泡亮的概率为：

$$p=C_{k}^{1}*a^1*b^{k-1}+C_{k}^{3}*a^3*b^{k-3}+C_{k}^{5}*a^5*b^{k-5}...​$$



即$(a+b)^k$二项式张展开的奇数项的和，想起来怎么求了吗？

将奇数项的和设为$S1$,偶数项的和设为$S0$。

有$S0+S1=1$

接下来我们令$a'=-a$,那么$(a'+b)^k=(-a+b)^k=-S0+S1$

有这两个方程我们就能联立解出$S1$，即二次项展开的奇数项的和，即灯泡$(x,y,z)$经过 k 次后被命中的概率。

期望$E=\sum_p p*val$，就可以求出经过k次操作后所有灯泡中亮期望个数。

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const double eps=1e-5;
double g[110][110][110];
double getp(int k,int n)
{
    double m=((k-1)*(k-1)+(n-k)*(n-k))/(1.0*n*n);
    return 1.0-m;
}
int main()
{
    int t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        int X,Y,Z,k;
        scanf("%d%d%d%d",&X,&Y,&Z,&k);
        double ans=0.0;
        for(int a=1; a<=X; ++a)
        {
            double pa=getp(a,X);
            for(int b=1; b<=Y; ++b)
            {
                double pb=getp(b,Y);
                for(int c=1; c<=Z; ++c)
                {
                    double pc=getp(c,Z);
                    g[a][b][c]=pa*pb*pc;
                    double gg=g[a][b][c];
                    double m=pow(1-2*gg,k);
                    ans+=(1-m)/2.0;
                }
            }
        }
        printf("Case %d: %.8f\n",++cas,ans);
    }
}

```




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




### C - Race to 1 Again


Rimi learned a new thing about integers, which is - any positive integer greater than **1** can be divided by its divisors. So, he is now playing with this property. He selects a number **N**. And he calls this **D**.

In each turn he randomly chooses a divisor of **D** **(1 to D)**. Then he divides **D** by the number to obtain new **D**. He repeats this procedure until **D** becomes **1**. What is the expected number of moves required for **N** to become **1**.

**Input**

Input starts with an integer **T (****≤ 10000)**, denoting the number of test cases.

Each case begins with an integer **N (1 ≤ N ≤ 105)**.

**Output**

For each case of input you have to print the case number and the expected value. Errors less than **10-6** will be ignored.

**Sample Input**


3

1

2

50


**Sample Output**


Case 1: 0

Case 2: 2.00

Case 3: 3.0333333333


### 分析：


$因为 所有数最终都会到达1，所以用dp[i]，表示i到1的的操作期望$

$dp[i]=\sum _{d|i}(dp[d]+1)*(1/tot)，tot代表i的因子的个数$

当$d=i$的时候，这时候将等式右边移项即可

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
const ll mod=1e9+7;
double dp[maxn];//n到i的期望
int tot;
void init()
{
    dp[1]=0;
    for(int k=2; k<=100000; ++k)
    {
        tot=2;
        dp[k]=2.0;
        for(int i=2; i*i<=k; ++i)//求出小于k的所有因子
            if(k%i==0)
            {
                dp[k]+=dp[i]+1;
                tot++;
                if(i!=k/i)
                {
                    dp[k]+=dp[k/i]+1;
                    tot++;
                }
            }
        dp[k]/=tot-1;
    }
}
int main()
{
    int cas=0;
    int n,t;
    init();
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        printf("Case %d: %.7f\n",++cas,dp[n]);
    }
    return 0;
}
```




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




## A - A Dangerous Maze


You are in a maze; seeing **n** doors in front of you in beginning. You can choose any door you like. The probability for choosing a door is equal for all doors.

If you choose the **ith** door, it can either take you back to the same position where you begun in **xi** minutes, or can take you out of the maze after **xi** minutes. If you come back to the same position, you can’t remember anything. So, every time you come to the beginning position, you have no past experience.

Now you want to find the expected time to get out of the maze.

**Input**

Input starts with an integer **T (****≤ 100)**, denoting the number of test cases.

Each case contains a blank line and an integer **n (1 ≤ n ≤ 100)** denoting the number of doors. The next line contains **n**space separated integers. If the **ith** integer **(xi)** is positive, you can assume that the **ith** door will take you out of maze after **xi** minutes. If it’s negative, then the **ith** door will take you back to the beginning position after **abs(xi)** minutes. You can safely assume that **1 ≤ abs(xi) ≤ 10000**.

**Output**

For each case, print the case number and the expected time to get out of the maze. If it’s impossible to get out of the maze, print **‘inf’**. Print the result in **p/q** format. Where **p** is the numerator of the result and **q** is the denominator of the result and they are relatively prime. See the samples for details.

**Sample Input**


3

1

1

2

-10 -3

3

3 -6 -9


**Sample Output**


Case 1: 1/1

Case 2: inf

Case 3: 18/1


### 题意：


有n个门，每个门有一个值，这个值的绝对值代表你开门的时间，正数则代表打开这个门你就能出去，负数代表进入这个门你将回到现在的位置，每次你等概率的选择其中一个们打开，求出去所用时间的期望。并以分数形式输出。

### 分析：


举个例子 有两个门一个门分别是2，-3，假设选择出去的时间的期望是E，那么

$E=0.5*2+0.5*(3+E)+,得出来E=5$

有没有恍然大悟？

我们只需要把左边的$0.5*2$改成第一次走正门的期望，右边的改成第一次走负门的概率乘以走负门的期望加上出去的期望即可

$第一次走正门的出去的期望=走每个正门的概率*花费的时间$

$第一次走负门的出去的期望=每个走负门的概率*(花费的时间+出去的期望)$

$出去的期望=第一次走正门出去的期望+第一次走负门出去的期望$

化简公式即可得到答案

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
const int maxn=1e3+100;
const int branch=26;
const int inf=0x7fffffff;
const ll mod=1e9+7;
int fcnt,sum,n;
int gcd(int a,int b)
{
    int t;
    t=a%b;
    while(t)
    {
        a=b;
        b=t;
        t=a%b;
    }
    return b;
}
int main()
{
    int cas=0,t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        sum=0;
        fcnt=0;
        int val;
        for(int i=0;i<n;++i)
        {
            scanf("%d",&val);
            if(val<0)
            {
                fcnt++;
                sum+=-val;
            }
            else
                sum+=val;
        }
        if(fcnt==n)
            printf("Case %d: inf\n",++cas);
        else
            printf("Case %d: %d/%d\n",++cas,sum/gcd(sum,n-fcnt),(n-fcnt)/gcd(sum,n-fcnt));
    }
    return 0;
}
```


