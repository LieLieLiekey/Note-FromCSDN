

 

### 先放题目


A supermarket has a set Prod of products on sale. It earns a profit px for each product x∈Prod sold by a deadline dx that is measured as an integral number of time units starting from the moment the sale begins. Each product takes precisely one unit of time for being sold. A selling schedule is an ordered subset of products Sell ≤ Prod such that the selling of each product x∈Sell, according to the ordering of Sell, completes before the deadline dx or just when dx expires. The profit of the selling schedule is Profit(Sell)=Σ x∈Sellpx. An optimal selling schedule is a schedule with a maximum profit. For example, consider the products Prod={a,b,c,d} with (pa,da)=(50,2), (pb,db)=(10,1), (pc,dc)=(20,2), and (pd,dd)=(30,1). The possible selling schedules are listed in table 1. For instance, the schedule Sell={d,a} shows that the selling of product d starts at time 0 and ends at time 1, while the selling of product a starts at time 1 and ends at time 2. Each of these products is sold by its deadline. Sell is the optimal schedule and its profit is 80.


![./figures/f9d071d9c472cbda044241e92bee7393](./figures/f9d071d9c472cbda044241e92bee7393)


 Write a program that reads sets of products from an input text file and computes the profit of an optimal selling schedule for each set of products. Input

A set of products starts with an integer 0 <= n <= 10000, which is the number of products in the set, and continues with n pairs pi di of integers, 1 <= pi <= 10000 and 1 <= di <= 10000, that designate the profit and the selling deadline of the i-th product. White spaces can occur freely in input. Input data terminate with an end of file and are guaranteed correct.

Output

For each set of products, the program prints on the standard output the profit of an optimal selling schedule for the set. Each result is printed from the beginning of a separate line.

Sample Input

```
4  50 2  10 1   20 2   30 1

7  20 1   2 1   10 3  100 2   8 2
   5 20  50 10
```


Sample Output

```
80
185```


题意：

给你n个商品，每个商品都有两个参数 v t ，v为该商品卖出后的利润，t表明该商品只能在这个期限卖出。

问你这批商品最多能获得多少利润

 

 

 

 

若不是当时刷的专题是并查集，还真不知道这个题能用并查集嘞！（话说并查集也真是厉害）

刚开始看这个题，自己先想了一波思路，思路中只用了贪心，然后算了下时间复杂度为O（n*n）  ，题中n=1w ,肯定会超时

 

想了半天也不知道怎么用并查集，后来搜了搜博客,,ԾㅂԾ,,，有了并查集的思想，并且认识到这种思想是多么的强大（可以看成树，但是看成链状更容易理解）

 

 

这道题你必须将时间看作离散状的，假设0~7的天数分作 第1天 ，第2天，第 3天， 第4天..................第7天。

分析：

将每个商品数据储存在结构体中，输入数据以后，所有商品按利润从大到小的顺序排列,利润相等的期限长的排在前面.

这样所有商品经这种规则排序后储存在结构体数组中（编号为0~(n-1)），从左到右开始遍历，根据每个商品的期限，找到**离这个期限最近**的且**可占用**的时间，去占用这个时间， 你可以想象一下“占用”后的该时间用一个数组标记一下，表示该时间已“占用”。这样保证每个被占用的时间段它所在的商品都是最佳的。

 

那么怎么实现快速找到 "**离这个期限最近的且可占用的"**时间呢? 假设用一个fahther[]数组来存放这个你所想要的时间，初始状态

father[x]=x，都为自己树上的根，当这个时间用过以后就把这个father[x]=x-1（这个时间用过之后，离这个时间期限最近的时间就是左边的那一个）表示这个时间已经用过，并且把这棵树与左边的一棵树连接起来，

**只有满足father[x]=x，才表明x这个时间段可占用 ()**

 

 

```cpp
#include<stdio.h>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#define N 10000
using namespace std;
int father[N+10];
struct node{
int v,t;
}a[N+10];
void up_date(int n)
{
    for(int i=0;i<=n;i++)
        father[i]=i;
}
int _find(int x)
{
    if(x==father[x])
        return x;
    return father[x]=_find(father[x]);//路径压缩
}
bool cmp(node q,node qq)
{
    if(q.v==qq.v)
        return q.t>qq.t;
    return q.v>qq.v;
}
int main()
{
    int n,ans,maxx=0,root;
    while(~scanf("%d",&n))
    {
        maxx=ans=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d %d",&a[i].v,&a[i].t);
            maxx=maxx>a[i].t?maxx:a[i].t;
        }
        up_date(maxx);
        sort(a,a+n,cmp);
        for(int i=0;i<n;i++)//核心代码
        {
            root=_find(a[i].t);//找这棵树的根，即可用的时间。
            if(root>0)//有可用时间
            {
                ans+=a[i].v;
                father[root]=root-1;
            }
        }
        printf("%d\n",ans);
    }
}
```


 

 

