# HDU - 3706 Second My Problem First （单调队列）

> 这题与洛谷的滑动窗口那题比较像,不过那题是维护两个单调队列，不过这题只能用线性的方法做。而且还不能开1e7的数组，会MLE.

**题目：**

[传送门]:<http://acm.hdu.edu.cn/showproblem.php?pid=3706>

**题意：**

​	给出一个n，A，B。其中$S_i=A^i \% B$  ,$T_i=Min(S_k), i-A <= k <= i, k >= 1$ ,

**思路：**

​	求对于$T_i$，求S中下标$[i-A,i]$中的最小值，我们那么前面大于$S_i$就可以舍去。这刚好符合单调队列的性质。所以可以为维护一个最小值单调队列。如果队首的下标小于i-A，就出队。

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
deque<P> q;
const int maxn=1e7+10;
ll S[maxn];
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll n,A,B;
    while(cin>>n>>A>>B)
    {
        q.clear();
        ll pdt=1,lasts=1ll;;//lasts记录上一次s的值
        for(ll i=1;i<=n;++i){
         ll val=lasts*A%B;
         lasts=val;
         ll l=max(i-A,1ll);
         while(!q.empty()&&q.back().second>=val) q.pop_back();
         q.push_back({i,val});
         while(!q.empty()&&q.front().first<l) q.pop_front();
         pdt=pdt*q.front().second%B;
        }
        cout<<pdt<<endl;
    }
    return 0;
}
```
