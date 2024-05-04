## [D - Series-Parallel Networks](https://cn.vjudge.net/problem/UVA-10253)

 [UVA - 10253 ](https://cn.vjudge.net/problem/34527/origin)

题意就不描述了

输入格式：

> ​	输入包含多组式布局，每组数据仅包含一个整数，即边数n（1<=n<=30）。输入结束标志为n=0。

输出格式：

> ​	对于每组数据，输出一行，即包含m条边的串并联网络的数目。



这是白皮书上117页的内容，其中给出了两个算法，第一个算法理解但是有点难实现，第二个算法是真心不懂（但是第二个算法代码确实很简单dp吧）



第一个算法：

> ​	把串并联网络看作一个树，因为每个串联网络一个分成**多个并联网络或者单边** 串联，并联网络可以分成
>
> **多个串联网络或者单边** 并联。可以想想成一棵树的形式，假设刚开始有一个根是一个串连网络（并联网络），下一层全是并联网络（串联网络），就这样交替出现，当然每一棵树的最少得有两个儿子，如果这个棵数是个单边，那么他就是个叶子节点，没有儿子，这样问题就转化为了“共n个叶子，且每个非叶子节点至少有两个子节点”的树的数目f（n）,再乘以2就是本题的答案。
>
>  即找出n个叶子的树有多少种。



因为题目中说串联在一起（并联在一起）的各个部分可以相互调换顺序，相当于每一层的树交换顺序后 属于同一种，所以我们只要保证从**左到右节点数**是**递增或者递减的就可以了**。



假设对于5个叶子的节点，子树可以分为

1 1 1 1 1  

1 1 1  2

1 1 3

1 4

1 2 2

2 3

**把每种的情况全加起来即可**

对于24个叶子的树：

2 10 12 的情况共有 $f(2)*f(10)*f(12)$种方法

对于 6  6   6有多少种方法吗？难道是$f(6)*f(6)*f(6)$ 吗？ 如果是这样那么你就错了，因为可能会有会有重复的，换句话说 6 6 6这三棵树还是可以互换的（而且还是保证序列递增），那么为了保证不重复

这个问题可化为f（6）中选取3个作为一个组合,且可重复的方案数目。即**可重复选取的组合问题**

应该是C（f（6）+3-1，3）种方案



这样这道题就有苗头了：

1.对于求f（n）枚举n的所有整数划分，（因为n并不大，所以这样方法是可行的）

2.对于每个不同的划分求出此划分的方案数目，相加就是f（n）

**这是个递归的求法**

实现代码：

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=30;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
int book[maxn+5];//记忆化，book[k]=1表示f(k)已经求出来了，防止递归计算子问题
ll vis[maxn+5];//存f(k)
ll C(ll a,ll b)//求出组合数目
{
    ll ans=1;
    if(b>a-b)  b=a-b;
    for(ll i=a;i>=a-b+1;--i)//乘以b个
    {
        ans*=i;
    }
    for(ll i=2;i<=b;++i)
        ans/=i;
    return ans;
}
void init()//初始化
{
    mset(book,0);
    book[0]=book[1]=book[2]=1;
    vis[0]=vis[1]=vis[2]=1;
}
ll calc(int n);
ll solve(vector<int>& mmp)//计算这个序列的值
{
    ll ans=1;
    int total=1;
    for(int i=0;i<mmp.size();++i)
    {
        if(i+1<mmp.size()&&mmp[i+1]==mmp[i])
        {
            total++;
            continue;
        }
        ans*=C(calc(mmp[i])+total-1,(ll)total);
        total=1;
    }
    return ans;
}
void dfs(int k,int sum,ll& ans,vector<int>& mmp)//上一个数字最大为k, 还剩sum个未加. ans记录值方案为多少，用于在 sum=0的时候计算
{
    if(sum==0)//开始计算 里面的数字都是从大到小
    {
        ans+=solve(mmp);
    }
    else//继续枚举划分
    {
        for(int i=min(k,sum);i>=1;--i)
        {
            mmp.push_back(i);
            dfs(i,sum-i,ans,mmp);
            mmp.pop_back();
        }
    }
}
ll calc(int n)//求f(n);
{
    if(book[n])
        return vis[n];
    vector<int> mmp;
    ll ans=0;
    for(int i=n-1;i>=1;--i)
    {
        mmp.push_back(i);
        dfs(i,n-i,ans,mmp);
        mmp.pop_back();
    }
    book[n]=1;//记忆化计算 防止重复计算子问题
    vis[n]=ans;
    return ans;
}
int main()
{
    init();
    int n;
    ios::sync_with_stdio(false);
    while(cin>>n,n)
    {
        if(n==1)
            cout<<1<<endl;
        else
            cout<<calc(n)*2<<endl;
    }
}

```



就这样吧，看代码觉得还是第二种简单，但是真心理解不动。