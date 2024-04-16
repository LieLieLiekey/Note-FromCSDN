

#### The 2017 ACM-ICPC Asia Beijing Regional (赛后整理)



PS: E，F是个大水题，但是因为队伍英语水平不高（菜是原罪），E题队友40分钟才A，我去读F题，发现是个水题，20分钟后又把F题A了，之后 J 题读错题意（successive 读成“成功的”，导致理解错题意，爆搜搞答案，当然是一直tle或wa到底）G题读完发现是个sb题，bfs+线段多边形规范相交就行，wa到底，比赛结束后发现我才是sb，G题坐标都没转换正确，线段多边形规范相交还有一种情况没判断。H题读完题意，发现不会。

比赛结束就A了2道，…好菜啊



不过这次的几何G题和 区间dp J 题不错。


#### E - Cats and Fish


思路：这道题用优先队列或者set模拟一下即可，太水就鸽了吧（本来很早就要写这题，不过没时间…拖到现在也不想搞了）

#### F - Secret Poems


思路：斜着一遍把原字符串还原，然后蛇形填数形成新的grid即可。


水题


代码：

```cpp
#include<bits/stdc++.h>
#define  mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int N=1e2+10;
char g[N][N];
char a[N][N];
string s;
int main()
{
   
    int n;
    while(~scanf("%d",&n))
    {
   
        for(int i=1; i<=n; ++i) scanf("%s",g[i]+1);
        s="";
        for(int i=1; i<=n; ++i)
        {
   
            if(i&1)//向上
            {
   
                for(int x=i,y=1; x>=1; x--,y++)
                    s+=g[x][y];
            }
            else
            {
   
                for(int x=1,y=i; y>=1; x++,y--)
                    s+=g[x][y];
            }
        }
        for(int i=2; i<=n; ++i)
        {
   
            if((n+i-1)&1)//向上
            {
   
                for(int x=n,y=i; y<=n; y++,x--)
                    s+=g[x][y];
            }
            else
            {
   
                for(int x=i,y=n; x<=n; x++,y--)
                    s+=g[x][y];
            }
        }
        mset(a,0);
        int k=0;
        a[1][1]=s[k++];
        int x=1,y=1;
        int mx=n*n;
        while(k < mx)
        {
   
            while(k < mx&&y < n&&a[x][y+1]==0)//向前走y++;
            {
   
                y++;
                a[x][y]=s[k++];
            }
            while(k<mx && x<n &&a[x+1][y]==0)//向下走  x++;
            {
   
                x++;
                a[x][y]=s[k++];
            }
            while(k<mx && y > 1&&a[x][y-1]==0)//向左走   y--;
            {
   
                y--;
                a[x][y]=s[k++];
            }
            while(k<mx &&x>1 && a[x-1][y] ==0)//向上走   x--
            {
   
                x--;
                a[x][y]=s[k++];
            }
        }
        for(int i=1; i<=n; ++i)
        {
   
            for(int j=1; j<=n; ++j)
                printf("%c",a[i][j]);
            puts("");
        }
    }
    return 0;
}
```


#### G - Liaoning Ship’s Voyage


**题意**：给出一个n*n的格子，和一个三角形，开始自己在左下角(0,0),现要去(n-1,n-1)坐标。每次可以走周围的8个方向，不能走’#’，每走一次的路线是直线，要求走的路线（线段）不能穿过三角形，但可以在三角形边上走。问走的最小步数。$n ∈ [ 1 , 20 ] n\in[1,20]$

**思路**：bfs+线段多边形规范相交吧，在输入坐标方面注意x轴是输入的列，y轴是输入的行，需要转化下。判断线段多边形不规范相交，首先线段与多边形的所有边都不规范相交，其次两个点都不在多边形内，但可能出现两个点在多边形边上，但中间的线段穿过多边形，这时可以在多边形上取几百个点判断下即可。

代码：

```cpp
#include<bits/stdc++.h>
#define  mset(a,b) memset(a,b,sizeof(a))
using namespace std;
double xx[10],yy[10];
double const eps=1e-8;
char gg[25][```


