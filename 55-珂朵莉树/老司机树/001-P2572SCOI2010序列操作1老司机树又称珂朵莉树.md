

## P2572 [SCOI2010]序列操作1(老司机树 又称 珂朵莉树)


#### 题目链接：[传送门](https://www.luogu.org/problem/P2572)


#### 题目：


**题目描述**：

lxhgww最近收到了一个01序列，序列里面包含了n个数，这些数要么是0，要么是1，现在对于这个序列有五种变换操作和询问操作：

0 a b 把[a, b]区间内的所有数全变成0

1 a b 把[a, b]区间内的所有数全变成1

2 a b 把[a,b]区间内的所有数全部取反，也就是说把所有的0变成1，把所有的1变成0

3 a b 询问[a, b]区间内总共有多少个1

4 a b 询问[a, b]区间内最多有多少个连续的1

对于每一种询问操作，lxhgww都需要给出回答，聪明的程序员们，你们能帮助他吗？

**输入格式**：

输入数据第一行包括2个数，n和m，分别表示序列的长度和操作数目

第二行包括n个数，表示序列的初始状态

接下来m行，每行3个数，op, a, b，（0<=op<=4，0<=a<=b<n）表示对于区间[a, b]执行标号为op的操作

**输出格式：**

对于每一个询问操作，输出一行，包括1个数，表示其对应的答案

这道题正解是用线段树的，但线段树写着非常麻烦。

#### 前聊


老司机树又称珂朵莉树，是一个用set维护的数据结构，他的每个节点都是一个具有相同性质的区间。

介绍：[OIwiki](https://oi-wiki.org/ds/odt/)

老司机树多用于区间赋值操作，和在此操作下的其他操作，比如区间不同数有多少个。其时间复杂度在**数据随机**的情况下，挺优的。但如果数据不随机，出题人想卡你，一定能卡成O(n^2logn)…


貌似在数据随机下时间复每次操作大概需要O(n/q)次在set中查找。


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=1e5+20;
struct ODT_tree
{
   
    struct node//闭区间[l,r]
    {
   
        int l,r,v;
        node(int l,int r,int v):l(l),r(r),v(v) {
   }
        node() {
   }
        bool operator < (const node & o) const
        {
   
            return l<o.l;
        }
    };
    int n;
    set<node> odtst;
    typedef set<node>::iterator iter;
    inline void iadd(int l,int r,int v)//init_add
    {
   
        odtst.insert(node(l,r,v));
    }
    iter ```


