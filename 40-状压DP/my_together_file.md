

## 1243E - Sum Balance（状压DP，图）

题目链接：[1243E - Sum Balance](https://codeforces.com/problemset/problem/1243/E)
题意：

给一个K，代表有K个箱子。第 $i$ 个箱子有 $n_i$ 个物品，价值分别为$a_{i,1},a_{i,2}...a_{i,n_i}$。

现在分别从K个箱子中取精确的一个物品，并放回K个箱子（每个箱子精确放一个），要求最后的所有箱子内物品价值相等。并输出方案。**保证所有物品的价值唯一**。

$k\in[1,15],n_i\in[1,5000],a_{i,j}\in[-1e9,1e9]$
思路：

每个箱子取出一个物品，并放入一个箱子，若此刻我们将箱子看成顶点，取放的过程看作一条有向边，那么这里有K个箱子K条边，且每个顶点的出度和入度都等于1，显然这个图是由若干个简单环组成的。

首先如果所有物品的总和不是 $K$ 的倍数，那么无解。否则我们将物品总和除以K，结果设为 $ave$。

因为保证所有的价值唯一，那么我们将所有物品看作顶点，我们记录第 $i$ 个箱子的总和是 $sum[i]$ ,对于第 $i$ 个箱子的物品 $a$ ,我们令 $b=ave-(sum[i]-a)$，即将物品 a 拿走后，将物品 b 放到箱子 $i$ 中可保证箱子总和为 $ave$，

**此时若物品 b 存在**且（（**物品b不在箱子 $i$ 中**）或（**在箱子 $i$ 中且是物品a** ））。我们就让 $a$ 向 $b$ 连接一条边。

这样我么形成了一个图，且每个顶点的出度为1，现在我们给顶点覆上颜色，颜色为所属箱子，然后求出图中所有的环，且环内颜色互不相同。

如果我们能组合出一组环，使得所有环的所有颜色互不相同且总颜色种类等于K，那么这个就是答案。对于这一步，我们实现的时候可以使用状压DP，记录每个环的状态和每个环内的边，然后状压DP即可，状态转移的时候用状态的枚举子集优化，时间复杂度可以达到$3^k$。

记录每个顶点的颜色可以使用map，这样总体的时间复杂度为$O(k*alln+alln*log(alln))+3^k$

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const int N=18;
vector<ll> box[N];
ll sum[N];
unordered_map<ll,ll> color;
int dp[1<<N];
vector<P> take[1<<N];
unordered_map<ll,ll> to;
/*
记录每个点的颜色，以及箱子的和
1.建图
2.找环 并记录过程
3.dp并记录过程
*/
P ans[N];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin>>n;
    ll allsum=0;
    for(int i=0; i<n; ++i)
    {
        ll k;
        cin>>k;
        box[i].resize(k);
        sum[i]=0;
        for(int j=0; j<k; ++j)
        {
            cin>>box[i][j];
            allsum+=box[i][j];
            sum[i]+=box[i][j];
            color[box[i][j]]=i;
        }
    }
    if(allsum%n!=0)
    {
        cout<<"No"<<'\n';
        return 0;
    }
    allsum/=n;
    for(int i=0; i<n; ++i)
    {
        for(ll v:box[i])
        {
            ll need=allsum-(sum[i]-v);
            auto it=color.find(need);
            if(it!=color.end())
            {
                ll w=it->second;
                if(w!=i||need==v)
                    to[v]=need;
            }
        }
    }
    for(int i=0; i < n; ++i)
    {
        for(ll v:box[i])
        {
            int S=0;
            bool isok=true;
            ll cur=v;
            vector<P> place;
            do
            {
                if( (S&(1<<color[cur])) !=0){
                    isok=false;
                    break;
                }
                S|=1<<color[cur];
                auto it=to.find(cur);
                if(it!=to.end())
                {
                    place.push_back(make_pair(it->second,color[cur]));//什么物品放到哪个箱子
                    cur=it->second;
                }
                else
                {
                    isok=false;
                    break;
                }

            }
            while(cur!=v);
            if(isok==true)
            {
                dp[S]=1;
                take[S]=place;
            }
        }
    }
    for(int i=0;i<(1<<n);++i){
        if(dp[i])
            continue;
        for(int sub=i;sub!=0;sub=(sub-1)&i)
        {
            int o=i^sub;
            if(dp[sub]&&dp[o])
            {
                dp[i]=1;
                take[i]=take[sub];
                take[i].insert(take[i].end(),take[o].begin(),take[o].end());
                break;
            }
        }
    }
    if(!dp[(1<<n)-1]){
        cout<<"No"<<'\n';
        return 0;
    }
    cout<<"Yes"<<'\n';
    for(P &p:take[(1<<n)-1]){
        ll val=p.first, id=p.second;
        ans[color[val]]=make_pair(val,id);
    }
    for(int i=0;i<n;++i)
        cout<<ans[i].first<<" "<<ans[i].second+1<<endl;
    return 0;
}

