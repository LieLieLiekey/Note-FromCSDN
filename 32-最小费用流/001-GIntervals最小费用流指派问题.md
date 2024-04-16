

### [G - Intervals](https://vjudge.net/problem/POJ-3680)


[POJ - 3680 ](https://vjudge.net/problem/12877/origin)

#### 题意：


​ 求n个区间，从中选取一些区间，使得每个点最多被覆盖k次，使得权值和最大。

#### 分析：


​ 等效问题：选出一些区间，使得区间分成$k k$个区间集合。每个集合里面区间不相交，要求总权值和最大。

网络流将所有端点排序，相邻节点连接一条费用为$0 0$，容量为$i n f inf$的边，对于每个区间$i i$，$a a$到$b b$端点连接一条费用为$− w [ i ] -w[i]$的边。容量为$1 1$。那么求最小费用流，每一个流都代表一个不重叠的区间选取。其权值和等于费用的相反数。

```cpp
#include<queue>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int maxn=500;//顶点数量
const int inf=0x3f3f3f3f;
/*求n个区间，从中选取一些区间，使得每个点最多被覆盖k次
等效问题：选出一些区间，使得区间分成k个集合。每个集合区间不相交，要求容量最大
网络流将所有端点排序，相邻节点连接一条费用为0，容量为inf的边，对于每个区间i，a到b端点连接一条费用为-w[i]的边。容量为1
那么求最小费用流，每一个流都代表一个不重叠的区间选取。其权值等于费用的相反数
*/
struct edge
{
   
    int to,cap,cost,rev;
    edge() {
   }
    edge(int to,int cap,int cost,int rev)
    {
   
        this->to=to,this->cap=cap,this->cost=cost,this->rev=rev```


