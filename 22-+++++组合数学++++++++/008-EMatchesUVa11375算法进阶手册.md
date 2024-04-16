

### [E - Matches](https://cn.vjudge.net/problem/UVA-11375)


[UVA - 11375 ](https://cn.vjudge.net/problem/22967/origin)

**题目描述** ：


​ 火柴，用n (1<=n<=2000棍能组成多少个非负整数？火柴不必用完，组成的整数不能有前导零（但蒸整数0是可以的）。比如你有三根火柴，可以组成1或者7；如果有四根，除了可以组成1和7之外，还可以组成4和77。


**分析：**


​ 可以用加法原理，n根火柴组成的种类数，可以分解成只用1，2，3…n根火柴组成的种类数之和。

假设计算dp[i]是只用i根火柴可以组成的种类数。



**有个状态转移的过程，假设c[j]代表数字j需要花费的火柴数目。那么**

​ dp[i+c [ j ] ]=dp[i+ c [ j ] ]+dp[i]

对于dp[k],只能由前一个状态后加一个数字转移过来的（前一个状态都是独立的，没有重复），那么只要保证k之前的都进行上面的状态转移，那么此时的dp[ k ] 就是花费k个火柴可以组成的种类数

需要注意的是，因为没有前导0，所以刚开始从0状态不能经过数字0转移到dp[6],不然会导致后面计算的状态都包含前导0。 最后只要判断如果n>=6 就加上0这个种类即可


**当然写状态转移的时候也需要注意几点 ：**

1.初始状态 //dp[0]设为1，代表从0状态由一种方法到达，所以可以由0状态加数字到其他状态。

2.状态的转移过程//

因为数据量较大，用高精度的方式写

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=2000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
/*
给你n个火柴棍,最多能组成几个非负数(不含前导零)

*/
struct BigNum{
    int a[2000];//储存 低位到高位   10000进制
    int len;//代表有效长度
    BigNum()
    {
         mset(a,0);
         len=1;
    }
    BigNum(int n)
    {
        mset(a,0);
        len=1;
        a[0]=n%10000;
        n/=10000;
        while(n)
        {
            a[len++]=n%10000;
            n/=10000;
        }
    }
    BigNum operator + (const BigNum &k)
    {
        BigNum  ans;
        ans.len=max(len,k.len);
        for(int i=0;i<ans.len;++i)
        {
            ans.a[i]+=a[i]+k.a[i];
            ans.a[i+1]+=ans.a[i]/10000;
            ans.a[i]%=10000;
        }
        if(ans.a[ans.len]>0)
        {
            ans.len++;
        }
        return ans;
    }
    BigNum(const BigNum &aa)//习惯用构造函数啥的，怕指针乱指
    {
        len=aa.len;
        mset(a,0);
        for(int i=0;i<len;++i)
            a[i]=aa.a[i];
    }
    BigNum operator = (const BigNum &aa)//也是上面的原理，怕指针乱指
    {
        len=aa.len;
        mset(a,0);
        for(int i=0;i<len;++i)
            a[i]=aa.a[i];
        return *this;
    }
    void out()
    {
        /*先输出最高位*/
        /*底位按5个长度输出*/
        printf("%d",a[len-1]);
        for(int i=len-2;i>=0;--i)
        {
            printf("%04d",a[i]);
        }
        printf("\n");
    }
};
int c[]={6,2,5,5,4,5,6,3,7,6};
BigNum dp[maxn+10];//dp[i] 表示*只用*i个柴火棍可以组成多少数组
void Preprocess()//需要用到高精度
{
    dp[0]=BigNum(1);//代表0 ~0有一步 初始状态
    for(int i=0;i<=maxn;++i)
    {
        for(int j=0;j<10;++j)
        {
            //第一个数字不能为0 如果n大于k 自动加上1
            if(!(!i&&!j)&&i+c[j]<=maxn)//i=0是不能走0
            {
                dp[i+c[j]]=dp[i+c[j]]+dp[i];
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
        BigNum ans;
        for(int i=1;i<=n;++i)
        {
            ans=ans+dp[i];
        }
        if(n>=6)
        {
            ans=ans+BigNum(1);
        }
        ans.out();
    }
}

```