```




### M - God of War


At 184~280 A.D ,there were many kingdoms in China. Three strongest among them are “Wei”, “Shu”, “Wu”. People call this period as “Three Kingdoms”. HH is a super “Three Kingdoms” fan, because at this period there were many heroes and exciting stories. Among the heroes HH worships LvBu most. LvBu is the God of War and is also intelligent, but his ambition is too big while enemies are too powerful .Many monarchs wanted to kill him. At 198 A.D ,CaoCao fought with LvBu at Xuzhou.Though Lvbu is the God of War ,CaoCao had so many generals: Xuchu,DianWei XiahouChun……Facing so many heroes ,could LvBu beat all of them? [外链图片转存失败(img-6OdICLXg-1567489110593)(https://vj.e949.cn/4bb2034f502de1d3b2505bd22cd22e5d?v=1547513997)] Given the LvBu’s ATI, DEF, HP, and enemies’ ATI, DEF,HP, experience (if LvBu killed one of his enemies, he can get that experience ,and if his experience got more than or equal to 100*level,he would level-up and become stronger) and the In_ATI,In_DEF,In_HP(indicating when LvBu levels up,his ability will increase this point). Each turn LvBu will choose an enemy to fight. Please help LvBu find a way to beat all of enemies and survive with the max HP. Here’s a fight between LvBu and A: **If LvBu attack A, A will lose Max(1,LvBu’s ATI- A’s DEF) hp;If A survived, he will give LvBu Max(1,A’ATI- LvBu’DEF) injury.If LvBu is still alive, repeat it untill someone is dead(hp <= 0).** LvBu’s initial level is 1 and experience is 0,and he can level up many times.

**Input**

The input contains at most 20 test cases. For each case , the first line contains six intergers ,indicating LvBu’s ATI,DEF,HP and In_ATI,In_DEF,In_HP. The next line gives an interger N(0<N<=20),indicating the number of the enemies . Then N lines followed, every line contains the name(the length of each name is no more than 20),ATI,DEF,HP, experience(1<experience<=100).

**Output**

If LvBu is dead output “Poor LvBu,his period was gone.” Or output the maximum HP left.

**Sample Input**

```bash
100  80  100  5  5  5
2
ZhangFei 95  75  100  100 
XuChu 90  90  100  90

100 75 100 5 5 5
1
GuanYu 95 85 100 100
```


**Sample Output**

```bash
30
Poor LvBu,his period was gone.
```


### 题意：


吕布要单挑n位英雄，每个英雄有四个属性，即攻击力，防御力，生命值，经验值，

吕布刚开始有初始的三个基本属性（攻击力，防御力，生命值），每打死一个英雄就会获得相应的经验值

如果经验值达到100*level就会升级，升级或会增加自身的属性值，问吕布打死n个英雄后最大生命值为多少？

### 分析：


用n个二进制位代表打死对应的英雄，为1代表把此英雄打死了。所以用$dp[state]​$表示此时吕布的状态，这个状态可以从打败过的英雄的状态过来，枚举所有前继状态，因为同一个状态获得的经验值肯定是相同的，即等级相同，,取血量最大的即可。初始化其他状态血量为0，代表打不过。

简单dp，可能中间需要注意升级啥的。

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
int Ina,Inb,Inhp;// up lever get shuxing
int a,b,hp;//lvbu of init state
struct Peo
{
    int a,b,hp,jy;
} peo[20];
struct Node
{
    int lev,hp,jy;//等级，血量 经验
    Node()
    {

    }
    Node(int l,int h,int j):lev(l),hp(h),jy(j)
    {

    }
};//等级和血量
int Getlev(int jy)//根据经验 算出来应该到第几个等级
{
    return jy/100+1;
}
Node judge(Node aa,Peo bb)//吕布的状态和 一个英雄 b 打完之后吕布的状态
{
    int hackb=max(1,a+(aa.lev-1)*Ina-bb.b);
    int hacka=max(1,bb.a-b-(aa.lev-1)*Inb);
    int tb=bb.hp/hackb+bool(bb.hp%hackb);
    int ta=aa.hp/hacka+bool(aa.hp/hacka);
    if(ta>=tb)//吕布胜利
    {
        int cc=Getlev(aa.jy+bb.jy)-aa.lev;
        return Node(aa.lev+cc,aa.hp-(tb-1)*hacka+cc*Inhp,aa.jy+bb.jy);
    }
    else
    {
        return Node(1,0,0);
    }
}
Node dp[1<<20];//处于该状态的最大血量
int main()
{
    int n;
    while(~scanf("%d %d %d %d %d %d",&a,&b,&hp,&Ina,&Inb,&Inhp))
    {
        scanf("%d",&n);
        for(int i=0; i<n; ++i)
        {
            scanf("%*s%d%d%d%d",&peo[i].a,&peo[i].b,&peo[i].hp,&peo[i].jy);
        }
        dp[0]=Node(1,hp,0);//初始状态
        int top=1<<n;
        for(int i=1; i<top; ++i)
        {
            dp[i].hp=0;
            for(int j=0; j<n; ++j)
            {
                if((1<<j)&i)//i的第j位为1 从上一个状态过来
                {
                    int lasts=i^(1<<j);
                    if(dp[lasts].hp>0)//上一个状态没死
                    {
                        Node mm=judge(dp[lasts],peo[j]);
                        if(mm.hp>dp[i].hp)
                            dp[i]=mm;
                    }
                }
            }
        }
        if(dp[top-1].hp==0)
            cout<<"Poor LvBu,his period was gone."<<endl;
        else
            cout<<dp[top-1].hp<<endl;
    }
    return 0;
}

```


