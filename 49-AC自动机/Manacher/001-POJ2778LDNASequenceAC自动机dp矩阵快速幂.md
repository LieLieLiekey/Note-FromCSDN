

It's well known that DNA Sequence is a sequence only contains A, C, T and G, and it's very useful to analyze a segment of DNA Sequence，For example, if a animal's DNA sequence contains segment ATC then it may mean that the animal may have a genetic disease. Until now scientists have found several those segments, the problem is how many kinds of DNA sequences of a species don't contain those segments.  Suppose that DNA sequences of a species is a sequence that consist of A, C, T and G，and the length of sequences is a given integer n. 

**Input**

First line contains two integer m (0 <= m <= 10), n (1 <= n <=2000000000). Here, m is the number of genetic disease segment, and n is the length of sequences.  Next m lines each line contain a DNA genetic disease segment, and length of these segments is not larger than 10. 

**Output**

An integer, the number of DNA sequences, mod 100000.

Sample Input

```
4 3
AT
AC
AG
AA
```


**Sample Output**

```
36```


 

困扰我一天的题┭┮﹏┭┮

**题意：**

给你m个序列，每个序列都是一种病毒（反正就是不能有就行了）， 问长度为n的字符串中有多少种不含病毒。

**思路：**

能有啥思路，瞎搞呗

看作有限状态机，每种字符串都有一个状态（一会解释什么状态），每个状态都有A T C G个方向，从而走向不同的状态。含有病毒的状态是不能走的。

**这里的状态是指什么状态？**

每个字符串有一个状态，状态就是与病毒串的匹配程度。

