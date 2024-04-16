

题目：

 

The Borg is an immensely powerful race of enhanced humanoids from the delta quadrant of the galaxy. The Borg collective is the term used to describe the group consciousness of the Borg civilization. Each Borg individual is linked to the collective by a sophisticated subspace network that insures each member is given constant supervision and guidance. Your task is to help the Borg (yes, really) by developing a program which helps the Borg to estimate the minimal cost of scanning a maze for the assimilation of aliens hiding in the maze, by moving in north, west, east, and south steps. The tricky thing is that the beginning of the search is conducted by a large group of over 100 individuals. Whenever an alien is assimilated, or at the beginning of the search, the group may split in two or more groups (but their consciousness is still collective.). The cost of searching a maze is definied as the total distance covered by all the groups involved in the search together. That is, if the original group walks five steps, then splits into two groups each walking three steps, the total distance is 11=5+3+3.

Input

On the first line of input there is one integer, N <= 50, giving the number of test cases in the input. Each test case starts with a line containg two integers x, y such that 1 <= x,y <= 50. After this, y lines follow, each which x characters. For each character, a space `` '' stands for an open space, a hash mark ``#'' stands for an obstructing wall, the capital letter ``A'' stand for an alien, and the capital letter ``S'' stands for the start of the search. The perimeter of the maze is always closed, i.e., there is no way to get out from the coordinate of the ``S''. At most 100 aliens are present in the maze, and everyone is reachable.

Output

For every test case, output one line containing the minimal cost of a succesful search of the maze leaving no aliens alive.

Sample Input

```
2
6 5
##### 
#A#A##
# # A#
#S  ##
##### 
7 7
#####  
#AAA###
#    A#
# S ###
#     #
#AAA###
#####  
```


Sample Output

```
8
11```


 

 

 

题意：这个题很抽象，真的很抽象，我按我的意思理解解释一下

**在走到S或者将外星人消灭后可以分身（也可以不分身），你把这些外星人全部消灭时你走的步数和你分身走的步数之和最小的就是所要求的答案**

**那么将S A堪称顶点，求任意两个顶点的距离（一定要是最短的，所以用到了BFS），然后把这些全部都连接起来所得的权值之和最小就是答案，即最小生成树**。

 

数据坑，本来一发就AC的题硬是坑了十几次RE，

 

 

 

```cpp
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<queue>
#define N  60  //代表迷宫最大边长 但是顶点数不会超过100
#define MAXX 2600
#define INF 0x3f3f3f3f
#define ABS(a) a>=0?a:-a
using namespace std;
int map[MAXX][MAXX],vis[N][N],dir[][4]={{-1,0},{0,-1},{0,1},{1,0}},a[N][N],dis[MAXX],book[MAXX]; //a[i][j]的值表示地图上这个点的编号，如果值为-1表示这个不是一个顶点（从1开始编号）
char maze[N][N];//输入地图
struct node
{
    int x,y,step;
};
queue<node>mmp;
void init_vis(int n,int m)
{
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            if(maze[i][j]=='#')
                vis[i][j]=1;
            else
                vis[i][j]=0;
        }
    }
}
int prim(int cnt)
{
    int t=cnt-1,minn,u,ans=0;
    for(int i=1;i<=cnt;i++)
    {
        dis[i]=map[1][i];
        book[i]=0;
    }
    book[1]=1;
    while(t--)
    {
        minn=INF;
        for(int i=1;i<=cnt;i++)
        {
            if(!book[i]&&dis[i]<minn)
            {
                minn=dis[i];
                u=i;
            }
        }
        ans+=dis[u];
        book[u]=1;
        for(int i=1;i<=cnt;i++)
            if((!book[i])&&dis[i]>map[u][i])
                dis[i]=map[u][i];
    }
    return ans;
}
void bfs(int x,int y)//x y坐标处的顶点与其他顶点的距离全部记下
{
    int u,v;//u到v的路径
    while(!mmp.empty())mmp.pop();
    struct node qq;
    qq.x=x;
    qq.y=y;
    qq.step=0;
    u=a[x][y];
    vis[x][y]=1;//不能走的变为1
    mmp.push(qq);
    while(!mmp.empty())
    {
        struct node mm;
        int xx,yy,ss;
        mm=mmp.front();
        mmp.pop();
        xx=mm.x;
        yy=mm.y;
        ss=mm.step;
        if(a[xx][yy]!=-1)
        {
            v=a[xx][yy];
            map[u][v]=ss;
        }
        for(int i=0; i<4; i++)
        {
            if(!vis[xx+dir[i][0]][yy+dir[i][1]])
            {
                struct node mm;
                mm.x=xx+dir[i][0];
                mm.y=yy+dir[i][1];
                mm.step=ss+1;
                vis[mm.x][mm.y]=1;
                mmp.push(mm);
            }
        }//共cnt个点
    }
}
int main()
{
    int t,m,n,cnt;//n行每行m个
    scanf("%d",&t);
    while(t--)
    {
        cnt=0;
        memset(a,-1,sizeof(a));
        scanf("%d %d",&m,&n);
        gets(maze[0]);//就是这里，我把它换成fflush（stdin）就不行

        for(int i=0; i<n; i++)
        {
            gets(maze[i]);
            for(int j=0; j<m; j++)
            {
                if(maze[i][j]=='A'||maze[i][j]=='S')
                    a[i][j]=++cnt;
            }
        }
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(a[i][j]!=-1)
                {
                    init_vis(n,m);
                    bfs(i,j);//从i，j这个地方开始搜索
                }
            }
        }
        printf("%d\n",prim(cnt));
    }
}
```


 

 



