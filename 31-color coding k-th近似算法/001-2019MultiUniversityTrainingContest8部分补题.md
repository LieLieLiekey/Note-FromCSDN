

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


