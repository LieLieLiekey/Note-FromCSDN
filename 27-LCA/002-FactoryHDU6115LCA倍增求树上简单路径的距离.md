

### Factory HDU - 6115（LCA倍增，求树上简单路径的距离）


##### 题目:[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=6115)


这题其实暴力LCA即可

##### 代码 :


```cpp
/*
暴力枚举两公司的所有顶点即可。
    求树上的两点到lca的距离
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
const int DEG=20;
vector<P> g[N];
int fa[N][DEG+1],deg[N];
int dis[N][DEG+1];
void bfs(int root)
{
   
    queue<int> Q;
    Q.push(root);
    fa[root][0]=root;
    dis[root][0]=0;
    deg[root]=0;
    while(!Q.empty())
    {
   
        int u=Q.front();
        Q.pop();
        for(int i=1; i<=DEG```