The island nation of Flatopia is perfectly flat. Unfortunately, Flatopia has a very poor system of public highways. The Flatopian government is aware of this problem and has already constructed a number of highways connecting some of the most important towns. However, there are still some towns that you can't reach via a highway. It is necessary to build more highways so that it will be possible to drive between any pair of towns without leaving the highway system. Flatopian towns are numbered from 1 to N and town i has a position given by the Cartesian coordinates (xi, yi). Each highway connects exaclty two towns. All highways (both the original ones and the ones that are to be built) follow straight lines, and thus their length is equal to Cartesian distance between towns. All highways can be used in both directions. Highways can freely cross each other, but a driver can only switch between highways at a town that is located at the end of both highways. The Flatopian government wants to minimize the cost of building new highways. However, they want to guarantee that every town is highway-reachable from every other town. Since Flatopia is so flat, the cost of a highway is always proportional to its length. Thus, the least expensive highway system will be the one that minimizes the total highways length.

Input

The input consists of two parts. The first part describes all towns in the country, and the second part describes all of the highways that have already been built. The first line of the input file contains a single integer N (1 <= N <= 750), representing the number of towns. The next N lines each contain two integers, xi and yi separated by a space. These values give the coordinates of i th town (for i from 1 to N). Coordinates will have an absolute value no greater than 10000. Every town has a unique location. The next line contains a single integer M (0 <= M <= 1000), representing the number of existing highways. The next M lines each contain a pair of integers separated by a space. These two integers give a pair of town numbers which are already connected by a highway. Each pair of towns is connected by at most one highway.

Output

Write to the output a single line for each new highway that should be built in order to connect all towns with minimal possible total length of new highways. Each highway should be presented by printing town numbers that this highway connects, separated by a space. If no new highways need to be built (all towns are already connected), then the output file should be created but it should be empty.

Sample Input

```
9
1 5
0 0 
3 2
4 5
5 1
0 4
5 2
1 2
5 3
3
1 3
9 7
1 2```


 

Sample Output

```
1 6
3 7
4 9
5 7
8 3```


 

题意：给你这n个城镇的坐标，和其中一些城镇之间的高速公路，，让你再修建几条公路使得所有城镇都连通在一起。使得总路径最短，输出时输出两个城镇代表这两个城镇之间建造了一条公路，即输出你建造的公路。

分析：最短路的思路，只不过要优化，不然会超时。

代码：

 

```cpp
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
int father[1100],vis[1010][2];
struct node
{
    int a,b;
    double u;
} e[N];
struct coord
{
    double x,y;
} point[1010];
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
double distant(double x1,double y1,double x2,double y2)
{
    x1=x1-x2;
    y1=y1-y2;
    return sqrt(x1*x1+y1*y1);
}
int main()
{
    int n,m,a,b,cnt=0,sign=0,flag=0;//sign表示自己修建公路的个数，flag表示最小生成树中已经有几条边了
    scanf("%d",&n);
    up_date(n);
    for(int i=1; i<=n; i++)
        scanf("%lf %lf",&point[i].x,&point[i].y);
    scanf("%d",&m);
    while(m--)
    {
        scanf("%d %d",&a,&b);
        if(_check(a,b))
            flag++;
    }
    for(int i=1; i<=n; i++)
        for(int j=i+1; j<=n; j++)
        {
            if(_find(i)==_find(j))//没有必要计算的边就不计算（在同一集合）
                continue;
            e[cnt].a=i;
            e[cnt].b=j;
            e[cnt++].u=distant(point[i].x,point[i].y,point[j].x,point[j].y);
        }
    sort(e,e+cnt,cmp);
    for(int i=0; i<cnt; i++)
    {
        if(_check(e[i].a,e[i].b))
        {
            vis[sign][0]=e[i].a;
            vis[sign++][1]=e[i].b;
            flag++;
        }
        if(flag+1==n)//提前退出
            break;
    }
    for(int i=0; i<sign; i++)
        printf("%d %d\n",vis[i][0],vis[i][1]);
}
```


 

 

 

 



 

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


 

 

