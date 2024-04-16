

### G - B-number


A wqb-number, or B-number for short, is a non-negative integer whose decimal form contains the sub- string “13” and can be divided by 13. For example, 130 and 2613 are wqb-numbers, but 143 and 2639 are not. Your task is to calculate how many wqb-numbers from 1 to n for a given integer n.

**Input**

Process till EOF. In each line, there is one positive integer n(1 <= n <= 1000000000).

**Output**

Print each answer in a single line.

**Sample Input**


13 100 200 1000


**Sample Output**


1 1 2 2


**分析 ：**

做了这么长时间的数位dp，这题套路太老了！

So，怎么做呢，任何一个数位dp只要只要pre****的求法，找出其中的状态，题目自然就迎刃而解了！

这题求pre****，主要注意三个东西

+ pre的值是多少(为了取余13用)+ pre最后一位是否为1+ pre中是否含有串13


所以着要题的状态就这三个，当然还得再加上一个pos，表用来求的位数是几位

试试能不能写出dp方程？



$$dp[pos][PreSum][Is1][Have13]=\sum _{i==0}^{9}dp[pos-1][(PreSum*10+i)\%Mod][i==1][Have13||(Is1\&amp;\&amp;i==3)])$$



代码：

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
const int MOD=13;
int dp[15][14][2][2];//dp[pos][PreSum%mod][is_1][have_13]
int num[20];
int dfs(int pos,int PreSum,bool Is1,bool Have13,bool Istop)//前缀是否为1，是否是含有13
{
    if(!pos)
        return ((PreSum%MOD==0)&&Have13);
    if(!Istop&&dp[pos][PreSum][Is1][Have13]!=-1)
        return dp[pos][PreSum][Is1][Have13];
    int endd=Istop?num[pos]:9;
    int res=0;
    for(int i=0;i<=endd;++i)
    {
        res+=dfs(pos-1,(PreSum*10+i)%MOD,i==1,Have13||(Is1&&i==3),Istop&&i==endd);
    }
    if(!Istop)
        dp[pos][PreSum][Is1][Have13]=res;
    return res;
}
int calc(int val)
{
    int pos=0;
    do{
     num[++pos]=val%10;
     val/=10;
    }
    while(val);
    return dfs(pos,0,0,0,1);
}
int main()
{
    int a;
    mset(dp,-1);
    while(~scanf("%d",&a))
    {
        printf("%d\n",calc(a));
    }
    return 0;
}

```


