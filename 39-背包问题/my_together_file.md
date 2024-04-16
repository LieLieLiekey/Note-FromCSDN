

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




大概写一下 有时间再完善

1.用vir[][][]数组记录此次选择的上一个选择位置

2.数组cc[][]记录此次选择的最长公共子序列的最后一位的在a字符串的下标  cc[i][j]=0表示从上个位置到此次位置没有更新更好的

 

回溯  数组cc里面存的就是最长公共子序列

 

 

 

 

 

```cpp
/*
最长公共子序列之回溯
*/
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#define N 1300
#define INF 0x3f3f3f3f
using namespace std;
int vir[N][N][2],cc[N][N];
int dp[N][N];
int lcs(char* a,char* b,int la,int lb)
{
    memset(dp,0,sizeof(dp));
    memset(cc,0,sizeof(cc));
    for(int i=1; i<=la; i++)
        for(int j=1; j<=lb; j++)
        {
            if(a[i]==b[j])
            {
                dp[i][j]=dp[i-1][j-1]+1;
                vir[i][j][0]=i-1;
                vir[i][j][1]=j-1;
                cc[i][j]=i;
            }
            else
            {
                cc[i][j]=0;
                if(dp[i-1][j]>=dp[i][j-1])
                {
                    dp[i][j]=dp[i-1][j];
                    vir[i][j][0]=i-1;
                    vir[i][j][1]=j;
                }
                else
                {
                    dp[i][j]=dp[i][j-1];
                    vir[i][j][0]=i;
                    vir[i][j][1]=j-1;
                }
            }
        }
    return dp[la][lb];
}
int main()
{
    char s1[N],s2[N];
    int res[N],la,len1,len2,ii,jj;
    int t=5;
    while(t--)
    {
        scanf("%s %s",s1+1,s2+1);
        len1=strlen(s1+1);
        len2=strlen(s2+1);
        lcs(s1,s2,len1,len2);
        la=0;
        ii=len1;
        jj=len2;
        int mi,mj;
        while(ii&&jj)
        {
            if(cc[ii][jj])
            {
                res[la++]=cc[ii][jj];
            }
            mi=ii;//回溯
            mj=jj;
            ii=vir[mi][mj][0];
            jj=vir[mi][mj][1];
        }
//        for(int i=0;i<la;i++)
//            printf("%d ",res[i]);
        puts("--------");
        printf("the most len ss:");
        for(int i=la-1;i>=0;i--)
            printf("%c",s1[res[i]]);
        puts("");


    }
}```


 



对于上面的动态规划以第2个问题为例：

 

最长递增子序列:dp[i]

状态：以i为自增序列结尾的最大长度为dp[i]；

决策：从第i个往前找，找到a[j]<a[i]，dp[i]=max(dp[i],dp[j]+1);（dp[j]表示符合条件的i前面的一个以j为结尾的最大长度）

符合无后效性

初始状态：dp[i]=1;

```cpp
#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#define INF 0x3f3f3f3f
#define PI  3.14159
#define N  1010
#define MOD 9997
using namespace std;
int dp[N],a[N];
int main()
{
    int n,ans;
    while(~scanf("%d",&n))
    {
        memset(dp,0,sizeof(dp));
        for(int i=0;i<n;i++)
            scanf("%d",&a[i]);
        for(int i=0;i<n;i++)
        {
            dp[i]=1;
            for(int j=i-1;j>=0;j--)
            {
                if(a[j]<a[i])
                    dp[i]=max(dp[i],dp[j]+1);
            }
        }
        ans=-1;
        for(int i=0;i<n;i++)
        {
            ans=ans>dp[i]?ans:dp[i];
        }
        cout<<ans<<endl;
    }
}```


 

 

至于第一个问题只需把动态规划公式的1改为a[i]即可；



 

