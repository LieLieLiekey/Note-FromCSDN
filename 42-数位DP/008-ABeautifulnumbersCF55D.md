

### A - Beautiful numbers


Volodya is an odd boy and his taste is strange as well. It seems to him that a positive integer number is beautiful if and only if it is divisible by each of its nonzero digits. We will not argue with this and just count the quantity of beautiful numbers in given ranges.

**Input**

The first line of the input contains the number of cases t (1 ≤ t ≤ 10). Each of the next *t* lines contains two natural numbers li and ri (1 ≤ \li≤ ri≤ 9 ·1018).

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d).

**Output**

Output should contain t numbers — answers to the queries, one number per line — quantities of beautiful numbers in given intervals (from li to ri, inclusively).

Examples

**Input**

```bash
1
1 9
```


**Output**

```bash
9
```


**Input**

```bash
1
12 15
```


**Output**

```bash
2
```


**分析：**

刚学dp，这dp搞我一天了，不过还真有意思的，里面又悟出来一点东西，dp方程要敢想

**状态：**

$dp[pos][PreSum][PreLcm]$ 是值pre*****(pos个*号，*号代表这个数随便取。这个数的前缀是pre),这个dp代表前缀为PreSum且前缀的lcm为PreLcm后pos个数满足条件的个数是多少。

举个例子：520***就是PreSum为520，PreLcm为10，其对应的dp方程为$dp[3][520][10]$

**故dp方程为：**

$dp[pos+1][PreSum][PreLcm]=\sum_{i==0}^{9}dp[pos][PreSum*10+i][LCM(PreLcm,i)]$

当pos==0时候（递归边界）

若满足PreSum%PreLcm==0就返回1，否则返回0

**这个需要注意两个点：**

+ 第三个参数最大为2520，但是真正能取的都是2520的因数（2520从哪来的呢，2520是LCM(1,2,3…9)），也就那48个，所以可以将第三个参数映射一下（相当于离散化），减少空间+ 第二个参数会很大吧，但是第三个参数是来干什么的？不是最后的时候取余第三个参数的吗！，又因为2520是所有可能第三个参数的倍数，故$PreSum\%PreLcm==0$等效于$PreSum\%2520\%PreLcm==0$(当然取余后的值可不相等)，所以可以让第二个参数取余2520，控制范围，减少空间


详情看代码

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
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
const int inf=0x3f;
const int MOD=2520;
ll dp[30][MOD+10][50];
int index[MOD+10];
int num[30];
void init()
{
    mset(dp,-1);
    int tot=0;
    /*将MOD仅有的因子离散化 每个值对应于一个下标*/
    for(int i=1;i<=MOD;++i)
        if(MOD%i==0)
            index[i]=++tot;
}
int Gcd(int a,int b)
{
    int temp;
    while(a%b)
    {
        temp=a%b;
        a=b;
        b=temp;
    }
    return b;
}
int Lcm(int a,int b)
{
    return a/Gcd(a,b)*b;
}
ll dfs(int pos,int pre_sum,int pre_lcm,bool is_top);
ll calc(ll val)
{
    int pos=0;
    do{
        num[++pos]=val%10;
        val/=10;
    }
    while(val);//位数从下标1开始存
    return dfs(pos,0,1,true);
}
ll dfs(int pos,int pre_sum,int pre_lcm,bool is_top)
{
    if(!pos)
        return pre_sum%pre_lcm==0;
    if(!is_top&&dp[pos][pre_sum][index[pre_lcm]]!=-1)
        return dp[pos][pre_sum][index[pre_lcm]];
    int endd=is_top?num[pos]:9;
    ll res=0ll;
    for(int i=0;i<=endd;++i)
    {
        int lcm,sum;
        lcm=pre_lcm;
        if(i)
            lcm=Lcm(lcm,i);
        sum=(pre_sum*10+i)%MOD;
        res+=dfs(pos-1,sum,lcm,is_top&&i==endd);
    }
    if(!is_top)
        dp[pos][pre_sum][index[pre_lcm]]=res;
    return res;
}
int main()
{
    int t;
    ll a,b;
    init();
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld %lld",&a,&b);
        printf("%lld\n",calc(b)-calc(a-1));
    }
    return 0;
}
```


