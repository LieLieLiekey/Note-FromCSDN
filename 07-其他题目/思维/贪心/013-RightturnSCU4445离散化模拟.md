

## Right turn(SCU-4445) (离散化+模拟)


frog is trapped in a maze. The maze is infinitely large and divided into grids. It also consists of nn obstacles, where the ii-th obstacle lies in grid (xi,yi)(xi,yi).

frog is initially in grid (0,0)(0,0), heading grid (1,0)(1,0). She moves according to *The Law of Right Turn*: she keeps moving forward, and turns right encountering a obstacle.

The maze is so large that frog has no chance to escape. Help her find out the number of turns she will make.

### Input


The input consists of multiple tests. For each test:

The first line contains 1 integer n (0≤n≤1000). Each of the following n lines contains 2 integers xi,y(|xi|,|yi|≤109,(xi,yi)≠(0,0) all (xi,yi)are distinct)

### Output


For each test, write 11 integer which denotes the number of turns, or `-1` if she makes infinite turns.

### Sample Input


```bash
    2
    1 0
    0 -1
    1
    0 1
    4
    1 0
    0 1
    0 -1
    -1 0
```


### Sample Output


```bash
    2
    0
    -1
```


### 题意:


​ 一个迷宫有n块石头,一个人从(0,0)出发,一开始是面向右边,如果他遇到石头就要向右转,问这个人要转几次弯,如果会无限次转弯就输出-1

我看网上题解大部分都是二分找点走，而这里采用的是坐标离散化，然后自动转弯走。

### 思路：


​ 离散化上所有石头坐标，这样形成的地图最多为$2*n$ * $2*n$，然后while循环自动转完即可，走到边界离散化的行或列就算走出去了。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
typedef long long ll;
using namespace std;
int X[1100],Y[1100],sx[1100],sy[1100],XX[2100],YY[2100];
int dir[4][2]={
1,0,
0,-1,
-1,0,
0,1
};
int book[2100][2100][4];
int flies[2100][2100];
void getd(int dr,int &dx,int &dy){
    dx=dir[dr][0];
    dy=dir[dr][1];
}
int main()
{
    //1e9+1 1e9+1
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    while(cin>>n)
    {
        int cnt=0;
        X[0]=Y[0]=XX[0]=YY[0]=0;
        for(int k=-1;k<1;++k)
        {
            XX[cnt]=k;
            YY[cnt]=k;
            cnt++;
        }
        for(int i=1;i<=n;++i){
            cin>>X[i]>>Y[i];
            for(int k=-1;k<1;++k)
            {
                XX[cnt]=X[i]+k;
                YY[cnt]=Y[i]+k;
                cnt++;
            }
        }
        X[n+1]=Y[n+1]=XX[cnt]=YY[cnt]=1e9+10;
        cnt++;
        X[n+2]=Y[n+2]=XX[cnt]=YY[cnt]=-1e9-10;
        cnt++;
        int tx,ty;
        sort(XX,XX+cnt);
        sort(YY,YY+cnt);
        tx=unique(XX,XX+cnt)-XX;
        ty=unique(YY,YY+cnt)-YY;
        for(int i=0;i<n+3;++i){
            sx[i]=lower_bound(XX,XX+tx,X[i])-XX;
            sy[i]=lower_bound(YY,YY+ty,Y[i])-YY;
            if(i>=1&&i<=n){
                flies[sx[i]][sy[i]]=1;
            }
        }
        int lx=sx[n+2],rx=sx[n+1],ly=sy[n+2],ry=sy[n+1];
        int nx=sx[0],ny=sy[0],dr=0,tus=0,flag=0;
        book[nx][ny][dr]=1;
        while(true)
        {
            if(nx<=lx||nx>=rx||ny<=ly||ny>=ry){
                flag=1;
                break;
            }
            int dx,dy;
            getd(dr,dx,dy);
            if(flies[nx+dx][ny+dy]==0){
                nx+=dx;
                ny+=dy;
                book[nx][ny][dr]=1;
                continue;
            }
            if(book[nx][ny][(dr+1)%4]==0)
            {
                dr=(dr+1)%4;
                tus++;
                book[nx][ny][dr]=1;
                continue;
            }
            break;
        }
        if(!flag)
            cout<<-1<<endl;
        else
            cout<<tus<<endl;
            mset(book,0);
            mset(flies,0);
    }
    return 0;
}

```