The aspiring Roy the Robber has seen a lot of American movies, and knows that the bad guys usually gets caught in the end, often because they become too greedy. He has decided to work in the lucrative business of bank robbery only for a short while, before retiring to a comfortable job at a university. 


![./figures/931cc59be308ad18cd98b5c8caec6454](./figures/931cc59be308ad18cd98b5c8caec6454)


 For a few months now, Roy has been assessing the security of various banks and the amount of cash they hold. He wants to make a calculated risk, and grab as much money as possible.  His mother, Ola, has decided upon a tolerable probability of getting caught. She feels that he is safe enough if the banks he robs together give a probability less than this.InputThe first line of input gives T, the number of cases. For each scenario, the first line of input gives a floating point number P, the probability Roy needs to be below, and an integer N, the number of banks he has plans for. Then follow N lines, where line j gives an integer Mj and a floating point number Pj .  Bank j contains Mj millions, and the probability of getting caught from robbing it is Pj .OutputFor each test case, output a line with the maximum number of millions he can expect to get while the probability of getting caught is less than the limit set.  Notes and Constraints  0 < T <= 100  0.0 <= P <= 1.0  0 < N <= 100  0 < Mj <= 100  0.0 <= Pj <= 1.0  A bank goes bankrupt if it is robbed, and you may assume that all probabilities are independent as the police have very low funds.Sample Input

```
3
0.04 3
1 0.02
2 0.03
3 0.05
0.06 3
2 0.03
2 0.03
3 0.05
0.10 3
1 0.03
2 0.02
3 0.05```


Sample Output

```
2
4
6```


 

 

这道题可以说是概率背包问题，第一次看这个题的时候思考了一下午，又看了会博客没看懂，故于晚上认真思考之后得出解法，有些博客没说清楚，可能会让读者误会其意思，我在这里对我以前迷惑之处重点指出。

这道题可以看作是可以看作0 1背包，但是我还是觉得看作动态规划更好。。。

先说下这道题重要的几点

1.把被抓概率转化为逃跑概率pp，故逃跑概率越大越好

 

这里第i个银行的钱为a[i]，被抓概率为pp[i];

**①状态：可以抢前i个银行得到j钱的逃跑概率为dp[i][j],（注意这里，j是可以抢到的总钱数量，也就是说一定有办法抢若干个银行的到j钱，若没办法则其概率自然为0）**

**②决策：第i个银行抢或者不抢**

**③        ：满足无后效性**

状态转移方程dp[i][j]=max（dp[i-1][j-a[i]]*pp[i],dp[i-1][j]）在抢到j钱的状态下左侧：抢第i个银行，右侧：不抢

dp[0][0]=1也是自然的。

 

 

 

```cpp
#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#define INF 0x3f3f3f3f
#define PI  3.14159
#define N 500
#define MOD 9997
using namespace std;
double dp[10010];
int main()
{
    int t,n,cost[N],sum,ans;
    double p0,pp[N];
    cin>>t;
    while(t--)
    {
        cin>>p0>>n;
        p0=1-p0;
        memset(dp,0,sizeof(dp));
        dp[0]=1;
        sum=0;
        for(int i=1; i<=n; i++)
        {
            cin>>cost[i]>>pp[i];
            sum+=cost[i];
            pp[i]=1-pp[i];
        }
//            for(int i=0;i<=sum;i++)
//        {
//            cout<<"抢到"<<i<<" 钱 ,pp="<<dp[i]<<endl<<endl;
//        }
        for(int i=1; i<=n; i++)
            for(int j=sum; j>=cost[i]; j--)
            {
                dp[j]=max(dp[j-cost[i]]*pp[i],dp[j]);
            }
//        cout<<"after....."<<endl;
//        for(int i=0;i<=sum;i++)
//        {
//            cout<<"抢到"<<i<<" 钱 ,pp="<<dp[i]<<endl<<endl;
//        }
        ans=-1;
        for(int i=0; i<=sum; i++)
        {
            if(dp[i]>=p0)
                ans=ans>i?ans:i;
        }
        cout<<ans<<endl;
    }
}
```


 

 



