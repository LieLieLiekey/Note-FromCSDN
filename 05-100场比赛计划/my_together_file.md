

## ccpc final trials 3总结


#### 比赛链接：[传送门](https://vjudge.net/contest/336724#problem/J)


##### 自我反思


对于B题，迅速写完，但因为数组开小的以至于RE。因为没注意数据范围而急着交导致一发罚时

错误

+ **心急导致没看数据范围**，以至于数据开小


注意

+ 数据范围+ 是否要开long long+ 数组是否开小


对于 I 题因为想到一种做法，但心急没有验证是否正确，导致1h多全浪费在错误的做法上，之后又用容斥写，但是没有想太多，很多地方没有优化。

错误

+ **想到一种做法，并没有仔细思考是否正确**，导致因为有重复计算的问题但却没注意，从而写二分浪费了很长时间+ 用容斥写，**但是没有计算时间复杂度，导致必定超时的却没有优化**，其实合数可以拆分成素数。+ 正确做法是平方数和其他次幂的数的筛法，这种做法简单但没有想到，也没有去往这方面想。**在次幂方面的问题应该在数据范围上多注意下，因为这样的数字可能很少**。


注意：

+ 不要心急，想到一种做法，一定要想好边界情况以及特殊情况是否成立，算法是否正确。+ 要适当的多往几个方面想


对于L题，一个DP+记录路径，但是因为没有想更方便的记录路径的做法，导致使用开一维vector+二分来找路径的麻烦方法，实际上只需记录顶点的前驱顶点即可。

错误

+ **不要着急做，应该适当的想想有没有更简单的做法**


##### 错误统计


+ 心急问题，3次出现+ 数组大小问题 ，1次出现


##### 补题问题


把别人都写过的题都补了，并且把没有人写过的题但是2100分以下的题补了



## Codeforces Global Round 5(赛后补题)



这场的体验挺好的，总体感觉题目给自己一些了good idea，不过就是比赛过程中不争气，只做出来了仅仅三道题目（赛后补题+两道


##### 比赛链接：[传送门](https://codeforces.com/contest/1237)


##### A - Balanced Rating Changes



水


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=2e4+5;
int a[N],b[N];
int main()
{
   
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,t;
    cin>>n;
    t=0;
    for(int i=1; i<=n; ++i)
    {
   
        cin>>a[i];
        if(abs(a[i])&1) t++;
        else b[i]=a[i]/2;
    }
    t/=2;
    for(int i=1; i<=n; ++i)
    {
   
        if((abs(a[i])&1))
        {
   
            if(t>0)
            {
   
                b[i]=(a[i]+1)/2;
                t--;
            }
            else
            {
   
                b[i]=(a[i]-1)/2;
            }
 
        }
    }
    for(int i=1; i<=n; ++i)
        cout<<b[i]<<endl;
}
```


##### B - Balanced Tunnel



水


思路：按照进入的顺序如果比车 $a a$ 与比该车之前进去的车 $b b$ 出来的早，那么车a就超车了

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int inf=0x3f3f3f3f;
const int N=2e5+5;
int in[N],to[N],out[N],num[N];
int main()
{
   
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;++i){
   
        scanf("%d",in+i);
        to[in[i]]=i;
    }
    for(int i=1;i<=n;++i){
   
        scanf("%d",out+i);
        int ps=to[out[i]];
        num[ps```




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




## Comet OJ - 2019国庆欢乐赛（赛后整理）


#### 比赛链接：[传送门](https://www.cometoj.com/contest/68/problems)



PS:

做题失误：

A题wa了好久不知道为什么，后来才知道乘法爆long long了

B题思路错了，应该在想清楚些。

比赛过程中就A了 4道题A,B,C,E，赛后补题两道D1，H。至于G题后缀数组，如果今天学会了就补上。

G题后缀数组，但是因为把长度int定义为char，导致wa，debug的很长时间。希望以后不要犯

时间：2019-10-4


#### A:轰炸平面镇魂曲


**思路**：三种情况判断即可


int乘法爆long long的错误+1


```cpp
#include<bits/stdc++.h>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
long long  x[2],y[2];
int main()
{
   
    int t;
    cin>>t;
    while(t--)
    {
   
        cin>>x[0]>>y[0]>>x[1]>>y[1];
        if(x[0]*x[1]>=0&&y[0]*y[1]>=0) cout<<"5"<<endl;
        else if(x[0]*x[1]<0&&y[0]*y[1]<0) cout<<"8"<<endl;
        else cout<<"6"<<endl;
    }
    return 0;
}
```


#### B:卖萌鸡尾酒


**思路**：可以理解为有5种不同的糖果，给出糖果数量，要求吃糖果时上一次与该次不能吃同一种糖果，求吃最多糖果数量/2


当最多的糖果数量>剩下的糖果数量+1，一定吃不完。否则每次取最多的两个吃。


```cpp
#include<bits/stdc++.h>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll w[10];
int main()
{
   
    ll sum=0,maxx=-1;
    for(ll i=1;i<=5;++i) {
   
        cin>>w[i],sum+=w[i],maxx=max(maxx,w[i]);
    }
    if(maxx<=sum-maxx+1)
        cout<<sum/2<<endl;
    else{
   
        cout<<sum-maxx<<endl;
    }
}
```


#### C:两排房子


**思路**：对于每个房子，二分出临界位置算贡献即可、

```cpp
#include<bits/stdc++.h>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=2e5+10;
struct node{
   
ll l,r;
node(){
   }
node(ll l,ll r):l(l),r(r){
   }
}a[N],b[N];
bool cmpl(const node &a,const node &b)
{
   
    return a.l<b.l;
}
bool cmpr(const node &a,const node &b)
{
   
    return a.r<b.r;
}
int main()
{
   
    ll n,m,ans=0;
    scanf("%lld%lld",&n,&m);
    for(ll i=1;i<=n;++i) scanf("%lld%lld",&a[i].l,&a[i].r);
    for(ll i=1;i<=m;++i) scanf("%lld%lld",&b[i].l,&b[i].r);
    for(ll i=1;i<=n;++i)
    {
   
        ll th1=lower_bound(b+1,b+1+m,node(0,a[i].l),cmpr```




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



## The Preliminary Contest for ICPC Asia Shenyang 2019赛后部分补题



这里把赛场上自己没写过的题写一下，写过不是自己写的写一下。

PS：E题一直以为是prufer序列计数，四天后重新做题发现题目不要求最后只有一个武器，蛤？这不就是bell数吗？D题树形dp赛场上没有时间写，最后没A…


#### B. Dudu’s maze


难度：中等题


自我感觉这道题题目读懂就好做了，第一次读以为每个怪物房间都有一次“传送门”的机会，然后咋想都想不出来，Google了一下，才明白传送门机会只有一次，那么也就是说只有一次机会碰见怪物并”接着捡糖“


**题意**：

​     给出一个n个节点和m个无向边的图，其中k个节点是“怪物节点”，剩下节点都是”糖果“节点，每个糖果节点里有一个糖果，并且拿到后就没有了。现在你知道这个图的构造，且起始位置为1号节点，且碰见怪物有一次使用”传送门“的机会，如果没有使用“传送门”就必须结束游戏。传送门会把送至怪物节点相邻的某一条遍的节点，每条边的概率是相等的。

    问聪明的自己使用最优策略，你可以获得的期望糖果是多少。

**思路**：

​     可以理解如果经过了一个”糖果“节点，那么可以与这个”糖果“节点相邻的”糖果“节点都可以经过，所以我们可以考虑缩点，使得每个点要么是怪兽节点，要么是连通的“糖果”节点。然后我们遍历与1号“糖果”节点所在的连通块邻接的”怪物“节点。

​     因为每个怪物节点使用一次传送门只能拿到送至的节点所在的"糖果"联通块的糖果，然后就必须结束游戏。所以每个“怪物”节点使用传送门获得的期望价值是 每条边另一个节点所在的”糖果“联通块的节点个数，选择每条边的概率=1/相邻的边的个数。我们就可以算出来每个怪物节点可以获得的期望价值。注意此时1号节点已径没有糖果了。

​     因为我们只能选择一个怪物节点，所以选择期望价值最高的那个+1号节点所在连通块的节点个数即可。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e5+100;
const int inf=0x3f3f3f3f;
vector<int> g[N];
/*
原图dfs缩点一下,建立新图,
*/
int color[N],cnt[N],top;
void dfs(int u,int sign)
{
    color[u]=sign;
    cnt[sign]++;
    for(int v:g[u]){
        if(color[v]) continue;
        dfs(v,sign);
    }
}
int link[N];
double lw[N];
vector<int> rg[N];
void work(int n,int m,int k)
{
    for(int i=1;i<=n;++i){
        if(!color[i]) dfs(i,++top);
    }
    //缩点染色，共top个点,/color[]<=k的都是怪兽
    double ans=cnt[color[1]];
    cnt[color[1]]=0;
    for(int i=1;i<=top;++i){
        rg[i].clear();
        link[i]=0;
    }
    for(int i=1;i<=n;++i){
        for(int v:g[i]){
            if(color[v]==color[i]) continue;
            rg[color[i]].push_back(color[v]);
        }
    }
    int u=color[1];
    for(int v:rg[u]){//取出所有与1连接的怪兽的点
        link[v]=true;
    }
    double maxx=0.0;
    for(int u=1;u<=top;++u){//枚举这些怪兽的点
        if(link[u]==true){
            double val=0;
            int totle=rg[u].size();
            for(int v:rg[u]){//连接v的出现个数
                //如果连接的怪兽，贡献自然为0
                val+=1.0/totle*cnt[v];
            }
            maxx=max(maxx,val);
        }
    }
    printf("%.7f\n",ans+maxx);
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m,k;
        scanf("%d%d%d",&n,&m,&k);
        for(int i=1;i<=n;++i){
            g[i].clear();
            color[i]=cnt[i]=0;
        }
        for(int i=1;i<=m;++i){
            int a,b;
            scanf("%d%d",&a,&b);
            g[a].push_back(b);
            g[b].push_back(a);
        }
        for(int i=1;i<=k;++i){
            int v;
            scanf("%d",&v);
            color[v]=i;
        }
        top=k;
        work(n,m,k);


    }
    return 0;
}
```


​

#### C. Dawn-K’s water


定位：简单题

**题意**：给你n个物品和最少需要买的重量m，并给出n个物品的价值和重量，问最少需要买m重量的的最小花费，如果最小花费下重量有多个，则输出最大的哪个。

**思路**：多重背包,$dp[i]$为刚好购买$i$重量的物品的最小花费。然后从$[m,10000]$遍历取最小值的a和对应的最大b即可。


赛后补题wa了几发，以为重量和买的价值是单调递增的关系。后来才记起来$dp[i]$是恰好买$i$重量物品所花费的最小金币，并没有单调性！！


**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e4+100;
const int inf=0x3f3f3f3f;
ll dp[N],p[1005],c[1005];
ll n,m;
void work()
{
    dp[0]=0;
    ll top=10000;
    for(ll i=1;i<=top;++i) dp[i]=1ll<<62;
    for(ll i=1;i<=n;++i)
        for(ll j=c[i];j<=top;++j){
                dp[j]=min(dp[j],dp[j-c[i]]+p[i]);
    }
    ll a=1ll<<62,b=0;
    for(int i=m;i<=top;++i){
        if(dp[i]<=a) a=dp[i],b=i;
    }
    printf("%lld %lld\n",a,b);
}
int main()
{
    while(~scanf("%lld%lld",&n,&m))
    {
        for(ll i=1;i<=n;++i)
            scanf("%lld%lld",p+i,c+i);
        work();
    }
    return 0;
}
```


#### D. Fish eating fruit(树形dp+换根)


定位：中上难度

**题意**： 给一个有n个点的树，求所有两点之间的路径权值和，且路径权值和分三类：模3为0，模3为1，模3为2的路径。对于每种路径，输出其种类路径的和。

