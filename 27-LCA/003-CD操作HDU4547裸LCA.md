

### CD操作 HDU - 4547（裸LCA）


##### 题目:[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=4547)


思路见注释

##### 代码 :


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
const int DEG=20;
vector<int> g[N];
int fa[N][DEG+1],deg[N],du[N];
unordered_map<string,int> mmp;
int tol;
int getid(string s)
{
   
    if(mmp[s]==0){
   
        mmp[s]=++tol;
        return tol;
    }
    return mmp[s];
}
void bfs(int root)
{
   
    queue```


