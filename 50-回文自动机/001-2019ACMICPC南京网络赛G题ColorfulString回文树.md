

#### 题目链接：[ 传送门](https://nanti.jisuanke.com/t/41389)


#### 题意：


一个字符串的价值为其字符串中出现字符的种类个数，现在给你一个字符串S，求S中所有回文串的价值。

#### 思路：


我们可以构建一颗回文树，并且在构建过程记录每个回文串节点中字符种类个数。最后遍历所有不同的回文串节点统计和即可。 代码：

```cpp
#include <bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=3e5+10;
struct PA_tree
{
   
    static const int branch=26;
    static const int MAXN=3e5+10;
    struct Node //每个节点代表一个回文串
    {
   
        ll len,cnt;//回文串的长度,回文串出现次数
        int next[branch],fail;
        int book[branch],dif;
        //next[c]:该节点左右增加字符c的回文串节点位置,默认为0
        //fail :该节点非本身的最长回文后缀节点
    } node[MAXN];
    int ls,top=0;//长度,此时使用的节点个数
    char *s;//字符首指针,下标从1开始
    int initnode(int id)//需要手动初始化fail和len
    {
   
        node[id].cnt=0;
        mset(node[id]```


