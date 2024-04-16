

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


 

 

