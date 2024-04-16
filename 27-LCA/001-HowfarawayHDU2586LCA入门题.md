

### How far away ？ HDU - 2586(LCA入门题)


##### 题目:[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=4547)


思路见注释

##### 代码 :


```cpp
/*
求树上无向图的两点简单路径距离距离
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
const int DEG=20;
vector<P> g[N];//v,w=(first,second)
int fa[N][DEG+1],deg[N];
int dis[N][DEG+1];//dis[u][i]为u到2^i个祖先的路径和
void bfs(int root)
{
   
    queue<int> Q;
    Q.push(root);
    fa[root][0]=root;
    dis[root][0]=0;
    deg[root```


