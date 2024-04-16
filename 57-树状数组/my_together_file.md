

## 1194E. Count The Rectangles（树状数组，离线扫描线）


##### 题目链接：[传送门](https://codeforces.com/problemset/problem/1194/E)


##### 思路：


首先看数据范围，$n\le5000$，我们首先处理出所有水平线段和垂直线段，然后将水平线段从低到高排序。

我们从低到高处理每条水平线段（计算出以该水平线段为底的矩形的数量）。

假设现在是第 $i$ 条水平线段，首先我们$O(n)$ 处理出所有与该线段相交的垂直线段，然后记录与相交的垂直线段的最高点。我们现在维护这个最高点集合（用树状数组，用点的横坐标当下标，记录某一横坐标范围内点的数量）。

之后我们遍历**剩下的**水平线段（比 $i$ 靠后的），假设现在遍历的是第 j 条水平线段，那么我们将集合中低于第 $j$ 条水平线段的点从集合中删除，之后统计在第 $j$ 条线段横坐标范围内的点的数量，这些点代表的垂直线段就与该两条水平线段相交，假设有cnt个，那么这两条水平线段围成的矩形就有$cnt*(cnt-1)/2$个,我们遍历完所有剩下的水平线段并向上面那样维护就可以计算出所有以第 $i$ 条线段为底的矩形的数量。

总的时间复杂度为$O(n^2logn)$

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=5e3+10;
const int MAXN=1e4+10;
struct HorizontalLine{
    int x1,x2,y;
    HorizontalLine(){}
    HorizontalLine(int y,int x1,int x2):y(y),x1(x1),x2(x2){}
    bool operator <(const HorizontalLine &o) const
    {
        return y<o.y;
    }
};
vector<HorizontalLine> hl;
struct VerticalLine{
    int x,y1,y2;
    VerticalLine(){}
    VerticalLine(int x,int y1,int y2):x(x),y1(y1),y2(y2){}
    bool operator < (const VerticalLine &o) const
    {
        return y2<o.y2;
    }
};
vector<VerticalLine> vl;
struct Point{
    int x,y;
    Point(){}
    Point(int x,int y):x(x),y(y){}
    bool operator < (const Point &o) const
    {
        return y<o.y;
    }
}po[N];
struct BITtree{
    int bt[N*2];
    int lowbit(int k)
    {
        return k&-k;
    }
    void add(int k,int val)
    {
        while(k<=MAXN)
        {
            bt[k]+=val;
            k+=lowbit(k);
        }
    }
    int getpre(int k)
    {
        int ans=0;
        while(k)
        {
            ans+=bt[k];
            k-=lowbit(k);
        }
        return ans;
    }
    int getlr(int l,int r)
    {
        return getpre(r)-getpre(l-1);
    }
}ooo;
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;++i)
    {
        int x1,x2,y1,y2;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        x1+=5001;
        x2+=5001;
        if(x1 > x2)
            swap(x1,x2);
        if(y1 > y2)
            swap(y1,y2);
        if(x1==x2)
        {
            vl.push_back(VerticalLine(x1,y1,y2));
        }
        else{
            hl.push_back(HorizontalLine(y1,x1,x2));
        }
    }
    sort(hl.begin(),hl.end());
    sort(vl.begin(),vl.end());
    long long ans=0;
    for(int i=0;i<int(hl.size());++i)
    {
        int y=hl[i].y,x1=hl[i].x1,x2=hl[i].x2;
        int top=0;
        for(int j=0;j<int(vl.size());++j)
        {
            if(vl[j].x<=x2&&vl[j].x>=x1&&vl[j].y1<=y&&vl[j].y2>=y)
            {
                po[top++]=Point(vl[j].x,vl[j].y2);
                ooo.add(vl[j].x,1);
            }
        }
        int p=0;//未添加的位置
        for(int j=i+1;j<int(hl.size());++j)
        {
            while(p<top&&po[p].y<hl[j].y)
            {
                ooo.add(po[p].x,-1);
                ++p;
            }
            int cnt=ooo.getlr(hl[j].x1,hl[j].x2);
            ans+=1ll*cnt*(cnt-1)/2;
        }
        while(p<top)
        {
            ooo.add(po[p].x,-1);
            ++p;
        }
    }
    printf("%lld\n",ans);
    return 0;
}

