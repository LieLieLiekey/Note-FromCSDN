

 

### Sunny Cup 2003 - Preliminary Round


April 20th, 12:00 - 17:00

#### Problem E: QS Network


 In the planet w-503 of galaxy cgb, there is a kind of intelligent creature named QS. QScommunicate with each other via networks. If two QS want to get connected, they need to buy two network adapters (one for each QS) and a segment of network cable. Please be advised that ONE NETWORK ADAPTER CAN ONLY BE USED IN A SINGLE CONNECTION.(ie. if a QS want to setup four connections, it needs to buy four adapters). In the procedure of communication, a QS broadcasts its message to all the QS it is connected with, the group of QS who receive the message broadcast the message to all the QS they connected with, the procedure repeats until all the QS's have received the message.

A sample is shown below:


![./figures/69b6522925a127184d81d3acb4847b92](./figures/69b6522925a127184d81d3acb4847b92)


 

 A sample QS network, and QS A want to send a message. Step 1. QS A sends message to QS B and QS C; Step 2. QS B sends message to QS A ; QS C sends message to QS A and QS D; Step 3. the procedure terminates because all the QS received the message.

Each QS has its favorate brand of network adapters and always buys the brand in all of its connections. Also the distance between QS vary. Given the price of each QS's favorate brand of network adapters and the price of cable between each pair of QS, your task is to write a program to determine the minimum cost to setup a QS network.

 

Input

 

The 1st line of the input contains an integer t which indicates the number of data sets. From the second line there are t data sets. In a single data set,the 1st line contains an interger n which indicates the number of QS. The 2nd line contains n integers, indicating the price of each QS's favorate network adapter. In the 3rd line to the n+2th line contain a matrix indicating the price of cable between ecah pair of QS.

Constrains:

all the integers in the input are non-negative and not more than 1000.

 

 

Output

 

for each data set,output the minimum cost in a line. NO extra empty lines needed.

 

Sample Input

 

1 3 10 20 30 0 100 200 100 0 300 200 300 0

Sample Output

 

370

 

 

 

 

 

```cpp
/*

题意有点扯淡。
两个QS之间通信不仅需要电缆还要买适配器，并且一个适配器只能保证他与一个QS通信
所以这是一个简单的最小生成树问题，即连接任意两个顶点的费用=这两点之间的电缆费用+两个顶点的适配器费用和
*/

#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<queue>
#define N 1000100
#define INF 0x3f3f3f3f
#define mem(a,b) memset(a,b,sizeof(a))
#define ABS(a) a>=0?a:-a
using namespace std;
int father[1100],price[1100];
struct node
{
    int a,b,u;
} e[N];
bool cmp(node q,node qq)
{
    return q.u<qq.u;
}
int _find(int x)
{
    if(x==father[x])
        return x;
    father[x]=_find(father[x]);
    return father[x];
}
void up_date(int n)
{
    for(int i=1; i<=n; i++)
        father[i]=i;
}
bool _check(int a,int b)//检测是否在一个集合内 1不在集合让其在一个集合内  and merge
{
    int root1,root2;
    root1=_find(a);
    root2=_find(b);
    if(root1==root2)
        return 0;
    father[root1]=root2;
    return 1;
}
int main()
{
    int n,u,cnt=0,ans=0,t;
    scanf("%d",&t);
    while(t--)
    {
        ans=cnt=0;
        scanf("%d",&n);
        up_date(n);
        for(int i=1;i<=n;i++)
            scanf("%d",&price[i]);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=i;j++)
                scanf("%d",&u);
            for(int j=i+1;j<=n;j++)
            {
                scanf("%d",&u);
                e[cnt].a=i;
                e[cnt].b=j;
                e[cnt++].u=u+price[i]+price[j];
            }
        }
        sort(e,e+cnt,cmp);
        for(int i=0;i<cnt;i++)
        {
            if(_check(e[i].a,e[i].b))
                ans+=e[i].u;
        }
        printf("%d\n",ans);
    }
}```


 

 