#### 




### L - Tiling Dominoes



闲聊

在大白书上$383$页，上面有详细讲解这道题的$dp$方法，

第一次做这类状压dp的题时，用的dp的时间复杂度是$O(2^m*2^m*n)$ 可以过另一个一模一样的题，当时是把每一行的放置情况当作状态进行转移，但是那个算法在这道题上过不去，于是开始寻找博客，网上说大白书上有一道一模一样的题，正好旁边就有一本这样的书，理解了一下就A了这道题时间复杂度为$O(2^m*m*n)$

在大白书上$383$页，上面有详细讲解这道题的dp方法，


### 分析：


把第i行第j个的m个位置（自身带上前m-1个数）的放置状态进行动态规划求解。

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
int n,m,cur;
ll dp[2][1<<10];

int main()
{
    while(~scanf("%d %d",&n,&m))
    {
        if(n<m)
            swap(n,m);
        mset(dp,0);
        dp[0][(1<<m)-1]=1;
        cur=0;
        int tot=1<<m;
        for(int i=0; i<n; ++i)
        {
            for(int j=0; j<m; ++j)
            {
                cur^=1;//根据上个位置得到这个 状态的存放位置
                mset(dp[cur],0);
                for(int s=0; s<tot; ++s) //枚举上个状态
                {
                    /*不放*/
                    int tos;
                    if(s&(1<<(m-1)))
                    {
                        tos=s<<1;
                        tos^=1<<m;//把第m位变为0
                        dp[cur][tos]+=dp[1-cur][s];
                    }
                    /*横着放*/
                    if(j&&(s&1)==0&&(s&(1<<(m-1))))
                    {
                        tos=s<<1;
                        tos^=1<<m;
                        tos|=(1<<1)|1;
                        dp[cur][tos]+=dp[1-cur][s];
                    }
                    /*竖着放*/
                    if(i&& !(s&(1<<(m-1))))
                    {
                        tos=s<<1;
                        tos|=1;
                        dp[cur][tos]+=dp[1-cur][s];
                    }
                }
            }
        }
        cout<<dp[cur][tot-1]<<endl;
    }
    return 0;
}