这道题写了篇博客，因为思路描述比较赘余就不在这里指出了:[博客链接](https://blog.csdn.net/Dch19990825/article/details/100848798)

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const ll N=1e4+20;
const ll mod=1e9+7;
vector<pair<ll,ll> > g[N];
ll dp[N][3];
ll res[N][3];
ll m[3];
ll tol[N][3],rtol[N][3];
ll ccc(ll a)
{
    return (a%mod+mod)%mod;
}
void dfs1(ll u,ll fa)
{
    for(ll i=0; i<3; ++i)
    {
        tol[u][i]=rtol[u][i]=dp[u][i]=res[u][i]=0;
    }
    tol[u][0]=1;
    for(P e:g[u])
    {
        ll v=e.first,w=e.second;
        if(v==fa) continue;
        dfs1(v,u);
        for(ll i=0; i<3; ++i)
        {
            dp[u][(i+w)%3]=ccc(dp[u][(i+w)%3]+dp[v][i]+w*tol[v][i]);
            tol[u][(i+w)%3]+=tol[v][i];
        }
    }
}
void dfs2(ll u,ll fa,ll c)
{
    if(fa!=u) //
    {
        for(ll i=0; i<3; ++i)
        {
            ll p=((i-c)%3+3)%3;
            m[(i+c)%3]=ccc(res[fa][i]-dp[u][p]-c*tol[u][p]+c*(rtol[fa][i]-tol[u][p]));
            rtol[u][(i+c)%3]=tol[u][(i+c)%3]+rtol[fa][i]-tol[u][p];
            res[u][(i+c)%3]=ccc(dp[u][(i+c)%3]+m[(i+c)%3]);
        }
    }
    for(P e:g[u])
    {
        ll v=e.first,w=e.second;
        if(v==fa) continue;
        dfs2(v,u,w);
    }
}
ll sum[3];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n;
    while(cin>>n)
    {
        for(ll i=0; i<n; ++i) g[i].clear();
        for(ll i=0; i<n-1; ++i)
        {
            ll a,b,c;
            cin>>a>>b>>c;
            g[a].push_back({b,c});
            g[b].push_back({a,c});
        }
        dfs1(0,0);
        for(ll i=0; i<3; ++i) res[0][i]=dp[0][i],rtol[0][i]=tol[0][i];
        dfs2(0,0,0);
        sum[0]=sum[1]=sum[2]=0;
        for(ll i=0; i<n; ++i)
        {
            for(ll k=0; k<3; ++k)
                sum[k]=(sum[k]+res[i][k])%mod;
        }
        cout<<sum[0]<<" "<<sum[1]<<" "<<sum[2]<<endl;
    }
    return 0;
}

```


#### E. Gugugu’s upgrade schemes


定位：性质题


这道题是赛后补题的


**题意**：n个元素的集合划分方法是有多少个，模p输出。

**思路**：bell数+Touchard同余。

Touchard同余就是若p为质数，且$B_n$是第n个贝尔数，那么$B_{p+n}=B_n+B_{n+1} (mod ~~p)$

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e3+10;
const int inf=0x3f3f3f3f;
ll C[N][N],f[1000005],p;
void init(int n)//求0~n的贝尔数
{
    C[0][0]=1;
    for(int i=1;i<=n;++i){
        C[i][0]=C[i][i]=1;
        for(int j=1;j<i;++j) C[i][j]=(C[i-1][j]+C[i-1][j-1])%p;
    }
    f[0]=1;
    for(int i=1;i<=n;++i){
        f[i]=0;
        for(int j=0;j<i;++j)
            f[i]=(f[i]+C[i-1][j]*f[i-1-j])%p;
    }
}
ll dfs(ll n)
{
    if(f[n]!=-1) return f[n];
    ll ans=(dfs(n-p)+dfs(n-p+1))%p;
    return f[n]=ans;
}
int main()
{
    ll T,n;
    cin>>T;
    while(T--)
    {
        cin>>n>>p;
        for(ll i=1;i<=n;++i) f[i]=-1;
        init(p);
        cout<<dfs(n)<<endl;
    }
    return 0;
}

```


#### F. Honk’s pool


定位：中下难度


这题赛场上自己A过


**题意** ：给出一个长度为n的序列，每天可以将序列中最小的一个数+1，最大的一个数-1，问k天之后序列中最大与最小值的差是多少？

**思路**：模拟一下，看k天后最小值最大能到多少，最大值最小能到多少，如果交叉了就判断和是否能被4整除，可以则输出0，否则输出1。没有交叉则输出上面两个值的差

**代码**：

```cpp
include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=5e5+20;
ll w[N];
ll n,K;
ll getlv()
{
    ll k=K,c=1;
    for(ll i=1; i<n; ++i) //第 i 个的个数
    {
        ll d=w[i+1]-w[i];
        if(d*c<=k)
        {
            k-=d*c;
            c+=1;
        }
        else
        {
            ll m=k/c;
            return w[i]+m;
        }
    }
    return w[n];
}
ll getrv()
{
    ll k=K,c=1;
    for(ll i=n; i>1; --i) //第 i 个的个数
    {
        ll d=w[i]-w[i-1];
        if(d*c<=k)
        {
            k-=d*c;
            c+=1;
        }
        else
        {
            ll m=k/c;
            return w[i]-m;
        }
    }
    return w[1];
}
int main()
{

    while(~scanf("%lld%lld",&n,&K))
    {
        ll sum=0;
        for(ll i=1; i<=n; ++i)
        {
            scanf("%lld",w+i);
            sum+=w[i];
        }
        sort(w+1,w+1+n);
        ll a=getlv(),b=getrv();
        if(a<b)
        {
            printf("%lld\n",b-a);
        }
        else
        {
            if(sum%n==0)
            {
                printf("0\n");
            }
            else
            {
                printf("1\n");
            }
        }

    }
    return 0;
}
```


#### H. Texas hold’em Poker


定位：难

**题意**：

**思路**：

K. Guanguan’s Happy water


这道题正解是高斯消元+矩阵快速幂，线性BM给过了，不知道数据有多水


