

求异或最大值

 

因为最近再刷字典树，所以直接想到一个树形方法(ˉ▽ˉ；)...

**1.把每个数字的二进制表达式当作一个字符串插入字典树中**

**2.**

    (1).从顶节点开始，和要求的数val的最大位数开始(第32位开始)

    (2).根据当前节点now，和当前位数k，找出下一节点（如果有与该位不同的边走则走那条边，否则走与此位相同的边），并赋给           now  

    (3).让k--，并找出当前位数的比特值

    (4).返回(2) ，直至k=0退出

**3.记下路径**

**4.求出异或最大值就OK**

 

代码：

```cpp
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
using namespace std;
const int maxn=5000000;
typedef struct Tire_Node
{
//    int cnt;
    int net[2];
    Tire_Node()
    {
//        cnt=0;
        for(int i=0; i<2; ++i)
            net[i]=-1;
    }
    void clear()
    {
//        cnt=0;
        for(int i=0; i<2; ++i)
            net[i]=-1;
    }
} node;
node nodearr[maxn];
int nodetop;
int ans[50];
int Get_bit(int n,int k)
{
    if(n&(1<<(k-1)))
        return 1;
    return 0;   
}
void Become_bit(int &val,int k,int bit)
{
    if(bit)
        val=val|(1<<(k-1));
    else
        val=val&(~(1<<(k-1)));
}
void insert_node(int n)
{
   int flag;
   int now=0;
   for(int i=32;i;--i)
   {
       flag=Get_bit(n,i);
       if(nodearr[now].net[flag]==-1)
       {
           nodearr[now].net[flag]=++nodetop;
       }
       now=nodearr[now].net[flag];
   }
}
void clear_node(int num)
{
    for(int i=0;i<=num;++i)
        nodearr[i].clear();
}
int bfs(int now,int b_val,int k)// 在now节点下面 根据自己的位数v_bal，找到第k位
{
    if(~nodearr[now].net[b_val?0:1])
    {
        ans[k]=b_val?0:1;
        return nodearr[now].net[b_val?0:1];
    }
    else
    {
       ans[k]=b_val;
       return nodearr[now].net[b_val];
    }
}
void Slove(int val)//求字典树中与val 异或最大的值
{
    int now=0;
    for(int i=32;i>=1;--i)
        now=bfs(now,Get_bit(val,i),i);
}
int main()
{
    int t,n,m,val,times=0,res;
    scanf("%d",&t);
    while(t--)
    {
        nodetop=0;
        scanf("%d %d",&n,&m);
        for(int i=0;i<n;++i)
        {
             scanf("%d",&val);
             insert_node(val);
        }
        printf("Case #%d:\n",++times);
        while(m--)
        {
            scanf("%d",&val);
            Slove(val);
            for(int i=1;i<=32;++i)
                Become_bit(res,i,ans[i]);
            printf("%d\n",res);
        }
        clear_node(nodetop);
    }
}
```


 