```




### J - Hie with the Pie


The Pizazz Pizzeria prides itself in delivering pizzas to its customers as fast as possible. Unfortunately, due to cutbacks, they can afford to hire only one driver to do the deliveries. He will wait for 1 or more (up to 10) orders to be processed before he starts any deliveries. Needless to say, he would like to take the shortest route in delivering these goodies and returning to the pizzeria, even if it means passing the same location(s) or the pizzeria more than once on the way. He has commissioned you to write a program to help him.

**Input**

Input will consist of multiple test cases. The first line will contain a single integer *n* indicating the number of orders to deliver, where 1 ≤ *n* ≤ 10. After this will be *n* + 1 lines each containing *n* + 1 integers indicating the times to travel between the pizzeria (numbered 0) and the *n* locations (numbers 1 to *n*). The *j*th value on the *i*th line indicates the time to go directly from location *i* to location *j* without visiting any other locations along the way. Note that there may be quicker ways to go from *i* to *j* via other locations, due to different speed limits, traffic lights, etc. Also, the time values may not be symmetric, i.e., the time to go directly from location *i* to *j* may not be the same as the time to go directly from location *j* to *i*. An input value of *n* = 0 will terminate input.

**Output**

For each test case, you should output a single number indicating the minimum time to deliver all of the pizzas and return to the pizzeria.

**Sample Input**


3 0 1 10 10 1 0 1 2 10 1 0 10 10 2 10 0 0


**Sample Output**


8


### 题意：


从0端点到n个端点送外卖，存在一条路径，使得从0开始经过n个端点后回到0端点，所走的最短距离是多少，每个顶点可以走多次。

### 思路：


$用dp[state][j],二进制代表以0为端点，走state的状态，到j的最短距离是多少,其中state对应的二进制为1代表回路中经过该端点$

枚举前继状态，从端点c过来，暴力找出最小值即可，不过在前继状态加上c到j的距离时，需要floyd计算任意两点的最短路径

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=15;
const int branch=26;
const int inf=0x3f3f3f3f;
const int mod=1e8;
int mm[maxn][maxn];
int dp[1<<11][maxn];//dp[i][j] 代表状态i下 ，0到j的最短距离是多少。对应位为1代表图中有他（不带端点）
int main()
{
    int n;
    while(~scanf("%d",&n)&&n)
    {
        for(int i=0;i<=n;++i)
            for(int j=0;j<=n;++j)
                scanf("%d",mm[i]+j);
        for(int k=0;k<=n;++k)
            for(int i=0;i<=n;++i)
                for(int j=0;j<=n;++j)
                    if(mm[i][j]>mm[i][k]+mm[k][j])
                        mm[i][j]=mm[i][k]+mm[k][j];
        //初始化0 状态i下0到点i的最短距离
        mset(dp,inf);
        for(int i=0;i<=n;++i)
        {
            dp[1<<(i)][i]=mm[0][i];
        }
        int tot=1<<(n+1);
        for(int i=0;i<tot;++i)
        {
            for(int v=0;v<=n;++v)
            {
                if((i&(1<<v))==0)//v在这个状态中 必须存在
                    continue;
                for(int s=0;s<=n;++s)
                {
                    if((i&(1<<s))==0)//从s点到这个状态，那么s点必须在i梭子啊状态中，s不能为起始点（这也是初始化的原因吧）
                        continue;
                    //dp[i][s]过来或者dp[i^(1<<v)][s]过来  花费都为m[s][v]
                    int val=min(dp[i][s],dp[i^(1<<v)][s])+mm[s][v];
                    if(val<dp[i][v])
                        dp[i][v]=val;
                }
            }
        }
        cout<<dp[tot-1][0]<<endl;
    }
    return 0;
}
```




### H - Imperishable Night


