

 

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


 

 