放个**非正解的线性BM**递推，正解有机会在写吧。

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef vector<long long> VI;
typedef long long ll;
const ll mod=1e9+7;
ll powmod(ll a,ll b)
{
    ll res=1;
    a%=mod;
    assert(b>=0);
    for(; b; b>>=1)
    {
        if(b&1)res=res*a%mod;
        a=a*a%mod;
    }
    return res;
}
namespace linear_seq
{
#define rep(i,a,n) for (long long i=a;i<n;i++)
#define pb push_back
#define SZ(x) ((long long)(x).size())
const long long N=10010;
ll res[N],base[N],_c[N],_md[N];

vector<long long> Md;
void mul(ll *a,ll *b,long long k)
{
    rep(i,0,k+k) _c[i]=0;
    rep(i,0,k) if (a[i]) rep(j,0,k)
        _c[i+j]=(_c[i+j]+a[i]*b[j])%mod;
    for (long long i=k+k-1; i>=k; i--) if (_c[i])
            rep(j,0,SZ(Md)) _c[i-k+Md[j]]=(_c[i-k+Md[j]]-_c[i]*_md[Md[j]])%mod;
    rep(i,0,k) a[i]=_c[i];
}
long long solve(ll n,VI a,VI b)
{
    // a 系数 b 初值 b[n+1]=a[0]*b[n]+...
    //        printf("%d\n",SZ(b));
    ll ans=0,pnt=0;
    long long k=SZ(a);
    assert(SZ(a)==SZ(b));
    rep(i,0,k) _md[k-1-i]=-a[i];
    _md[k]=1;
    Md.clear();
    rep(i,0,k) if (_md[i]!=0) Md.push_back(i);
    rep(i,0,k) res[i]=base[i]=0;
    res[0]=1;
    while ((1ll<<pnt)<=n) pnt++;
    for (long long p=pnt; p>=0; p--)
    {
        mul(res,res,k);
        if ((n>>p)&1)
        {
            for (long long i=k-1; i>=0; i--) res[i+1]=res[i];
            res[0]=0;
            rep(j,0,SZ(Md)) res[Md[j]]=(res[Md[j]]-res[k]*_md[Md[j]])%mod;
        }
    }
    rep(i,0,k) ans=(ans+res[i]*b[i])%mod;
    if (ans<0) ans+=mod;
    return ans;
}
VI BM(VI s)
{
    VI C(1,1),B(1,1);
    long long L=0,m=1,b=1;
    rep(n,0,SZ(s))
    {
        ll d=0;
        rep(i,0,L+1) d=(d+(ll)C[i]*s[n-i])%mod;
        if (d==0) ++m;
        else if (2*L<=n)
        {
            VI T=C;
            ll c=mod-d*powmod(b,mod-2)%mod;
            while (SZ(C)<SZ(B)+m) C.pb(0);
            rep(i,0,SZ(B)) C[i+m]=(C[i+m]+c*B[i])%mod;
            L=n+1-L;
            B=T;
            b=d;
            m=1;
        }
        else
        {
            ll c=mod-d*powmod(b,mod-2)%mod;
            while (SZ(C)<SZ(B)+m) C.pb(0);
            rep(i,0,SZ(B)) C[i+m]=(C[i+m]+c*B[i])%mod;
            ++m;
        }
    }
    return C;
}
long long gao(VI a,ll n)
{
    VI c=BM(a);
    c.erase(c.begin());
    rep(i,0,SZ(c)) c[i]=(mod-c[i])%mod;
    return solve(n,c,VI(a.begin(),a.begin()+SZ(c)));
}
};
long long k,n,f[220],sum[220];
vector<long long>  v;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        for(int i=1;i<=2*k;++i) cin>>f[i];
        if(k==1){
            cout<<(f[1]*(n%mod))%mod<<endl;
            continue;
        }
        sum[0]=0;
        for(int i=1;i<=2*k;++i) sum[i]=(sum[i-1]+f[i])%mod;
        v.clear();
        for(int i=1;i<=2*k;++i) v.push_back(sum[i]);
        cout<<linear_seq::gao(v,n-1)<<endl;
    }
    return 0;
}
```




## The Preliminary Contest for ICPC Asia Shanghai 2019 赛后补题


#### 比赛链接:[传送门](https://www.jisuanke.com/contest/3003?view=challenges)



这次比赛过程中大部分都是队友A的，所以这里补一下自己没有A到的题和没A的题。

这次又出到了Bell 数的相关知识，跟昨天的网络赛有相似的题但是还没时间补。尽快把不会的知识点补全。

增加了退背包的思想。

G题hash字符串还未补


#### B：Light bulbs


定位：简单题

**题意**：t组输入，有一排长度为n的灯泡，初始状态都是关闭，接下来m次操作，每次操作使得区间$[l,r]$ 灯泡状态反转，问最后有多少个灯泡开着的。$t\in[1,1000],n\in(1,1e6),m\in[1,1000]$

**思路**：这是明显的区间异或，我们可以将区间异或变成异或差分的形式。这样每组时间复杂度为$O(n)$，但是t组却超时了，我们注意到m很小，所以我们处理出所有变化的点，然后排序统计答案即可。每组的时间复杂度为$O(mlogm)$。

**代码**：

```cpp
#include <bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef pair<int,int> P;
const int N=1e6+20;
int sq[N];
int main()
{
    int n,m,t,cas=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        int top=0;
        for(int i=1;i<=m;++i){
            int l,r;
            scanf("%d%d",&l,&r);
            l++,r++;
            sq[top++]=l;
            sq[top++]=r+1;
        }
        sort(sq,sq+top);
        int ans=0,pe=0,last=1;
        for(int i=0;i<top;++i){
            if(pe&1)    ans+=sq[i]-last;
            last=sq[i];
            pe^=1;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
}
```


#### D：Counting Sequences I


定位：中等偏难

**题意**：给出一个n，求满足条件$a_1+a_2+a_3...+a_n=a_1*a_2*a_3...*a_n$的序列的个数。

**思路**：我们可以看出来序列的顺序改变不影响等式成立，并且模拟几下可以看出来总有$n-2$个1，一个2，一个n的序列满足条件，并且当次大的数增大1时，最大的数减小速度快，所以我们可以推断出这个序列的和不超过$2*n$，并且不考虑位置的情况下，满足条件的序列数目应该很少，所以我们可以暴力搜索+大剪枝。然后对于每一个序列计算该序列考虑位置的组合数即可


只要知道前面的信息，那么随意剪枝就行。

这题因为check快速幂的一个小错误，检测a^b是否大于k，应该先让b/2，再判断a是否在于k。找了1h30min的bug…


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const ll N=3000+20;
const ll mod=1e9+7;
ll qpow(ll a,ll b,ll m)
{
    ll ans=1;
    while(b)
    {
        if(b&1) ans=ans*a%m;
        a=a*a%m;
        b>>=1;
    }
    return ans;
}
int ok;
ll ckpow(ll a,ll b,ll limt)
{
    ll ans=1;
    while(b)
    {
        if(b&1)
        {
            ans=ans*a;
            if(ans>limt)
                return -1;
        }
        b>>=1;
        a=a*a;
        if(b!=0&&a>limt)
            return -1;

    }
    return ans;
}
ll inv(ll a)
{
    return qpow(a,mod-2,mod);
}
ll f[N],g[N];//i!,i!逆元
void init()
{
    f[0]=1;
    for(ll i=1; i<=3000; ++i) f[i]=(f[i-1]*i)%mod;
    for(ll i=1; i<=3000; ++i)
    {
        g[i]=inv(f[i]);
    }
}
ll calc(ll w[],ll n)
{
    ll ans=f[n];
    map<ll,ll> mmp;
    for(ll i=1; i<=n; ++i) mmp[w[i]]++;
    for(P p:mmp)
    {
        ans=ans*g[p.second]%mod;;
    }
    return ans;
}
ll s[3005],res,n;
void dfs(ll ps,ll pt,ll limt,ll k)
{

    if(pt > 2*n) return ;
    if(pt > ps &&limt > 1) return ;
    if((n-k+1)*limt + ps> 2*n) return ;//数列和优化
    ll si=ckpow(limt,n-k+1,2*n);
    if(limt>1 &&si==-1) return ;//数列乘积优化
    if(limt>1&& si*pt>2*n) return ;//数列乘积优化

    if(k > n){
        if(ps==pt){
            res=(res+calc(s,n))%mod;
        }

        return ;
    }
    for(ll i=limt;i<=n;++i){
        int si=ckpow(i,n-k,2*n);
        if(si==-1||si*i*pt>2*n) return ;
        s[k]=i;
        dfs(ps+i,pt*i,i,k+1);
    }
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    init();
    ll t;
    cin>>t;
    while(t--)
    {
        cin>>n;
        res=0;
        dfs(0,1,1,1);
        cout<<res<<endl;
    }
    return 0;
}

```


#### J：Stone game


定位：中等偏难

**题意**：给出n个石头，每个石头的价值为$a_i$，求有多少种取法使得，取的石头价值和大于等于未取的石头价值和，且满足从拿到的石头中任意减去一个石头的价值使得 剩下的价值小于等于未取的石头价值和。$n\in[1,300],a_i\in[1,500]$

**思路**：01退背包思想，然后枚举最小值计算满足其题意的解的个数即可。

我们首先将物品从小到大排序，先计算出01背包满足总价值为 $j$ 的取法个数。然后退去物品$a_1$求出满足总价值为 $j$ 的取法个数，满足条件的价值是一个区间$[(sum+1)/2-a_i,(sum-a_i)/2]$，统计其种类数即可。接下来就是枚举$a_2$是所取集合中最小的物品，此时我们只需要将$a_1,a_2​$从背包中退去即可，然后模仿上面统计即可。以此类推一直到$a_n$。


比赛中只有想到用$dp[i][j]$为集合中最小值为 $i$ ,集合元素和为$j$的方法数，但时间复杂度不允许。

也是第一次碰到这种退背包的思想。与此同时还有多重背包的退背包。


**代码**:

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=300+20;
const int mod=1e9+7;
int dp[305*505],w[305];
int main()
{
    int t,n,ans,sum;
    scanf("%d",&t);
    while(t--)
    {
        ans=sum=0;
        scanf("%d",&n);
        dp[0]=1;
        for(int i=1;i<=n;++i) {
            scanf("%d",&w[i]);
        }
        sort(w+1,w+n+1);
        for(int i=1;i<=n;++i){
            sum+=w[i];
            for(int j=sum;j>=w[i];--j){
                    dp[j]=(dp[j]+dp[j-w[i]])%mod;
            }
        }
        for(int i=1;i<=n;++i)
        {
            for(int j=w[i];j<=sum;++j) dp[j]=(dp[j]-dp[j-w[i]]+mod)%mod;
            int down=max((sum+1)/2 - w[i],0),up=(sum-w[i])/2;

            for(int j=down;j<=up;++j){
                ans=(ans+dp[j])%mod;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
```


#### L：Digit sum


定位：简单题

**题意**：给出n和b，求$[1,n]$所有的数在b进制下的数位和。$n\in [1,1e6],b\in[2,10]$

**思路**：我们只要算出每位的每个数对答案的贡献即可。算贡献的方法：假设n在b进制表示为$a_ka_{k-1}a_{k-2}...a_0​$。

那么对于下标为$i$，其所有情况的贡献为$pre[i]*\sum _{i=0} ^{b-1}*b^i+\sum _{i=0} ^{a_i-1}*b^i+a_i*(suf[i]+1)$ 。其中$pre[i]$等于$a_ka_{k-1}...a_{i+1}$，$suf[i]$表示为$a_{i-1}...a_0$。

当然也可以数位dp。

```cpp
#include <bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll num[45],pre[45],suf[45];
ll init(ll n,ll b)
{
    ll nn=n;
    ll top=0;
    do{
        num[top++]=n%b;
        n/=b;
    }
    while(n);
    suf[0]=0;
    ll m=1;
    for(ll i=1;i<top;++i){
        suf[i]=suf[i-1]+m*num[i-1];
        m*=b;
    }
    m=nn;
    for(ll i=0;i<top;++i){
        m/=b;
        pre[i]=m;
    }
    return top;
}
ll qpow(ll a,ll b)
{
    ll ans=1;
    while(b)
    {
        if(b&1) ans=ans*a;
        a=a*a;
        b>>=1;
    }
    return ans;
}
ll work(ll n,ll b)
{
    ll top=init(n,b);
    ll ans=0;
    for(ll i=top-1;i>=0;--i)
    {
        ll m=0;
        m+=pre[i]*((b-1)*b)/2*qpow(b,i);
        if(num[i]!=0){
            m+=qpow(b,i)*((num[i]-1)*num[i])/2;
        }
        m+=num[i]*(suf[i]+1);
        ans+=m;
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    ll t,cas=0;
    cin>>t;
    while(t--)
    {
        ll n,b;
        cin>>n>>b;
        cout<<"Case #"<<++cas<<": "<<work(n,b)<<endl;
    }
    return 0;
}

```




### 2019 Multi-University Training Contest 8 部分补题


还是老方式，把自己比赛没A过的题，用自己思路敲一边，该补的题补一下。

这场比赛吧…感觉自己带节奏了，要不然矩形联通块那题应该能早A一个小时。


因为堕落重温了一部哈利波特电影，导致补题晚了3小时 结束时间：2019-8-17 凌晨1：19


##### 1003：Acesrc and Good Numbers


**题意**：题意求$&lt;=x$最大的$n$，满足1−n中的所有数的数位中数$d$ 出现n次

​ 题解证明了对于d=1…9，f(d,x)的值不会超过$10^{11}$ ，其中的证明自己不太能看懂。这题正解可以暴力打表，打表过程中可以剪枝。自己也看了很多博客,都是前几项打表，然后在OEIS中找数列（比赛过程中哪能看什么网站。

所以

**思路**：无（其实打表可以正着O(n)打表，也可以写个$log_{10}n$ 复杂度的计算1~n中数位d出现的总和的函数。

**代码**：无


##### 1006：Acesrc and Travel


**题意**：nothing

**思路**：nothing

**代码**：nothing


**1008：Andy and Maze**

**题意**：你迷失在了一个迷宫里，这里有n个房间，共有m条无向边连接两个房间（三无图），每个房间有一颗宝石，没经过一条边e，都要花费e.w的时间，现在你并不知道自己在哪个房间里，但是你必须找到k颗宝石才能走出走出迷宫，**不能重复经过同一个房间**，问收集到k颗宝石你需要最大需要的时间是多少？

总结：k个顶点的简单路径和的最大值。

**思路**：暴力搜索+剪纸竟然过了，当然后来出题人说数据水了，正解是一种随机算法，使用color coding的思想。

**暴力剪枝代码**：（数据水过的

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e4+10;
/*暴力+剪纸*/
int n,m,k,ans,mx;
vector<P> g[N];
bool vis[N];
void dfs(int u,int cnt,int sum)
{
    if(vis[u]) return ;
    if(sum+(k-cnt)*mx <=ans) return ;
    vis[u]=1;
    if(cnt==k){
        ans=max(ans,sum);
        vis[u]=0;
        return ;
    }
    for(P &e:g[u]){
        int v=e.first,w=e.second;
        dfs(v,cnt+1,sum+w);

    }
    vis[u]=0;

}
int main()
{
    int t ;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&n,&m,&k);
        mx=ans=-1;
        for(int i=1;i<=n;++i) g[i].clear();
        for(int i=0;i<m;++i){
            int u,v,w;
            scanf("%d%d%d",&u,&v,&w);
            mx=max(mx,w);
            g[u].push_back({v,w});
            g[v].push_back({u,w});
        }
        mset(vis,0);
        for(int i=1;i<=n;++i){
            dfs(i,1,0);
        }
        if(ans==-1) printf("impossible\n");
        else printf("%d\n",ans);

    }
}
```


下面来讲下正解color coding的思想。

我们对图中的点随机染色，颜色的种类是k种（为选取的简单路径的顶点个数）

我们接下来进行dp，$dp[ls][v][s]$ 代表长度为ls的路径，结尾顶点是v，此条路径颜色集合为s的最大时间。那么$dp[1][v][1&lt;&lt;color[v]]=0$ ，其他的$dp[1][*][*]=-inf$(无效值)

**而这个算法要求路径的所有顶点颜色不同。**

我们枚举路径长度ls，对于其中一个状态$dp[ls][v][s ]​$，枚举v的临界顶点u，那么$dp[ls][v][s]=max(dp[ls][v][s],dp[ls-1][u][s\ Xor\ (1&lt;&lt;color[v])])​$ ，且要求$s\&amp;(1&lt;&lt;color[v])!=0​$

我们枚举到答案的概率为$k!/k^k$。故我们只需要$T*(k^k/k!)$次遍历这个算法，T越大，就越有可能获得到答案那条路径。

但是这每一次的dp计算时间复杂度还是太大，为$O(k*2^k*m)$ , 但细心的话会发现，求$dp[ls][v][s]$ 是通过$dp[ls-1][u][s\ Xor\ (1&lt;&lt;color[v])])$来求的,而$[s\ Xor\ (1&lt;&lt;color[v])])$ 总是比s小的。所以我们可以省略第一维的ls，只需从小到大枚举s，对于每一个s枚举所有的顶点v，然后求$dp[s][v]$即可，这样的时间复杂度为$O(2^k*m)$


[color coding k-path近似算法详解](https://blog.csdn.net/u010352695/article/details/40924019?utm_source=blogxgwz5)


代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e4+10;
int n,m,k;
vector<P> g[N];
int color[N],dp[80][N];//s,v
void init(int n)
{
    for(int i=1; i<=n; ++i) color[i]=rand()%k;
}
int solve(int n,int m,int k)
{
    init(n);

    int top=1<<k;
    for(int i=1; i<=n; ++i)
    {
        for(int s=0; s<top; ++s) dp[s][i]=-inf; // 无效值
        dp[1<<color[i]][i]=0;
    }
    for(int s=0; s<top; ++s)
    {
        for(int u=1; u<=n; ++u) //枚举顶点
        {
            if(!(s&(1<<color[u]))) continue;//不符合
//                cout<<"asdasd"<<endl;
            for(P &p:g[u])
            {
                int v=p.first,w=p.second;
                dp[s][u]=max(dp[s][u],dp[s^(1<<color[u])][v]+w);
            }
        }
    }
    int ans=-inf;
    for(int i=1; i<=n; ++i) ans=max(ans,dp[top-1][i]);
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    srand(time(NULL));
    cin>>t;
    while(t--)
    {
        cin>>n>>m>>k;
        for(int i=1; i<=n; ++i) g[i].clear();
        for(int i=0; i<m; ++i)
        {
            int u,v,w;
            cin>>u>>v>>w;
            g[u].push_back({v,w});
            g[v].push_back({u,w});
        }
        int p=300;//随机300次
        int ans=-inf;
        while(p--)
            ans=max(ans,solve(n,m,k));
//        cout<<"ans:"<<ans<<endl;
        if(ans<0)
            cout<<"impossible"<<endl;
        else
            cout<<ans<<endl;
    }
    return 0;
}

```



##### 1009：Calabash and Landlord


**题意**：给你两个矩形，每个矩形给出其左下角坐标和右上角坐标，问矩形把所以所有格子分成几个联通块。

**思路**：坐标离散化+dfs。需要注意的是，对于矩形的边界需要格外处理。我们把矩形边界只在偶数坐标出现，奇数坐标看成格子即可。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=20;
int X[10],Y[10];//x1, x2,
int sa[N];
void disperse(int X[],int n)
{
    int top=0;
    for(int i=0; i<n; ++i)
    {

        sa[top++]=X[i];
        sa[top++]=X[i]+1;
    }
    sort(sa,sa+top);
    top=unique(sa,sa+top)-sa;
    for(int i=0; i<n; ++i)
    {
        int th=lower_bound(sa,sa+top,X[i])-sa;
        X[i]=th+1;
    }
}
int grid[20][20];
int dir[4][2]={0,1,0,-1,1,0,-1,0};
void dfs(int i,int j)
{
    grid[i][j]=2;
    for(int k=0;k<4;++k){
        int x=i+dir[k][0];
        int y=j+dir[k][1];
        if(x>0&&x<N&&y>0&&y<N&&grid[x][y]!=1){//如果有墙就不能过去
            x+=dir[k][0];
            y+=dir[k][1];
            if(x>0&&x<N&&y>0&&y<N&&grid[x][y]!=2)//没墙但走过也不能过去
                dfs(x,y);
        }
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        for(int i=0; i<4; ++i)
            cin>>X[i]>>Y[i];
        disperse(X,4);
        disperse(Y,4);
        mset(grid,0);
        for(int i=2*X[0];i<=2*X[1];++i)
        {
            grid[i][2*Y[0]]=1;
            grid[i][2*Y[1]]=1;
        }
        for(int i=2*X[2];i<=2*X[3];++i)
        {
            grid[i][2*Y[2]]=1;
            grid[i][2*Y[3]]=1;
        }
        for(int j=2*Y[0];j<=2*Y[1];++j){
            grid[2*X[0]][j]=1;
            grid[2*X[1]][j]=1;
        }
        for(int j=2*Y[2];j<=2*Y[3];++j){
            grid[2*X[2]][j]=1;
            grid[2*X[3]][j]=1;
        }
        int ans=0;
        for(int i=1;i<N;i+=2){
            for(int j=1;j<N;j+=2){
                if(grid[i][j]==0){
                    ans+=1;
                    dfs(i,j);
                }
            }
        }
        cout<<ans<<endl;
    }
}
```



##### 1010：Quailty and CCPC（水题）


**题意**：共有n个队伍参加比赛，给你一个n，d和n个队伍的信息。令$p=n*10d\%$，如果p的小数部分是0.5那就排名输出第p+1队伍的名字，否则输出Quailty is very great。

**思路**：$n*d\%10=5$，则输出排序后第$(n*d)/10+1$个队伍名称

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
struct Node
{
    string name;
    int cnt,time;
    bool operator <(const Node& other ) const
    {
        if(cnt!=other.cnt) return cnt>other.cnt;
        return time<other.time;
    }
}node[N];
int  main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t,n,d;
    cin>>t;
    while(t--)
    {
        cin>>n>>d;
        for(int i=0;i<n;++i) cin>>node[i].name>>node[i].cnt>>node[i].time;
        if(n*d%10!=5){
            cout<<"Quailty is very great"<<endl;
        }
        else{
            int th=n*d/10+1;
            nth_element(node,node+th-1,node+n);
            cout<<node[th-1].name<<endl;
        }
    }
    return 0;
}

```



##### 1011 ：Roundgod and Milk Tea



因为马虎，补题过程中wa了一发（应该是先减再赋为0，写成先赋为0，再相见


**题意**：现在有n个队伍，每个队伍有ai，并且造出了bi杯奶茶。现在要和奶茶，规则是每个队伍不可以和自己造的奶茶，问最后可以又多少个人喝到奶茶。

**思路**：我们这个让这n个队伍，倒着喝奶茶，即品茶人的顺序是1~n，喝奶茶的顺序是n~1, 这样只会有一个地方出现交叉，我们只要特殊判断处理这个地方即可。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e6+10;
ll A[N],B[N];
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll t,n;
    cin>>t;
    while(t--)
    {
        ll ans=0;
        cin>>n;
        for(ll i=1; i<=n; ++i)
            cin>>A[i]>>B[i];
        ll r=n;
        for(ll i=1; i<=n&&r>=1; ++i)
        {
            while(A[i]>0&&r>=1)
            {
                if(i==r)//处理交叉情况
                {
                    for(ll k=r-1; k>=1&&A[i]!=0; --k)
                    {
                        if(A[i]>=B[k])
                        {
                            ans+=B[k];
                            A[i]-=B[k]; 
                            B[k]=0;
                        }
                        else
                        {
                            ans+=A[i];
                            B[k]-=A[i];
                            A[i]=0;
                            break;
                        }
                    }
                    A[i]=0;
                }
                else if(A[i]>=B[r])
                {
                    ans+=B[r];
                    A[i]-=B[r];
                    B[r]=0;
                    --r;
                }
                else
                {
                    ans+=A[i];
                    B[r]-=A[i];
                    A[i]=0;
                }
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}


```




## 2019 Multi-University Training Contest 7 部分补题


这场比赛三个人一起组队，比赛期间自己感觉并没有奉献多少东西，所以补题。而且总感觉比赛到后期很乏力(没力气那种)，希望能改变。


–分割线–

这五道题补了两天


##### 1001 : A + B = C （模拟+思路）


**题意：** $a⋅10^x+b⋅10^y=c⋅10^z ~~ and~~~ 0≤x,y,z≤10^6.​$求解$x,y,z​$

**解法1:** 先去掉a,b,c末尾的零。然后可以得出来新的a,b,c数字，我们求出解后,可以在

​ 我们考虑c这个数的最高位的**来源**，c这个数的最高位有两种可能的来源。第一种是a或者b的最高位**直接相加**（包括a或b的这一位是0的情况）而来，另外一种是a和b的最高位进行相加通过**进位**而来。

​ 对于第一种我们让c与a和b的其中一个先加零到相同位，然后判断相减后是否可以得到另一个数的10次幂。

​ 对于第二种我们让c为比a多一位即可，判断相减后是否可以得到另一个数的10次幂。

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int inf=0x3f3f3f3f;
const int N=1e5+20;
const ll mod=1e9+7;
char a[N],b[N],c[N];
char sa[N],sb[N],sc[N];
int la,lb,lc;
int take_a,take_b,take_c;
int x,y,z;
char ans[N];
bool check1(char c[],int lc,char a[],int la,char b[],int lb)
{
    strcpy(sc,c);
    strcpy(sa,a);
    strcpy(sb,b);
    int ml=max(lc,la);
    for(int i=lc; i<ml; ++i) sc[i]='0';
    sc[ml]='\0';
    for(int i=la; i<ml; ++i) sa[i]='0';
    sa[ml]='\0';
    if(strcmp(sc,sa)< 0 ) return false;
    /*大数减法*/
//    printf("sc:%s,sa:%s\n",sc,sa);
    reverse(sc,sc+ml);
    reverse(sa,sa+ml);
    mset(ans,0);
    for(int i=0; i<ml; ++i)
    {
        ans[i]+='0'+sc[i]-sa[i];
        if(ans[i]<'0')
        {
            ans[i]+=10;
            sc[i+1]--;
        }
    }
    int p=ml-1;
    while(p>0&&ans[p]=='0') --p;
    reverse(ans,ans+p+1);
    ans[p+1]='\0';
//     printf("ans:%s\n",ans);
//    bool flag=true;
    if(p+1<lb) return false;
    for(int i=lb; i<=p; ++i)
    {
        if(ans[i]!='0') return false;
    }
    ans[lb]='\0';
    if(strcmp(ans,sb)==0)
    {
        x=ml-lc;
        y=ml-la;
        z=p+1-lb;
        return true;
    }
    else
        return false;
}
bool check2(char c[],int lc,char a[],int la,char b[],int lb)/*c的最高位通过进位得到的*/
{
    strcpy(sc,c);
    strcpy(sa,a);
    strcpy(sb,b);
    int ml=max(lc,la);
    for(int i=lc; i<=ml; ++i) sc[i]='0';
    sc[ml+1]='\0';
    for(int i=la; i<ml; ++i) sa[i]='0';
    sa[ml]='\0';
    /*大数减法*/
//    printf("sc:%s,sa:%s\n",sc,sa);
    reverse(sc,sc+ml+1);
    reverse(sa,sa+ml);
    mset(ans,0);
    for(int i=0; i<ml; ++i)
    {
        ans[i]+='0'+sc[i]-sa[i];
        if(ans[i]<'0')
        {
            ans[i]+=10;
            sc[i+1]--;
        }
    }
    int ans_len=ml;
    if(sc[ans_len]>'0')
    {
        ans[ans_len++]=sc[ml];
    }
    while(ans_len>0&&ans[ans_len-1]=='0') --ans_len;
    reverse(ans,ans+ans_len);
//    ans[ans_len]='\0';
//    printf("ans:%s\n",ans);
//    bool flag=true;
    if(ans_len<lb) return false;
    for(int i=lb; i<ans_len; ++i)
    {
        if(ans[i]!='0') return false;
    }
    ans[lb]='\0';
    if(strcmp(ans,sb)==0)
    {
        x=ml-lc+1;
        y=ml-la;
        z=ans_len-lb;
        return true;
    }
    else
        return false;
    /*接下里判断字符串sc是否是ans的前缀*/
}
void solve(int add_a,int add_b,int add_c)
{
    add_a-=take_a;
    add_b-=take_b;
    add_c-=take_c;
    int add=0;
    if(add_a<0&&-add_a>add) add=-add_a;
    if(add_b<0&&-add_b>add) add=-add_b;
    if(add_c<0&&-add_c>add) add=-add_c;
    printf("%d %d %d\n",add_a+add,add_b+add,add_c+add);
}
int main()
{
//    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    scanf("%d",&t);
    while(t--)
    {
        take_a=take_b=take_c=0;
        scanf("%s%s%s",a,b,c);
        la=strlen(a);
        lb=strlen(b);
        lc=strlen(c);
        while(la>0&&a[la-1]=='0') --la,++take_a;
        a[la]=0;
        while(lb>0&&b[lb-1]=='0') --lb,++take_b;
        b[lb]=0;
        while(lc>0&&c[lc-1]=='0') --lc,++take_c;
        c[lc]=0;
//        printf("chedan_%d %d %d\n",take_a,take_b,take_c);
        if(check1(c,lc,a,la,b,lb))//x,y,z
        {
            solve(y,z,x);
            continue;
        }
        if(check1(c,lc,b,lb,a,la))//x,y,z
        {
            solve(z,y,x);
            continue;
        }
        else
        {
            if(check2(c,lc,a,la,b,lb))//
            {
                solve(y,z,x);
                continue;
            }
            if(check2(c,lc,b,lb,a,la))//x,y,z
            {
                solve(z,y,x);
                continue;
            }
            //未处理
        }
        printf("-1\n");
    }
    return 0;
}
```


**解法2：**

首先把$a,b,c$ 末尾的$0$ 全去掉, 考虑$C*10^k$，

K>0的情况只存在$A+B=C*10^k$。因为假设$A*10^n+B=C*10^k$ 总是不满足的, 得到的结果末尾位必为非零数，与假设矛盾

剩下的就是$k=0$的情况，此时只有 $A*10^n+B=C$的情况 。


解法$2$写了一上午，一直超时，最后发现for循环的++$i$写成$+i$了.（打脸


**代码:**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
string add(string a,string b)
{
    reverse(a.begin(),a.end());reverse(b.begin(),b.end());
    int maxl=max(a.size(),b.size());
    for(int i=a.size();i<maxl;++i) a.append("0");
    for(int i=b.size();i<maxl;++i) b.append("0");
    for(int i=0;i<maxl;++i){
        b[i]+=a[i]-'0';
        if(b[i]>'9'){
            b[i]-=10;
            if(i==maxl-1){
                b.append("1");
            }
            else
                b[i+1]++;
        }
    }
    reverse(b.begin(),b.end());
    return b;
}
string mul(string a,string b)//要求是a-b   //这里函数名应该写成sub...
{
     reverse(a.begin(),a.end());reverse(b.begin(),b.end());
     int maxl=a.size();
     for(int i=b.size();i<maxl;++i) b.append("0");
     for(int i=0;i<maxl;++i)
     {
         a[i]-=b[i]-'0';
         if(a[i]<'0'){
            a[i]+=10;
            a[i+1]-=1;
         }
     }
     while(a.size()>1&&a[a.size()-1]=='0') a.pop_back();
    reverse(a.begin(),a.end());
   return a;
}
int add_a,add_b,add_c;
int take_a,take_b,take_c;
bool check1(string &a,string& b,string &c)//计算a+b=c*k中k的10次多少次幂
{
    string ans=add(a,b);
    if(ans.size()<c.size()||(ans.size()==c.size()&&ans<c)) return false;
    int cnt=0;
    for(int i=c.size();i<ans.size();++i) {
        if(ans[i]!='0') return false;
        ++cnt;
    }
    for(int i=0;i<c.size();++i){
        if(ans[i]!=c[i]) return false;
    }
    add_a=add_b=0;
    add_c=cnt;
    return true;
}
bool check2(string &a,string &b,string &c)
{
    if(c.size()<b.size()||(c.size()==b.size()&&c<b)) return false;
    string ans=mul(c,b);
    int cnt=0;
    for(int i=a.size();i<ans.size();++i) {
        if(ans[i]!='0') return false;
        ++cnt;
    }
    for(int i=0;i<a.size();++i){
        if(ans[i]!=a[i]) return false;
    }
    add_a=cnt;
    add_b=0;
    add_c=0;
    return true;
}
void solve(int add_a,int add_b,int add_c)
{
    add_a-=take_a;
    add_b-=take_b;
    add_c-=take_c;
    int add=0;
    if(add_a<0&&-add_a>add) add=-add_a;
    if(add_b<0&&-add_b>add) add=-add_b;
    if(add_c<0&&-add_c>add) add=-add_c;
    cout<<add_a+add<<" "<<add_b+add<<" "<<add_c+add<<endl;
//    printf("%d %d %d\n",add_a+add,add_b+add,add_c+add);
}
string a,b,c;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        take_a=take_b=take_c=0;
        cin>>a>>b>>c;
        while(a.size()>1&&a[a.size()-1]=='0'){
            take_a++;
            a.pop_back();
        }
        while(b.size()>1&&b[b.size()-1]=='0'){
            take_b++;
            b.pop_back();
        }
        while(c.size()>1&&c[c.size()-1]=='0'){
            take_c++;
            c.pop_back();
        }
        if(check1(a,b,c))
        {
            solve(add_a,add_b,add_c);
            continue;
        }
        else if(check2(a,b,c))
        {
            solve(add_a,add_b,add_c);
            continue;
        }
        else if(check2(b,a,c))
        {
            solve(add_b,add_a,add_c);
            continue;
        }
        else
            cout<<"-1"<<endl;
    }
    return 0;
}
```



##### 1006：Final Exam（构造+思路）



就是这题，让我补了一天零一个晚上


**题意：**一共有n道题，需要做对k道题，自己只知道这n道题的总分为m，不知道分数的分布。若一道题为x分，则需要x+1时间去复习。问最少需要多长时间复习，能保证自己肯定能过k个题。

**思路：** 如果我是老师的话，我会卡你复习课本的最少科目n-k+1个。比如现在有5门课复习时间分别是0 1 2 3 4，自己要过3门，那老师用最少的分数卡你只需要卡你最少前3门就行，会让5们课的分数分别为0 1 2 * * ，* 代表这门课分数随便给，给0也行。

​ 那么我们再换回学生的角度，假如我们最多让他卡n-k 门课，我们可以让，前n-k+1门课的复习总时间为m+1。剩下k-1门课让他不想选就行。假如他只选前n-k+1门，那么其中必有一门不会被卡。那么怎么样让他不想选后k-1门课呢？假设后k-1门课每门课的时间为t，那么我们只需要$m-(n-k)*t&lt;t$ 即可。

​ 上面那个公式的意思就是：前1,2,…n-k门课的复习时间都设置成t，最后一门功课的时间只能小于t,这样他就不会选后k-1门课。

**代码：**

```cpp
#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        ll n,m,k;
        scanf("%lld%lld%lld",&n,&m,&k);
        ll t=m/(n-(k-1))+1;
        printf("%lld\n",t*(k-1)+m+1);
    }
    return 0;
}
```



##### 1007：Getting Your Money Back（动态规划+单调性优化）



这题因为看不懂题解，但是因为题解产生出了另一个DP思想。从头到尾wa了20多发，找bug找了不下6个小时。这里写下当时所犯的错误，给自己提个醒！

1.边界问题未考虑清楚. （例如对于单调性用p做指针时，p应该从1开始，刚开始写成了0，又如对于$dp[0][0]$不存在，值应该设为无效值。）

2.未考虑清楚状况，马马虎虎。

3.刚开始不相信自己，总想往题解上靠。事实证明思路有多种，dp方式千遍万化

补题时间2019-8-16 凌晨0:20


**题意：**

**思路：**这里的思路与题解不同。

​ 我们可以看出来答案与区间的关系归为答案与区间长度的关系。但是对于区间长度又有两种不同的状态，一种是左端点肯定可以取钱，另一种是左端点不一定可以取钱。

我们用$dp[0][i]$表示长度为$i$ 的区间，且左端点一定可以取钱，其在**最坏情况**下把**确定已经把所有的钱取出来**的**最小花费金币。**

其次$dp[1][i]$表示长度为$i$的区间,且左端点不一定可以取钱，其在**最坏情况**下把**确定已经把所有的钱取出来**的**最小花费金币。**

对于$0$点比较特殊，我们因为$[0,0]区间是不用确定的，但该区间左端点为0时$，我们可以把$[0,r]$的最小花费转化为$dp[1][r]$

对于其他区间$[l,r]​$，我们只需求$dp[0][r-l+1]​$即可

​ dp方程：

$dp[0][x]=min(max(dp[1][x-j]+a,dp[0][j-1]+b)) ，j\in[1,x]$

$dp[1][x]=min(max(dp[1][x-j]+a,dp[1][j-1]+b)) ,j\in[1,x]$

又因为$dp[0][x]$状态中 枚举长度1的处肯定是必成功的，所以不存在失败的情况，这也是$dp[0][0]$值是无效值的原因。

但是朴素的思想是每次需要O(n)枚举端点的，时间复杂度O(n^2)。


感觉下一段有篇博客说的不错，这里引用一下。[来源博客地址](https://blog.csdn.net/u013534123/article/details/99413758)


​ 显然，区间跨度越大，花费的代价也就越大，$dp[0[i]$和$dp[1][i]$是具有单调性的。然后考虑这个转移方程，取前后两部分大的那个，可以预见，代价随着决策点$j$从左往右移动先变小后变大。所以，我们可以考虑直接对这个转移方程进行三分，找到中间的最小决策。但是，用上三分理论复杂度可以过去，不过我写的确实TLE了，当然可能是我写残了。（三分我也TLE了(⊙﹏⊙)

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
ll dp[2][200005];
ll t,x,y,a,b;
ll f0(ll i,ll j)
{
    return max(dp[0][j-1]+b,dp[1][i-j]+a);
}
ll f1(ll i,ll j)
{
    return max(dp[1][j-1]+b,dp[1][i-j]+a);
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>t;
    dp[0][0]=-1e15;
    dp[1][0]=0;
    while(t--)
    {
        cin>>x>>y>>a>>b;
        dp[0][1]=a;
        dp[1][1]=max(a,b);
        ll ls=y-x+1;
        int flag=0;
        if(x==0)
        {
            --ls;
            flag=1;
        }
        int p0=1,p1=1;
        for(ll i=2;i<=ls;++i){
            /*求dp[0][i]*/
            while(p0<i&&f0(i,p0)>=f0(i,p0+1)) ++p0;
            dp[0][i]=f0(i,p0);
            while(p1<i&&f1(i,p1)>=f1(i,p1+1)) ++p1;
            dp[1][i]=f1(i,p1);
        }
        if(flag==1)
            cout<<dp[1][ls]<<endl;
        else
            cout<<dp[0][ls]<<endl;//
    }
    return 0;
}
```



##### 1010：Just Repeat（思维，贪心）



这题让我补了一上午，其实并不难，主要读懂题意。这里记录下补题过程中犯下的错

1.题意没读清楚，误以为是不能打对手上次出的牌的颜色，其实是对手所有出过的牌的颜色。

2.以为O(n*logn)会超时，一直在想O(n)的方法，没想到用unordered_map过了。更可笑的是以为p=2的情况出的数据有规律,可以O(n)求（~~>_<~~。

补题时间：2019-8-16 12：53


**题意：**两个人打赌用玩游戏决定输赢。这两个人手里分别有n和m和张牌,并且他们都知道对手的牌，每张牌都有一个颜色，**游戏的规则是**：双方轮流每次打出一张牌，但是**不能打对手已经出过的颜色的牌**，先不能打出牌的人输，(包括没牌和有牌不能出的情况)。问双方都使用最优策略，最后谁是赢。

**思路：** 这题其实就是算谁打出的牌数量最多。

​ 首先对于双方不重复颜色的牌，双方都是可以打出来的，没有限制。所以我们只需要考虑双方重复颜色的即可。假如黄色牌我有x个，对方有y个。那么自己打黄色的牌得到的贡献是x，对面打黄色的牌得到的贡献为y。


下一段引用题解


​ 到此为止, 问题转换成另一个问题, 就是有一堆东西, 每个东西有两个值, A 拿到这个东西的收益是 ai, B 拿到的收益是 bi．两人依次拿．求最优策略下两人的各自收益．这是一个经典问题, 答案就是按照 ai + bi 排序模拟一下就好了。（最优策略是指最终获得的价值减去对面的价值的差最大。排序处理后我们只需要让A,B轮流取即可。

​ 那么QQ打出的牌就是QQ在重复颜色的牌获得的价值加上不重复颜色的牌的数量。CC同理

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
u64 k1,k2,mod;
unordered_map<u64,int> mmp_q;
unordered_map<u64,int> mmp_c;
unsigned long long rng() {
    unsigned long long k3 = k1, k4 = k2;
    k1 = k4;
    k3 ^= k3 << 23;
    k2 = k3 ^ k4 ^ (k3 >> 17) ^ (k4 >> 26);
    return k2 + k4;
}
u64 repQ,repC,remQ,remC;
u64 card[2][N];
void read(int kinds,int n,int cmd)
{
//    puts("--------");
    if(cmd==1)
        for(int i=0;i<n;++i)
             scanf("%llu",&card[kinds][i]);
    else{
        scanf("%llu%llu%llu",&k1,&k2,&mod);
        for(int i=0;i<n;++i)
            card[kinds][i]=rng()%mod;
    }
}
P reap[N];
int top;//重复的种类以及对应的总和
bool cmp(P a, P b)
{
    return a.first+a.second>b.first+b.second;
}
int main()
{
    int t,n,m,cmd;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&n,&m,&cmd);
        read(0,n,cmd);
        read(1,m,cmd);
        repQ=repC=0;
        mmp_q.clear();
        mmp_c.clear();
        for(int i=0;i<n;++i) ++mmp_q[card[0][i]];
        for(int i=0;i<m;++i) ++mmp_c[card[1][i]];
        top=0;
        for(pair<u64,int> p :mmp_q)
        {
            u64 val=p.first;
            int cnt=p.second;
            if(mmp_c.find(val)!=mmp_c.end()){
                int other_cnt=mmp_c[val];
                repQ+=cnt;
                repC+=other_cnt;
                reap[top++]={cnt,other_cnt};
            }
        }
        u64 sum_q=n-repQ,sum_c=m-repC;
        sort(reap,reap+top,cmp);
        for(int i=0;i<top;++i){
            if(i&1){
                sum_c+=reap[i].second;
            }
            else
                sum_q+=reap[i].first;
        }
        if(sum_q>sum_c)
            printf("Cuber QQ\n");
        else
            printf("Quber CC\n");
    }
    return 0;
}
```



##### **1011：Kejin Player**（简单概率DP）


**题意：**有$n​$个等级分别为$1​$到$n​$,我们从第$i​$级升到$i+1​$级时，需要花费$a[i]​$金币，并有$r[i]/r[i]​$的概率升级成功，否则失败并降到$x[i]​$级，问从第从$l​$级别到$r​$级别所需期望金币是多少？

**思路：**我们发现升级只能一级一级升，假设$f(1,x)$为从$1$级升到$x$级的期望金币,那么从$l$级别到$r$级别所需期望金币就是$f(1,r)-f(1,l)$。我们用$dp[i]$代表从$i$ 升级到$i+1$的期望金币,那么就有

$dp[i]=a[i]+(1-p)(dp[i]+dp[i-1]+dp[i-2]...dp[x[i]])$

我们移项后得到

$dp[i]=(a[i]+(1-p)*(dp[i-1]+dp[i-2]...dp[x[i]]))/p​$

其中连续和一部分可以用前缀和O(1)求

故从第从$l$级别到$r$级别所需期望金币是=$dp[l]+dp[l+1]...+dp[r-1]$

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int inf=0x3f3f3f3f;
const int N=5e5+5;
const ll mod=1e9+7;
ll qpow(ll a,ll b)
{
    ll ans=1;
    while(b)
    {
        if(b&1) ans=ans*a%mod;
        a=a*a%mod;
        b>>=1;
    }
    return ans;
}
ll inv(ll a)
{
    return qpow(a,mod-2);
}
ll r[N],s[N],x[N],a[N];
ll sum[N];
int main()
{
    ll t;
    scanf("%lld",&t);
    while(t--)
    {
        ll n,q;
        scanf("%lld %lld",&n,&q);
        sum[0]=0;
        for(ll i=1;i<=n;++i)
            scanf("%lld%lld%lld%lld",r+i,s+i,x+i,a+i);
        for(ll i=1;i<=n;++i)
        {
            ll p=r[i]*inv(s[i])%mod;
            ll ans=(a[i]+(1ll-p+mod)*((sum[i-1]-sum[x[i]-1]+mod)%mod)%mod)%mod;
            ans=ans*inv(p)%mod;
            sum[i]=(sum[i-1]+ans)%mod;//*****
        }
        while(q--)
        {
            ll l,r;
            scanf("%lld%lld",&l,&r);
            ll ans=(sum[r-1]-sum[l-1])%mod;
            ans=(ans+mod)%mod;
            printf("%lld\n",ans);
        }
    }
    return 0;
}
```




## 2019百度之星初赛第二场C题度度熊与运算式 1（hdu6676）


题目网址：[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=6676)


这道题赛场上没写出来，补题时候看了题解才会的。


思路：若把最终的运算时用^切成许多段，定义一段的长度为该段1的个数,若某一段的长度不是2的幂次,那么可以把该段用异或分成2的幂次个1相加。 所以我们枚举幂次i,是否可以构成2^i。 剩下的段就全变为1个即可

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
//typedef  __int128 i128 ;
const int inf=0x3f3f3f3f;
const int N=2.6e5+10;
char s[2][N```




## 2019牛客暑期多校训练营（第十场） 补题


​ 这场比赛是三个人一起写的，但都是单挑，比赛过程中第一水题以为是找规律，然后浪费了半个小时，其实暴力递归就能写。还有一道水题，对于两个图的判断情况没想清除，导致一直wa，最后总的来说自己着只A了三道吧。补了两道题


比赛链接：[https://ac.nowcoder.com/acm/contest/890#question](https://ac.nowcoder.com/acm/contest/890#question)


##### B:Coffee Chicken



以为是找规律，从而浪费了半个小时。其实就是个简单的暴力递归。


**题意**：有一个字符串序列$s[i]$，满足$s[1]=&quot;COFFEE&quot;,s[2]=&quot;CHICKEN&quot;$，且$s[i]=s[i-2]+s[i-1]$，给你一个n和k，让求$s[n]$中第k个开始的10个字符是多少。如果不够则输出第k个到结尾即可。$n&lt;=500,k&lt;=10^{12}$

**思路**：该序列形似斐波那契，长度增长极快，当$i=60$，字符串长度早已经大于k的最大值，对于n>60的字符串的长度为$10^{12}+10$，他们的前缀一定是$s[59]$或$s[60]$, 这样我们就可以把范围归为$n&lt;=60$。

​ 我们只要预处理出前60个字符的长度。那么求字符串$s[i]$的第k往后的几个字符可以转化为求$s[i-2],s[i-1]$的第k’往后的几个字符。当递归到$n&lt;=10$小范围时，直接输出答案即可。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e4+10;
//string s[20];
ll f[100];//56就已经超过了
string s[100];
void back(ll n,ll k,ll cnt)
{
    if(n<=10)
    {
        for(ll i=0;i<cnt;++i) cout<<s[n][k+i-1];
        return ;
    }
    if(k+cnt-1<=f[n-2]){//在s[n-2]
        back(n-2,k,cnt);
    }
    else if(k<=f[n-2]&&k+cnt-1>f[n-2]){//在s[n-2]和s[n-1]上
        back(n-2,k,f[n-2]-k+1);
        back(n-1,1,10-(f[n-2]-k+1));
    }
    else{
        back(n-1,k-f[n-2],cnt);//在 s[n-1]上
    }
}

void init()
{
    f[1]=6ll,f[2]=7ll;
    s[1]="COFFEE";
    s[2]="CHICKEN";
    for(ll i=3; i<=10; ++i) s[i]=s[i-2]+s[i-1];
    for(ll i=3; i<=57; ++i) f[i]=f[i-1]+f[i-2];
}
int main()
{
    init();
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,k;
        cin>>n>>k;
        if(n>56)//控制到60以内
        {
            ll k=n-56;
            if(k&1) n=57;
            else n=56;
        }
        if(f[n] <k+10-1 )
        {
            back(n,k,f[n]-k+1);
        }
        else
        {
            back(n,k,10);
        }
        cout<<endl;
    }
}

```


##### D:Han Xin and His Troops



这道题补的也不太顺序，因为我的代码中用的是不互质的扩展CRT，但是自己对扩展CRT不理解。导致对于炸long long的地方不知道入手点。然而比赛过后因为马虎导致又 wa了三次


**题意**：

​ 给出n个同余方程$ai,bi​$，代表$x=bi( mod\ \ ai)​$。解的可能最大值max，判定属于**无解，解太大，正常解** 的哪种情况，对于第三种情况输出其解。$0&lt;=max&lt;=1e^{18},ai&lt;=1e^5,bi&lt;=1e^5​$。

**思路**：

​ 可以考虑将$ai$分解为质数，再使用CRT。或者使用扩展CRT，不过要注意模数和解爆long long 的情况。可以使用$\_\_int128$。但这里使用$\_\_ int128$只能过95%，这里猜测是模数炸$\_\_ int128$ 。因为使用可扩展CRT解一次方程过程中，解是不断增大的，所以我们可以提前判断解是否大于max。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
//#define  i128 __int128
typedef  __int128 i128 ;
const int inf=0x3f3f3f3f;
const int N=1e4+10;
i128 extend_gcd(i128 a,i128 b,i128 &x,i128  &y)

{
    if(a == 0 && b == 0)return -1;
    if(b ==0 )
    {
        x = 1;
        y = 0;
        return a;
    }
    i128 d = extend_gcd(b,a%b,y,x);
    y -= a/b*x;
    return d;
}
long long  m[110],a[110];//模数为m,余数为a, X % m = a
long long _n,_m;
bool is_big;
bool solve(i128 &m0,i128 &a0,i128 m,i128 a)
{
    i128 y,x;
    i128 g = extend_gcd(m0,m,x,y);
    i128 d=a0-a;
    if(d < 0) d = -d;
    if(d % g) return false;
    x *= (a - a0)/g;
    x %= m/g;
    a0 = (x*m0 + a0);
    m0 *= m/g;
    a0 %= m0;
    if( a0 < 0 )a0 += m0;
    if(a0>_m)
         is_big=true;
    return true;
}
/*
 * 无解返回false,有解返回true;
 * 解的形式最后为 a0 + m0 * t  (0<=a0<m0)
 */
bool MLES(i128 &m0,i128 &a0,i128 n) //解为  X = a0 + m0 * k
{
    bool flag = true;
    m0 = 1;
    a0 = 0;
    for(i128 i = 0; i < n; i++)
        if( !solve(m0,a0,m[i],a[i]) )
        {
            flag = false;
            break;
        }
    return flag;
}

int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    cin>>_n>>_m;
    for(i128 i=0;i<_n;++i){
        cin>>m[i]>>a[i];
    }
    i128 m0,a0;
    is_big=false;
    bool ok=MLES(m0,a0,_n);
    if(ok==false){
        cout<<"he was definitely lying"<<endl;
    }
    else if(a0>_m||is_big){
        cout<<"he was probably lying"<<endl;
    }
    else
        cout<<(long long)(a0)<<endl;
    return 0;
}
```


##### H：Hilbert Sort



简单的递归，但是因为打代码不细心，wa了两次。导致慢了20分钟


**题意**：给你一个递归图，图中每个坐标的二维大小为区间经过点的顺序，给出n个点，输出二维排序后的点。

**思路**：递归求出每个点是几个经过的即可

**代码**：

```cpp
	#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e6+10;
ll get(int k,int x,int y)
{
    if(k==0) return 1;
    ll cnt=(1ll<<(2*k-2));
    int md=1<<(k-1);
    if(x<=md&&y<=md){
        return get(k-1,y,x);
    }
    if(x<=md&&y>md){
        y-=md;
        return 3ll*cnt+get(k-1,md-y+1,md-x+1);
    }
    if(x>md&&y<=md){
        x-=md;
        return cnt+get(k-1,x,y);
    }
    if(x>md&&y>md){
        x-=md,y-=md;
        return cnt*2ll+get(k-1,x,y);
    }
    return 0;
}
struct S
{
    int x,y;
    ll pos;
    bool operator <(const S& other) const{
        return pos<other.pos;
    }
}sta[N];
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int n,k;
    cin>>n>>k;
    for(int i=1;i<=n;++i)
    {
        cin>>sta[i].x>>sta[i].y;
        sta[i].pos=get(k,sta[i].x,sta[i].y);
    }
    sort(sta+1,sta+n+1);
    for(int i=1;i<=n;++i)
        cout<<sta[i].x<<" "<<sta[i].y<<endl;
    return 0;

}
```


##### F: Popping Balloons



思路+模拟，因为没考虑完全所有情况，导致代码有所不及。出过一次bug，因为注意点错导致找了1个小时bug


**题意**：给出n个气球的坐标，自己可以选择三行，和三列进行射击。射击该行或该列可以打爆这条直线上的所有气球。现要求选择的相邻行和列列的距离必须为d。求打爆气球的最大个数。

**思路**：


引用题解


​ 用f(i)表示中间一枪打第i行，能够射中的气球个数；用g(i)表示中间一枪打第i列，能射中的气球个数。 用multiset存所有g(i)的值，枚举中间一枪打第x行，将对每一个位于第x-r,x,x+r行的气球，将它们影响到 的列（共三列）的g(j)的值更新，然后更新multiset内的元素。 中间一枪打第x行的最大收益即f(x)+(当前multiset内最大元素)。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
//typedef  __int128 i128 ;
const int inf=0x3f3f3f3f;
const int N=1e5+10;
vector<int> row[N];
multiset<int,greater<int>> mmp;
int r_sum[N],c_sum[N];
int f[N],g[N];
int n,k,maxr,maxc;

void del(int val)
{
    mmp.erase(mmp.find(val));
}
void add(int val)
{
    mmp.insert(val);
}
void work(int i,int val)//将第i列的和增加1
{

     del(g[i]);
     add(g[i]+val);
     g[i]+=val;

    if(i-k>=0)
    {
        del(g[i-k]);
        add(g[i-k]+val);
        g[i-k]+=val;
    }

    if(i+k<=maxc)//i+k>=k
    {
        del(g[i+k]);
        add(g[i+k]+val);
        g[i+k]+=val;
    }
}

int main()
{
//    freopen("C:\\Users\\12495\\Desktop\\data\\9.in","r",stdin);
    scanf("%d%d",&n,&k);
    maxr=-1,maxc=-1;
    for(int i=0;i<n;++i){
        int x,y;
        scanf("%d%d",&x,&y);
        maxr=max(maxr,x);
        maxc=max(maxc,y);
        ++r_sum[x];
        ++c_sum[y];
        row[x].push_back(y);
    }
//    cout<<"k:"<<k<< "maxc:"<<maxc<<endl;
    int ans=-1;
    for(int i=0;i<=maxr;++i){
        int sum=r_sum[i];
        if(i-k>=0)
            sum+=r_sum[i-k];
        if(i+k<=maxr)
            sum+=r_sum[i+k];
        f[i]=sum;
    }
    for(int i=0;i<=maxc;++i){
        int sum=c_sum[i];
        if(i-k>=0)
            sum+=c_sum[i-k];
        if(i+k<=maxr)
            sum+=c_sum[i+k];
        g[i]=sum;
    }
    for(int i=0;i<=maxc;++i)  mmp.insert(g[i]);
    for(int i=0;i<=maxr;++i){
        for(int v:row[i])   work(v,-1);
        if(i-k>=0)
            for(int v:row[i-k]) work(v,-1);
        if(i+k<=maxr)
            for(int v:row[i+k]) work(v,-1);

        int maxx=*(mmp.begin());
        ans=max(ans,f[i]+maxx);
        for(int v:row[i])   work(v,1);
        if(i-k>=0)
            for(int v:row[i-k]) work(v,1);
        if(i+k<=maxr)
            for(int v:row[i+k]) work(v,1);
    }
    printf("%d\n",ans);
}

```


##### H:Stammering Chemists



签到，这就是前面提到的签到题没考虑完所有状况导致卡了快两个小时的题


**题意**：水题

**思路**：可以根据度数的个数来判断出4个图，剩下的两个图可以根据最大度数的顶点到叶子的最大距离来区分

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef unsigned long long u64;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=1e4+10;
int du[6],cnt[6];
vector<int> g[7];
int root,mx;

int dfs(int u,int fa)
{
    int maxx=0;
    for(int v:g[u]){
        if(v==fa) continue;
        maxx=max(maxx,dfs(v,u));
    }
    return maxx+1;
}
int mid;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    cin>>t;
    while(t--)
    {
        for(int i=1;i<=6;++i) g[i].clear();
        for(int i=1;i<=6;++i) du[i]=cnt[i]=0;
        int inx=0;
        for(int i=0;i<5;++i){
            int u,v;
            cin>>u>>v;
            du[u]++;
            du[v]++;
            g[u].push_back(v);
            g[v].push_back(u);
        }
        for(int i=1;i<=6;++i){
            if(du[i]>du[inx]) inx=i;
        }
        for(int i=1;i<=6;++i) cnt[du[i]]++;
        if(cnt[1]==2&&cnt[2]==4){
            cout<<"n-hexane"<<endl;
        }
        else if(cnt[1]==3&&cnt[2]==2&&cnt[3]==1){
            if(dfs(inx,inx)==3){
                cout<<"3-methylpentane"<<endl;
            }
            else{
                cout<<"2-methylpentane"<<endl;
            }
        }
        else if(cnt[1]==4&&cnt[3]==2){
            cout<<"2,3-dimethylbutane"<<endl;
        }
        else if(cnt[1]==4&&cnt[2]==1&&cnt[4]==1)
        {
            cout<<"2,2-dimethylbutane"<<endl;
        }

    }
    return 0;
}
```


##### 总结：


​ 其实还有一些题目不难，比如 J 题的DP等等，这场比赛还有color coding近似算法可以说是非常精彩了。

不过在比赛中自己也犯了不少错误，导致浪费了很多时间。比如刚开局，花了20分钟去找规律，其实开始感觉这题可以分治，但是没往上面想，导致题目半小时的时候才开始写正解，但是期间因为马虎出bug了，调试了10分钟左右才给A了。接下来去做H题的签到题了，因为思路是错误的，就一直wa，wa了6发左右才清楚过来。D题是个暴力递归（分治）。思路是正确的，但是实现上有些问题导致wa了2发。

​ 总的来说比赛过程中因为思路不全面，写代码不严谨导致wa了许多发，浪费了很多时间，今后要注意。

补题过程中也不顺利，比如说气球那题，找一个简单的bug找了许久，感觉原因是因为自己注意力不够。（当然思路也有点不严谨）。至于D题扩展CRT，这也是我第一次用int128（发现code blocks 不支持$\_\_ int128$) ，也学了一下扩展CRT，复习了CRT。



## CCPC－Wannafly & Comet OJ 夏季欢乐赛（2019）比赛总结


##### 总结：


​ 这场比赛不太顺心，B，I水题 10分钟内A了。A题推公式用double写卡了1个小时，换成其他暴力也错了，赛后补题与AC代码对比发现一个语句的与想象中的不一样，但是现在还不知道为什么。C题阶乘没想到4!!爆int，一直以为会有个公式，真是大意了导致卡了1个小时。D题是线段树+扫描线，不熟悉主动放弃。G题想到了每类取前5个然后暴搜，但是算错时间复杂度了以为会超时就没写，不过5分钟之后想到状压dp就给A了。H题分配学号，思路也是比较顺利，不过代码写完之后有诸多bug（写错语句这种低级错误），导致比赛结束后也没A出来，赛后才直到一个变量没有赋新值，就这样浪费了一个多小时。

​ 总的来的这场比赛小错误犯的太多了，打代码的时候应该再用点心，初始化、语句写错等低级错误不用犯了。

##### 比赛链接：[传送门](https://www.cometoj.com/contest/59)


##### 题解：


**A题完全k叉树**

解决方案：满层的与根的距离*2+残缺层的最左边节点与上一层的距离+最右边的节点是否可以可以让答案更远。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int inf=0x3f3f3f3f;
const double eps=1e-9;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t;
    ll n, k,ans=0;
    cin>>t;
    while(t--)
    {
        cin>>k>>n;
        if(k==1ll){
            cout<<n-1ll<<endl;
            continue;
        }
        ll d=0ll,det=1ll,fsum=1ll;
        while(true)
        {
            if(det*k+fsum>n) break;
            d++;
            det*=k;
            fsum+=det;
        }
        ans=d*2;
        if(n-fsum>0ll) ans++;
        if(n-fsum>det) ans++;
        cout<<ans<<endl;

    }
    return 0;
}
```


**B题距离产生美**

解决方案：贪心

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll A[100005];
int main()
{
    int n;
    ll k;
    ios::sync_with_stdio(false);cin.tie(0);
    cin>>n>>k;
    ll ppp=1e18+10;
    for(int i=0;i<n;++i) cin>>A[i];
    int ans=0;
    for(int i=1;i<n;++i)
    {
        if(abs(A[i]-A[i-1])<k){
            ans++;
            A[i]=ppp;
        }
    }
    cout<<ans<<endl;
    return 0;
}
```


**C题烤面包片**

解决方案：n>=4的话，n!!的值一定大于mod，结果是0，其他情况暴力求解

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll calc(ll a)
{
    ll ans=1;
    for(ll i=a; i; --i)
    {
        ans=ans*i;
    }
    return ans;
}
ll calc(ll a,ll mod)
{
    if(a>=mod) return 0;
    ll ans=1;
    for(ll i=a;i;--i)
    {
        ans=ans*i%mod;
        if(!ans) return 0;
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n,mod;
    cin>>n>>mod;
    if(n>=4){
        cout<<0<<endl;
    }
    else if(n==1||n==0)
    {
        cout<<1%mod<<endl;
    }
    else {
        ll ans=calc(n);
        ans=calc(ans);
        ans=calc(ans,mod);
        cout<<ans%mod<<endl;
    }
    return 0;

}
```


**D题茶颜悦色**

解决方案：线段树+扫描线不会，数据结构靠队友，没时间了只能后来再补了

**E飞行棋**

还没看题概率dp，先放这，有时间再补吧

**F题三元组**

解决方案：考虑$a_i+a_j&lt;=b_i+b_j​$ 时候，公式化成$2*a_i-b_i+2*a_j+b_j&lt;=0​$,

否则$a_i+a_j &gt;b_i+b_j$ 时候公式化为$2*b_i-a_i+2*b_j+a_j&lt;=0$,考虑到这两种情况不会同时出现，我们可以分类统计。

先按照第一种情况按$2*a_i-b_i$的值从到大排序，假如对于i，其符合条件的的最远的下标为p[i],那么对于i+1,符合条件的最远的下标在[i+1,p[i]]中，即p[i]不会增大，所以我们可以O(n)双指针来计算对于每个 i 符合条件的最远的下标为 p[i]。然后统计贡献值即可

第二种情况将$a_i$和$b_i$交换然后再按第一种情况统计贡献值即可

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
vector<P> comb;
map<int,int> mmp;
const ll mod=1e9+7;
struct Node{
ll a,b,c;
bool operator <(const Node & other)const {
    return (2*a-b)<(other.a*2-other.b);
}
};
Node tup[100005];
ll presum[100005];
ll getlr(ll l,ll r)
{
    if(r<l) return 0ll;
    return (presum[r]-presum[l-1])%mod;
}
ll solve(ll n)//1到n统计个数
{
    ll ans=0,p=0,r;
    ll last=tup[1].a*2-tup[1].b;
    for(ll i=1;i<=n;++i){
        ll now=tup[i].a*2-tup[i].b;
        if(last+now<=0)
            p++,r=i;
    }
    ans+=tup[1].c*getlr(1,p);
    ans%=mod;
    for(ll i=2;i<=n;++i)
    {
         last=tup[i].a*2-tup[i].b;
         while(p>=i&&(last+tup[p].a*2-tup[p].b>0)) p--;
         ans+=(tup[i].c*getlr(i,p))%mod;
         ans%=mod;
    }
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll n;
    cin>>n;
    for(ll i=1;i<=n;++i){
        cin>>tup[i].a>>tup[i].b>>tup[i].c;
    }
    sort(tup+1,tup+n+1);
    for(ll i=1;i<=n;++i){
        presum[i]=presum[i-1]+tup[i].c;
    }
    ll ans=0;
    ans +=solve(n);
    for(ll i=1;i<=n;++i) swap(tup[i].a,tup[i].b);
    sort(tup+1,tup+n+1);
    for(ll i=1;i<=n;++i){
        presum[i]=presum[i-1]+tup[i].c;
    }
    ans+=solve(n);
    ans%=mod;
    cout<<ans<<endl;
    return 0;
}

```


**G篮球校赛**

解决方案：可以考虑将每类的前5名放在一起去重之后爆搜答案。也考虑考虑状压dp，$dp[i][s]$ 代表前i个人，位置的状态的s的最大价值，然后对于第i 个人的每个状态考虑自己上不上场即可。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll A[100005][35];
ll dp[100005][35];
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll n;
    cin>>n;
    for(ll i=1;i<=n;++i){
        for(ll j=0;j<5;++j) cin>>A[i][j];
    }
    ll top=1<<5;
    for(ll i=1;i<=n;++i)
    {
        for(ll s=0;s<top;++s){
            dp[i][s]=dp[i-1][s];
            for(ll j=0;j<5;++j){
                ll ns=1<<j;
                if(!(s&ns)) continue;
                dp[i][s]=max(dp[i][s],dp[i-1][s^ns]+A[i][j]);
            }
        }
    }
    cout<<dp[n][top-1]<<endl;
    return 0;

}

```


**H题分配学号**

解决方案：考虑统计出现的所有学号和出现的次数，然后用rem来表示前面待选的有多个少个，详情看代码。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
vector<P> comb;
map<ll,ll> mmp;
const ll mod=1e9+7;
ll calc(ll a,ll b)//计算阶乘A(a,b)
{
    ll ans=1;
    for(ll k=0;k<b;++k)
        ans=ans*(a-k)%mod;
    return ans;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll n;
    cin>>n;
    for(ll i=0;i<n;++i){
        ll x;
        cin>>x;
        mmp[x]+=1;
    }
    ll lap=-1,lan=-1,rem=0,nwp,nwn;//lap为上一个元素的元号，lan表示上一个元素有多少个，rem表示前面未选位置的的个数
    for(P p:mmp)
    {
        nwp=p.first;
        nwn=p.second;
        if(lap!=-1){
            ll dx=nwp-lap;
            if(rem>dx)//前面未选的的个数大于与前面的学号和该学号间距，放不完，只能放dx个
            {
                comb.push_back({rem,dx});//存放A(rem,dx)
                rem-=dx;rem+=nwn;
            }
            else//前面未选的的个数小于与前面的学号和该学号间距，可以放rem个
            {
                 comb.push_back({rem,rem});
                 rem=nwn;
            }
            lap=nwp;
            lan=nwn;
        }
        else{
            rem=nwn;
            lap=nwp;
            lan=nwn;
        }
    }
    comb.push_back({rem,rem});

    ll ans=1;
    for(P &p:comb){
        ans=ans*calc(p.first,p.second)%mod;
    }
    cout<<ans<<endl;
    return 0;
}
```


**I题Gree的心房**

解决方案：水题

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll A[100005];
int main()
{
    ios::sync_with_stdio(false);
    ll n,m,k;
    ll ans=0;
    cin>>n>>m>>k;
    n--;m--;
    if(k>m*n) ans=-1;
    else ans=n+m;
    cout<<ans<<endl;
    return 0;

}
```




## Codeforce#558（div 2）A~C题解 第一场


​ 这场比赛失误的地方

+ B2一个情况判断错误wa了1发+ C1函数用错导致找了30分钟bug并且没A，赛后结束C2有思路（题解的更让我恍然大悟）。


​ 比赛链接：[https://codeforces.com/contest/1163](https://codeforces.com/contest/1163)

​

A. Eating Soup

​ 水题不说了

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    int n,m,ans;
    cin>>n>>m;
    if(n==m){
        ans=0;
    }
    else if(m==0){
        ans=1;
    }
    else{
        ans=min(m,n-m);
    }
    cout<<ans<<endl;
}
```


​

​

B1. Cat Party (Easy Edition)

​ B2刚开始没思路，就先B1，暴力过的

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int X[100005];
int times[15];
const int inf=0x3f3f3f3f;
bool chk()
{
    int tot=-1;
    for(int i=1;i<=10;++i){
        if(!times[i]) continue;
        if(tot==-1) tot=times[i];
        else if(times[i]!=tot) return false;
    }
    return true;
}
bool check()
{
    int flag=0;
    for(int i=1;i<=10;++i){
        if(times[i]){
            times[i]--;
            if(chk()){
               flag=1;
            }
            times[i]++;
            if(flag) return true;
        }
    }
    return false;
}
int main()
{
    int n,ans=1;
    scanf("%d",&n);
    for(int i=1;i<=n;++i) scanf("%d",X+i);
    for(int i=1;i<=n;++i){
        times[X[i]]++;
        if(check()) ans=i;
    }
    printf("%d\n",ans);
    return 0;
}
```


​

B2. Cat Party (Hard Edition)

​ 维护一个map，key：次数，val：对应次数的数的种类数.，下面几种情况会有解

+ size（）=1，次数=1+ size（）=1，次数>1,数的种类=1+ size（）=2，最小的次数等于1，对应的个数只有一个+ size（）=2，最大的次数 $-$ 次大的次数==1，且最大次数只有一种，



正着推不好推，反过来推出所有情况就好了


```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int X[100005],times[100005];
map<int,int> mmp;
bool check()
{
    map<int,int>::iterator it;
    if(mmp.size()==1){
        P p=*mmp.begin();
        if(p.first==1||p.second==1) return true;
        else return false;
    }
    else if(mmp.size()==2){
        it=mmp.begin();
        P p1=*it;
        it++;
        P p2=*it;
        if(p1.first==1&&p1.second==1) return true;
        else if(p2.first-p1.first==1&&p2.second==1) return true;
        else return false;
    }
    else return false;
}
void handle(int x)
{
    if(times[x]==0){
        times[x]=1;
        mmp[1]++;
    }
    else{
        mmp[times[x]]--;
        if(mmp[times[x]]==0){
            mmp.erase(times[x]);
        }
        times[x]++;
        mmp[times[x]]++;
    }
}
int main()
{
    int n,ans=1;
    scanf("%d",&n);
    for(int i=1;i<=n;++i) scanf("%d",X+i);
    for(int i=1;i<=n;++i){
        handle(X[i]);
        if(check())
            ans=i;
    }
    cout<<ans<<endl;
        return 0;
}
```


​

C2. Power Transmission (Hard Edition) （补题）

题解非常巧妙的处理了直线。先用一定规则的三元一次方程表示直线，接下来实现对直线的去重。

构造直线分两步

+ 计算出直线的一般式+ 规定直线的格式，使得不同的三元组<a,b,c>对应不同的直线


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const ll maxn=1e4+200;
const ll inf=0x3f3f3f3f;
ll X[1005],Y[1005];
map<P,set<ll> > mmp;
int main()
{
    ll n,tot=0,ans=0;
    scanf("%lld",&n);
    for(ll i=1;i<=n;++i) scanf("%lld%lld",X+i,Y+i);
    for(ll i=1;i<=n;++i){
        for(ll j=i+1;j<=n;++j){
            ll a,b,c;
            a=Y[i]-Y[j],b=X[i]-X[j],c;
            ll d=__gcd(a,b);
            a/=d;b/=d;
            if(a<0||(a==0&&b<0)  ){//保证a>0或者 a存在的情况下b>0
                a*=-1;
                b*=-1;
            }
            c=a*X[i]-b*Y[i];
            set<ll> &mys=mmp[{a,b}];
            if(mys.count(c)==0)//这个直线没出现过
            {
                ans+=tot-mys.size();
                mys.insert(c);
                tot++;
            }
        }
    }
    cout<<ans<<endl;
}
```


#### 更新的知识点


+ 直线去重的简单方法——一般式


两点式：

$(y-y2)/(y1-y2) = (x-x2)/(x1-x2)$

转化为一般式之后

经过两点 $A(x1,y1)$ $B(x2,y2)$的直线，设为一般式$ ax−by=c$

则有 $a=y1−y2$, $b=x1−x2$, $c=y1x2−y2x1.$

两点式多用于检查直线的重合，平行和去重（只需排序操作即可）



比赛链接：[https://acm.ecnu.edu.cn/contest/173](https://acm.ecnu.edu.cn/contest/173)

这次比赛A了4道题，因为SQL等课程的原因，做了3个多小时做不动就放弃了

###  


### Problem A、小花梨的字符串



![./figures/20190518231557629.png](./figures/20190518231557629.png)


 

第一眼以为防ak，过了5分钟看下榜，这么多人过，猜了一下答案应该是他的全部子串， 就这样过了

难度未知.....

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
string s;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll n,q,l,r;
    cin>>n>>q>>s;
    while(q--)
    {
        cin>>l>>r;
        ll k=r-l+1;
        ll ans=k*(k+1)/2;
        cout<<ans<<endl;
    }
    return 0;
}```


 

### Problem B、小花梨的三角形 



![./figures/20190518225226932.png](./figures/20190518225226932.png)


 

这题第一次读错题意了，没过样例，以为只有小三角形，测了才知道是所有三角形。

因为每一行的两个端点l,r都确定一个或者两个三角形的下底，且不同的端点对应的三角形不同。所以枚举每一行(第 i 行)的l，r端点，找出向上方向的三角形和向下方向的三角形，其实把每一行字符串输入时都从下标0输入，那么可以看作这个大三角形是靠着左边的墙的样子。如果下底的端点分别是l，r的话，令h=r-l，那么向上方向的端点坐标是(i-h,l)，向下方向的端点坐标是(i+h,r)，然后判断是否在数据范围内，如果在就得到一个三角形。最后用set储存所有三角形的编号(从小到大排序，这样能保证每一个三角形都对应一个顺序串) 

难度:简单

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
set<string> mmp;
string calc(string s)
{
    sort(s.begin(),s.end());
    return s;
}
char str[110][110];
int main()
{
    int n;
    string s;
    scanf("%d",&n);
    for(int i=0; i<=n; ++i)
        scanf("%s",str+i);
    for(int i=1; i<=n; ++i) //第i层 i+1个字符
        for(int r=0; r<=i; ++r)
            for(int l=0; l<r; ++l)
            {
                int h=r-l;
                if(i-h>=0){
                    s="";
                    s+=str[i-h][l];
                    s+=str[i][l];
                    s+=str[i][r];
                    s=calc(s);
                    mmp.insert(s);
                }
                if(i+h<=n){
                    s="";
                    s+=str[i+h][r];
                    s+=str[i][l];
                    s+=str[i][r];
                    s=calc(s);
                    mmp.insert(s);
                }
            }
    cout<<mmp.size()<<endl;
    return 0;
}

```


###  


### Problem C、小花梨判连通 



![./figures/20190518230115627.png](./figures/20190518230115627.png)


这道题是比较有水平的了，（比赛时候没做出来）首先复习了一下类函数模板，map的自定义排序。然后熟悉这种新的题型（不同图的联通块交集，只要染色序列相同，那么这两个顶点就在最后结果的同一个联通快中）

思路： 1.对于每个图用并查集对每个联通块染色 2.k次染色可以的得出每个点(1~n)的染色序列 3.如果i j两个点联通那么他们的染色序列相同,所以map所有染色序列即可 

难度：偏难

```cpp
/*
思路：
1.对于每个图用并查集对每个联通块染色
2.k次染色可以的得出每个点(1~n)的染色序列
3.如果i j两个点联通那么他们的染色序列相同,所以map所有染色序列即可

*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
int father[100005];
int n,k;
void init()
{
    for(int i=1; i<=n; ++i) father[i]=i;
}
int Find(int x)
{
    if(x==father[x]) return x;
    return father[x]=Find(father[x]);
}
class cmp{
    public:
    bool operator()(vector<int> aa,vector<int> bb)
    {
        for(int i=0; i<k; ++i)
            if(aa[i]!=bb[i]) return aa[i]<bb[i];
        return false;//相等时候一定要返回false,想一下两个数之间判断是否相等的原理就知道了
    }
};
vector<int> seq[100005];
map< vector<int>,int,cmp> mmp;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>k;
    for(int pp=0; pp<k; ++pp)
    {
        int m;
        cin>>m;
        init();
        for(int i=1; i<=m; ++i)
        {
            int u,v,fu,fv;
            cin>>u>>v;
            fu=Find(u);
            fv=Find(v);
            father[fu]=fv;
        }
        for(int i=1; i<=n; ++i)
        {
            int bb=Find(i);//这个顶点所在联通快的颜色为 该集合代表顶点的顶点号
            seq[i].push_back(bb);
        }
    }
    for(int i=1;i<=n;++i)
         mmp[seq[i]]+=1;

    for(int i=1;i<=n;++i)
        cout<<mmp[seq[i]]<<endl;
    return 0;
}```


### Problem D、小花梨的取石子游戏



![./figures/20190518230519999.png](./figures/20190518230519999.png)


一道博弈题。

我是怎么博出来的呢？有点靠感觉A了。对于一个序列如果前k个都是1的话，那么他们拿石子的情况是确定的，不能改变，所以这时候什么最优策略都用不出来了。从第一个不是1的地方开始后面的几堆石子你会发现永远是先手的胜，因为先手的可以利用游戏规则，这一堆我可以取完，也可以只剩一个让另一个人来取。这样给我的感受就是局势永远掌握在先手的手中（什么博弈没用上别骂我。

所以只需求出每个序列开始连续1的个数即可。因为n太大两层for实现不太现实，不过下一次的结果可以利用上一次的结果，故我们可以双指针O(n)复杂度实现

难度：中等以上(我推了1h多...)

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
vector<int> A(100000+100);
vector<int> ans(100000+100);
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin>>n;
    for(int i=0;i<n;++i) cin>>A[i];
    int k=0,val=0;
    for(int i=0;i<n;++i)
    {
        k=max(k-1,0);//利用上一次计算的结果
        while(k<n&&A[(i+k)%n]==1) k++;//求下标i开始的连续1的个数，为k个
        ans[i]=k;
    }
    for(int i=0;i<n;++i)
    {
//        printf("%d\n",ans[i]);
        if(ans[i]==n) cout<<((n%2==0)?"Second":"First")<<endl;
        else cout<<(ans[i]%2==0?"First":"Second")<<endl;
    }
    return 0;
}
```


### Problem I、小花梨点外卖 


签到题

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
vector<int> val(100*2);
int main()
{
    int sum=0,ans,a,b,c,d,n;
    cin>>n>>a>>b>>c>>d;
    for(int i=0;i<n;++i)
    {
        cin>>val[i];
        sum+=val[i];
    }
    ans=sum;
    if(sum>=a)
        ans=min(ans,sum-b);

    if(sum>=c)
        ans=min(ans,sum-d);
    cout<<ans<<endl;
    return 0;
}```


 

比赛总结

1.map自定义比较是通过map类模板的第三个参数实现的，且第三个参数必须是一个类函数模板

2.求几个图的联通快的交集可以通过染色序列相同判断是否在同一个联通块中

