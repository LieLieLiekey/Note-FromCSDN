

### [J - Vasya and a Tree](https://vjudge.net/problem/CodeForces-1076E) （树状数组+离线处理）


[CodeForces - 1076E ](https://vjudge.net/problem/2028113/origin)

### 题意：


​ 给定有n个点的一棵树，顶点1为根。m次操作，每次都把以v为根，深度dep以内的子树中所有的顶点（包括v本身）加x。求出最后每个点的值为多少

### 思路：


​ 离线处理+树状数组。其中树状数组维护当前深度区间信息。 （终于知道什么是离线查询）


​ 我们可以$D F S DFS$序遍历以$1 1$为根的树，每到一个节点，就根据当前节点的修改信息向下修改，离开该节点就修改回来，这样每到一个节点，影响他状态的只有他的祖宗节点。而当前节点的值也都是只有祖宗节点才能修改，那么当前深度的信息就是该节点应有的信息。

不懂的推荐看代码

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const ll MAXN=3e5+10;
ll MAX=MAXN;
ll n;
vector<ll> adja[MAXN];
vector<P> oper[MAXN];
ll bt[MAXN],res[MAXN];
ll ```