科大本部食堂的饭卡有一种很诡异的设计，即在购买之前判断余额。如果购买一个商品之前，卡上的剩余金额大于或等于5元，就一定可以购买成功（即使购买后卡上余额为负），否则无法购买（即使金额足够）。所以大家都希望尽量使卡上的余额最少。 某天，食堂中有n种菜出售，每种菜可购买一次。已知每种菜的价格以及卡上的余额，问最少可使卡上的余额为多少。

Input多组数据。对于每组数据： 第一行为正整数n，表示菜的数量。n<=1000。 第二行包括n个正整数，表示每种菜的价格。价格不超过50。 第三行包括一个正整数m，表示卡上的余额。m<=1000。 n=0表示数据结束。 Output对于每组输入,输出一行,包含一个整数，表示卡上可能的最小余额。Sample Input

```
1
50
5
10
1 2 3 2 1 1 2 3 2 1
50
0```


Sample Output

```
-45
32```


 

 

很容易看出来是0 1背包，但不完全是0 1背包，属于0 1背包的变形；

**对于给定的金钱m，可以考虑先从m中拿出来5元，那5元作为最后用来支付开销最大的饭。那用（m-5）d的钱来购买除开销最大饭以外的饭。也就是0 1背包求价值最大。**

但是为什么把开销最大的饭作为杀手锏最后花一定是最优的呢？下面我来给出证明

①假设杀手锏（也就是用5元买的饭）是开销最大的饭。

②假设杀手锏不是开销最大的饭。

如果说杀手锏是开销最大的饭，那么思路就跟上面说说的一样，

如果杀手锏不是开销最大的饭设其值为v”,(开销最大的设为V.max)，n那么这种情况下V.max一定包含在背包内了(如果在背包外，那杀手锏也不会让v"出手)，如果我现在让v"与V.max换换位置（V.max在背包中占的位置大，v"一定可以与他交换），那么造成的价值是不变的，也就是说情况②又回归到了情况①上

所以说杀手锏必定是开销最大的饭。

就照着黑体字的思路开始写代码（注意m<5时是用不了杀手锏的）

```cpp
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<iostream>
#define N 1010
#define INF 0x3f3f3f3f
using namespace std;
int dp[N];
int val[N];
int book[N];//表示对应标号能不能用(1为不能用)
int main()
{
    int n,maxx,u,m;
    while(~scanf("%d",&n)&&n)
    {
        memset(book,0,sizeof(book));
        memset(dp,0,sizeof(dp));
        maxx=-INF;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&val[i]);
            if(val[i]>maxx)
            {
                u=i;
                maxx=val[i];
            }
        }
        book[u]=1;
        cin>>m;
        if(m<5)
        {
            cout<<m<<endl;
            continue;
        }
        m-=5;
        for(int i=0;i<n;i++)//枚举背包
        {
            if(book[i])
                continue;
            for(int j=m;j>=val[i];j--)
            {
                dp[j]=max(dp[j-val[i]]+val[i],dp[j]);//最后的值表示为用m-5最多能选多少元的菜
            }
        }

        cout<<m+5-dp[m]-val[u]<<endl;
    }
}
```


 



## 背包问题之退背包


退背包就是从可选物品中删除其中一个物品，问满足所取总价值为 $j j$ 的方案数。

像普通背包一样，退背包先普通dp以下，然后退去所选物品。

对于**01背包**，假设$d p [ i ] ​ dp[i]​$为未退背包前满足所取总价值为 $i ​ i​$ 的方案数。$d p ′ [ i ] ​ dp'[i]​$ 为退去第$x ​ x​$个物品后满足所取总价值为$i ​ i​$的方案数，那么 dp方程为


+ 当$i < w [ x ] ​ i<w[x]​$



