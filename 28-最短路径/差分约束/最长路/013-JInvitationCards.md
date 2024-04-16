

**待更新..........**

题目：

In the age of television, not many people attend theater performances. Antique Comedians of Malidinesia are aware of this fact. They want to propagate theater and, most of all, Antique Comedies. They have printed invitation cards with all the necessary information and with the programme. A lot of students were hired to distribute these invitations among the people. Each student volunteer has assigned exactly one bus stop and he or she stays there the whole day and gives invitation to people travelling by bus. A special course was taken where students learned how to influence people and what is the difference between influencing and robbery. The transport system is very special: all lines are unidirectional and connect exactly two stops. Buses leave the originating stop with passangers each half an hour. After reaching the destination stop they return empty to the originating stop, where they wait until the next full half an hour, e.g. X:00 or X:30, where 'X' denotes the hour. The fee for transport between two stops is given by special tables and is payable on the spot. The lines are planned in such a way, that each round trip (i.e. a journey starting and finishing at the same stop) passes through a Central Checkpoint Stop (CCS) where each passenger has to pass a thorough check including body scan. All the ACM student members leave the CCS each morning. Each volunteer is to move to one predetermined stop to invite passengers. There are as many volunteers as stops. At the end of the day, all students travel back to CCS. You are to write a computer program that helps ACM to minimize the amount of money to pay every day for the transport of their employees.

Input

The input consists of N cases. The first line of the input contains only positive integer N. Then follow the cases. Each case begins with a line containing exactly two integers P and Q, 1 <= P,Q <= 1000000. P is the number of stops including CCS and Q the number of bus lines. Then there are Q lines, each describing one bus line. Each of the lines contains exactly three numbers - the originating stop, the destination stop and the price. The CCS is designated by number 1. Prices are positive integers the sum of which is smaller than 1000000000. You can also assume it is always possible to get from any stop to any other stop.

Output

For each case, print one line containing the minimum amount of money to be paid each day by ACM for the travel costs of its volunteers.

Sample Input

```
2
2 2
1 2 13
2 1 33
4 6
1 2 10
2 1 60
1 3 20
3 4 10
2 4 5
4 1 50```


Sample Output

```
46
210```


 

推荐博客：[https://www.cnblogs.com/liuxin13/p/4656746.html](https://www.cnblogs.com/liuxin13/p/4656746.html)

 

 

```cpp
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
#include<queue>
#define N 1000000
#define INF 0x03ffffffffffffff;
using namespace std;
struct node{
    int u,v,w,next;
}e[N+10];
int head[N+10],book[N+10];
long long dis[N+10],sum[N+10];//book表示该顶点有没有进入队列
void Add(int u,int v,int w,int k)//将特征元素为u的连接到一条链上，并且将对应结构体数据改为从u松弛的
{
    e[k].u=u;
    e[k].v=v;
    e[k].w=w;
    e[k].next=head[u];
    head[u]=k;
}
void spfa_quick()
{
    int u,k;//u松弛  k实现链表
    long long mid;
    queue<int>mmp;
    mmp.push(1);//将松弛点加入队列
    book[1]=1;
    while(!mmp.empty())
    {
        u=mmp.front();
        k=head[u];
        while(k!=-1)//遍历链上的数据//k为此时链上的下标
        {
            mid=dis[e[k].u]+e[k].w;
            if(mid<dis[e[k].v])
            {
                dis[e[k].v]=mid;
                if(!book[e[k].v])
                {
                    mmp.push(e[k].v);
                    book[e[k].v]=1;
                }
            }
            k=e[k].next;
        }
        mmp.pop();
        book[u]=0;
    }
}
int main()
{
    int t,n,m,u,v,w;
    long long ans;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&n,&m);
        for(int i=1;i<=n;i++)//
            head[i]=-1;
        for(int i=1;i<=m;i++)
        {
            scanf("%d %d %d",&u,&v,&w);
            Add(u,v,w,i);
        }
        for(int i=1;i<=n;i++)
        {
            dis[i]=INF;
            book[i]=0;
        }
        dis[1]=0;
        spfa_quick();
        for(int i=1;i<=n;i++)//存下去的路径 初始化head  初始化DIS
        {
//            printf("1->i dis[%d]=%d\n",i,dis[i]);
            sum[i]=dis[i];
            dis[i]=INF;
            head[i]=-1;
        }
        dis[1]=0;
        for(int i=1;i<=m;i++)//填上表
            Add(e[i].v,e[i].u,e[i].w,i);
//        printf("atter.....\n");
        spfa_quick();
        for(int i=1;i<=n;i++)//此时就计算好总路径1到i的来回路径最小和
        {
//            printf("i->1  dis[%d]=%d\n",i,dis[i]);
             sum[i]+=dis[i];
        }
        ans=0;
        for(int i=2;i<=n;i++)
            ans+=sum[i];
        printf("%lld\n",ans);
    }
}
```


 

 

