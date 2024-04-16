

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


