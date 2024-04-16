

## 20182019-acmicpc-asia-nanjing-regional 赛后整理



这次比赛中就a了三道题(a,i,j)，但其实还有四道是可做题目。

这次比赛g题因为推错第4项和第5项导致整个过程GG，一直推错公式还以为自己很对。

E题是开关性质的一个题，也可以做，但是当时没看这道题，M题是最后一个小时才看的，没想起来让字符串s反转一下，当时也没报太大希望…赛后表示这道题不难（赛后一直还sb的认为自己正确的思路是错的，以为回文自动机+exkmp会有重复计算，实际上这是不可能），D题爬山就可以a了。



因为鄙人英语不太好，所以每次比赛也会把不会做的题目给翻一下，若发现有错误，指正不胜感激



PS: 时间2019-9-30,这个整理鸽了快一星期了…


比赛链接：[传送门](https://codeforces.com/gym/101981/)

#### Problem A. Adrien and Austin


**题意**：n个石子，每次只能取连续的1到k个石子，最优策略下谁输

**思路**：第一个人先取中间的几个，另一个人取的时候第一个人对称取即可，需要判断特判n=0时先手输和k=1时即可

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int N=2e3+50;
int main()
{
   
    int n,k;
    cin>>n>>k;
    if(n==0||(k==1&&n%2==0)) puts("Austin");
    else puts("Adrien");
    return 0;
}
```


#### Problem B. Tournament


**题意**： 给你n个村庄的位置(这些村庄在一条线上)，第一个村庄的位置是0。让你在这条直线上建立K个体育馆，问建立之后村民到体育馆的距离和最小是多少。（定义村民到体育馆的距离为该村民到最近的体育馆的距离

**思路**： 不会

#### Problem C. Cherry and Chocolate


**题意**：给出一颗树，有两个人，第一个人先从树上选个点染成粉红色，然后第二个人从树上选个点染成巧克力色，最后第一个人又从树上选一个点染成粉红色。如果树上某个点到粉红点的路径不经过巧克力色的点，第一个人就获得一个节点，第二个不想让第一个人获得多的节点，最优策略下第一个人可以获得多少节点

**思路**：不会

#### Problem D. Country Meow


**题意**： 求最小球覆盖

**思路**： 爬山每次往较远的点逼近就行。


ps:顺便偷了个三分套三分的模板


```cpp
#include <bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
//typedef pair<int,int>  P;
const int N=105;
struct pnode{
   
double x,y,z;
pnode(){
   }
pnode(double x,double y,double z):x(x),y(y),z(z){
   }
}p[N];
double getdis(const pnode&a,const pnode &b)
{
   
    double dx=a.x-b.x,dy=a.y-b.y,dz=a.z-b.z;
    return dx*dx+dy*dy+dz*dz;
}
int main()
{
   
    int n;
    scanf("%d",&n);
    double ans=1e10;
    for(int i=1;i<=n;++i) scanf("%lf%lf%lf",&p[i].x,&p[i].y,&p[i].z);
    double x=0,y=0,z=0;
    double L=2e5,desc=0.99;
    while(L>=1e-7)
    {
   
        //找到最远的点,然后移动部分距离
        pnode far;
        double d=0;
        for(int i=1;i<=n;++i)
        {
   
            double m=getdis(pnode(x,y,z),p[i]);
            if(m>d)
            {
   
                d=m;
                far=p[i];
            }
        }
        double dx=far.x-x,dy=far.y-y,dz=far.z-z;
        double m=sqrt(dx*dx+dy*dy+dz*dz);
        ans=min(ans,m);
        x+=L*dx/m;
        y+=L*dy/m;
        z+=L*dz/m;
        L*=desc;
    }
    printf("%.10f\n",ans);
    return 0;
}
```


#### Problem E. Eva and Euro coins


**题意**： 给你n个硬币的状态(0,1正反面)，每次可以反转k个连续同状态的硬币，问A状态能否到达B状态

**思路**：模拟几次你会发现，从A状态反转后的任意一个状态C，两个状态不停的去掉连续的k个1或0后剩下的字符串相同，所以我们只需判断A状态和B状态去掉连续的K个1或0之后剩下的字符串是否相同即可。

据说这是个开关性质，但是目前我还不会证明。。。

```cpp
#include <bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e6+10;
int k;
char e[N];
int d[N];
int work(char s[],int ls)//返回处理后的字符串的长度
{
   
    int top=0;
    e[0]=' ';
    d[0]=0;
    for(int i=0;i<ls;++i)
    {
   
        e[++top]=s[i];
        if(e[top]==e[top-1])
            d[top]=d[top-1]+1;
        else
            d[top]=1;
        if(d[top]==k)
        {
   
            top-=k;
        }
    }
    for(int i=0;i<top;++i)
        s[i]=e[i+1];
    s[top]=0;
    return top;
}
char s[N],t[N];
int main()
{
   
    int ls;
    scanf("%d%d",&ls,&k);
    scanf("%s%s",s,t);
    int ls1=work(s,ls);
    int ls2=work(t,ls);
    if(ls1==ls2&&strcmp(s,t)==0)
        puts("Yes");
    else
        puts("No");
    return 0;
}
```


#### Problem F. Frank


**题意**：给出一个图可能有重边，每次给出初始城市C0和旅行的列表，每天自己会从一个城市随机选一条边去另一个城市，从c0走的路线中包含旅行列表的序列的时停止，问期望的天数。

**思路**：不会

#### Problem G. Pyramid


**题意**：数三角形

**思路**：答案：$( n$