此时我盗一个图**（**参考博客[https://blog.csdn.net/morgan_xww/article/details/7834801](https://blog.csdn.net/morgan_xww/article/details/7834801)**）**

 

这是病毒串 （ACG      C）建立的tire树，每个节点代表一个状态 (红色有向边表示fail指针，蓝色有向边代表状态之间的转移)


![./figures/1344225710_8785.jpg](./figures/1344225710_8785.jpg)


0的话就代表此时的字符串没有跟任何病毒串有一点匹配（该字符串后缀跟病毒的前缀匹配程度 ）

比如  T ，G，T T,  TG, AG ，AT等等

从O节点的状态可以有A T C G的走向 。走A进入状态1，代表与病毒串的匹配程度为状态1；走T进入状态0，代表跟任何病毒序列没有一毛钱关系，走C进入状态4代表病毒串匹配程度为状态4（这个状态是有病毒的），走G进入状态0.

解释下状态2的转移过程

如果一个串处于状态2，那么走A进入状态1，（与病毒串的最大匹配只能为状态1），走T进入状态0，走C进入状态4，走G进入状态0

 

用矩阵dp[i][j]代表走一步从i状态到j状态有多少方法。

那么就得到一个矩阵

2 1 0 0 1

2 1 1 0 0

1 1 0 1 1

2 1 0 0 1

2 1 0 0 1

那么走n步的结果就是求从0状态走n步能到到所有的状态数的方法和就是答案。即j矩阵dp的n次方（快速幂求）

**需要注意的是：**

1.含有病毒串的节点全都要标记成成病毒串

2.不能从含有病毒串的状态走，也不能走含有病毒串的节点（用病毒的继承，和fail指针找后缀就可做到）

**坑点：**

1.矩阵开long long

2.n用long long

 

每种字符串只能由一种状态

AC在状态2

ACG在状态3

ACC在状态4

**所以 步骤**

1.构建字典树

2.建造fail指针,标记病毒节点

3.求状态转移矩阵

4.矩阵快速幂求长度为n不含病毒串的种类数目

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
using namespace std;
typedef long long ll;
const int maxn=100+7;
const int branch=4;
const ll mod=100000;
const int inf=0x3f3f3f3f;
ll Dp_Matrix[maxn][maxn];
struct Node
{
    int cnt;
    int fail;
    int net[branch];
    void clear()
    {
        cnt=0;
        fail=0;
        for(int i=0; i<branch; ++i)
            net[i]=0;
    }
};
class AcTree
{
public:
    Node *node;
    int top;
    AcTree()
    {
        node=new Node[maxn];
        top=0;
        node[0].clear();
    }
    void init()
    {
        top=0;
        node[0].clear();
    }
    int hash_letter(char c)
    {
        switch(c)
        {
        case 'A':
            return 0;
        case 'T':
            return 1;
        case 'C':
            return 2;
        case 'G':
            return 3;
        }
    }
    void insert(char *p)
    {
        int now=0;
        while(*p)
        {
            int i=hash_letter(*p);
            if(!node[now].net[i])
            {
                node[now].net[i]=++top;
                node[top].clear();
            }
            now=node[now].net[i];
            ++p;
        }
        node[now].cnt=1;
    }
    void Bulid_fail()
    {
        queue<int> mmp;
        int now=0,to;
        for(int i=0; i<branch; ++i)
        {
            if(node[0].net[i])
                mmp.push(node[0].net[i]);
        }
        while(!mmp.empty())
        {
            now=mmp.front();
            mmp.pop();
            //为这个 儿子建造fail指针
            if(node[node[now].fail].cnt)//fail含有病毒
                node[now].cnt=1;
            for(int i=0; i<branch; ++i)
            {
                if(node[now].net[i])
                {
                    if(node[now].cnt)//病毒继承
                        node[node[now].net[i]].cnt=1;
                    to=node[now].fail;//为这个 儿子建造fail指针
                    while(to>0&&node[to].net[i]==0)
                        to=node[to].fail;
                    if(node[to].net[i])
                        to=node[to].net[i];
                    node[node[now].net[i]].fail=to;
                    mmp.push(node[now].net[i]);
                }
            }
        }
    }
    void Bulid_Matrix()
    {
        int now, to;
        memset(Dp_Matrix,0ll,sizeof(Dp_Matrix));
        for(int i=0; i<=top; ++i)
        {
            for(int j=0; j<branch; ++j)
            {
//                if(!node[i].net&&!node[node[i].net[j]].cnt)
//                    Dp_Matrix[i][node[i].net[j]]++;
                to=i;
                while(to>0&&node[to].net[j]==0)
                    to=node[to].fail;
                if(node[to].net[j])
                    to=node[to].net[j];
                if(!node[i].cnt &&!node[to].cnt)
                    Dp_Matrix[i][to]++;
            }
        }
    }
    ~AcTree()
    {
        delete []node;
    }
};
void matix_mult(ll a[maxn][maxn],ll b[maxn][maxn],int n)//结果存到a 上
{
    ll ans[maxn][maxn];
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<n; ++j)
        {
            ans[i][j]=0ll;
            for(int k=0; k<n; ++k)
            {
                ans[i][j]=(ans[i][j]+a[i][k]*b[k][j])%mod;
            }
        }
    }
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<n; ++j)
        {
            a[i][j]=ans[i][j];
        }
    }
}
void quick_matrixpow(ll a[maxn][maxn],long long b,int top)//结果存到a 上
{
    ll ans[maxn][maxn];
    memset(ans,0ll,sizeof(ans));
    for(int i=0; i<top; ++i)
        ans[i][i]=1ll;
    while(b)
    {
        if(b&1)
        {
            matix_mult(ans,a,top);
        }
        matix_mult(a,a,top);
        b/=2;
    }
    for(int i=0; i<maxn; ++i)
    {
        for(int j=0; j<maxn; ++j)
        {
            a[i][j]=ans[i][j];
        }
    }
}
int main()
{
    AcTree dch;
    int top;
    int m,ans;
    long long n;
    char str[15];//记录病毒序列
    while(~scanf("%d %lld",&m,&n))
    {
        dch.init();
        for(int i=0; i<m; ++i)
        {
            scanf("%s",str);
            dch.insert(str);
        }
        dch.Bulid_fail();
        dch.Bulid_Matrix();
        top=dch.top;
        quick_matrixpow(Dp_Matrix,n,top+1);
        ans=0;
        for(int i=0; i<=top; ++i)
        {
            ans=(ans+Dp_Matrix[0][i])%mod;
        }
        printf("%d\n",ans);

    }
    return 0;
}
```


 