```




## P2163 [SHOI2007]园丁的烦恼（离线，树状数组二维数点）


#### 题目链接：[传送门](<https://www.luogu.org/problem/P2163)


#### 输入格式


第一行有两个整数n，m（0≤n≤500000，1≤m≤500000）。n代表皇家花园的树木的总数，m代表骑士们询问的次数。

文件接下来的n行，每行都有两个整数xi，yi，代表第i棵树的坐标（0≤xi，yi≤10000000）。

文件的最后m行，每行都有四个整数aj，bj，cj，dj，表示第j次询问，其中所问的矩形以（aj，bj）为左下坐标，以（cj，dj）为右上坐标。

#### 输出格式


共输出m行，每行一个整数，即回答国王以（aj，bj）和（cj，dj）为界的矩形里有多少棵树

二维数点，很容易想到离线让矩阵的点按x轴右端点从小到大排个序，依此添加新加入的点就好了。但是我们会发现树状数组每次统计的 不是y轴区间$[y1,y2]$在x轴的$[x1,x2]$范围的点的个数，而是x轴$[0,x2]$范围的个数。所以我们可以将矩形$x\in[x1,x2],y\in[y1,y2]$,分成矩阵$x\in[0,x2],y\in(y1,y2)$点的个数减去矩形$x\in[0,x1-1],y\in[y1,y2]$的点的个数就好了。也可以分成四个前缀矩形加减组合。（因为当时直接想的就是前缀矩形，所以就分成了四个矩形了，不过都一样啦


另外也可以cdq分治求，像二维偏序那样


#### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
#define lson rt<<1,l,m
#define rson rt<<1|1,m+1,r
using namespace std;
typedef long long ll;
const int N=5e5+20;
const int inf=0x3f3f3f3f;
struct BitTree
{
    int bt[N*4],MXN;
    int lowbit(int k)
    {
        return k&-k;
    }
    void add(int k)
    {
        while(k<=MXN)
        {
            bt[k]+=1;
            k+=lowbit(k);
        }
    }
    int getpre(int k)
    {
        int ans=0;
        while(k>0)
        {
            ans+=bt[k];
            k-=lowbit(k);
        }
        return ans;
    }
} ooo;
int xx[N],yy[N];
int a1[N],b1[N],a2[N],b2[N];
int ans[N][4];
vector<int> sx;
vector<int> sy;
struct pnode
{
    int x,y;
    bool operator < (const pnode &o) const
    {
        return x<o.x;
    }
} pp[N];
struct qnode
{
    int x,y,id,f;
    qnode(){}
    qnode(int x,int y,int id,int f):x(x),y(y),id(id),f(f){}
    bool operator < (const qnode &o) const
    {
        return x<o.x;
    }
} qt[N*4];
int getxid(int v)
{
    return lower_bound(sx.begin(),sx.end(),v)-sx.begin()+1;
}
int getyid(int v)
{
    return lower_bound(sy.begin(),sy.end(),v)-sy.begin()+1;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n,m;
    cin>>n>>m;
    for(int i=1; i<=n; ++i)
    {
        cin>>xx[i]>>yy[i];
        sx.push_back(xx[i]);
        sy.push_back(yy[i]);
    }
    for(int i=1; i<=m; ++i)
    {
        cin>>a1[i]>>b1[i]>>a2[i]>>b2[i];
        sx.push_back(a1[i]);
        sx.push_back(a2[i]);
        sy.push_back(b1[i]);
        sy.push_back(b2[i]);
    }
    sort(sx.begin(),sx.end());
    sx.erase(unique(sx.begin(),sx.end()),sx.end());
    sort(sy.begin(),sy.end());
    sy.erase(unique(sy.begin(),sy.end()),sy.end());
    for(int i=1;i<=n;++i) {
        xx[i]=getxid(xx[i]);
        yy[i]=getyid(yy[i]);
        pp[i-1].x=xx[i];
        pp[i-1].y=yy[i];
    }
    int top=0;
    for(int i=1;i<=m;++i) {
        a1[i]=getxid(a1[i]);
        a2[i]=getxid(a2[i]);
        b1[i]=getyid(b1[i]);
        b2[i]=getyid(b2[i]);
        qt[top++]=qnode(a2[i],b2[i],i,3);
        qt[top++]=qnode(a1[i]-1,b1[i]-1,i,0);
        qt[top++]=qnode(a2[i],b1[i]-1,i,1);
        qt[top++]=qnode(a1[i]-1,b2[i],i,2);
    }
    sort(qt,qt+top);
    sort(pp,pp+n);
    ooo.MXN=sy.size();
    int p=0;//待选位置
    for(int i=0;i<top;++i)
    {
        while(p < n&& pp[p].x<=qt[i].x){
            ooo.add(pp[p].y);
            ++p;
        }
        ans[qt[i].id][qt[i].f]=ooo.getpre(qt[i].y);
    }
    for(int i=1;i<=m;++i){
        cout<<ans[i][3]+ans[i][0]-ans[i][1]-ans[i][2]<<endl;;
    }
    return 0;
}
```




## 计算区间不同数的和（离线+树状数组）


#### 题目传送门:[牛客练习赛52-B：Galahad](https://ac.nowcoder.com/acm/contest/1084/B)


### 题意：


给一个长度为n的数组，有q次询问，每次询问一个区间$[ l , r ] ​ [l,r]​$ ，问这个区间的和，但如果某一个数在这个区间出现了多次，这个数只能被计算一次。

### 思路：


题目中只有修改操作，所以我们可以离线处理。

