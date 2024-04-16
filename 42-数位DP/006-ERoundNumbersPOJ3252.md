

### E - Round Numbers


The cows, as you know, have no fingers or thumbs and thus are unable to play Scissors, Paper, Stone’ (also known as ‘Rock, Paper, Scissors’, ‘Ro, Sham, Bo’, and a host of other names) in order to make arbitrary decisions such as who gets to be milked first. They can’t even flip a coin because it’s so hard to toss using hooves.

They have thus resorted to “round number” matching. The first cow picks an integer less than two billion. The second cow does the same. If the numbers are both “round numbers”, the first cow wins, otherwise the second cow wins.

A positive integer *N* is said to be a “round number” if the binary representation of *N* has as many or more zeroes than it has ones. For example, the integer 9, when written in binary form, is 1001. 1001 has two zeroes and two ones; thus, 9 is a round number. The integer 26 is 11010 in binary; since it has two zeroes and three ones, it is not a round number.

Obviously, it takes cows a while to convert numbers to binary, so the winner takes a while to determine. Bessie wants to cheat and thinks she can do that if she knows how many “round numbers” are in a given range.

Help her by writing a program that tells how many round numbers appear in the inclusive range given by the input (1 ≤ *Start* < *Finish* ≤ 2,000,000,000).

**Input**

Line 1: Two space-separated integers, respectively *Start* and *Finish*.

**Output**

Line 1: A single integer that is the count of round numbers in the inclusive range*Start*… *Finish*

**Sample Input**


2 12


**Sample Output**


6


**分析 ：**

有组合数学和数位dp两种方法，组合数学比较简单，这里只说数位dp。

dp能解决大部分区间计数问题，用枚举位数和动规来解决问题 dp[0][pos][k]代表000****中满足0-1>=k的种类数 dp[1][pos][k]代表 (1)****中满足0-1>=k的种类数前缀是1 **所以状态三个：** 1.前缀是否全为0 2.随便的有几位 3.这几位满足0-1>=k的个数

+ 当前缀有1时候，枚举第pos位是0是1即可。




$$dp[1][pos][k]=dp[1][pos-1][k-1]+dp[1][pos][k+1]$$



+ 当前缀前全位0时，枚举第pos位0，1即可


$dp[0][pos][k]=dp[0][pos-1][k]+dp[1][pos-1][k+1]$

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
int dp[2][40][70];//dp[0/1]第一维意思：满足后pos位数中0-1>=k的个数中，pos位之前是否全为0。      最高31位
int num[40];
int GetDp(int flag,int pos,int k)//-31<=k<=31
{
    return dp[flag][pos][k+31];
}
void  enDp(int flag,int pos,int k,int val)
{
    dp[flag][pos][k+31]=val;
}
int dfs(int pos,int flag,int k,bool Istop)
{
    if(!pos)
        return k<=0;
    if(!Istop&&GetDp(flag,pos,k)!=-1)
        return GetDp(flag,pos,k);
    int endd=Istop?num[pos]:1;
    int res=0;
    for(int i=0;i<=endd;++i)
    {
        if(i==1)
            res+=dfs(pos-1,1,k+1,Istop&&i==endd);
        else
        {
            if(flag==0)
                    res+=dfs(pos-1,0,0,Istop&&i==endd);
            else
                res+=dfs(pos-1,1,k-1,Istop&&i==endd);
        }
    }
    if(!Istop)
        enDp(flag,pos,k,res);
    return res;
}
int calc(int val)//如果前导全为0，就是0 否则为1
{
    int pos=0;
    do{
        num[++pos]=val%2;
        val/=2;
    }
    while(val);
    return dfs(pos,0,0,1);
}
int main()
{
    mset(dp,-1);
    int a,b;
    while(~scanf("%d %d",&a,&b))
    {
        printf("%d\n",calc(b)-calc(a-1));
    }
    return 0;
}
```


