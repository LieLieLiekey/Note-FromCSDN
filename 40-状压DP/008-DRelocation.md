

### D - Relocation


mma and Eric are moving to their new house they bought after returning from their honeymoon. Fortunately, they have a few friends helping them relocate. To move the furniture, they only have two compact cars, which complicates everything a bit. Since the furniture does not fit into the cars, Eric wants to put them on top of the cars. However, both cars only support a certain weight on their roof, so they will have to do several trips to transport everything. The schedule for the move is planed like this:

+ At their old place, they will put furniture on both cars.+ Then, they will drive to their new place with the two cars and carry the furniture upstairs.+ Finally, everybody will return to their old place and the process continues until everything is moved to the new place.


Note, that the group is always staying together so that they can have more fun and nobody feels lonely. Since the distance between the houses is quite large, Eric wants to make as few trips as possible.

Given the weights *wi* of each individual piece of furniture and the capacities *C*1 and *C*2 of the two cars, how many trips to the new house does the party have to make to move all the furniture? If a car has capacity *C*, the sum of the weights of all the furniture it loads for one trip can be at most *C*.

**Input**

The first line contains the number of scenarios. Each scenario consists of one line containing three numbers *n*, *C*1 and *C*2. *C*1 and *C*2 are the capacities of the cars (1 ≤ *Ci* ≤ 100) and *n* is the number of pieces of furniture (1 ≤ *n* ≤ 10). The following line will contain *n* integers *w*1, …, *wn*, the weights of the furniture (1 ≤ *wi* ≤ 100). It is guaranteed that each piece of furniture can be loaded by at least one of the two cars.

**Output**

The output for every scenario begins with a line containing “`Scenario #`*i*`:`”, where *i* is the number of the scenario starting at 1. Then print a single line with the number of trips to the new house they have to make to move all the furniture. Terminate each scenario with a blank line.

**Sample Input**

```bash
2
6 12 13
3 9 13 3 10 11
7 1 100
1 2 33 50 50 67 98
```


**Sample Output**

```bash
Scenario #1:
2

Scenario #2:
3
```


### 题意：


有两个车子，容量分别为c1,c2，现在我有n个家具需要运送，容量分别是w1,w2…wn。要求运送家具的时候两个车子必须一起去，问最少几个来回把家具运完，保证每个家具都能被其中一个车运走

### 分析：


因为车子少，所以用二进制状态0，1来表示是否运走对应家具

首先暴力出车子可以一次运完的状态。然后对可以一次运完的状态进行记忆话化搜索，dfs（state）代表state状态最少需要运的次数。

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
int vis[1<<11],w[10];// vis用来 枚举子集的 物品的重量和，
int n,c1,c2;//n个物品。车子的重载量分别为c1 c2
int state[1<<11],tot;//存放一次可以运走的所有状态
int dp[1<<11];
bool judge(int x)//判断x能否一次运走
{
    /*
    枚举C1一次运走的所有情况，如果同时C2也能一次运走那么可以一次运走
    */
    int top=0;
    vis[0]=0;
    int sum=0;
    for(int i=0;i<n;++i)
        if(x&(1<<i))
            sum+=w[i];
    if(sum<=c1||sum<=c2)
        return 1;
    for(int i=0;i<n;++i)//时间复杂度为2^k(0<=k<=10)
    {
        if(x&(1<<i))//第i个物品存在
        {
            int cnt=top;
            for(int j=0;j<=cnt;++j)//加上前面j个状态
            {
                if(w[i]+vis[j]>c1)//这个c1肯定运不过去，更不用说再在后面加物品了，所以不用加入集合中
                    continue;
                vis[++top]=w[i]+vis[j];
                if(vis[top]<=c1&&sum-vis[top]<=c2)
                    return 1;
            }
        }
    }
    return 0;
}
int dfs(int ss)//此状态，枚举此状态最少需要运多少次
{
    if(!ss)
        return 0;
    if(dp[ss]!=-1)
        return dp[ss];
    int ans=100;
    for(int i=0;i<tot;++i)
    {
        if((ss&state[i])==state[i])
            ans=min(ans,dfs(ss^state[i])+1);
    }
    return dp[ss]=ans;
}
int main()
{
    int t;
    int cas=0;
    scanf("%d",&t);
    while(t--)
    {
        mset(dp,-1);
        scanf("%d%d %d",&n,&c1,&c2);
        for(int i=0;i<n;++i)
            scanf("%d",w+i);
        tot=0;
        for(int i=1;i<(1<<n);++i)//状态0不加入
        {
            if(judge(i))
                state[tot++]=i;
        }
        printf("Scenario #%d:\n",++cas);
        printf("%d\n\n",dfs((1<<n)-1));
    }
    return 0;
}
```


