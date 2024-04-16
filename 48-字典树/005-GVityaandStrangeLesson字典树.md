

### [G - Vitya and Strange Lesson](https://cn.vjudge.net/problem/CodeForces-842D)


[CodeForces - 842D ](https://cn.vjudge.net/problem/1046355/origin) src="https://cn.vjudge.net/problem/description/89614?1540820430000" width="100%" height="900px" scrolling="no"> 

题意：给你一个数组，让数组里面的值都异或一下x，并构成一个新的数组，求这个数组的mex

mex的含义：不在数组中的最小正整数。

思路：

异或的交换律

1.首先我们知道，异或x之后得到的数组将其再异或y值得到的数组，其实就是原数组异或（x^y）的结果。所以这里我们没有必要将原数组进行变化。

异或的唯一性即 a^b=c 如果b，c确定则a就确定

2.我们将原数组中不存在的数入树。那么对于每一个查询temp，其实就相当于我们在树上找一个值，使得这个值亦或temp最小。（如果此处不懂，请看最后面）

3.找出异或最小值即可

**那么这个数的范围怎么确定呢？**题中所有数据的范围都在0~3e5之间，即二进制第25位之前的全为0，

所以数组中的数与x异或后的数也都满足第二进制第25位之前的全为0，那么所求的mex的二进制的第25位之前也全为0，a^b=c b c满足这样，所以a的进制的第25位之前也全为0，

即要求原数组中不存在的数的范围最下为2^25即可(这样的1~25位的的二进制所有情况全部枚举，答案肯定是与其中一个异或)

```
#include<iostream>
#include<string.h>
#include<string>
#include<stdio.h>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
const int maxn=10000010;
const int maxval=524288;
int ans[40];
int book[maxval];
struct Node{
    int net[2];
    Node()
    {
        clear();
    }
    void clear()
    {
      net[0]=net[1]=-1;
    }
}node[maxn];
int top;
void clear_tree(int &top)//清空树
{
    for(int i=0;i<=top;++i)
        node[i].clear();
    top=0;
}
int Getbit(int &val,int k)//val的第k位是多少
{
    if(val&(1<<(k-1)))
        return 1;
    return 0;
}
void Becomebit(int &val,int k,int BitVal)//将val的第k位变为BitVal
{
    if(BitVal)
        val=val|(1<<(k-1));
    else
        val=val&(~(1<<(k-1)));
}
void insert_node(int &val)//将val的二进制位从高到低插入进字典树内
{
    int now=0;
    for(int i=32;i;--i)
    {
        if(node[now].net[Getbit(val,i)]==-1)
            node[now].net[Getbit(val,i)]=++top;
        now=node[now].net[Getbit(val,i)];
    }
}
int dfs(int now,int bit,int k)//根据当前节点和位数返回下一个节点  并且记下选的位数
{
    if(~node[now].net[bit])
    {
        ans[k]=bit;
        return node[now].net[bit];
    }
    ans[k]=bit?0:1;
    return node[now].net[bit?0:1];
}
int Solve(int &val)//x的值不能改变
{
    int now=0;
    for(int i=32;i;--i)
    {
      now=dfs(now,Getbit(val,i),i);//this?
    }
    int res;
    for(int i=32;i;--i)
      Becomebit(res,i,ans[i]);
    return res;
}
int main()
{
    int x,n,m;
    scanf("%d %d",&n,&m);
    memset(book,0,sizeof(book));
    for(int i=0;i<n;++i)
    {
        int mid;
        scanf("%d",&mid);
        book[mid]=1;
    }
    x=0;
    for(int i=0;i<=maxval;++i)
        if(!book[i])
           insert_node(i);//this?
    while(m--)
    {
        int mid;
        scanf("%d",&mid);
        x^=mid;
        printf("%d\n",x^Solve(x));
    }
}

```


参考博客 [https://blog.csdn.net/mengxiang000000/article/details/77718605](https://blog.csdn.net/mengxiang000000/article/details/77718605)

为什么与**原数组异或x后的数组的mex**是**不在原数组中的数与x异或的最小值**？

假设现在数组a与x异或得到数组c 那么因为异或的唯一性，不在数组c的值构成的集合**即为**不在数组a的值与x异或构成的集合，（因为在数组a的值与x异或一定在数组c中） 
![./figures/2018110110332253.png](./figures/2018110110332253.png)


