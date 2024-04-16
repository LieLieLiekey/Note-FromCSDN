

## 980E. The Number Games（倍增，思维）


##### 题目链接：[传送门](https://codeforces.com/problemset/problem/980/E)


##### 思路：


​ 我们转化为，从一颗树上选n-k个点，使得贡献最大，且这n-k个点两两连通。贪心的取，我们必定先取大的（因为如果可以取大的但不取必亏）。

​ 我们可以将原图变为以n为根的有根树，首先n号点必选，我们接下来探讨下面选点，我们建立倍增数组，$fa[u][i]$代表u的第$2^i$个祖先的编号，我们看编号为$n-1$的点。

如果编号为$n-1$到编号为 $n$ 的点的数量小于剩下可选的点的数量，那就不能选。

否则，我们选$n-1$号点，为了连通性， $n-1$号点到$n$号点之间的点都要选。

我们将选的点进行标记。

所以我们有一个算法：

先选编号为n的点，然后遍历剩下编号为的点（从大到小），假设此时编号为$i$，如果编号为$i$的点已经被选，则跳过，否则倍增找祖先没有被标记的最小的近的祖先，（为什么是祖先呢？，因为被标记的不可能是 i 的儿子，否则他就被选了）那么找最近被标记的点就可以用倍增。

如果之间点的数量小于可选的点的数量，就不选。否则就选，并选其之间的点。

```cpp
#include<bits/stdc++.h>
#define mse(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e6+10;
vector<int> g[N];
int book[N];
int fa[N][20];
void bfs(int root)
{
    queue<int> qe;
    qe.push(root);
    fa[root][0]=root;
    while(!qe.empty())
    {
        int u=qe.front();qe.pop();
        for(int i=1;i<20;++i) fa[u][i]=fa[fa[u][i-1]][i-1];
        for(int v:g[u])
        {
            if(v==fa[u][0]) continue;
            fa[v][0]=u;
            qe.push(v);
        }
    }
}
int mincost(int v)
{
    int ans=0;
    if(book[fa[v][0]]) return 1;
    int wv=v;
    for(int i=19;i>=0;--i)
    {
        if(book[fa[wv][i]]) continue;
        ans+=1<<i;
        wv=fa[wv][i];
    }
    return ans+1;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    cout.tie(0);
    int n,k;
    cin>>n>>k;
    for(int i = 1; i < n; ++i)
    {
        int u,v;
        cin>>u>>v;;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    k=n-k-1;
    bfs(n);
    book[n]=1;
    for(int i=n-1;i>=1&&k;--i)
    {
        if(book[i]) continue;
        int m=mincost(i);
        if(m<=k)
        {
            k-=m;
            int wv=i;
            while(!book[wv]){
                book[wv]=1;
                wv=fa[wv][0];
            }
        }
    }
    for(int i=1;i<=n;++i)
    {
        if(!book[i])
            cout<<i<<" ";
    }
    cout<<endl;
    return 0;
}
```


