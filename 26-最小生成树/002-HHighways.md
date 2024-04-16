

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


 

 

 

 

