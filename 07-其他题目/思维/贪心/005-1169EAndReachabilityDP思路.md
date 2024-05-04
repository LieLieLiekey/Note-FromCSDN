# 1169E. And Reachability(DP+思路)

题目链接：[传送门](<https://codeforces.com/contest/1169/problem/E>)

思路：

涉及到位运算，很容易想到按位考虑。

我们用$go[i][j]$表示第 $i$ 个数可以到达第 $j$ 位为1的最小下标是多少，如果没有则等于$n+1$。

对于这个状态方程，我们倒过来递推，我们让 $i$ 从 $n$ 开始遍历到 $1$ ,并用$last[k]$ 表示满足 $j>i$ 且 $a_j$ 的第 $k$ 位为 $1$ 的最小 $j$ ，初始化为$n+1$。

假设当前为 $i$，考虑 第 $j$ 位

- 如果 $a_i$ 的第 $j$ 位为1，那么$go[i][j]=i$
- 否则遍历 $a_i$ 所有位数为 1 的位，假设为 $k$ ，那么$go[i][j]=min(g[i][j],g[last[k]][j])$
- 随后更新$last[]$

那么对于每次查询$x,y$ ，我们枚举 $a_y$ 位数为 $1$ 的位， 假设为 $k$，判断是否存在 $k$ 使得$go[x][k]\le y$ 即可。

（很容易想到如果满足则必有解，且如果有解，必有上述表达式满足，即两问题等效）



代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int N=3e5+10;
const int M=19;
int g[N][M],a[N],last[N];
int main()
{
    int n,q;
    scanf("%d%d",&n,&q);
    for(int i=1; i<=n; ++i) scanf("%d",a+i);
    for(int i=0; i<M; ++i) {
        last[i]=n+1;
        g[n+1][i]=n+1;
    }
    for(int i=n; i>=1; --i)
    {
        for(int j=0; j<M; ++j)
        {
            if((a[i]>>j)&1)
                g[i][j]=i;
            else
            {
                g[i][j]=n+1;
                for(int k=0; k<M; ++k)
                {
                    if((a[i]>>k)&1)
                        g[i][j]=min(g[i][j],g[last[k]][j]);
                }
            }
        }
        for(int j=0; j<M; ++j)
            if((a[i]>>j)&1)
                last[j]=i;
    }
    for(int o=0; o<q; ++o)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        bool isok=false;
        for(int i=0; i<M; ++i)
            if((a[y]>>i)&1)
                isok|=(g[x][i]<=y);
        printf("%s\n",isok?"Shi":"Fou");
    }
    return 0;
}
```