我们让所有查询按右端点从小到大排序。对于每个区间将未添加的原数组元素设为$w [ p ] w[p]$，如果 $w [ p ] w[p]$ 在前面已经出现过，那就让前面的删除。让p这个位置的值变为$w [ p ] w[p]$。最后对于这个区间求区间合即可。

这样的话区间中出现相同的数只有最后出现位置才有贡献。且有这个数必可以计算出贡献。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long ```




## 洛谷P2487 [SDOI2011]拦截导弹（cdq分治+dp）


**题目链接**：[传送门](https://www.luogu.org/problem/P2487)

**思路**：

​ 这个其实就是求三维偏序的最长子序列，且求出每个三元组在所有最长子序列中的出现次数。其中第一维是导弹出现的顺序。

我们先写下dp方程，$f l s [ i ] fls[i]$为第 i 个元素结尾的最长子序列的长度，$f k i n d [ i ] fkind[i]$为第 i 个元素结尾的最长子序列的方法数。容易写出dp方程$f l s [ i ] = m a x ( f l s [ i ] , f l s [ j ] + 1 ) fls[i]=max (fls[i],fls[j]+1)$，其中${ j ≤ i   ,   b j ≤ b i   ,   c j ≤ c i } \{j\le i ~,~b_j\le b_i~, ~c_j\le c_i\}$。

对于区间$( l , r ) (l,r)$，设$m = ( l + r ) / 2 m=(l+r)/2$。那么对于i ,j的转移不外乎三种情况：


+ $j ∈ ( l , m ) , i ∈ ( l , m ) ​ j\in(l,m),i\in(l,m)​$
+ $j ∈ ( l , m ) , i ∈ ( m + 1 , r ) ​ j\in(l,m),i\in(m+1,r)​$





## HDU 6681（树状数组，统计平面内射线的交点个数）


题目链接：[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=6681)

**题意**：给出k条射线，求射线将$n ∗ m n*m$ 的区域分成几个联通块。每两条射线的端点x坐标和y坐标都互不相同。

**思路**：根据 *欧拉公式* 可以推导出联通块的个数等于射线的焦点个数c+1。但其实赛场上根本不知道这个定理，但有个很明显的道理，对于每条竖线，每条横着的射线与该竖线相交都会使联通块个数+1.(注意因为题目限制，这个射线的端点不会在边界上，不然在边界的射线会使联通块+2)。所以我们直接统计出射线的交点个数即可，这是个经典问题（但是我当时不会

​ 其实对于每条竖着的射线(假设端点为$x 0 , y 0 ​ x0,y0​$)，只要能统计出它**左边横着的射线与之相交的射线个数**和，即相交的射线的端点$x , y ​ x,y​$满足射线方向向右且$x &lt; x 0 ​ x&lt;x0​$，y在射线($x 0 , y 0 ​ x0,y0​$)纵坐标覆盖范围之内即可。统计**左边横着的射线与之相交的射线个数**也是同样道理

​ 因为射线的个数$k k$的范围为$1 e 5 ​ 1e5​$，故使用二维前缀和肯定是不行的。

​ 我们可以分类统计，我们先来统计每条射线**左边横着的射线与之相交的射线个数**，我们可以先将所有竖直方向的射线按$x x$从小到大排序，所有横着的射线按$x x$从小到大排序，对于第$i i$ 条竖直方向的射线，我们可以处理所有左边的横着向右的射线，然后把他们的$y y$坐标加入树状数组 (这里需要对$y y$坐标进行离散化)。然后可以$O$



#### zzuli2520: 大小接近的点对（CCPC河南省省赛） 离线处理+DFS遍历树+树状数组


### 思路：


​ 我们可以利用$DFS$序，统计子树中与该节点权值相差为$k$的个数，这个范围是一个区间。

$DFS$序遍历树，进入一个节点的时候记录符合条件的个数记作$cntf$，然后树状数组添加该节点信息，$DFS$遍历儿子即可。(注意，遍历过程中不撤销节点信息)

离开该节点时记录符合条件的个数记作$cntb$。那么$cntb-cntf$ 就是该节点与子树符合条件的个数。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll maxn=1e5+10;
ll MAX=1e5+5;
ll X[maxn],sa[maxn],XX[maxn];
ll Sum[maxn],bt[maxn],tot;
vector<ll> adja[maxn];
ll n,K;
ll lowbit(ll k)
{
    return k&-k;
}
void modify(ll k)
{
    while(k<=MAX)
    {
        bt[k]+=1;
        k+=lowbit(k);
    }
}
ll getsum(ll k)
{
    ll ans=0;
    while(k>0)
    {
        ans+=bt[k];
        k-=lowbit(k);
    }
    return ans;
}
void dfs(ll u)
{
    ll l,r;
    l=lower_bound(XX,XX+tot,X[u]-K)-XX;
    r=upper_bound(XX,XX+tot,X[u]+K)-XX-1;
    ll cntf=getsum(r)-getsum(l-1);
    modify(sa[u]);
    ll sum=0;
    for(ll i=0;i<adja[u].size();++i)
    {
        ll v=adja[u][i];
        dfs(v);
        sum+=Sum[v];
    }
    ll cntb=getsum(r)-getsum(l-1);
    Sum[u]=sum+cntb-cntf;
}
int main()
{
    scanf("%lld%lld",&n,&K);
    XX[0]=0;
    for(ll i=1;i<=n;++i)
        scanf("%lld",&X[i]),XX[i]=X[i];
    for(ll i=2;i<=n;++i)
    {
        ll fa;
        scanf("%lld",&fa);
        adja[fa].push_back(i);
    }
    sort(XX,XX+1+n);
    tot=unique(XX,XX+1+n)-XX;
    MAX=tot;
    for(ll i=1;i<=n;++i)
        sa[i]=lower_bound(XX,XX+tot,X[i])-XX;
    dfs(1);
    for(ll i=1;i<=n;++i)
        printf("%lld\n",Sum[i]);
    return 0;
}

```




