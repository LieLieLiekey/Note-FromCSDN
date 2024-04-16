

 

题目：

You have just moved from a quiet Waterloo neighbourhood to a big, noisy city. Instead of getting to ride your bike to school every day, you now get to walk and take the subway. Because you don't want to be late for class, you want to know how long it will take you to get to school. You walk at a speed of 10 km/h. The subway travels at 40 km/h. Assume that you are lucky, and whenever you arrive at a subway station, a train is there that you can board immediately. You may get on and off the subway any number of times, and you may switch between different subway lines if you wish. All subway lines go in both directions.

Input

Input consists of the x,y coordinates of your home and your school, followed by specifications of several subway lines. Each subway line consists of the non-negative integer x,y coordinates of each stop on the line, in order. You may assume the subway runs in a straight line between adjacent stops, and the coordinates represent an integral number of metres. Each line has at least two stops. The end of each subway line is followed by the dummy coordinate pair -1,-1. In total there are at most 200 subway stops in the city.

Output

Output is the number of minutes it will take you to get to school, rounded to the nearest minute, taking the fastest route.

Sample Input

```
0 0 10000 1000
0 200 5000 200 7000 200 -1 -1 
2000 600 5000 600 10000 600 -1 -1```


Sample Output

```
21```


 

 

 

 

题目大意：

先输入两个点的坐标是self and School的坐标

然后输入一系列的坐标，其中以-1 -1结尾的表示之前的坐标是在一个地铁线上，地铁的运行速度是40km/h.

坑点：

1.输入数据是距离单位是m，让你求的时间的单位是分钟。而题中的速度是km/h，所以需要转化一下

2.在同一地铁线上，两个地铁站不能直接建造“地铁线路”，因为这两点的地铁线路可能是折线（到另一个地铁站必须按照地铁的线路去），当然两个地铁站之间可以选择步行到达。

3.最扯淡的也就是数据的输入方式。看完输入就搜博客去了,,ԾㅂԾ,,

 

题解：

将所有坐标都编上号1~n 其在同一条线路上的地铁都将坐标用一个相同的特征元素标记（那么不同地铁线上的特种元素标记的值肯定不同），然后求任意两个点坐标直接通过所用的时间，最后用dijkstra求1->2的最短时间即可（数据要四舍五入）。

 

 

```cpp
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
#define N 250
#define INF 0x7fffffff
using namespace std;
const double vb=10.0*1000/60.0;//Step   速度  m/分钟
const double vs=40.0*1000/60.0;//Subway 速度  m/分钟
double map[N][N],dis[N];//从i到j所用的时间
int book[N];
struct node {
    int  x,y,k;//K为特征元素
}point[N]; //把位置看成点 //结构体下标就是点的编号
double _distant(double x1,double y1,double x2,double y2)
{
    x1=x1-x2;
    y1=y1-y2;
    return sqrt(x1*x1+y1*y1);
}
void dijkstra(int n)
{
    int t=n-1,u;
    double mid,minn;
    while(t--)
    {
        minn=INF;
        for(int i=1;i<=n;i++)
        {
            if((!book[i])&&dis[i]<minn)
            {
                minn=dis[i];
                u=i;
            }
        }
        book[u]=1;
        if(u==2)
            return ;
        for(int i=1;i<=n;i++)
        {
            mid=dis[u]+map[u][i];
            if(mid<dis[i])
                dis[i]=mid;
        }
    }
}
int main()
{
    int cnt=1,k=1;//k表示不同的种类数//同一种类的是在同一线路上
    double mid;
    scanf("%d %d",&point[cnt].x,&point[cnt].y);
    point[cnt++].k=k++;
    scanf("%d %d",&point[cnt].x,&point[cnt].y);
    point[cnt++].k=k++;
    while(~scanf("%d %d",&point[cnt].x,&point[cnt].y))//   cnt=3   k=3
    {
        point[cnt++].k=k;
        while((scanf("%d %d",&point[cnt].x,&point[cnt].y))&&point[cnt].x!=-1)
            point[cnt++].k=k;
        k++;
//        if(k==5)
//            break;
    }//共cnt-1个点  其k相同的就是在同一线路上的 从一开始编号的
    cnt--;
//    printf("cnt=%d\n",cnt);
    for(int i=1;i<=cnt;i++)
        for(int j=1;j<=cnt;j++)
            map[i][j]=INF;
    for(int i=1;i<=cnt;i++)
            map[i][i]=0;
    for(int i=1;i<=cnt;i++)
    {
        for(int j=i+1;j<=cnt;j++)//求编号为i的到编号为J的时间
        {
            mid=_distant(point[i].x,point[i].y,point[j].x,point[j].y);
            if(point[i].k==point[j].k&&(j==i+1))//一条地铁线上且相邻的点
                mid=mid/vs;
            else
                mid=mid/vb;
            if(mid<map[i][j])
                map[i][j]=map[j][i]=mid;
        }
    }
//用于测试数据查看map内数据
/*
    for(int i=0;i<=cnt;i++)
        printf("%5d  ",i);
    printf("\n");
    for(int i=1;i<=cnt;i++)
    {
        printf("%5d  ",i);
        for(int j=1;j<=cnt;j++)
        {
            printf("%5.1lf  ",map[i][j]);
        }
         printf("\n");
    }
*/
     for(int i=1;i<=cnt;i++)//记录1到其他点的时间
        dis[i]=map[1][i];
      book[1]=1;
      dijkstra(cnt);
//      for(int i=1;i<=cnt;i++)
//          printf("dis[%d]=%.2lf\n",i,dis[i]);
      printf("%.0lf\n",dis[2]);
}```


参考博客：[https://www.cnblogs.com/Sunshine-tcf/p/5752027.html](https://www.cnblogs.com/Sunshine-tcf/p/5752027.html)

 

