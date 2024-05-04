

## 1223D. Sequence Sorting(DP)


##### 题目链接：[传送门](https://codeforces.com/problemset/problem/1223/D)


##### 思路：


​ 我们假设序列$D=\{d_1,d_2,d_3...d_k\}$，序列$M=\{x|x= a_i\&\&x\notin D,i\in[1,n]\}$。

即序列D是没有移动的数，序列M是向左移动或向右移动的数，我们设 $maxpos[x]​$ 和 $minpos[x]​$ 分别是数 $x​$ 在序列 $a​$ 中出现的最大位置下标和最小位置下标。那么序列D和序列M必定满足下列条件

+ 对于 $D_i,D_j$ ，假设 $D_i<D_j$ ，那么 $minpos[D_j]>maxpos[D_i]$。（原因：这样序列才能有序且不移动）+ 对于序列M中的任意一个数，满足$M_i​$ 不夹在序列D的最大和最小值之间，即$M_i>max\{x|x\in D\}​$或$M_i<min\{x|x\in D\}​$ 成立，即数列D中相邻的两个元素在排序上也是相邻的（原因：因为序列M中的数字向左或向右移动，那么其必定移动到序列D的两侧，又因为最终序列是有序的，则满足上述条件）


因为序列M的长度加序列D的长度之和为元素的种类数，我们现在只需求出序列D最长为多长即可。

我们用$DP[i]$表示序列D中最后一个数是排名为 $i$ 的数的最大长度，

+ 如果$i=1,than~dp[i]=1​$，排名为 $i​$ 的最小出现位置小于排名为 $i-1​$的最大出现位置，$than~~dp[i]=1​$+ 否则 $dp[i]=dp[i-1]+1​$


代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int N=3e5+10;
int minp[N],maxp[N];
vector<int> v;
int dp[N];
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;++i)
            minp[i]=-1;
        v.clear();
        for(int i=1;i<=n;++i)
        {
            int x;
            scanf("%d",&x);
            v.push_back(x);
            if(minp[x]==-1) minp[x]=i;
            maxp[x]=i;
        }
        sort(v.begin(),v.end());
        v.erase(unique(v.begin(),v.end()),v.end());
        int ans=n;
        for(int i=0;i<int(v.size());++i)
        {
            if(i==0||minp[v[i]]<maxp[v[i-1]]) dp[i]=1;
            else dp[i]=dp[i-1]+1;
            ans=min(ans,int(v.size())-dp[i]);
        }
        printf("%d\n",ans);
    }
//    for()
    return 0;
}
```