### [J - Vasya and a Tree](https://vjudge.net/problem/CodeForces-1076E) （树状数组+离线处理）


[CodeForces - 1076E ](https://vjudge.net/problem/2028113/origin)

### 题意：


​ 给定有n个点的一棵树，顶点1为根。m次操作，每次都把以v为根，深度dep以内的子树中所有的顶点（包括v本身）加x。求出最后每个点的值为多少

### 思路：


​ 离线处理+树状数组。其中树状数组维护当前深度区间信息。 （终于知道什么是离线查询）


​ 我们可以$D F S DFS$序遍历以$1 1$为根的树，每到一个节点，就根据当前节点的修改信息向下修改，离开该节点就修改回来，这样每到一个节点，影响他状态的只有他的祖宗节点。而当前节点的值也都是只有祖宗节点才能修改，那么当前深度的信息就是该节点应有的信息。

不懂的推荐看代码

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const ll MAXN=3e5+10;
ll MAX=MAXN;
ll n;
vector<ll> adja[MAXN];
vector<P> oper[MAXN];
ll bt[MAXN],res[MAXN];
ll ```




## 二维树状数组更块查点



在此不给予证明,但是证明很简单。


二维树状数组成块更新，查定点的值。

我们以一维的推广，我们可不可以成块更新转化为修改一些点的值，然后求点的值转化统计一块的和？

我们可以构造一个M矩阵，让M矩阵初始化为0，我们可以让坐标（x，y）的值等于以（1，1）和（x，y）组成的M子矩阵的元素之和（你看看，这个条件在刚开始的时候是成立的），我们更新以（x1，y1）和（x2，y2）组成的矩阵的值的时候，我们只需在M矩阵中插入（x1，y1）（x1，y2+1）（x2+1，y1）（x2+1，y2+1）的值。

比如我们将以（x1，y1）和（x2，y2）组成的矩阵的元素都加上val。那么我们将（x1，y1）+val，（x1，y2+1）-val，（x2+1，y1）-val，（x2+1，y2+1）+val即可。

题意：对一个n∗m的矩阵进行一些操作和查询，操作：成块修改。查询：求某个元素的值，

```cpp
#include<bits/stdc++.h>
using namespace std;
int bt[1100][1100];
int MAXN,MAXM;//矩阵的行和列
int lowbit(int k)
{
    return k&-k;
}
void modify(int x,int y,int val){//更新所有与他有关的节点
    for(int i=x;i<=MAXN;i+=lowbit(i)){
        for(int j=y;j<=MAXM;j+=lowbit(j))
            bt[i][j]+=val;
    }
}
int getsum(int x,int y)//等于其左上角矩阵的和
{
    int ans=0;
    for(int i=x;i>0;i-=lowbit(i)){
        for(int j=y;j>0;j-=lowbit(j))
            ans+=bt[i][j];
    }
    return ans;
}
void update(int x1,int y1,int x2,int y2,int val)//更新差值矩阵
{
    modify(x1,y1,val);
    modify(x1,y2+1,-val);
    modify(x2+1,y1,-val);
    modify(x2+1,y2+1,val);
}
int main()
{
    int q,val,x,y,x1,y1,x2,y2;
    cin>>MAXN>>MAXM;
    cin>>q;
    while(q--){//修改操作
        cin>>x1>>y1>>x2>>y2>>val;
        update(x1,y1,x2,y2,val);
    }
    cin>>q;//查询操作的次数
    while(q--)
    {
        cin>>x>>y;
        int ans=getsum(x,y);
        cout<<ans<<endl;
    }
}
```




## 树状数组基础总结


入门博文：[http://www.cnblogs.com/acgoto/p/8583952.html](http://www.cnblogs.com/acgoto/p/8583952.html)

#### 树状数组与线段树的思想的一些相同与不同。


共同点：同时一个节点维护多个叶子节点的信息

不同点：线段树节点采用二分的规则，而树状数组节点利用了bit位的性质来锁定管理的叶子节点，且树状数组只能直接查询1~i区间的信息，而线段树可以直接查询$[l,r]$ 区间信息，

树状数组可以解决问题的思路推广到线段树都可以用线段树解决。不过树状数组代码量是真的小！

**树状数组核心函数：**

这样的代码要求其叶子节点必须从1开始（因为此处维护的都是1~i的信息，可以改下代码使维护0到i的信息，不过代码就不简洁了）

```cpp
int lowbit(ll val){ //获得val的1的最低位的二进制权值
    return  val&(-val);
}
int getsum(ll k)//遍历1~k区间的管理节点。
{
    ll ans=0;
    while(k>0)
    {
        ans+=bt[k];
        k-=lowbit(k);
    }
    return ans;
}
void modify(ll k,ll val)//向上更新管理叶子节点k的节点信息。
{
    while(k<=n)
    {
        bt[k]+=val;
        k+=lowbit(k);
    }
}
```


洛谷模板题，改点查段：[https://www.luogu.org/problemnew/show/P3374](https://www.luogu.org/problemnew/show/P3374)

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn=5e5+100;
ll  qwe[maxn],n,q;
int lowbit(ll val){
    return  val&(-val);
}
int getsum(ll k)
{
    ll ans=0;
    while(k>0)
    {
        ans+=qwe[k];
        k-=lowbit(k);
    }
    return ans;
}
int modify(ll k,ll val)
{
    while(k<=n)
    {
        qwe[k]+=val;
        k+=lowbit(k);
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>q;
    for(int i=1;i<=n;++i){
        ll val;
        cin>>val;
        modify(i,val);
    }
    while(q--)
    {
        ll fa,x,y;
        cin>>fa>>x>>y;
        if(fa==1)
        {
            modify(x,y);
        }
        else{
            cout<<getsum(y)-getsum(x-1)<<endl;
        }

    }
    return 0;

}

```


比如：LIS(最长递增子序列)，求逆序对，改点查段，改段查点的问题都可以用树状数组解决。

#### 经典问题转化：


**LIS(最长递增子序列)思想：**

$f[i]$ 表示当前以值 $i$ 为递增子序列末尾的序列最长长度。每个叶子 $i$ 记录当前$f[i]$, 最大值，那么用树状数组节点维护其叶子节点的最大值即可。如果该此时序列中数字值为val，那么$f[val]=max(f[i])_{i\in[1,val]}+1 =\ \ ~getmax(i)+1$ ps：有时候需要离散化，所以还是二分求LIS比较好用

**求逆序对思想：**

每个叶子 $i$ 记录当前值i的出现次数，那么用树状数组节点维护其管理的叶子节点出现次数和即可，假设当前第k个数其值为val，那么前面大于val的个数=$k-1-getsum(val)$

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn=5e5+100;
int tot,n;
int unq[maxn],qwe[maxn],bt[maxn];
int getind(int val)
{
    return lower_bound(unq,unq+tot,val)-unq;
}
int lowbit(int val)
{
    return val&-val;
}
ll getsum(int k)
{
    ll ans=0ll;
    while(k>0)
    {
        ans+=bt[k];
        k-=lowbit(k);
    }
    return ans;
}
void modify(int k)//k叶子+1
{
    while(k<=n)
    {
        ++bt[k];
        k+=lowbit(k);
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n;
    for(int i=0;i<n;++i)
        cin>>unq[i],qwe[i]=unq[i];
    sort(unq,unq+n);
    tot=unique(unq,unq+n)-unq;
    ll ans=0ll;
    mset(bt,0);
    for(int i=0;i<n;++i)
    {
        int ind=getind(qwe[i])+1;
//        cout<<"ind:"<<ind<<endl;
        ans+=i-getsum(ind);
        modify(ind);
        /*先求逆序数i- 1~val的个数 然后插入*/
    }
    cout<<ans<<endl;
}
```


**改段查点：**

修改：将区间 $[l,r] $ 的每个数加val，查询：求点k处的值

假设原数组为$Num[]$,我们用$d[]$ 记录相邻元素的差值，比如$d[i]=num[i]-num[i-1]$,且我们让 $d[1]=num[1]$ ,那么$num[i]=d[1]+d[2].....+d[i]$

至于修改操作，我们只需将$d[l]$加上$val$，$d[r+1]$减去$val$即可，

我们维护d数组即可。

洛谷模板：[https://www.luogu.org/problemnew/show/P3368](https://www.luogu.org/problemnew/show/P3368)

代码:

```cpp
// luogu-judger-enable-o2
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn=5e5+100;
ll  qwe[maxn],n,q;
int lowbit(ll val){
    return  val&(-val);
}
int getsum(ll k)
{
    ll ans=0;
    while(k>0)
    {
        ans+=qwe[k];
        k-=lowbit(k);
    }
    return ans;
}
void modify(ll k,ll val)
{
    while(k<=n)
    {
        qwe[k]+=val;
        k+=lowbit(k);
    }
}
ll va[maxn];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>n>>q;
    for(int i=1;i<=n;++i){
        cin>>va[i];
    }
    modify(1,va[1]);
    for(int i=2;i<=n;++i)
        modify(i,va[i]-va[i-1]);
    while(q--)
    {
        ll fa,x,y,z;
        cin>>fa;
        if(fa==1)
        {
            cin>>x>>y>>z;
            modify(y+1,-z);
            modify(x,z);
        }
        else{
            cin>>x;
            cout<<getsum(x)<<endl;
        }
    }

    return 0;
}

```




### [I - 80-th Level Archeology](https://vjudge.net/problem/CodeForces-731D)（前缀和，区间交集）


[CodeForces - 731D ](https://vjudge.net/problem/525657/origin)

### 题意：


​ 给出n个串，一共有c种字母编号为1-c。然后描述每一个串。每一次可以使得所有串的所有字母编号+1（编号为c的变成1）.问最少多少次吼能够使得所有的串按照字典序递增

### 思路：


​ 我们只要保证相邻的两个串都递增即可。对于每两个串，我们求出假设我们旋转k次就可以使得着两个串递增。其中k的区间可以线性求出来。最后我们只要找出被区间覆盖n-1次的点即可。这个k就是答案。

​ 至于怎么线性求k的区间，因为两个串不管旋转多少次他们的大小都取决于最前面的不同的数。那么我们只要找到第一个不同的数字，分情况讨论从而得出k的区间。

### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int MAXN=1000000+20;
int MAX=1000000+10;
const int inf=0x3f3f3f3f;
int bt[MAXN];//  叶子存储相邻元素差
int num[2][500100];
int lowbit(int k)
{
    return k&-k;
}
void modify(int k,int val)
{
    while(k<=MAX)
    {
        bt[k]+=val;
        k+=lowbit(k);
    }
}
int getsum(int k)
{
    int ans=0;
    while(k>0)
    {
        ans+=bt[k];
        k-=lowbit(k);
    }
    return ans;
}
void addInterval(int l,int r)
{
//    if(l>r) return ;
    l++,r++;
    modify(l,1);
    modify(r+1,-1);
}
int main()
{
    int n,c,cur=0,flag=1;
    int lastcnt,cnt;
    scanf("%d%d",&n,&c);
    MAX=c+5;
    scanf("%d",&cnt);
    for(int i=0; i<cnt; ++i)
        scanf("%d",&num[cur][i]);
    lastcnt=cnt;
    cur^=1;
    for(int k=1; k<n; ++k)
    {
        scanf("%d",&cnt);
        for(int i=0; i<cnt; ++i)
            scanf("%d",&num[cur][i]);
        if(flag) //可能存在解
        {
            int sign=0;;
            for(int i=0; i<min(lastcnt,cnt); ++i)
            {
                if(num[cur][i]>num[cur^1][i])
                {
                    sign=1;
                    addInterval(0,c-num[cur][i]);
                    addInterval(c-num[cur^1][i]+1,c-1);
                    break;
                }
                else if(num[cur][i]<num[cur^1][i])
                {
                    sign=1;
                    addInterval(c-num[cur^1][i]+1,c-num[cur][i]);
                    break;
                }
            }
            if(sign==0)
            {
                if(lastcnt>cnt)//无解
                    flag=0;
                else
                    addInterval(0,c-1);
            }
        }
        lastcnt=cnt;
        cur^=1;
    }
    int ans=-1;
    if(flag)
    {
        for(int i=1; i<=c; ++i)
        {
            if(getsum(i)==n-1)
            {
                ans=i-1;
                break;
            }
        }
    }
    printf("%d\n",ans);
    return 0;
}

```




### H - Babaei and Birthday Cake CodeForces - 629D


[https://vjudge.net/contest/301590#problem/H](https://vjudge.net/contest/301590#problem/H)

题意：

​ 有n个蛋糕，从1编号到n，现在用这些蛋糕制作一个大蛋糕，要求编号大的蛋糕必须放在编号小的蛋糕上面，且上面的蛋糕的体积必须严格大于下面蛋糕的体积，问能制作出的大蛋糕的最大体积

思路：

​ 每次找出面积比他小的堆起来的最大蛋糕面积即可。找的过程可以将所有面积离散化，然后用树状数组查找（线段树，map都可以实现）。

​ 且面积之间的累加和比较可以用$h*r*r$ 来表示。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
const ll MAX=100000;
const ll inf=0x3f3f3f3f;
const double PI=acos(-1);
ll n;
ll sa[MAXN],X[MAXN];//离散化后的sa  原来的X
ll XX[MAXN],dp[MAXN],bt[MAXN];
ll lowbit(ll k)
{
    return k&-k;
}
void modify(ll k,ll val)
{
    while(k<=MAX)
    {
        bt[k]=max(bt[k],val);
        k+=lowbit(k);
    }
}
ll getmax(ll k)
{
    ll ans=0;
    while(k>0)
    {
        ans=max(ans,bt[k]);
        k-=lowbit(k);
    }
    return ans;
}
int main()
{
    ll n,r,h;
    scanf("%lld",&n);
    XX[0]=X[0]=sa[0]=dp[0]=0;
    for(ll i=1;i<=n;++i)
    {
        scanf("%lld%lld",&r,&h);
        X[i]=h*r*r;
        XX[i]=X[i];
    }
    sort(XX,XX+1+n);
    ll tot=unique(XX,XX+1+n)-XX;
    for(ll i=1;i<=n;++i)
        sa[i]=lower_bound(XX,XX+tot,X[i])-XX;
    for(ll i=1;i<=n;++i){
        dp[i]=X[i]+getmax(sa[i]-1);
        modify(sa[i],dp[i]);
    }
    ll maxx=0;
    for(ll i=1;i<=n;++i)
    {
        maxx=max(maxx,dp[i]);
    }
    printf("%.10f\n",double(maxx)*PI);
    return 0;
}

```




### [ KiKi’s K-Number](https://vjudge.net/problem/HDU-2852)  (树状数组)


[HDU - 2852 ](https://vjudge.net/problem/17358/origin)

**题意：**

题意：题目给定三种操作: 0 x 表示把x插入容器 ; 1 x 表示删除一个x如果没有x则输出 No Elment! ; 2 a k 表示比a大的数中的第k大的数 如果没有输出No Find!

**思路：**

​ 树状数组维护元素出现次数前缀和即可。操作0即修改；操作1先查询x是否存在，如果存在删除一个即可。操作2可以用二分逐渐逼近答案。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
const int MAX=100000;
int bt[MAXN];
int lowbit(int k)
{
   
    return k&-k;
}
void modify(int k,int val)
{
   
    while(k<=MAX)
    {
   
        bt[k]```




### [F - Disharmony Trees](https://vjudge.net/problem/HDU-3015)


[HDU - 3015 ](https://vjudge.net/problem/17589/origin)

##### **题意：**


​ 对于n棵树，给出所在位置和高度，根据给出的规则算出每棵树的位置等级$xlev$和高度等级$hlev$

然后，定义f=两树之间的位置的那估计的绝对值，s=两树中最小的高度等级，求所有树之间f*s和。

##### 思路：


​ 预处理把所有的树重新构造距离和高度熟属性，我们让所有树按照树的高度从高到低排序，那么每次求当前这个树与前面每个树的 Disharmony Value 即可，因为高度是从高到低，所以与前面每颗数计算的min(H1,H2)都为自己的高度。且求Disharmony Value操作可以优化到logn级别，假设前面的树的距离为aX，高度为aH，当前树的距离为X，高度为H，那么$abs(aX-X)*min(aH,H)=abs(aX-X)*H$

+ 如果$aX&gt;=X$ ： $abs(aX-X)*H=aX*H-X*H​$+ 否则：$abs(aX-X)*H=X*H-aX*H$


那么我们可以**统计当前所有的树满足$x&gt;=X$ 的所有**距离和** 以及**个数**，以及当前满足$x&lt;X$的所有**距离和** 以及**个数** 即可。然后加到答案上。

即用树状数组维护区间个数个区间和即可。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
ll MAX=1e5+1;
ll sx[MAXN],sh[MAXN];//数据的等级
ll X[MAXN],H[MAXN];//数据
ll n;
struct Node
{
    ll x,h;
} node[MAXN];
bool cmp(Node a,Node b)
{
    return a.h<b.h;
}
ll getxth(ll x)
{
    ll th=lower_bound(X,X+1+n,x)-X;
    return sx[th];
}
ll gethth(ll h)
{
    ll th=lower_bound(H,H+1+n,h)-H;
    return sh[th];
}
ll btt[MAXN],bts[MAXN];//对应节点出现的个数  和出现的X的和
ll book[MAXN],SUM,TOT;
ll lowbit(ll k)
{
    return k&-k;
}
void modify(ll k)
{
    ll val=k;
    while(k<=MAX)
    {
        btt[k]++;
        bts[k]+=val;
        k+=lowbit(k);
    }
}
pair<ll,ll> getinfo(ll k)//1~k 的个数为tot，他们的和为sum
{
    ll tot=0,sum=0;
    while(k>0)
    {
        tot+=btt[k];
        sum+=bts[k];
        k-=lowbit(k);
    }
    return make_pair(tot,sum);
}
void calc(ll l,ll r,ll &tot,ll &sum)
{
    pair<ll,ll> PA,PB;
    PB=getinfo(r);
    PA=getinfo(l-1);
    tot=PB.first-PA.first;
    sum=PB.second-PA.second;
}
int main()
{
    while(~scanf("%lld",&n))
    {
        X[0]=H[0]=0;
        sx[0]=sh[0]=0;
        MAX=-1;
        for(ll i=1; i<=n; ++i)
        {
            scanf("%lld%lld",X+i,H+i);
            node[i].x=X[i];
            node[i].h=H[i];
        }
        sort(X,X+n+1);
        sort(H,H+n+1);
        sort(node+1,node+1+n,cmp);
        for(ll i=1; i<=n; ++i)
        {
            if(X[i]==X[i-1])
                sx[i]=sx[i-1];
            else
                sx[i]=i;
            if(H[i]==H[i-1])
                sh[i]=sh[i-1];
            else
                sh[i]=i;
            MAX=max(MAX,sx[i]);
        }
        mset(btt,0);
        mset(bts,0);
        mset(book,0);
        ll ans=0;
        SUM=TOT=0;
        for(ll i=n; i>=1; --i) //h从大到小遍历, 找到当前比他小 和比他大的个数
        {
            ll xlev=getxth(node[i].x),hlev=gethth(node[i].h);
            TOT++;
            SUM+=xlev;
            modify(xlev);
            ll lstot,lssum,uptot,upsum;
            calc(1,xlev,lstot,lssum);
            uptot=TOT-lstot;
            upsum=SUM-lssum;
            ll mid=((lstot-uptot)*xlev+upsum-lssum)*hlev;
            ans+=((lstot-uptot)*xlev+upsum-lssum)*hlev;
        }
        printf("%lld\n",ans);
    }
    return 0;
}

```




### [E - Apple Tree](https://vjudge.net/problem/POJ-3321)


[POJ - 3321 ](https://vjudge.net/problem/10486/origin)

题意：

​ 一颗苹果树，刚开始所有节点都有苹果，有以下两种操作，一种是改变一个节点的状态（有苹果就取走，没苹果就产生一个），一种是询问一个点的子树（包括节点自己）一共有多少个苹果，对于每次询问输出结果

分析：

```bash
重新DFS序给节点标号，那么没个节点的子孙就对应一个连续的区间。那么修改点的状态相当于单点修改，查询操作相当于区间求和，树状数组和线段树都可以写。
```


注：POJ存树图用vector超时

```cpp
#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=1e5+20;
const ll MAX=100000;
ll DS[MAXN],L[MAXN],R[MAXN];//顶点u对应的区间为[L,R],u的虚拟节点为DS[u]
ll book[MAXN],tot,ecnt;
ll bt[MAXN],sw[MAXN];
int head[MAXN];
struct Edge{
 int v,to;
}edge[MAXN<<1];
void addEdge(int u,int v,int ed)
{
    edge[ed].v=v;
    edge[ed].to=head[u];
    head[u]=ed;
}
void dfs(ll u)
{
    tot++,book[u]=1;
    DS[u]=tot,L[u]=tot;
    int to=head[u];
    while(to!=-1)
    {
        int v=edge[to].v;
        to=edge[to].to;
        if(book[v]) continue;
        dfs(v);
    }
    R[u]=tot;
}
/*
重现构造搜索序列
*/
ll lowbit(ll k)
{
    return k&-k;
}
void modify(ll k,ll val)
{
    while(k<=MAX){
        bt[k]+=val;
        k+=lowbit(k);
    }
}
ll getsum(ll k)
{
    ll ans=0;
    while(k>0)
    {
        ans+=bt[k];
        k-=lowbit(k);
    }
    return ans;
}
char s[10];
int main(){
    ll n;
    scanf("%lld",&n);
    ecnt=0ll;
    mset(head,-1);
    for(ll i=0;i<n-1;++i){
        ll u,v;
        scanf("%lld%lld",&u,&v);
        addEdge(u,v,ecnt++);
        addEdge(v,u,ecnt++);
    }
    tot=0;
    dfs(1);
    for(ll i=1;i<=n;++i)
        modify(i,1);
    ll q;
    scanf("%lld",&q);
    while(q--)
    {
        scanf("%s",s);
        if(s[0]=='Q'){
            ll u;
            scanf("%lld",&u);
            printf("%lld\n",getsum(R[u])-getsum(L[u]-1));
        }
        else{
            ll u;
            scanf("%lld",&u);
            if(sw[u]==1){
                sw[u]=0;
                modify(DS[u],1);
            }
            else{
                sw[u]=1;
                modify(DS[u],-1);
            }
        }
    }
    return 0;
}

```




### [C - Mobile phones](https://vjudge.net/problem/POJ-1195)（二维树状数组）


[POJ - 1195 ](https://vjudge.net/problem/17086/origin)

题意：对一个$n ∗ n n*n$的矩阵进行一些操作和查询，操作：单点修改。查询：求子矩阵元素和

思路：

​ 真没想到二维的树状数组是这样的。（真不知道二维线段树应该怎么维护，期待(☆▽☆)！ ）

构建二维树状数组之后我们可以求$i , j i,j$左上角矩阵的和 。求子矩阵可以转化为多个左上角矩阵元素和的加减。


二维树状数组的第二维(也就是行向量代表的节点吧)之间的关系，跟一维向量的 节点之间关系相同。

看博文：[https://blog.csdn.net/chaiwenjun000/article/details/47973737](https://blog.csdn.net/chaiwenjun000/article/details/47973737)


```cpp
#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
```


