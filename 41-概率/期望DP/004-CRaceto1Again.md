

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


