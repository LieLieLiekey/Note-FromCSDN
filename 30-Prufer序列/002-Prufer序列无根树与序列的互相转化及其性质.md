

## Prufer序列（无根树与序列的互相转化及其性质）


##### 什么是Prufer序列？


Prufer序列是将一个带有节点编号的无根树转化为一个序列的过程，且每一个无根树唯一的确定一个prufer序列。反过来也成立。


##### Prufer序列的性质



+ 原树中顶点 吧的度数 -1 = 序列中顶点v的出现次数
+ n个顶点的无根树的Prufer序列的长度为n-2
+ 一个Prufer序列与一个无根树一一对应




##### 将无根树转化为Prufer序列


**方法：**

一棵树要得到普吕弗序列，方法是逐次去掉树的顶点，直到剩下两个顶点。考虑树*T*，其顶点为{1, 2, …, *n*}。在第*i*步，去掉标号最小的叶，并把普吕弗序列的第*i*项设为这叶的邻顶点的标号。

一棵树的序列明显是唯一的，而且长为*n* − 2。

**算法：**

**使用的数据结构**：维护一个度数为1的set集合即可.


+ 初始度数为1的集合（所有叶子）.
+ 每次从度数为1的叶子顶点集合中找到编号最小的顶点u，并将其从度数为1的集合中删去。将u连接的顶点v加入prufer序列，删除u连接的所有边。
+ 更新u和v的度数，v的度数为1则加入度数为1的集合。
+ 当加入序列的数的个数为n-2时候停止。否则返回到第二步。



**具体实现：**


时间复杂度为O(nlogn)。代码经过自己的部分测试是正确的，若有人发现bug请在评论区指出，我将尽快进行修改


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int N=1e5+10;
vector<int> prufer;
vector<int> g[N];
int du[N];
/*
输入:顶点个数n和树g[]
输出:prufer序列
*/
void TreeToPrufer(int n,vector<int> g[])//g[]中存储的是无向边,共有n个顶点
{
   
    set<int> leaf;
    mset(du,0);
    prufer.clear();
    for(int u=1;u<=n;++u)
        for(int v:g[u]) du[v]++;
    for(int i=1;i<=n;++i) if(du[i]==1) leaf.insert(i);
    while(prufer.size()!=n-2)
    {
   
        int u=*leaf.begin();
        du[u]=0;
        leaf.erase(leaf.begin());
        for(int v:g[u])
        {
   
            if(!du[v]) continue;
            prufer.push_back(v);
            du[v]--;
            if(du[v]==1) leaf.insert(v);
        }
    }
    printf("following is prufer sequence of tree:\n");
    for(int```


