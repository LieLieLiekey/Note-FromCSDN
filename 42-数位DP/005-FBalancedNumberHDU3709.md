

### F - Balanced Number


A balanced number is a non-negative integer that can be balanced if a pivot is placed at some digit. More specifically, imagine each digit as a box with weight indicated by the digit. When a pivot is placed at some digit of the number, the distance from a digit to the pivot is the offset between it and the pivot. Then the torques of left part and right part can be calculated. It is balanced if they are the same. A balanced number must be balanced with the pivot at some of its digits. For example, 4139 is a balanced number with pivot fixed at 3. The torqueses are 4*2 + 1*1 = 9 and 9*1 = 9, for left part and right part, respectively. It’s your job to calculate the number of balanced numbers in a given range [x, y].

**Input**

The input contains multiple test cases. The first line is the total number of cases T (0 < T ≤ 30). For each case, there are two integers separated by a space in a line, x and y. (0 ≤ x ≤ y ≤ 10 18).

**Output**

For each case, print the number of balanced numbers in the range [x, y] in a line.

**Sample Input**

```bash
2
0 9
7604 24324
```


**Sample Output**

```bash
10
897
```


**题意 ：**

求a~b之间有多少平衡数字，所谓平衡数就是可以从其十进制位中找到一个支点，使得力矩为0。例如4139 ，找支点3，满足4*2 + 1*1 ==9*1 =9。故4139就是平衡数。

**分析：**

对于非0数字，若存在支点，那么他的支点只有一个。

所以，枚举所有支点，知道在每个支点下的平衡数，加起来减去多计算的0就是答案。

**对于每个支点0 ：**

我们还是按照传统的方法dp数位，

设$dp[pos][o][k]$ pos为待定的位，o为支点，k为在该支点下前缀的力矩是k。满足条件的数有$dp[pos][o][k]$ 个.

**那么在支点o下dp方程为：**

$dp[pos][o][k]=\sum _{i==0} ^9dp[pos-1][o][k+(pos-o)*i]$

在这个过程中，如果k<0就肯定没有满足条件的数，直接返回0（在支点左边肯定为0，在支点右边如果为负，就肯定不满足）

**代码：**

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
ll dp[20][20][1500];
int num[20];
ll dfs(int pos,int o,int pre,bool istop)
{
    /*
    1.jianzhi  pre<0 return 0;
    2.记忆话
    */
    if(!pos)
        return pre==0;
    if(pre<0)
        return 0;
    if(!istop&&dp[pos][o][pre]!=-1)
        return dp[pos][o][pre];
    int endd=istop?num[pos]:9;
    ll ans=0;
    for(int i=0;i<=endd;++i)
    {
        ans+=dfs(pos-1,o,pre+(pos-o)*i,istop&&i==endd);
    }
    if(!istop)
        dp[pos][o][pre]=ans;
    return ans;
}
ll calc(ll val)
{
    if(val==-1)
        return 0;
    int pos=0;
    do{
        num[++pos]=val%10;
        val/=10;
    }
    while(val);
    ll ans=0;
    for(int i=1;i<=pos;++i)
    {
        ans+=dfs(pos,i,0,1);
    }
    return ans+1-pos;//数字0支点多加了pos-1个
}
int main()
{
    ll a,b;
    int t;
    scanf("%d",&t);
    mset(dp,-1);
    while(t--)
    {
        scanf("%lld %lld",&a,&b);
        printf("%lld\n",calc(b)-calc(a-1));
    }
    return 0;
}

```


