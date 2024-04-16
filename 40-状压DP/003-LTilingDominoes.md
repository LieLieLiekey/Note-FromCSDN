

### L - Tiling Dominoes



闲聊

在大白书上$383$页，上面有详细讲解这道题的$dp$方法，

第一次做这类状压dp的题时，用的dp的时间复杂度是$O(2^m*2^m*n)$ 可以过另一个一模一样的题，当时是把每一行的放置情况当作状态进行转移，但是那个算法在这道题上过不去，于是开始寻找博客，网上说大白书上有一道一模一样的题，正好旁边就有一本这样的书，理解了一下就A了这道题时间复杂度为$O(2^m*m*n)$

在大白书上$383$页，上面有详细讲解这道题的dp方法，


### 分析：


把第i行第j个的m个位置（自身带上前m-1个数）的放置状态进行动态规划求解。

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
int n,m,cur;
ll dp[2][1<<10];

int main()
{
    while(~scanf("%d %d",&n,&m))
    {
        if(n<m)
            swap(n,m);
        mset(dp,0);
        dp[0][(1<<m)-1]=1;
        cur=0;
        int tot=1<<m;
        for(int i=0; i<n; ++i)
        {
            for(int j=0; j<m; ++j)
            {
                cur^=1;//根据上个位置得到这个 状态的存放位置
                mset(dp[cur],0);
                for(int s=0; s<tot; ++s) //枚举上个状态
                {
                    /*不放*/
                    int tos;
                    if(s&(1<<(m-1)))
                    {
                        tos=s<<1;
                        tos^=1<<m;//把第m位变为0
                        dp[cur][tos]+=dp[1-cur][s];
                    }
                    /*横着放*/
                    if(j&&(s&1)==0&&(s&(1<<(m-1))))
                    {
                        tos=s<<1;
                        tos^=1<<m;
                        tos|=(1<<1)|1;
                        dp[cur][tos]+=dp[1-cur][s];
                    }
                    /*竖着放*/
                    if(i&& !(s&(1<<(m-1))))
                    {
                        tos=s<<1;
                        tos|=1;
                        dp[cur][tos]+=dp[1-cur][s];
                    }
                }
            }
        }
        cout<<dp[cur][tot-1]<<endl;
    }
    return 0;
}

```