After coding so many days,Mr Acmer wants to have a good [rest.So](http://rest.So) travelling is the best choice!He has decided to visit n cities(he insists on seeing all the cities!And he does not mind which city being his start station because superman can bring him to any city at first but only once.), and of course there are m roads here,following a fee as usual.But Mr Acmer gets bored so easily that he doesn’t want to visit a city more than twice!And he is so mean that he wants to minimize the total fee!He is lazy you [see.So](http://see.So) he turns to you for help.

**Input**

There are several test cases,the first line is two intergers n(1<=n<=10) and m,which means he needs to visit n cities and there are m roads he can choose,then m lines follow,each line will include three intergers a,b and c(1<=a,b<=n),means there is a road between a and b and the cost is of course c.Input to the End Of File.

**Output**

Output the minimum fee that he should pay,or -1 if he can’t find such a route.

**Sample Input**

```bash
2 1
1 2 100
3 2
1 2 40
2 3 50
3 3
1 2 3
1 3 4
2 3 10
```


**Sample Output**

```cpp
100
90
7 
```


### 题意：


现在有n个顶点，有m个边，每个边有相应的权值，要求每个顶点最多经过两次，要求经过n个顶点的权值和最小。如果不能经过n个点，则输出-1

### 分析：


每个顶点可以最多经过两次，$n$个顶点，用3进制数字$s$代表对应的顶点有没有经过，$0$代表没有经过，$1$代表经过一次，$2$代表此状态中该顶点经过$2$次，那么所有情况有$3^n$种，我们让该三进制数的最低位到最高位分别代表顶点$1到n$ ，那么我们要求的就是$3$进制数中$n$个位中状态都非$0$的形成这种状态的最小值。

因为每一个通路可以用一个状态和一个端点表示

所以用$dp[state][v]$代表状态state，且该路径的端点为$v$。这种情况所花费的最小值。

那么求$dp[state][v]$ 只需枚举连接$v$端点的另一个端点即可。

初始化：$dp[state(v)][v]=0$ ，其他都是$inf$，即只有端点v的状态的最小花费为$0$

又因为每种状态的值至于前面的状态有关，所以$for$循环 三进制的值从小到大遍历所有状态即可。最后找出满足条件的最小值即可

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=11;
const int branch=26;
const int inf=0x3f3f3f3f;
const int mod=1e8;
int mm[maxn][maxn];//存放地图
int dp[60000][maxn];
int a[maxn];//存放状态
int n,m;
int quick_pow(int a,int b)
{
    int ans=1;
    while(b)
    {
        if(b&1)
            ans=ans*a;
        a=a*a;
        b>>=1;
    }
    return ans;
}
int Add(int state,int v)//从state中增加v顶点的一次
{
    return state+quick_pow(3,v-1);
}
int Subtract(int state,int v)//从state中减去v顶点的一次数
{
    return state-quick_pow(3,v-1);
}
int getcnt(int state,int v)//得到state中 端点v的出现次数
{
    return (state/quick_pow(3,v-1))%3;
}
int judge(int state)//判断state是否符合条件
{
    for(int i=0;i<n;++i)
    {
        if(state%3==0)
            return 0;
        state/=3;
    }
    return 1;
}
int main()
{
    while(~scanf("%d %d",&n,&m))
    {
        mset(mm,inf);
        int u,v,w;
        for(int i=0;i<m;++i)
        {
            scanf("%d %d %d",&u,&v,&w);
            if(mm[u][v]>w)
                mm[u][v]=mm[v][u]=w;
        }
        /*开始状态转移 dp[state][r]，代表这个状态时statte，且改状态末尾的顶点是r,所花费的最小代价*/
        mset(dp,inf);
        for(int i=1;i<=n;++i)
        {
            dp[Add(0,i)][i]=0;
        }//初始化 刚开始的状态
        int tot=quick_pow(3,n);
        for(int i=0;i<tot;++i)//枚举状态
        {
            for(int j=1;j<=n;++j)//枚举now state
            {
                if(!getcnt(i,j))// out can't rule
                    continue;
                int sss=Subtract(i,j);// out the state
                for(int s=1;s<=n;++s)//enum last v
                {
                    if(!getcnt(sss,s)||mm[s][j]==inf||dp[sss][s]==inf)
                        continue;
                    dp[i][j]=min(dp[i][j],dp[sss][s]+mm[s][j]);
                }
            }
        }
        int minn=inf;
        for(int i=(quick_pow(3,n)-1)/2;i<tot;++i)
        {
            if(judge(i))
            {
                 for(int j=1;j<=n;++j)
                    minn=min(minn,dp[i][j]);
            }

        }
        if(minn==inf)
            printf("-1\n");
        else
            printf("%d\n",minn);
    }
    return 0;
}


```




### G - Corn Fields


Farmer John has purchased a lush new rectangular pasture composed of *M* by *N* (1 ≤ *M*≤ 12; 1 ≤ *N* ≤ 12) square parcels. He wants to grow some yummy corn for the cows on a number of squares. Regrettably, some of the squares are infertile and can’t be planted. Canny FJ knows that the cows dislike eating close to each other, so when choosing which squares to plant, he avoids choosing squares that are adjacent; no two chosen squares share an edge. He has not yet made the final choice as to which squares to plant.

Being a very open-minded man, Farmer John wants to consider all possible options for how to choose the squares for planting. He is so open-minded that he considers choosing no squares as a valid option! Please help Farmer John determine the number of ways he can choose the squares to plant.

**Input**

Line 1: Two space-separated integers: *M* and *N* Lines 2… *M*+1: Line *i*+1 describes row *i* of the pasture with *N* space-separated integers indicating whether a square is fertile (1 for fertile, 0 for infertile)

**Output**

Line 1: One integer: the number of ways that FJ can choose the squares modulo 100,000,000.

**Sample Input**

```bash
2 3
1 1 1
0 1 0
```


**Sample Output**

```bash
9
```


**Hint**

Number the squares as follows:

```bash
1 2 3
  4  
```


There are four ways to plant only on one squares (1, 2, 3, or 4), three ways to plant on two squares (13, 14, or 34), 1 way to plant on three squares (134), and one way to plant on no squares. 4+3+1+1=9.

### 题意：


牛吃草，给你一个m*n规格的地方，1的地方为草，0的地方为空地，现在要建造围栏，围栏必须建在草上，且围栏不能上下左右相邻。

### 分析：


暴力出所有情况即可，数位dp的入门题，用n位数的二进制代表这一行围栏放的情况，$d[r][state]$为第 r 行状态为state的方法数，计算该方法数的时候 暴力枚举上一行所有的状态，如果状态兼容，则可以有这种状态，上一行状态的方法数即可。

$dp[r][state]表示只考虑前r行兼容，第r行状态为state的方法数，然后dp即可，得到dp[m][state]求和即是答案$

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
const ll  mod=1e8;
int w[15];
ll dp[15][1<<12];
int state[1<<12],tot;
char hhh()
{
    char c=getchar();
    while(c==' '||c=='\n')
        c=getchar();
    return c;
}
int main()
{
    int m,n;
    scanf("%d%d",&m,&n);
    for(int i=1; i<=m; ++i)
    {
        w[i]=0;
        for(int j=0; j<n; ++j)
        {
            w[i]<<=1;
            if(hhh()=='1')
                w[i]+=1;
        }
    }
    tot=0;
    for(int i=0; i<(1<<n); ++i)//预处理出肯定的一行可能的状态
    {
        if(((i<<1)&i)==0)//1 1不能相邻
            state[tot++]=i;
    }
    mset(dp,0);
    for(int i=0; i<tot; ++i)//预处理第一行
    {
        if((state[i]&w[1])==state[i])
            dp[1][i]=1;
    }
    for(int r=2; r<=m; ++r)
    {
        for(int i=0; i<tot; ++i)
        {
            if((state[i]&w[r])==state[i])
            {
                for(int j=0; j<tot; ++j)
                {
                    if(((state[j]&w[r-1])==state[j])&&(state[i]&state[j])==0)
                    {
                        dp[r][i]+=dp[r-1][j];
                    }

                }
                dp[r][i]%=mod;
            }

        }
    }
    ll ans=0;
    for(int i=0;i<tot;++i)
    {
        ans=(ans+dp[m][i])%mod;
    }
    cout<<ans<<endl;
    return 0;

}
```




### E - Mondriaan’s Dream


Squares and rectangles fascinated the famous Dutch painter Piet Mondriaan. One night, after producing the drawings in his ‘toilet series’ (where he had to use his toilet paper to draw on, for all of his paper was filled with squares and rectangles), he dreamt of filling a large rectangle with small rectangles of width 2 and height 1 in varying ways. 
![./figures/91cd2a849209448a71d50fa577e5d5ed](./figures/91cd2a849209448a71d50fa577e5d5ed)
 Expert as he was in this material, he saw at a glance that he’ll need a computer to calculate the number of ways to fill the large rectangle whose dimensions were integer values, as well. Help him, so that his dream won’t turn into a nightmare!

**Input**

The input contains several test cases. Each test case is made up of two integer numbers: the height h and the width w of the large rectangle. Input is terminated by h=w=0. Otherwise, 1<=h,w<=11.

**Output**


![./figures/9275391b5c2fd4e3cb556e4ab10140b5](./figures/9275391b5c2fd4e3cb556e4ab10140b5)
For each test case, output the number of different ways the given rectangle can be filled with small rectangles of size 2 times 1. Assume the given large rectangle is oriented, i.e. count symmetrical tilings multiple times.

**Sample Input**

```bash
1 2
1 3
1 4
2 2
2 3
2 4
2 11
4 11
0 0
```


**Sample Output**

```bash
1
0
1
2
3
5
144
51205
```


#### 题意：


一个h*w规格的地方，用1*2的砖铺满，有多少种方法

#### 分析：



可跳过此处…

闲聊一下:

这题其实我是一开始就有思路的，并且思路是对的。但是我想看其他人的代码是怎么写的。

然后就发生了我看了20多篇博客（先看的他们的思路,一会一个用0，1一会一个用1，0表示）,

把我给整迷了，觉得大部分博客并没有说到重点，状态压缩谁都会，这题重点是判断上一行与此行的状态兼容。


**先从第一行说起**，对于每一列，1代表这个位置不**暂时**不铺砖。0代表这个位置铺 **横着的砖块**。则用w位的0，1的二进制数来表示砖块的情况，

​ 很容易看出 **连着的0**的**个数**必须**是偶数**

从第i(i>=2)行说起，对于每一列

+ 如果这一列的上一行是1，那么这个位置必须要是0，代表我铺上砖了,（且这个砖是竖着的）+ 如果这一列的上一行是0，但是这个位置可以是0，也可以是1。 但是要求这一行的状态与上一行的状态兼容，怎么兼容呢，如果对于每一列**出现（1，0）或者（0,1）代表这这砖是竖着的**，如果是**(0，0)代表这个砖是横着的**，**且不允许出现(1,1)的状态**(即上一行不铺，这一行也不铺)


可以看出此时需要满足两个条件

+ 不允许出现（1,1）的状态+ 竖着的砖之间的横着的地方是偶数个


然后针对每个状态，遍历上一行的所有状态，进行状态转移即可，答案在$dp[h][0]$里面

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
int h,w;
//1代表不铺 0代表铺砖
ll dp[12][1<<11];
bool JudgeOne(int s)//判断这一行状态是否成立，1代表这个是竖着的，否则就是0(横着放的)
{
    //保证竖着的砖之间的0的个数是偶数个
    int cnt=0;
    for(int i=0; i<w; ++i)
    {
        if(s&1)
        {
            if(cnt&1)
                return 0;
        }
        else
            cnt++;
        s>>=1;
    }
    if(cnt&1)
        return 0;
    return 1;
}
/*
从第行开始需要两行结合到一起判断
1.(0 1)或者(1 0)都算作1
2.(1,1)不允许此状态
3.竖着放的之前的横着放的位置一定有偶数个
*/
int main()
{
    int top;
    while(~scanf("%d %d",&h,&w)&&h|w)
    {
        if(h<w)
            swap(h,w);
        if((h*w)&1)
        {
            printf("0\n");
            continue;
        }
        mset(dp,0);
        top=(1<<w);
        for(int s=0; s<top; ++s)
        {
            if(JudgeOne(s))
                dp[1][s]=1;
        }
        for(int i=2; i<=h; ++i)
        {
            for(int s=0; s<top; ++s)
            {
                for(int ss=0; ss<top; ++ss)
                {
                    if((s&ss)==0&&JudgeOne(s^ss))
                    {
                        dp[i][s]+=dp[i-1][ss];
                    }
                }
            }
        }
        printf("%I64d\n",dp[h][0]);
    }
    return 0;
}

```




### D - Relocation


mma and Eric are moving to their new house they bought after returning from their honeymoon. Fortunately, they have a few friends helping them relocate. To move the furniture, they only have two compact cars, which complicates everything a bit. Since the furniture does not fit into the cars, Eric wants to put them on top of the cars. However, both cars only support a certain weight on their roof, so they will have to do several trips to transport everything. The schedule for the move is planed like this:

+ At their old place, they will put furniture on both cars.+ Then, they will drive to their new place with the two cars and carry the furniture upstairs.+ Finally, everybody will return to their old place and the process continues until everything is moved to the new place.


Note, that the group is always staying together so that they can have more fun and nobody feels lonely. Since the distance between the houses is quite large, Eric wants to make as few trips as possible.

Given the weights *wi* of each individual piece of furniture and the capacities *C*1 and *C*2 of the two cars, how many trips to the new house does the party have to make to move all the furniture? If a car has capacity *C*, the sum of the weights of all the furniture it loads for one trip can be at most *C*.

**Input**

The first line contains the number of scenarios. Each scenario consists of one line containing three numbers *n*, *C*1 and *C*2. *C*1 and *C*2 are the capacities of the cars (1 ≤ *Ci* ≤ 100) and *n* is the number of pieces of furniture (1 ≤ *n* ≤ 10). The following line will contain *n* integers *w*1, …, *wn*, the weights of the furniture (1 ≤ *wi* ≤ 100). It is guaranteed that each piece of furniture can be loaded by at least one of the two cars.

**Output**

The output for every scenario begins with a line containing “`Scenario #`*i*`:`”, where *i* is the number of the scenario starting at 1. Then print a single line with the number of trips to the new house they have to make to move all the furniture. Terminate each scenario with a blank line.

**Sample Input**

```bash
2
6 12 13
3 9 13 3 10 11
7 1 100
1 2 33 50 50 67 98
```


**Sample Output**

```bash
Scenario #1:
2

Scenario #2:
3
```


### 题意：


有两个车子，容量分别为c1,c2，现在我有n个家具需要运送，容量分别是w1,w2…wn。要求运送家具的时候两个车子必须一起去，问最少几个来回把家具运完，保证每个家具都能被其中一个车运走

### 分析：


因为车子少，所以用二进制状态0，1来表示是否运走对应家具

首先暴力出车子可以一次运完的状态。然后对可以一次运完的状态进行记忆话化搜索，dfs（state）代表state状态最少需要运的次数。

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
int vis[1<<11],w[10];// vis用来 枚举子集的 物品的重量和，
int n,c1,c2;//n个物品。车子的重载量分别为c1 c2
int state[1<<11],tot;//存放一次可以运走的所有状态
int dp[1<<11];
bool judge(int x)//判断x能否一次运走
{
    /*
    枚举C1一次运走的所有情况，如果同时C2也能一次运走那么可以一次运走
    */
    int top=0;
    vis[0]=0;
    int sum=0;
    for(int i=0;i<n;++i)
        if(x&(1<<i))
            sum+=w[i];
    if(sum<=c1||sum<=c2)
        return 1;
    for(int i=0;i<n;++i)//时间复杂度为2^k(0<=k<=10)
    {
        if(x&(1<<i))//第i个物品存在
        {
            int cnt=top;
            for(int j=0;j<=cnt;++j)//加上前面j个状态
            {
                if(w[i]+vis[j]>c1)//这个c1肯定运不过去，更不用说再在后面加物品了，所以不用加入集合中
                    continue;
                vis[++top]=w[i]+vis[j];
                if(vis[top]<=c1&&sum-vis[top]<=c2)
                    return 1;
            }
        }
    }
    return 0;
}
int dfs(int ss)//此状态，枚举此状态最少需要运多少次
{
    if(!ss)
        return 0;
    if(dp[ss]!=-1)
        return dp[ss];
    int ans=100;
    for(int i=0;i<tot;++i)
    {
        if((ss&state[i])==state[i])
            ans=min(ans,dfs(ss^state[i])+1);
    }
    return dp[ss]=ans;
}
int main()
{
    int t;
    int cas=0;
    scanf("%d",&t);
    while(t--)
    {
        mset(dp,-1);
        scanf("%d%d %d",&n,&c1,&c2);
        for(int i=0;i<n;++i)
            scanf("%d",w+i);
        tot=0;
        for(int i=1;i<(1<<n);++i)//状态0不加入
        {
            if(judge(i))
                state[tot++]=i;
        }
        printf("Scenario #%d:\n",++cas);
        printf("%d\n\n",dfs((1<<n)-1));
    }
    return 0;
}
```




### A - LianLianKan


I like playing game with my friend, although sometimes looks pretty naive. Today I invent a new game called LianLianKan. The game is about playing on a number stack. Now we have a number stack, and we should link and pop the same element pairs from top to bottom. Each time, you can just link the top element with one same-value element. After pop them from stack, all left elements will fall down. Although the game seems to be interesting, it’s really naive indeed. 
![./figures/791b82e30179bc1b498d58e6ad7733d3](./figures/791b82e30179bc1b498d58e6ad7733d3)
 To prove I am a wisdom among my friend, I add an additional rule to the game: for each top element, it can just link with the same-value element whose distance is less than 6 with it. Before the game, I want to check whether I have a solution to pop all elements in the stack.

**Input**

There are multiple test cases. The first line is an integer N indicating the number of elements in the stack initially. (1 <= N <= 1000) The next line contains N integer ai indicating the elements from bottom to top. (0 <= ai <= 2,000,000,000)

**Output**

For each test case, output “1” if I can pop all elements; otherwise output “0”.

**Sample Input**

```bash
2
1 1
3
1 1 1
2
1000000 1
```


**Sample Output**

```bash
1
0
0
```


##### 题意：


给你一个栈，栈中有n个元素，下面输入n个数，依此从栈底到栈顶。接下来你必须从找到一个**与栈顶距离小于等于5的位置**，若这个位置的数和栈顶相同，可以让**这个数**和**栈顶的数**从栈中消去。

问有没有一种方法是所有数字全部消去

##### 分析：


消去与栈底最远的或者最近的什么贪心都是不行的，都可以找出反例。这道题只有暴力来写

当然暴力的DP也是算是暴力?

第h高度**之前的数**全消去的时候最多能消去高度h之后的后4位，且最大距离与h不超过9，又因为h的后9位肯定有5个没有被消去的数，那么只要枚举h高度之后的9个状态压缩一下，模拟从从栈顶消去元素的所有的情况。

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
int dp[1100][1<<10],a[1100];
int dfs(int h,int state)//当前高度为h，状态为state
{//能将第一个消去则进入下个状态 不能则返回0
    if(!h)
        return 1;
    if(dp[h][state]!=-1)
        return dp[h][state];
    if((state&1)==0)//第h高度没有数字则整下个
    {
        int nextstate=state>>1;
        if(h>10)//第9位是否要添进去
        {
                nextstate|=(1<<9);
        }
        return dp[h][state]=dfs(h-1,nextstate);
    }
    /*
    枚举删除的位置
    */
    int dis=1;
    int ans=0;
    int i=1;
    while(i<=9&&dis<=5&&h-i>0)
    {

        if((state&(1<<i))==0)//这一位是消去过了
        {
             i++;
             continue;
        }
        if(a[h-i]==a[h])//这h的下i位相等
        {
            int nextstate=(state^(1<<i))>>1;
            if(h>10)//第9位是否要添进去
            {
                nextstate|=(1<<9);
            }
            ans+=dfs(h-1,nextstate);
            if(ans)
            {
                return dp[h][state]=1;
            }
        }
        i++;
        dis++;
    }
    return dp[h][state]=0;

}
int main()
{
    int n;
    while(~scanf("%d",&n))
    {
        for(int i=1; i<=n; ++i)
            scanf("%d",a+i);
        if(n&1)
        {
            printf("0\n");
            continue;
        }
        mset(dp,-1);
        int ans=0;
        if(n<=10)
        {
            ans=dfs(n,(1<<n)-1);
        }
        else{
            ans=dfs(n,(1<<10)-1);
        }
        printf("%d\n",ans);
    }
    return 0;
}
```


