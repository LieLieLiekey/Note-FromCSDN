

圣诞节要到了，坤神和瑞瑞这对基佬想一起去召唤师大峡谷开开车。百度地图一下，发现周围的召唤师大峡谷还不少，这对基佬纠结着，该去哪一个。。。坤神：我要去左边的这个（因为离自己比较近 哈哈~）。。瑞瑞：我要去右边的这个（因为离自己比较近 嘿嘿~） ........这对基佬闹矛盾了，开车有危险了！  为了不让他们去召唤师大峡谷坑人，riot决定让他们去X召唤师大峡谷，保证他俩所走的路程和最短。每走一个点需要花费11分钟，输出他们一共花费多少时间（最短时间噢）Input 

多组测试数据

每组数据，开始一行n，m (2<=n,m<=200)

接下来是个n x m的矩阵

'Y' 表示坤神所在的初始位置

'M' 表示瑞瑞所在的初始位置

'#' 该点禁止通行

'.' 该点可通行

'@' 召唤师大峡谷Output 

每组测试数据，输出坤神和瑞瑞到达同一个召唤师大峡谷所花费的最短时间。Sample Input 
4 4
Y.#@
....
.#..
@..M
4 4
Y.#@
....
.#..
@#.M
5 5
Y..@.
.#...
.#...
@..M.
#...#Sample Output 
66
88
66



****

**这个题也可以将召唤师峡谷看作路走。（当时就因为这一点一直wa）;**

**简单的多路搜索**

每个源点Y  M 搜索到每个召唤师峡谷  ,,ԾㅂԾ,,  的最短路径 ， 接下来遍历召唤师峡谷 ，找出都能到此处并且最短路径和最小的步数。

过程实现的细节:

1.vis[4][2]作为搜索的方向的增量

2.用map存输入数据的地图，数组bbj[][]将走过的坐标记作1，  所以搜索过程中坐标能走的必要条件是map中该坐标能走且bbj[i][j]==0（这个坐标未搜过）

3.其中存放答案的mapp[][][]数组    mapp[i][j][0],中  i ,j表示map地图对应的坐标，而mapp[i][j][0]存的是**所有源点中能到达此坐标**的**最短路径和。**

mapp[i][j][1]表示全部源点中能到此坐标的数量.（**在此题中map[i][j]=2才有效**）



```cpp
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<queue>
#define N 200
#define inf 0x1f1f1f1f//使得能更新ans
using namespace std;
char map[N+10][N+10];
int bbj[N+10][N+10],n,m;
int vis[4][2]={{-1,0},{0,-1},{0,1},{1,0}},mapp[N+10][N+10][2];//存放答案的
struct node{
    int i,j,step;
};
typedef struct node Node;
queue<Node>mmp;
void dfs()//与bfs分开写纯属个人喜好
{
    Node mm;
    int ii,jj,ss,aa,bb;
    mm=mmp.front();
    ii=mm.i;
    jj=mm.j;
    ss=mm.step;
    mmp.pop();
    for(int i=0;i<4;i++)
    {
        aa=ii+vis[i][0];
        bb=jj+vis[i][1];
        if((!bbj[aa][bb])&&aa>=1&&aa<=n&&bb>=1&&bb<=m&&map[aa][bb]!='#')//这个方向能走
        {
            bbj[aa][bb]=1;//使这个坐标已经在搜索的队列中,不让其他路搜索
            mapp[aa][bb][0]+=ss+1;//加上此源点到这个坐标的step
            mapp[aa][bb][1]++;//该源点已经到达该坐标
            Node mm;
            mm.i=aa;
            mm.j=bb;
            mm.step=ss+1;
            mmp.push(mm);
        }
    }
}
void bfs(int a,int b)//开始坐标
{
    while(!mmp.empty())
        mmp.pop();
  Node qq;
  qq.i=a;
  qq.j=b;
  qq.step=0;
  mmp.push(qq);
  while(!mmp.empty())
        dfs();
}
int main()
{
    int ans,x1,x2,y1,y2;
    while(~scanf("%d %d",&n,&m))
    {
        memset(bbj,0,sizeof(bbj));
        memset(mapp,0,sizeof(mapp));
        for(int i=1;i<=n;i++)//输入地图
            scanf("%s",map[i]+1);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(map[i][j]=='Y')
                {
                    x1=i,y1=j;
                }
                if(map[i][j]=='M')
                {
                    x2=i,y2=j;
                }
            }
        }
        bfs(x1,y1);
        memset(bbj,0,sizeof(bbj));//重置bbj
        bfs(x2,y2);
        ans=inf;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(map[i][j]=='@' && mapp[i][j][1]==2)//两个源点都能到的召唤师峡谷
                    ans=mapp[i][j][0]>ans?ans:mapp[i][j][0];
            }
        }
        printf("%d\n",ans*11);
    }
}```





简单的多路搜索


