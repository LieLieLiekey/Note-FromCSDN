

## 欧拉，素数，莫比乌斯反演函数筛法


## 


此筛法依据原理：每个合数肯定能被自己的最小素因子筛到，即val=素数*数。若没被筛到则为素数

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
const int maxn=100000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=10007;
bool check[maxn+10];
int prime[maxn+10],mu[maxn+10];
int phi[maxn+10];
void init()//欧拉 素数 莫比乌斯反演函数
{
    mset(check,0);
    mu[1]=1;
    phi[1]=1;
    int tot=0;
    for(int i=2;i<=maxn;++i)
    {
        if(!check[i])
        {
            prime[tot++]=i;
            phi[i]=i-1;
            mu[i]=-1;
        }
        for(int j=0;j<tot;j++)
        {
            if(i*prime[j]>maxn) break;
            check[i*prime[j]]=true;
            if(i%prime[j]==0)
            {
                mu[i*prime[j]]=0;
                phi[i*prime[j]]=phi[i]*prime[j];
                break;
            }
            else
            {
                mu[i*prime[j]]=-mu[i];
                phi[i*prime[j]]=phi[i]*phi[prime[j]];//积性函数的性质
            }
        }
    }
}
```




### V - 排列组合 HDU(1521)


有n种物品，并且知道每种物品的数量。要求从中选出m件物品的排列数。例如有两种物品A,B，并且数量都是1，从中选2件物品，则排列有"AB","BA"两种。

Input

每组输入数据有两行，第一行是二个数n,m(1<=m,n<=10)，表示物品数，第二行有n个数，分别表示这n件物品的数量。

Output

对应每组数据输出排列数。(任何运算不会超出2^31的范围)

Sample Input

```bash
2 2
1 1
```


Sample Output

```bash
2
```


分析：

第一看出是就是dp


dp[i][j]含义：可以从前i个物品中选出j个的排列种类数

加法原理：第n个物品使用了k个,0<=k<=tot[i]

那么使用第n个物品时有：



$$dp[n][m]=\sum C[m][k]*dp[n-1][m-k] ,0&lt;=k&lt;=tot[i]$$




所以dp方程为:



$$dp[i][j]=\sum C[j][k]*dp[i-1][j-k] ,0&lt;=k&lt;=tot[i]$$



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
int C[30][30];
int dp[20][20],tot[20];
int n,m;//从n个物品中选m个数
void init()//求排列组合
{
    C[0][0]=1;
    for(int i=1;i<=20;++i)
    {
        C[i][0]=C[i][i]=1;
        for(int j=1;j<i;++j)
            C[i][j]=C[i-1][j]+C[i-1][j-1];
    }
}
int solve()
{
    mset(dp,0);
    dp[0][0]=1;
    int minn;
    for(int i=1;i<=n;++i)
    {
        for(int j=0;j<=m;++j)//可以选前i个物品 j个物品的排列
        {
            minn=min(j,tot[i]);//枚举第i个物品选的个数
            for(int k=0;k<=minn;++k)//第i个物品选了k个  从j中选了k个位置
                dp[i][j]+=C[j][k]*dp[i-1][j-k];
        }
    }
    return dp[n][m];
}
int main()
{
    init();
    while(~scanf("%d %d",&n,&m))
    {
        for(int i=1;i<=n;++i)
            scanf("%d",tot+i);
        printf("%d\n",solve());
    }
}
```




### 欧拉函数的求法


证明过程暂不讨论

##### 单个求欧拉函数


```cpp
long long eular(long long n)
{
    long long ans=n;
    for(int i=2;i*i<=n;++i)
    {
        if(n%i==0)
        {
            ans-=ans/i;
            while(n%i==0)
                n/=i;
        }
    }
    if(n>1)
        ans-=ans/n;
    return ans;
}
```


##### 筛法求欧拉函数


```cpp
const int maxn=1e5;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
int euler[maxn+10];
void getEuler()
{
    mset(euler,0);
    euler[1]=1;
    for(int i=2; i<=maxn; ++i)
        if(!euler[i])
            for(int j=i; j<=maxn; j+=i)
            {
                if(!euler[j])
                    euler[j]=j;
                euler[j]=euler[j]/i*(i-1);
            }
}
```


##### 用素因子求欧拉函数


```cpp
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<map>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e6;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
int book[maxn+10],prime[(int)1e5+10];
int top;
void init()//求出100w以内的所有素因子
{
    top=0;
    book[0]=book[1]=1;
    for(int i=2;i*i<=maxn;++i)
        if(!book[i])
    {
        for(int j=i*i;j<=maxn;j+=i)
            book[j]=1;
    }
    for(int i=2;i<=maxn;++i)
        if(!book[i])
            prime[top++]=i;
}
int phi(int val)//求1~n中与n互质的个数
{
    int ans=val;
    for(int i=0;prime[i]*prime[i]<=val;++i)
    {
        if(!(val%prime[i]))
        {
            ans=ans/prime[i]*(prime[i]-1);
            while(!(val%prime[i]))
            {
                val/=prime[i];
            }
        }
    }
    if(val>1)
        ans=ans/val*(val-1);
    return ans;
}
```


##### 线性筛（同时得到欧拉函数和素数表）


```cpp
bool check[maxn+10];
int phi[maxn+10];
int prime[maxn+10];
int tot;//素数的个数
void phi_and_prime_table(int N)//1~n以内的所有素数  已经欧拉函数
{
    memset(check,false,sizeof(check));
    phi[1]=1;
    tot=0;
    for(int i=2;i<=N;++i)
    {
        if(!check[i])
        {
            prime[tot++]=i;
            phi[i]=i-1;
        }
        for(int j=0;j<tot;++j)
        {
            if(i*prime[j]>N) break;
            check[i*prime[j]]=true;
            if(i%prime[j]==0)
            {
                phi[i*prime[j]]=phi[i]*prime[j];
                break;
            }
            else
            {
                phi[i*prime[j]]=phi[i]*(prime[j]-1);
            }
        }
    }
}
```


