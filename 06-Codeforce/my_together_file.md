

## Ozon Tech Challenge 2020 (Div.1 + Div.2, Rated)补题



都快没有自信了，这场比赛做题量是有史以来最少的一次。

总觉的做一些题没有把知识结合在一起，诸多性质都没有使用，不知道复习完算法有没有帮助。

唉，还要找工作。

confidence ！confidence！confidence！


#### [ B - Kuroni and Simple Strings](https://codeforces.com/contest/1305/problem/B)


**错误：**

+ 没有过早归纳 结果 的性质，")))(((("+ 没有仔细思考思路是否正确，就直接写，甚至连样例的没检测。


**改正**：

+ 想出一个不确定的思路时，用样例或手写数据去检测是否可能正确。+ 充分利用性质去解题，这题的性质是最后左括号都在右括号右边，即左括号索引的最小值大于右括号索引的最大值，那么就可以把左右括号下标序列分别提出来设为$a[],b[]$。最后的结果肯定是数组a的最右边(索引大)和数组$b$的最左边（索引小）留下。


代码：

```cpp
#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define lson l,m,u<<1
#define rson m+1,r,u<<1|1
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
const int N = 5e3+10;
char s[N];
int main()
{
    scanf("%s",s+1);
    int n=strlen(s+1);
    vector<int> a,b;
    for(int i=1;i<=n;++i){
        if(s[i]=='(') a.pb(i);
        else b.pb(i);
    }
    int l=0,r=b.size()-1;
    while(l < a.size()&&r >=0 ){
        if(a[l] < b[r]) {
            l++;
            r--;
        }
        else break;
    }
    if(l==0){
        printf("0\n");
    }
    else{
        printf("1\n");
        vector<int> ans;
        for(int i=0;i<l;++i) ans.pb(a[i]);
        for(int i=r+1;i<b.size();++i) ans.pb(b[i]);
        printf("%d\n",ans.size());
        for(int v:ans)
            printf("%d ",v);
        puts("");
    }
}
```


##### [C - Kuroni and Impossible Calculation](https://codeforces.com/contest/1305/problem/C)


错误：

+ 没有注意数据范围，这里特指m的数据范围+ 没有想到将结果等价于原数组取模在进行操作。简单的模运算性质都不使用。


改正：

+ 充分利用数据范围大小+ 很简单的知道如果至少有两个数相同则答案为0，因为表达式是对称的，所以我们可以将数据取模再运算也可以。然后运用鸽笼定理就知道当n>m时必定有两个数相同，则答案为0.


代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
const int N = 2e5+10;
const int inf=0x3f3f3f3f;
int a[N];
int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;++i){
        scanf("%d",a+i);
    }
    int ans=1;
    if( n > m){
        ans=0;
    }
    else{
        for(int i=1;i<=n;++i){
            for(int j=i+1;j<=n;++j){
                ans=ans*(abs(a[j]-a[i])%m)%m;
            }
        }
    }
    printf("%d\n",ans);
    return 0;
}
```


##### [ D - Kuroni and the Celebration](https://codeforces.com/contest/1305/problem/D)



交互题：

题意，给你一颗树，这个树是有根树，让你确定出根是谁。

每次询问两个顶点$u,v$ ，后台会回答$u,v$的最近公共祖先。要求询问不超过$\lfloor \frac n 2\rfloor$次。

我的错误思路：用数组fq来标记那些节点不能选。刚开始时随机选一个点u，并把fq[u]=1，标记为接下来不能选顶点u。

每次选出一个顶点x，如果顶点被标记就continue，计算u与x的lca，并把fq[lca]=1，fq[x]=1,并让u和x 遍历所有连通的未标记顶点，并将之标记，目的在于将u和x到lca上的顶点不能选和子树顶点不能选。

但这样最坏情况下每次只能排除一个顶点，会超过询问次数。


错误：

+ 思路错误，但是以为正确，就直接使用了，即思考不严谨。（以为每次操作至少排除两个，其实至少排除一个）


技巧：

+ 每次维护叶子顶点（度为1的顶点），随便找两个叶子顶点u和v 
  
+ 如果lca(u,v)的值为u或v，那么答案就是lca，因为如果叶子都不是根的话，那么其lca不会等于其中任意一个。+ 否则把u和v从中删除，并维护叶子节点集合。+ 注意节点个数大于1的情况下根节点必定经过度为1的过程。
 


代码：

```cpp
#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define lson l,m,u<<1
#define rson m+1,r,u<<1|1
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
const int N = 1e3+10;
int ask(int u,int v)
{
    printf("? %d %d\n",u,v);
    fflush(stdout);
    int w;
    scanf("%d",&w);
    return w;
}
set<int> g[N];
int du[N];
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1; i<n; ++i)
    {
        int x,y;
        scanf("%d%d",&x,&y);
        g[x].insert(y);
        g[y].insert(x);
    }
    set<int> leaves;
    for(int i=1; i<=n; ++i)
        if(g[i].size()==1)
            leaves.insert(i);
    int ans=-1;
    while(!leaves.empty())
    {
        if(leaves.size()==1)
        {
            ans=*leaves.begin();
            break;
        }
        int a=*leaves.begin();
        leaves.erase(leaves.begin());
        int b=*leaves.begin();
        leaves.erase(leaves.begin());
        int lca=ask(a,b);
        if(lca==a||lca==b)
        {
            ans=lca;
            break;
        }
        else
        {
            for(int v:g[a])
            {
                g[v].erase(a);
                if(g[v].size()==1)
                    leaves.insert(v);
            }
            for(int v:g[b])
            {
                g[v].erase(b);
                if(g[v].size()==1)
                    leaves.insert(v);
            }
        }
    }
    printf("! %d\n",ans);
    fflush(stdout);
    return 0;
}
```


##### [E - Kuroni and the Score Distribution](https://codeforces.com/contest/1305/problem/E)


**错误：**

**技巧**：

+  这题感觉很难想到，要慢慢来总结出性质。假设三元组为$(x,y,z)$

+  首先每个第 $i$个数作为三元组的第三个元素，满足条件的$x,y$的组合最多有$\lfloor \frac {i-1} 2\rfloor$个，这样就可以确定n个元素的数组最多可能由多少个三元组。 +  **注意到**自然数序列是满足三元组数量最多的序列。 +  所以我们找到一个k满足前k个数是自然数，即$\sum_{i=1}^{k}\lfloor \frac {i-1}{2} \rfloor \le m$的最大的$k$，即前k+1个数是自然数的时候组成的三元组必定大于m 即$\sum_{i=1}^{k+1}\lfloor \frac {i-1}{2} \rfloor > m$，令$rem=m-\sum_{i=1}^{k}\lfloor \frac {i-1}{2}\rfloor$，如果$rem!=0$且$k==n$时无解。 +  我们让前k个全为自然数，那么剩余的还需的三元组的个数为rem，且满足$rem<\lfloor \frac k 2 \rfloor$，即$2*rem\le k$ +  根据前面的 $1$ 很容易想到让$a[k+1]=k+k-2*rem+1=2*k-2*rem+1$，这样第k+1个数与前k个组组成的三元组的个数是rem。 +  我们要让剩下的$k+2....n$全部填充为奇数，这样后边的序列不会组成三元组（因为奇数与奇数的和等于偶数），为了还不满足$x\in[1,k+1],y,z\in[k+2,n]$ 的三元组成立，我们让后边部分的数间隔大点，比如$a[k+1]+1$，还不让满足$x,y\in[1,k+1],z\in[k+2,n]$的三元组成立，让后半部分的每个值都大于$a[k]+a[k+2]$ 
 


代码：

```cpp
#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define lson l,m,u<<1
#define rson m+1,r,u<<1|1
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
const int N = 5e3+10;
int a[N];
int main()
{
    int n,m,index=-1;
    scanf("%d%d",&n,&m);
    int sum=0;
    for(int i=1;i<=n;++i)
    {
        sum=sum+(i-1)/2;
        if(sum >= m){
            index=i;
            break;
        }
    }
    if(index==-1){
        printf("-1");
        return 0;
    }
    int k=(sum==m)?index:index-1;
    for(int i=1;i<=k;++i) a[i]=i;
    int rem;
    if(sum==m){
        rem=0;
    }
    else{
        sum-=(index-1)/2;
        rem=m-sum;
    }
    a[k+1]=2*k-2*rem+1;
    for(int i=k+2;i<=n;++i){
        if(i==k+2) a[i]=2*a[k+1]+1;
        else a[i]=a[i-1]+4*k+100;
    }
    for(int i=1;i<=n;++i) printf("%d ",a[i]);
    return 0;
}
```


##### [ F - Kuroni and the Punishment](https://codeforces.com/contest/1305/problem/F)


**技巧**：

+ 让整个序列都是d的倍数的代价$\ge$整个序列都是d的素因子p的代价+ 为了使整个序列都是p的倍数，所需最小的代价可以$O(n)$的用贪心来计算，即每个元素的代价为$min(a[i]\%p,p-a[i]\% p)$，注意当元素小于 $p$ 时，不能减少到0，代价只能是$p-a[i]\%p$。+ 让所有元素都是2的倍数，那么所需代价等于序列中的奇数的个数.+ 很容易想到最优代价$\le n$+ 所以最优解中值改变两个以上的元素个数$\le \frac{n}{2}$个。+ 由结论5得最优解中对每个元素改变值$\le 1$的数的个数$> \frac n 2$。+ 我们从中选择一个数，根据结论6，这个数是最优解中的改变值$\le 1$的数的概率至少是$\frac 1 2$+ 所以选k次，选不中最优解中改变值$\le 1$的数的概率最多是$(\frac 1 2 )^{k}$+ 所以每次随机选择一个数假设为$x$，那么对$x-1,x,x+1$分别素因子分解，然后按照结论2贪心计算需要的代价（可以剪枝：不重新计算，当前代价>最优解 直接舍去）。如果最优解中数x的改变值小于1，就能根据这步计算出最优解。+ 所以随机选择k个数，按照结论9计算，能命中最优解的概率$\ge1-(\frac 1 2 )^{k}$


代码：

```cpp
#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
const int N = 2e5+10;
ll a[N];
ll best;
map<ll,int> table;
void update(ll p,int n)
{
    if(table.count(p)) return ;
    table[p]=1;
    ll sum=0;
    for(int i=1; i<=n; ++i)
    {
        ll t=a[i]%p;
        if(a[i] < p) sum+=p-t;
        else sum+=min(t,p-t);
        if(sum > best){
             return ;
        }
    }
    best=sum;
}
void solve(ll w,int n)// prime factor check
{
    for(ll i=2; i*i<=w; ++i)
    {
        if(w%i==0)
        {
            update(i,n);
            while(w%i==0) w/=i;
        }
    }
    if(w > 1){
        update(w,n);
    }
}
int main()
{
    long beg=clock();
    int n;
    srand(time(NULL));
    scanf("%d",&n);
    best=0;
    for(int i=1; i<=n; ++i)
    {
        scanf("%lld",a+i);
        if(a[i]&1) best++;
    }
    table[2ll]=1;
    mt19937   rd(rand());
    while(clock()-beg <=2200)
    {
        unsigned  id=(unsigned)rd()%n+1;
        solve(a[id],n);
        solve(a[id]-1,n);
        solve(a[id]+1,n);
    }

    printf("%lld\n",best);
    return 0;
}

```




## 1284D. New Year and Conference(思路)


##### 比赛链接：[传送门](https://codeforces.com/problemset/problem/1284/D)



总结：

如何快速的判断一个区间集合是否都与某区间Q相交？

如果区间集合内存在一个区间A不与区间Q相交，那么一定满足区间A的右端点 小于 区间Q的左端点，或区间A的左端点 大于 区间Q的右端点，所以我们只需维护区间集合内 右端点最小的位置sp 和 左端点最大的位置ep，如果满足ep > Q.r 或sp < Q.l ，证明区间集合内存在某区间不与区间Q相交。

证明：一个区间集合是否都与某区间Q相交的充分必要条件是…(代指上面的一短句子)

充分性：区间集合都与区间Q相交，那么集合内所有区间的右端点 $x\ge l$，左端点$x \le r$，故右端点的最小值$sp \ge l$，左端点的最大值$ep \le r$.

必要性：显然


##### 思路：


对于敏感集合，一定能归结到一对区间敏感。

证明：敏感集合内一定对于某个地点内所有区间都不相交，另一个地点所有区存在相交，那么我们只需找出那一对相交的区间即为敏感的一堆区间。

我们可以遍历所有相交的区间，那么如何遍历呢？我们对于时间点x，维护一个集合S，这个集合内存储满足地点A的时间区间包含时间点x 的**地点B的时间区间**。即如果$a\le x\le b$，那么集合S内存储$(c,d)$。这个集合S很容易维护到，我们可以对于每个event，将事件$(a,b,c,d)$ 变成在时间点 $a$ 加入 $(c,d)$，时间点 $b+1$ 删除 $(c,d)$ 即可。

那么此时集合S内都是在事件点 $x$ 相交的地点B的区间，如果集合S中存在两个区间不相交，那么存在敏感的区间。在维护的过程中，我们只需判断新加入的区间是否与集合S的区间都相交即可。如何判断呢？

我们另需维护集合S中左端点的最大值ep和右端点的最小值sp，如果新加入的区间Q与集合S内某个区间不相交，那么一定有ep > Q.r 或sp < Q.l 。


退役后长时间不刷题思路退化了QAQ。


##### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=3e5+10;
multiset<P> table;
multiset<int> mxtable,mitable;
struct node
{
    int x,l,r,flag;
    node() {}
    node(int x,int l,int r,int flag):x(x),l(l),r(r),flag(flag) {}
    bool operator < ( const node &o)
    {
        if(x!=o.x)
            return x < o.x;
        return flag < o.flag;
    }
} t[N];
int data[N][4];
/*
按照端点排序
for端点，从而进行add和del maintain Set
*/
void addme(int l,int r)
{
    table.insert(make_pair(l,r));
    mxtable.insert(l);
    mitable.insert(r);
}
void delme(int l,int r)
{
    auto it=table.find(make_pair(l,r));
    table.erase(it);
    mxtable.erase(mxtable.find(l));
    mitable.erase(mitable.find(r));

}
bool work(int n,int tol)
{
    table.clear();
    mxtable.clear();
    mitable.clear();
    mxtable.insert(-1);
    mitable.insert(inf);
    for(int i=0; i<tol; ++i)
    {
        int mx=(*mxtable.rbegin()),mi=*mitable.begin();
        if(t[i].flag==1)
        {
            if(mx > t[i].r||mi < t[i].l)
                return false;
            else
                addme(t[i].l,t[i].r);
        }
        else
            delme(t[i].l,t[i].r);
    }
    return true;
}
int main()
{
    int n;
    bool isok=true;
    scanf("%d",&n);
    for(int i=1; i<=n; ++i)
    {
        for(int k=0; k<4; ++k) scanf("%d",&data[i][k]);
    }
    int tol=0;
    for(int i=1; i<=n; ++i)
    {
        int a=data[i][0],b=data[i][1],c=data[i][2],d=data[i][3];
        t[tol++]=node(a,c,d,1);
        t[tol++]=node(b+1,c,d,-1);
    }
    sort(t,t+tol);
    isok=work(n,tol);
    if(isok)
    {
        tol=0;
        for(int i=1; i<=n; ++i)
        {
            int a=data[i][0],b=data[i][1],c=data[i][2],d=data[i][3];
            t[tol++]=node(c,a,b,1);
            t[tol++]=node(d+1,a,b,-1);
        }
        sort(t,t+tol);
        isok=work(n,tol);
    }
    printf("%s\n",isok?"Yes":"No");
    return 0;
}

```




## codeforces 1253 E. Antenna Coverage（DP）


##### 题意：


现有一个一维的OX轴，给出n个antenna，每个antenna的属性有$( x i , r i ) (x_i,r_i)$,代表该antenna 可以覆盖区间$[ x i − r i , x i + r i ] [x_i-r_i,x_i+r_i]$，我们可以花费一个硬币使得某个antenna的 $r r$ 增大1，问使区间$[ 1 , m ] [1,m]$都被某个antenna覆盖所需最小花费。$n ∈ [ 1 , 80 ] , m ∈ [ 1 , 2 e 5 ] , x i ∈ [ 1 , m ] n\in[1,80],m\in[1,2e5],x_i\in [1,m]$,

##### 思路：


因为所有antenna的中心都在$[ 1 , m ] [1,m]$，所以我们在位置0处放一个半径为0的antenna答案不收影响，（因为位置0处的antenna覆盖到位置x，那么x+1位置必定被覆盖了，所以x+1位置必定能花费同样的硬币进行扩展到左边的位置1，我们覆盖位置$[ 1 , x ] [1,x]$所需要的花费不会比之前坏）。我们用$d p [ p o s ] dp[pos]$代表假设位置$p o$



## 2018 CCPC Final B - Balance of the Force


##### 题目链接：[传送门](https://codeforces.com/gym/102055/status)


##### 题意：


给定 $N$个人，每个人可以选择加入黑暗 DarkDark 或者光明 LightLight 两种阵营，他们加入不同的阵营之后获得的力量值是不同的，即 $D_i$ 和 $L_i$ 。然后有些人之间有矛盾，是不能加入同一阵营的，矛盾的对数共有 MM 对，现在给出所有的矛盾和所有的 $L_i,D_i$，问在所有可能存在的最终阵营分配情况中，力量值最大的人和力量值最小的人之间的差**最小**可能是多少？如果说不可能分配的话输出IMPOSSIBLE。其中 $1\le N\le 2*10^5,,0\le M\le 2*10^5,,1\le L_i D_i \le 10^9$ ,共20组test，时限4S

##### 思路：


因为每个联通块内对立的状态已经给出，首先很容易想到对每个联通块进行二分图染色，如果存在奇环就impossible，否则我们对二分图赋予状态（染色0的赋予状态L和染色0的赋予状态D），每种状态会产生一个最大值和最小值。

如果没有奇环，那么现在问题就转化为有k堆物品，每堆物品有要么取(maxx1,minn1)或(maxx2,minn2)，现在要求如何对每堆物品赋予状态使得k堆物品中maxx的最大值减去minn的最小值的差最小。

##### **这个问题与另一个问题相似**：


**n个物品，每个物品价值要么取$a_i$,要么取$b_i$ ，你对这n个物品赋值，求这n堆物品中的最大值减最小值最大为多少**。

这个问题的做法：我们首先称$a_i$和$b_i$是孪生的，即同一种类，但不可同时取。然后我们把所有$a_i$和 $b_i$ 从小到大排序，然后依次枚举最大值，然后用数据结构维护当前所有前面所有值的集合，更新答案。

我们从小到大遍历价值：

+ 首先把该值插入到数据结构中+ 如果至此出现种类数不够n的话，就不更新答案，然后进行下面操作。 
  
+ 如果该物品的孪生物品出现过的话，对孪生物品进行选择,因为现在只有最小值才能影响答案，从数据结构中删除孪生物品中最小的那个，只留下大的那个.+ 否则什么也不做
 + 如果至此出现种类数够n的话，更新答案 
  
+ 如果孪生物品在前面出现过，那么先将孪生物品从数据结构中删除，然后更新答案（该值减去数据结构中的最小值），然后再将孪生物品插入进数据结构+ 然后对孪生物品进行选择，从数据结构中删除孪生物品中最小的那个，只留下大的那个。
 


我们现在回到这个题，这个题跟上面基本一样，枚举最大值，更新答案，当出现孪生的话，我们选择最小值大的那个。

+ 按照maxx值从小到大排序，然后用数据结构维护至此出现的minn+ 每遍历到一个物品就加入minn，如果出现孪生物品就选择minn较大的那个（因为之后的maxx，只有minn会影响答案）


代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> P;
const int N=2e5+10;
const int inf=0x3f3f3f3f;
vector<int> g[N];
int prices[N][2],color[N];
vector<int> seq;
struct State
{
    int maxx,minn,id;
    State() {}
    State(int maxx,int minn,int id):maxx(maxx),minn(minn),id(id) {}
    bool operator < (const State &o) const
    {
        return maxx<o.maxx;
    }
};
vector<State> t;
bool dfs(int u,int c)
{
    seq.push_back(u);
    color[u]=c;
    for(int v:g[u])
    {
        if(color[v]==-1)
        {
            if(!dfs(v,c^1))
                return false;
        }
        else
        {
            if(color[v]==c)
                return false;
        }
    }
    return true;
}
int lastpos[N];//lastpos[id], 种类id出现的数组下标pos
void set_delete(multiset<int> & mst,int v)
{
    auto it=mst.find(v);
    mst.erase(it);
}
void work(int n,int cas)//n种物品,每种物品两个状态，每个状态属性(maxx,minn)
{
    int cnt=0;
    fill(lastpos,lastpos+n+1,-1);
    multiset<int> mst;
    int ans=inf;
    for(int i=0; i<int(t.size()); ++i)
    {
        int tmaxx=t[i].maxx,tminn=t[i].minn,tid=t[i].id;
        mst.insert(tminn);
        if(lastpos[tid]==-1)
        {
            cnt++;//孪生没有出现
            lastpos[tid]=i;
            if(cnt==n)
            {
                ans=min(ans,tmaxx-*mst.begin());
            }
        }
        else //孪生出现了
        {
            if(cnt==n)
            {
                set_delete(mst,t[lastpos[tid]].minn);
                ans=min(ans,tmaxx-*mst.begin());
                mst.insert(t[lastpos[tid]].minn);
            }
            set_delete(mst,min(t[lastpos[tid]].minn,tminn));
        }
    }
    printf("Case %d: %d\n",cas,ans);
}
int main()
{
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=1; i<=n; ++i)  g[i].clear();
        for(int i=1; i<=m; ++i)
        {
            int u,v;
            scanf("%d%d",&u,&v);
            g[u].push_back(v);
            g[v].push_back(u);
        }
        for(int i=1; i<=n; ++i)
            scanf("%d%d",&prices[i][0],&prices[i][1]);
        fill(color,color+n+1,-1);
        int kinds=0;
        bool isok=true;
        t.clear();
        for(int i=1; i<=n; ++i)
        {
            if(color[i]==-1)
            {
                seq.clear();
                kinds++;
                isok=dfs(i,0);
                if(!isok) break;
                int minn=inf,maxx=-1;
                for(int sign=0; sign<=1; ++sign)
                {
                    minn=inf,maxx=-1;
                    for(int a:seq)
                    {
                        if(color[a]==sign)
                        {
                            minn=min(minn,prices[a][0]);
                            maxx=max(maxx,prices[a][0]);
                        }
                        else
                        {
                            minn=min(minn,prices[a][1]);
                            maxx=max(maxx,prices[a][1]);
                        }
                    }
                    t.push_back(State(maxx,minn,kinds));
                }
            }
        }
        if(!isok)
        {
            printf("Case %d: IMPOSSIBLE\n",++cas);
            continue;
        }
        sort(t.begin(),t.end());
        work(kinds,++cas);
    }
}
```




## 1223D. Sequence Sorting(DP)


##### 题目链接：[传送门](https://codeforces.com/problemset/problem/1223/D)


##### 思路：


​ 我们假设序列$D=\{d_1,d_2,d_3...d_k\}$，序列$M=\{x|x= a_i\&\&x\notin D,i\in[1,n]\}$。

即序列D是没有移动的数，序列M是向左移动或向右移动的数，我们设$maxpos[x]​$ 和 $minpos[x]​$ 分别是数 $x​$ 在序列 $a​$ 中出现的最大位置下标和最小位置下标。那么序列D和序列M必定满足下列条件

+ 对于$D_i,D_j$，假设$D_i<D_j$，那么$minpos[D_j]>maxpos[D_i]$。（原因：这样序列才能有序且不移动）+ 对于序列M中的任意一个数，满足$M_i​$ 不夹在序列D的最大和最小值之间，即$M_i>max\{x|x\in D\}​$或$M_i<min\{x|x\in D\}​$成立，即数列D中相邻的两个元素在排序上也是相邻的（原因：因为序列M中的数字向左或向右移动，那么其必定移动到序列D的两侧，又因为最终序列是有序的，则满足上述条件）


因为序列M的长度加序列D的长度之和为元素的种类数，我们现在只需求出序列D最长为多长即可。

我们用$DP[i]$表示序列D中最后一个数是排名为 $i$ 的数的最大长度，

+ 如果$i=1,than~dp[i]=1​$，排名为 $i​$ 的最小出现位置小于排名为 $i-1​$的最大出现位置，$than~~dp[i]=1​$+ 否则 $dp[i]=dp[i-1]+1​$


代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int N=3e5+10;
int minp[N],maxp[N];
vector<int> v;
int dp[N];
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;++i)
            minp[i]=-1;
        v.clear();
        for(int i=1;i<=n;++i)
        {
            int x;
            scanf("%d",&x);
            v.push_back(x);
            if(minp[x]==-1) minp[x]=i;
            maxp[x]=i;
        }
        sort(v.begin(),v.end());
        v.erase(unique(v.begin(),v.end()),v.end());
        int ans=n;
        for(int i=0;i<int(v.size());++i)
        {
            if(i==0||minp[v[i]]<maxp[v[i-1]]) dp[i]=1;
            else dp[i]=dp[i-1]+1;
            ans=min(ans,int(v.size())-dp[i]);
        }
        printf("%d\n",ans);
    }
//    for()
    return 0;
}
```




## 1169E. And Reachability(DP+思路)


题目链接：[传送门](https://codeforces.com/contest/1169/problem/E)

思路：

涉及到位运算，很容易想到按位考虑。

我们用$g o [ i ] [ j ] go[i][j]$表示第 $i i$ 个数可以到达第 $j j$ 位为1的最小下标是多少，如果没有则等于$n + 1 n+1$。

对于这个状态方程，我们倒过来递推，我们让 $i i$ 从 $n n$ 开始遍历到 $1 1$ ,并用$l a s t [ k ] last[k]$ 表示满足 $j > i j>i$ 且 $a j a_j$ 的第 $k k$



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




## 980E. The Number Games（倍增，思维）


##### 题目链接：[传送门](https://codeforces.com/problemset/problem/980/E)


##### 思路：


​ 我们转化为，从一颗树上选n-k个点，使得贡献最大，且这n-k个点两两连通。贪心的取，我们必定先取大的（因为如果可以取大的但不取必亏）。

​ 我们可以将原图变为以n为根的有根树，首先n号点必选，我们接下来探讨下面选点，我们建立倍增数组，$fa[u][i]$代表u的第$2^i$个祖先的编号，我们看编号为$n-1$的点。

如果编号为$n-1$到编号为 $n$ 的点的数量小于剩下可选的点的数量，那就不能选。

否则，我们选$n-1$号点，为了连通性， $n-1$号点到$n$号点之间的点都要选。

我们将选的点进行标记。

所以我们有一个算法：

先选编号为n的点，然后遍历剩下编号为的点（从大到小），假设此时编号为$i$，如果编号为$i$的点已经被选，则跳过，否则倍增找祖先没有被标记的最小的近的祖先，（为什么是祖先呢？，因为被标记的不可能是 i 的儿子，否则他就被选了）那么找最近被标记的点就可以用倍增。

如果之间点的数量小于可选的点的数量，就不选。否则就选，并选其之间的点。

```cpp
#include<bits/stdc++.h>
#define mse(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=1e6+10;
vector<int> g[N];
int book[N];
int fa[N][20];
void bfs(int root)
{
    queue<int> qe;
    qe.push(root);
    fa[root][0]=root;
    while(!qe.empty())
    {
        int u=qe.front();qe.pop();
        for(int i=1;i<20;++i) fa[u][i]=fa[fa[u][i-1]][i-1];
        for(int v:g[u])
        {
            if(v==fa[u][0]) continue;
            fa[v][0]=u;
            qe.push(v);
        }
    }
}
int mincost(int v)
{
    int ans=0;
    if(book[fa[v][0]]) return 1;
    int wv=v;
    for(int i=19;i>=0;--i)
    {
        if(book[fa[wv][i]]) continue;
        ans+=1<<i;
        wv=fa[wv][i];
    }
    return ans+1;
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    cout.tie(0);
    int n,k;
    cin>>n>>k;
    for(int i = 1; i < n; ++i)
    {
        int u,v;
        cin>>u>>v;;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    k=n-k-1;
    bfs(n);
    book[n]=1;
    for(int i=n-1;i>=1&&k;--i)
    {
        if(book[i]) continue;
        int m=mincost(i);
        if(m<=k)
        {
            k-=m;
            int wv=i;
            while(!book[wv]){
                book[wv]=1;
                wv=fa[wv][0];
            }
        }
    }
    for(int i=1;i<=n;++i)
    {
        if(!book[i])
            cout<<i<<" ";
    }
    cout<<endl;
    return 0;
}
```




## 955C. Sad powers(思维)


##### 题目链接：[传送门](https://codeforces.com/contest/955/problem/C)


思路：对于1到n的满足$a b = x a^b=x$的数$x x$（幂次$b b$>1）。

我们可以将之分为两种，一种是$b = 2 b=2$，另一种$b > 2 b>2$且不是完全平方数的个数。

对于第一种情况($b = = 2 b==2$)，即我们计算完全平方数的个数，这部我们可以二分$O ( l o g n ) O(logn)$

对于第二种情况($b > 2 b>2$)，因为$b = 3 b=3$时这样数最多只有$1 0 18 / 3 = 1 0 6 10^{18/3}=10^6$种，$b > 3 b>3$的则更少，所以这种情况的数我们可以暴力预处理。

但是第二种情况可能有重复计算，我们去重即可。但是第一种情况和第二种情况可能也有重复计算，我们再筛去第二种情况的完全平方数。

这样我们计算$f ( n ) f(n)$即小于等于$n n$，满足



## codeforce.999E Reachability from the Capita(dfs+强连通分量)


##### 比赛链接：[传送门](https://codeforces.com/problemset/problem/999/E)


##### 题意：


​ 给出一个有向图，n个顶点，m条边，现在给出一个源点S，问最少添加多少条有向边才能使顶点S可以到达其他所有顶点。

##### 思路：


​ 我们dfs出刚开始dfs可以到达的所有顶点，然后对于剩下的顶点，我们将剩下顶点构建成的图强连通分量缩点( 对有环的情况处理)，然后形成一个拓扑图，我们只有计算处缩点后度数为0的点的个数即可（让S连接度数为0的点即可）

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=1e5+10;
vector<int> g[N];
vector<int> tg[N];
int book[N];
void dfs(int u)
{
    book[u]=true;
    for(int v:g[u]){
        if(!book[v]) dfs(v);
    }
}
int dfn[N],S[N],top,low[N],ins[N],tol;
int color[N],cgt;
void tarjin(int u)
{
    dfn[u]=low[u]=++tol;
    S[top++]=u;
    ins[u]=1;
    for(int i=0;i<g[u].size();++i)
    {
        int v=g[u][i];
        if(book[v]) continue;
        if(!dfn[v])
        {
            tarjin(v);
            low[u]=min(low[u],low[v]);
        }
        else if(ins[v]){
            low[u]=min(low[u],dfn[v]);
        }
    }
    if(low[u]==dfn[u])
    {
        int v;
        ++cgt;
        do{
            v=S[top-1];
            top--;
            ins[v]=0;
            color[v]=cgt;
        }
        while(v!=u);
    }
}
void getall(int n)
{
    fill(dfn,dfn+1+n,0);
    fill(ins,ins+1+n,0);
    tol=cgt=top=0;
    for(int i=1;i<=n;++i){
        if(book[i]) continue;
        if(!dfn[i]) tarjin(i);
    }
}
int ind[N];
int main()
{
    int n,m,s;
    scanf("%d%d%d",&n,&m,&s);
    for(int i=1;i<=m;++i)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        g[a].push_back(b);
    }
    dfs(s);
    getall(n);
    fill(ind,ind+cgt+1,0);
    for(int u=1;u<=n;++u){
        for(int v:g[u]){
            if(book[u]||book[v]) continue;
            int a=color[u],b=color[v];
            if(a!=b)
                ind[b]++;
        }
    }
    int ans=0;
    for(int i=1;i<=cgt;++i)
        if(ind[i]==0) ans++;
    printf("%d\n",ans);
    return 0;
}

```




## codeforces1236D.Alice and the Doll(贪心模拟)


**题目链接**：[传送门](https://codeforces.com/contest/1236/problem/D)

思路：

题意感觉描述的有点模糊（至此我还不太清楚是每个格子只能进行走一次，还是走多次，但是走一次的话代码就能A，如果走多次的话下面出的样例也能hack出代码的错误，但目前来看应该每个格子只能走一次，且只能左转一次）

因为每个格子只能走一起，且只能右转一次，所以我们前进的时候要尽可能多的走，从当前位置计算直线走到哪个位置可以用二分O(logn)求出位置。（蛇皮走位


3 5 5

1 4

1 5

3 3

3 4

3 5

No


```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=1e5+10;
/*
模拟蛇皮走位
不能走：
1.转弯后还是原位置不能动
*/
int n,m,k;
vector<int> row[N],col[N];
void work(int x,int y,int d)//
{
    //朝该方向走,走不动停止
    //0 1 2 3
    long long sum=1;
    int r1=0,r2=n+1,c1=0,c2=m+1;
    while(true)
    {
        if(d==0)
        {
            auto it=upper_bound(row[x].begin(),row[x].end(),y);
            int yy=*it-1;
            yy=min(yy,c2-1);
            if(yy==y) break;
            sum+=yy-y;
            y=yy;
            r1=x;
            d=1;
        }
        if(d==1)
        {
            auto it=upper_bound(col[y].begin(),col[y].end(),x);
            int xx=*it-1;
            xx=min(xx,r2-1);
            if(xx==x) break;
            sum+=xx-x;
            x=xx;
            c2=y;
            d=2;
        }
        if(d==2)
        {
            auto it=upper_bound(row[x].begin(),row[x].end(),y);
            int yy=*(--it)+1;
            yy=max(yy,c1+1);
            if(yy==y)
                break;
            sum+=y-yy;
            y=yy;
            r2=x;
            d=3;
        }
        if(d==3)
        {
            auto it=upper_bound(col[y].begin(),col[y].end(),x);
            int xx=*(--it)+1;
            xx=max(xx,r1+1);
            if(xx==x)
                break;
            sum+=x-xx;
            x=xx;
            c1=y;
            d=0;
        }
    }
    long long en=1ll*n*m-1ll*k;
    if(sum==en)
        puts("Yes");
    else
        puts("No");
}
int main()
{
    scanf("%d%d%d",&n,&m,&k);
    int flag=0;
    for(int i=1;i<=k;++i)
    {
        int x,y;
        if(x==1&&y==2) flag=1;
        scanf("%d%d",&x,&y);
        row[x].push_back(y);
        col[y].push_back(x);
    }
    for(int i=1;i<=n;++i)
    {
        row[i].push_back(0);
        row[i].push_back(m+1);
    }
    for(int i=1;i<=m;++i)
    {
        col[i].push_back(0);
        col[i].push_back(n+1);
    }
    for(int i=1;i<=n;++i)
        sort(row[i].begin(),row[i].end());
    for(int i=1;i<=m;++i)
        sort(col[i].begin(),col[i].end());
    int d=0;
    if(m==1||flag)
        d=1;
    work(1,1,d);
    return 0;
}

```




## codeforces 1214E.Petya and Construction Set（构造）


#### 题目链接：[传送门](https://codeforces.com/contest/1214/problem/E)


#### 题意：


    现在有$2*n$个顶点，并且给一个长度为$n$的数组$d[]$，让我们构建一颗树，满足树上顶点$2*i-1$与顶点$2*i$之间的距离为$d[i]$。对于结果输出$2*n-1$条边。

#### 思路：



构造题，头脑风暴瞎想吧。


    其实我题目要求的就是构造出$2*n$个节点的树满足有不同的n对顶点之间的距离分别为$d[i]$。我们可以假设$d[]$中元素是非递增的（这可以通过排序后的顶点变换得到）。

    初始时有n个节点线性连接在一起：1-3-5…-2*n-1，并且d[1]>=d[2]>=d[3]。

    对于第 i 个节点，我们寻找对应的顶点 i+1所连接的节点，那么第i+d[i]-1个节点是可行的。如果他连接的是序列最后一个节点，那么就让该节点添加到序列结尾即可。（因为d[]是不递增的，所以总是有节点连接。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=1e5+20;
int V[2*N];
P seq[N];//d,id
vector<P> E;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n;
    cin>>n;
    for(int i=1;i<=n;++i)
    {
        int d;
        cin>>d;
        seq[i].first=d;
        seq[i].second=i;
    }
    sort(seq+1,seq+n+1,greater<P>());
    for(int i=1;i<=n;++i){
        V[i]=2*seq[i].second-1;
        if(i!=1) E.push_back({V[i],V[i-1]});
    }
    int top=n;
    for(int i=1;i<=n;++i)
    {
        int d=seq[i].first;
        E.push_back({V[i]+1,V[i+d-1]});
        if(i+d-1==top)
            V[++top]=V[i]+1;
    }
    for(P e:E)
        cout<<e.first<<" "<<e.second<<endl;
    return 0;
}

```




## codeforces 1207F. Remainder Problem(平方启发)


#### 题目链接：[传送门](https://codeforces.com/contest/1207/problem/F)


#### 题意：


现在有一个大小为500000的数组，初始每个元素都为0，索引从1开始，现有两个操作：

1 x y–代表将索引为x的元素值加y

2 x y–代表求数组中所有索引满足**取余x等于y**的的元素值和。

#### 思路：


对于每个查询如果采用暴力的方式话时间复杂度为$O(N/x)$，其中N为数组大小。这对x较大的时候可以使用这种方法。

对于 $x$ 较小时，假设 $x\le K$，那么查询有$K^2$种，假如我们维护每组查询的结果，那么对于每次1操作，我们需要$O(K)$维护较小的$x\le K$的查询。

我们让$K$取$sqrt(N)$，那么总的时间复杂度为$O(N*sqrt(N))$

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int a[750][750],b[500005];//<=720处理,>720暴力
int main()
{
    int q;
    scanf("%d",&q);
    while(q--)
    {
        int cmd,x,y;
        scanf("%d%d%d",&cmd,&x,&y);
        if(cmd==1)
        {
            b[x]+=y;
            for(int i=1;i<=720;++i)
                a[i][x%i]+=y;
        }
        else{
            if(x<=720){
                printf("%d\n",a[x][y]);
            }
            else{
                int ans=0;
                for(int k=0;k*x+y<=500000;++k){
                    ans+=b[k*x+y];
                }
                printf("%d\n",ans);
            }
        }
    }
    return 0;
}

```




#### 题目链接：[ Let Them Slide](https://codeforces.com/contest/1208/problem/E)


#### 题意：


现有n行w列的墙,每行有一排连续方块，一排方块可以左右连续滑动，且每个方块都有一个价值，第i 列的价值定义为这列的方块的价值和。求1到w列中每列的最大价值。注：如果一个位置没有方块，那么这个位置的价值为0

#### 思路：



我一直没想到可以这样实现，颠覆了我当时混乱的思想。


     对于第 $i$ 行的第 $j$ 个方块，如果这排方块的总长度为$cnt$，那么可以算出来该方块可以移动到$[j,w+j-cnt]$区间列，对于每一列（假设为 j ）我们可以使用两个vector分别记录第$j​$ 列添加的元素(行，值)，开始移除的元素(行,值)。

     那么我们就可以动态更新第 j 列每行的待选元素。 我们使用一个multiset[i]来表示当前列中第 $i$ 行待选的值，假设前面的已经维护好了，我们从第j列到第j+1列的时候，只需要对**j+1列中移除对应元素(行，值)**后更新对应的行对该列的贡献，第 **j+1列中添加对应元素(行，值)**后更新改行对该列的贡献即可，其他没有影响到的行还是上列的值。

#### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=1e6+20;
vector<P> add[N],rve[N];//row,val
multiset<int> nrow[N];
long long ans[N];
int main()
{
    int n,w;
    scanf("%d%d",&n,&w);
    for(int i=1; i<=n; ++i)
    {
        int cnt;
        scanf("%d",&cnt);
        for(int j=1; j<=cnt; ++j)
        {
            //[j,w+j-cnt]
            int x;
            scanf("%d",&x);
            add[j].push_back({i,x});
            rve[w+j-cnt+1].push_back({i,x});
        }
        if(cnt<w)
        {
            add[1].push_back({i,0});
            rve[w-cnt+1].push_back({i,0});
            add[cnt+1].push_back({i,0});
            rve[w+1].push_back({i,0});
        }
    }
    for(int i=1; i<=w; ++i) //第i列
    {
        for(P p:rve[i])
        {
            int id=p.first,v=p.second;
            ans[i]-=*nrow[id].rbegin();
            nrow[id].erase(nrow[id].find(v));
            ans[i]+=(nrow[id].empty()?0:*nrow[id].rbegin());
        }
        for(P p:add[i])
        {
            int id=p.first,v=p.second;
            ans[i]-=(nrow[id].empty()?0:*nrow[id].rbegin());
            nrow[id].insert(v);
            ans[i]+=(*nrow[id].rbegin());
        }
        if(i<w)
            ans[i+1]=ans[i];
    }
    for(int i=1; i<=w; ++i)
        printf("%lld ",ans[i]);
    return 0;
}

```




## codeforec 1208C Magic Grid（构造题）


题目链接：[传送门](https://codeforces.com/problemset/problem/1208/C)

**题意：**

​ 给你一个n，满足n是4的倍数。让你构造一个$n ∗ n n*n$的矩阵，满足该矩阵的元素分别为$0 0$ 到$n ∗ n − 1 n*n-1$。且不重复。还要满足矩阵每一行每一列元素的异或值都相同

**思路：**

​ 这两天发现了异或的另一个性质：



Codeforces Round #525 (Div. 2) D. Ehab and another another xor problem

链接：[https://codeforces.com/contest/1088/problem/D](https://codeforces.com/contest/1088/problem/D)

题意：


让你猜两个整数a b的值是多少。

你可以给出最多62次提问，

其中0<=a,b<230(也就是说二进制位最多30位)



提问方法就是你给他两个数c，d他会返回 1或-1或0

+ **1 if a⊕c>b⊕d**+ **0 if a⊕c=b⊕d**+ **-1 if a⊕c<b⊕d**



交互题


首先异或的性质

针对每个二进制位

1.与0异或之后 结果为本身

2.与1异或之后 相当于取反

3.自身与自身异或为0


如果正在判断从高位到低位的第k位,进行两次猜测，第一次将c d**第k位** 置为1 0异或后比较，第二次c,d**第k位**置为0 1异或后进行比较（c，d第k位前面的全置为对应a b已经确定过了，第k位后面的置为0）

a b此时的位有四种情况

a b

1 1 返回值分别为 -1 1

0 0 返回值分别为1 -1

1 0 返回值相同 由剩下的位确定

0 1 返回值相同 由剩下的位确定

由此可见

+  如果两个数对应的位相同就可以猜测两次确定出来 +  如果两个数对应的位不同 ，我们需要计算a，b的大小才能确定答案。


那么我们可以先开始的时候确定都异或0 0 判断ab的大小，如果出现位不同的，就可以根据ab的大小来确定位是多少，然后在根据当前返回值来确定剩下的位的大小关系。如果位相同就可以直接判断位是多少。每次分别异或1 0，异或0 1 结合上面判断就可确定30位的值，总共需要提问61次
 


```cpp
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<map>
#include<vector>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e3+10;
const int branch=26;
const int inf=0x3f3f3f3f;
int ask(int c,int d)
{
    printf("? %d %d\n",c,d);
    fflush(stdout);
    int ans;
    scanf("%d",&ans);
    return ans;
}
int main()
{
    int a,b;
    int aIsBiger=1;
    a=0,b=0;
    aIsBiger=ask(0,0);
    for(int i=29;~i;--i)
    {
            int x=ask(a|1<<i,b);//第i位为 1 0
            int y=ask(a,b|1<<i);//第i位为 0 1
            if(x==-1&&y==1)//同为1
            {
                if(x==-1)// 1 -1
                {
                    a|=1<<i;
                    b|=1<<i;
                }
            }
            else if(x==y)
            {
                if(aIsBiger==1)
                    a|=1<<i;
                else
                    b|=1<<i;
                aIsBiger=(x==1);
            }
    }
    printf("! %d %d\n",a,b);
    return 0;
}
```




##[CodeForces - 949B ](https://vjudge.net/problem/1412027/origin)

题意：现在给你一个n，表示有2*n-1个方格，第奇数方格上会有一个数字 1-n按顺序放。第偶数个方格上是没有数字的。变动规则是排在最后一个位置的数字，移动到它前边最近的空位 。 直到数字之间没有空位。最终的数列是由n已经确定的。给你q，表示q次查询，每次查询输入一个x，问数列第x位上的数字是多少？ .
![./figures/01fef3d910f5d625885b73d8d9765452](./figures/01fef3d910f5d625885b73d8d9765452)


**Input**

The first line contains two integers *n* and *q* (1 ≤ *n* ≤ 1018, 1 ≤ *q* ≤ 200 000), the number of elements in the array and the number of queries for which it is needed to find the answer.

Next *q* lines contain integers *x**i* (1 ≤ *x**i* ≤ *n*), the indices of cells for which it is necessary to output their content after Dima’s algorithm finishes.

**Output**

For each of *q* queries output one integer number, the value that will appear in the corresponding array cell after Dima’s algorithm finishes.

**Examples**

**Input**

```bash
4 3
2
3
4
```


**Output**

```bash
3
2
4
```


**Input**

```bash
13 4
10
5
4
8
```


**Output**

```bash
13
3
8
9
```


**Note**

The first example is shown in the picture.

当n=13时，数列为[1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10, 7].

### 题意：


中文的我想大家都看得懂

### 分析:


假设现在询问的位置是$x,且（1&lt;=x&lt;=n）$


奇数位置的值一定能立马确定为$(x+1)/2$，因为奇数位置刚开始都有值且确定，往前移动只能移动到偶数位置上


+  如果$x$是奇数 $val=(x+1)/2​$ +  $x$是偶数 $假设最后x数的位置的数为val，那么我们回到val刚放到x这个位置的状态，此时位置x之前的偶数位置一定是空的$,$即位置x前面有x/2个数，又因为val刚放到x这个位置，故x后面的数一定是连续的数共有n-x/2-1个$, $那么val放到位置x之前一定在位置x+(n-x/2-1)+1的位置上$，$如果此时x是奇数，则val=(x+1)/2,否则重复x为偶数的状态$，$直到x为奇数即可​$ 


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
const int maxn=1e3+100;
const int branch=26;
const int inf=0x7fffffff;
int main()
{
    ll n,q,x;
    ios::sync_with_stdio(false);/*这语句加速cin输入，去了也没关系*/
    cin>>n>>q;
    while(q--)
    {
        cin>>x;
        while(x%2==0)
        {
            x=n+x/2;
        }
        cout<<(x+1)/2<<endl;
    }
    return 0;
}
```




### A. Game 23


思路：

深搜即可

```
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
typedef long long ll;
using namespace std;
const int maxn=120;
const int inf=0x3f3f3f3f;
ll m;
int dfs(ll val,int s)
{
    if(val==m)
        return s;
    if(val>m)
        return -1;
    int ans=dfs(val*2ll,s+1);
    if(ans!=-1)
        return ans;
    ans=dfs(val*3ll,s+1);
    return ans;
}
int main()
{
    ll n;
    cin>>n>>m;
    cout<<dfs(n,0);
    return 0;
}
```


B. Maximal Continuous Rest

思路：

把序列*2 ，找出最长连续1即可

```
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
typedef long long ll;
using namespace std;
const int maxn=4e5+100;
const int inf=0x3f3f3f3f;
int Tt[maxn];
int n;
int main()
{
    cin>>n;
    for(int i=0; i<n; ++i)
    {
        cin>>Tt[i];
        Tt[i+n]=Tt[i];
    }
    int ans=0,maxx=0;
    for(int i=0; i<2*n; ++i)
    {
        if(Tt[i]==0){
            ans=0;
            continue;
        }
        if(i==0||Tt[i]==Tt[i-1])
            ans++;
        else
            ans=1;
        maxx=max(maxx,ans);
    }
    cout<<maxx<<endl;
    return 0;
}
```


C. Polycarp Restores Permutation

思路：

将所有的$p i p_{i}$



## [Forethought Future Cup - Elimination Round](https://codeforces.com/contest/1146) C. Tree Diameter( 树的直径的性质)


### 题意：


```bash
		交互题，最多问9次，求一棵树的直径。每次给他两个不重复的顶点集合，后台返回这两个顶点集合的之间的最短距离
```


### 思路


​ 我们可以随便找一个顶点a，找出a顶点到的最远距离顶点假设为X，那么X必定为树的直径两端的一个顶点，然后求X到其他顶点的最大距离即为树的直径即可。

```cpp
#include<bits/stdc++.h>
using namespace std;
const int inf =0x3f3f3f3f;
int ask(int th,vector<int>& V)//第th个顶点  跟V顶点集合的询问
{
    printf("%d %d %d",1,V.size(),th);
    for(int i:V)
        printf(" %d",i);
    puts("");
    fflush(stdout);
    int ans;
    scanf("%d",&ans);
    return ans;
}
int main()
{
    int t,n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        vector<int> V;
        for(int i=2;i<=n;++i) V.push_back(i);
        int maxx=ask(1,V),l=2,r=n;
        V.clear();
        while(l!=r){
            int mid=(l+r)/2;
            for(int i=l;i<=mid;++i) V.push_back(i);
            int val=ask(1,V);
            if(val==maxx){
                r=mid;
            }
            else
                l=mid+1;
            V.clear();
        }
        int th=l;
        for(int i=1;i<=n;++i) if(i!=th) V.push_back(i);
        int ans=ask(th,V);
        printf("-1 %d\n",ans);
        fflush(stdout);
    }
}

```




### [Codeforces Round #552 (Div. 3)](https://codeforces.com/contest/1154) E Two Teams


#### 题意：


​ n个人排成一排，每个人都有一个iq，且iq不重复。现在给你一个k，且有两个教练编号为分别为1，2轮流进行以下操作

​ 该教练从排成的一行中找出iq最大的人加入自己的团队，且让iq最大的人左边的k个人和右边的k个人都加入自己的团队（如果人数不够k个，则只把剩余的加入即可）。

​ 现在问所有的人都被选出之后所处的团队编号。

#### 思路：


​ 我们需要维护两个信息

+ 一行人的编号的顺序，以及对应的iq.+ 此时所有人的iq最大的人的编号。


​ 我们第一个可以采用set容器实现；第二个使用map容器实现（也可以采用线段树维护），即让一个iq对应一个编号。

​ 那么每次删除中只要找到最大的iq对应的编号，然后在set容器中删除他左边和右边的信息，同时在map中删除对应的记录即可。 每次删除和查找的时间复杂度为logn，总体时间复杂度为nlogn 代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=2e5+20;
const int MAX=100000;
const int inf=0x3f3f3f3f;
set<int> seq;
map<int,int> maxIQ;//val id
int n,k;
int ansb[MAXN],iq[MAXN];
int delleft(int id,int sign)
{
    int tot=0;
    set<int>::iterator it=seq.find(id);
    if(it==seq.begin())
        return tot;
    it--;
    while(tot<k)
    {
        tot++;
        if(it==seq.begin())
        {
            int id=*it;
            ansb[id]=sign;
            seq.erase(it--);
            maxIQ.erase(iq[id]);
            return tot;
        }
        else{
            int id=*it;
            ansb[id]=sign;
            seq.erase(it--);
            maxIQ.erase(iq[id]);
        }
    }
    return tot;
}
int delright(int id,int sign)
{

    int tot=0;
    set<int>::iterator it=seq.find(id);
    it++;
    while(it!=seq.end()&&tot<k)
    {
        int nowid=*it;
        int nowiq=iq[nowid];
        ansb[nowid]=sign;
        seq.erase(it++);
        maxIQ.erase(nowiq);
        tot++;;
    }
    return tot;
}
int main()
{
    scanf("%d %d",&n,&k);
    for(int i=1; i<=n; ++i)
    {
        scanf("%d",iq+i);
        seq.insert(i);
        maxIQ[iq[i]]=i;
    }
    int sign=0;
    mset(ansb,-1);
    int tot=n;
    while(tot)
    {
        int maxid=(maxIQ.rbegin()->second);
        int maxiq=maxIQ.rbegin()->first;
        tot-=delleft(maxid,sign);
        tot-=delright(maxid,sign);
        ansb[maxid]=sign;
        seq.erase(maxid);
        maxIQ.erase(maxiq);
        tot--;
        sign^=1;
    }
    for(int i=1;i<=n;++i)
        printf("%d",ansb[i]+1);
    puts("");
    return 0;
}

```




## [1156B - Ugly Pairs](https://codeforces.com/contest/1156/problem/B) (贪心，构造算法)


### 解法：


​ 偶数位置的串在一起为a，奇数位置的串在一起为b，其中a和b串的内部是一定合法的。故只需检查a+b串合法，或者b+a是否合法即可。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
#define x first
#define y second
using namespace std;
typedef long long ll;
const double EPS=1e-10;
const int maxn=1e6+10;
bool check(string s)
{
    for(int i=1;i<s.length();++i){
        if(abs(s[i]-s[i-1])==1) return false;
    }
    return true;
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s,odd,even;
        cin>>s;
        for(auto i:s){
            if(i%2) odd+=i;
            else even+=i;
        }
        sort(odd.begin(),odd.end());
        sort(even.begin(),even.end());
        if(check(odd+even)){
            cout<<odd+even<<endl;
        }
        else if(check(even+odd)){
            cout<<even+odd<<endl;
        }
        else
            cout<<"No answer"<<endl;
    }
    return 0;
}
```




## [1156C - Match Points](https://codeforces.com/contest/1156/problem/C)（二分 贪心）


### 题意：


​ 给出一个整数n和一个整数z。代表下面有n个数，如果 $a b s ( a [ i ] − a [ j ] ) &gt; = z abs(a[i]-a[j])&gt;=z$



## [Codeforces Round #553 (Div. 2)](https://codeforces.com/contest/1151) ABCD题解


### A. Maxim and Biology


思路：暴力即可

```cpp
#include<bits/stdc++.h>
using namespace std;
const int inf=0x3f3f3f3f;
const int MAXN=1e5+10;
int MAX=1e5+1;
char cc[]="ACTG";
int getans(char c,char tc)
{
    return min((tc-c+26)%26,(c-tc+26)%26);
}
char s[1000];
int main(){
    int ans=inf;
    int ls;
    scanf("%d",&ls);
    scanf("%s",s);
    for(int i=0;i<ls-3;++i)
    {
        int mid=0;
        for(int k=0;k<4;++k)
        {
            mid+=getans(s[i+k],cc[k]);
        }
        ans=min(ans,mid);
    }
    cout<<ans<<endl;
    return 0;
}
```


### B. Dima and a Bad XOR


思路：

​ 首先如果存在一行有两个不同的数，那么就一定有解。证明：如果一行存在两个不同的的数.。现在我们从中随机选取一组，如果异或不等于0则这组就是解。否则该组异或为0，那么可以在那一行中换成另一个不同的数则异或一定不等于0。

正解：先选出每一行的第一个数，如果异或不等于0，则该组就是解。否则在一行中与选出第一个数不同的数来替换即可。如果没有则无解。

```cpp
#include<bits/stdc++.h>
using namespace std;
int mat[520][520];
int ans[520];
int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;++i)
        for(int j=1;j<=m;++j)
            scanf("%d",&mat[i][j]);
    int val=0;
    for(int i=1;i<=n;++i){
        ans[i]=1;
        val^=mat[i][1];
    }
    if(val==0)
    {
        for(int i=1;i<=n&&!val;++i){
            for(int j=2;j<=m;++j){
                if(mat[i][j]!=mat[i][1])
                {
                    val=1;
                    ans[i]=j;
                    break;
                }
            }
        }
    }
    if(val==0)
        puts("NIE");
    else{
        puts("TAK");
        for(int i=1;i<=n;++i)
            printf("%d%c",ans[i],i==n?'\n':' ');
    }
}
```


随机算法：每一行随机选一个位置。因为只要有一行有两个不同的数则有解，所以如果有解，那么只要随机一定次数一定会找到一个解。

```cpp
#include<bits/stdc++.h>
using namespace std;
int rd(int l,int r)
{
    int le=(r-l+1);
    return rand()%le+l;
}
int ans[520];
int mat[520][520];
int main(){
    srand(time(NULL));
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;++i)
        for(int j=1;j<=m;++j)
            scanf("%d",&mat[i][j]);
    int flag=1;
    int times=1000000/n;
    for(int i=0;i<times;++i)
    {
        int val=0;
        for(int k=1;k<=n;++k){
            ans[k]=rd(1,m);
            val^=mat[k][ans[k]];
        }
        if(val!=0){
            flag=0;
            break;
        }
    }
    if(flag)
        printf("NIE\n");
    else{
        printf("TAK\n");
        for(int i=1;i<=n;++i)
            printf("%d%c",ans[i],i==n?'\n':' ');
    }
    return 0;
}
```


### C. Problem for Nazar


思路：每次加的偶数和奇数都是连续的。且是以指数形式加的，那么我们可以暴力模拟加的过程，我们只需统计加这个过程有多少个连续偶数和奇数即可。 详情看代码

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
const ull mod=1e9+7;
ull fodd(ull n)
{
    return (n%mod)*(n%mod)%mod;
}
ull feven(ull n)
{
    return (n+1)%mod*(n%mod)%mod;
}
ull f(ull n)
{
    ull cntj=0,cnto=0,val=1,k=1;
    while(n){
        if(val>n){
            if(k&1)
                cntj+=n;
            else
                cnto+=n;
            n=0;
        }
        else{
            if(k&1)
                cntj+=val;
            else
                cnto+=val;
            n-=val;
        }
        val<<=1;
        k++;
    }
    cntj%=mod;cnto%=mod;
    return (fodd(cntj)+feven(cnto))%mod;
}
int main(){
    ull l,r;
    cin>>l>>r;
    cout<<(f(r)+mod-f(l-1))%mod<<endl;
    return 0;
}
```


### D. Stas and the Queue at the Buffet


思路：对于第i个数，每往后移动一次，即贡献增加$a-b$, 我们要想贡献最小，则差越大排的越靠前

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll inf=0x3f3f3f3f;
const ll MAXN=1e5+10;
struct Node
{
 ll a,b;
}node[100100];
bool cmp(Node aa,Node bb)
{
    return (aa.b-aa.a)<(bb.b-bb.a);
}
int main()
{
    ll n;
    scanf("%lld",&n);
    for(ll i=0;i<n;++i)
        scanf("%lld %lld",&node[i].a,&node[i].b);
    sort(node,node+n,cmp);
    ll ans=0;
    for(ll i=0,j=n-1;i<n;++i,--j)
    {
        ans+=node[i].a*i+j*node[i].b;
    }
    printf("%lld\n",ans);
    return 0;
}
```




## CodeForce [666C - Codeword](https://codeforces.com/contest/666/problem/C)(dp)


### 题意:


​ 求只含小写字母, 长度为n, 且可以与给定模板串匹配的字符串个数 (多组数据)

### 思路：


​ 很容易发现结果与字符串的内容没关系，所以我们用$f[i][j]$ 表示长度为 $i$ 的字符串扩展为长度为 $j$ 的字符串的个数，我们假设前者字符串为s，则$len(s)=i$ ,可以很简单的推出一个dp方程 $f[i][j]=f[i][j-1]*25 +f[i-1][j-1]$

（你可以假设s字符串最后一个字符放在最后一个位置 ，则种类数有$f[i-1][j-1]$,否则种类数有$f[i][j-1]*26$ ，很显然这两种情况中有重复，我们减去重复的即最后一个字符为$s[i]$, 且前 $j-1$ 个字符包含 $s$ 的前 $i$ 个字符，也包含 $s$ 的前$i-1$个字符的种类数，这个数为$f[i][j-1]$，故$f[i][j]=f[i][j-1]*25 +f[i-1][j-1]$）

但是这个dp方程对于10000的数据来说显然有点慢…


其实我们可以从另外一个角度分析。

对于长度为$j$ 的包含字符串s的字符串我们命名为ss，字符串ss匹配字符串s，我们令第一次匹配的位置为匹配位置吗，即字符串s的每个字符s[1] s[2] s[3]…s[i]在字符串 $j$ 的匹配位置分别为p[1] p[2] p[3] …p[i] 那么满足对于第k个匹配位置p[k] 在满足前k-1个匹配之后 第k个匹配是之后最早出现的s[k] 。

那么如果s[i]出现在位置j ，这样的数量有$C(j-1,i-1)*25^{j-i}​$ 个

否则最后一个匹配不在位置i，这样的数量有$f[i][j-1]*26​$ 个

故$f[i][j]=C(j-1,i-1)*25^{j-i}+f[i][j-1]*26$

这样对于字符串s，求解的复杂度就降为O(n)了

```cpp
/*
3260 ms	3200 KB
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
#define x  first
#define y  second
using  namespace std;
typedef long long ll;
typedef  pair<ll,ll> _p;
const ll MAX=100000;
const ll inf=0x3f3f3f3f;
const double EPS=1e-10;
const ll MOD=1e9+7;
char s[100005];
ll inv[100005],p25[100005];
ll qst[100005],tq,table[100005];
ll quick_pow(ll a,ll b)
{
    ll ans=1;
    while(b){
        if(b&1) ans=ans*a%MOD;
        a=a*a%MOD;
        b>>=1;
    }
    return ans;
}
ll Inv(ll a)
{
    return quick_pow(a,MOD-2);
}
void solve(ll ls)
{
    if(tq==0) return ;
    ll mx=ls;
    for(ll i=0ll;i<tq;++i)
        mx=max(mx,qst[i]);
    ll C=1;
    table[ls-1]=0;
    for(ll i=ls;i<=mx;++i){
        table[i]=(C*p25[i-ls]%MOD+table[i-1]*26%MOD)%MOD;
        C=C*i%MOD*inv[i-ls+1]%MOD;
    }
    for(ll i=0;i<tq;++i){
        if(qst[i]<ls) printf("0\n");
        else printf("%lld\n",table[qst[i]]);
    }
}
int main()
{
    ll q,ls,x,cmd,tot=0;
    p25[0]=1;
    for(ll i=1;i<=MAX;++i){
        p25[i]=p25[i-1]*25ll%MOD;
        inv[i]=Inv(i);
    }
    scanf("%lld %s",&q,s);
    tq=0;
    ls=strlen(s);
    while(q--)
    {
        scanf("%lld",&cmd);
        if(cmd==1){
            solve(ls);
            tq=0;
            scanf("%s",s);
            ls=strlen(s);
        }
        else{
            ll n;
            scanf("%lld",&n);
            qst[tq++]=n;
        }
    }
    solve(ls);
    return 0;
}

```


预处理优化后的代码

```cpp
/*
1528 ms	7900 KB
*/
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
#define x  first
#define y  second
using  namespace std;
typedef long long ll;
typedef  pair<ll,ll> _p;
const ll MAX=100000;
const ll inf=0x3f3f3f3f;
const double EPS=1e-10;
const ll MOD=1e9+7;
char s[100005];
vector<_p> g[100005];
ll ans[100005],inv[100005],p25[100005];
ll quick_pow(ll a,ll b)
{
    ll ans=1;
    while(b){
        if(b&1) ans=ans*a%MOD;
        a=a*a%MOD;
        b>>=1;
    }
    return ans;
}
ll Inv(ll a)
{
    return quick_pow(a,MOD-2);
}
int main()
{
    ll q,ls,x,cmd,tot=0;
    scanf("%lld %s",&q,s);
    ls=strlen(s);
    while(q--)
    {
        scanf("%lld",&cmd);
        if(cmd==1){
            scanf("%s",s);
            ls=strlen(s);
        }
        else{
            ll n;
            scanf("%lld",&n);
            g[ls].push_back({n,++tot});
        }
    }
    p25[0]=1;
    for(ll i=1;i<=MAX;++i){
        p25[i]=p25[i-1]*25ll%MOD;
        inv[i]=Inv(i);
    }
    for(ll x=1;x<=MAX;++x){
        if(g[x].size()==0) continue;
        sort(g[x].begin(),g[x].end());
        ll top=g[x].size();
        ll mx=g[x][top-1].x;
        ll C=1,F=0,now=0;
        while(g[x][now].x<x&&now<top){
            ll th=g[x][now].y;
            ans[th]=0ll;
            now++;
        }
        for(ll i=x;i<=mx;++i){
            F=(C*p25[i-x]%MOD+F*26%MOD)%MOD;
            C=C*i%MOD*inv[i-x+1]%MOD;
            while(g[x][now].x==i&&now<top){
                ll th=g[x][now].y;
                ans[th]=F;
                now++;
            }
        }
    }
    for(int i=1;i<=tot;++i){
        printf("%lld\n",ans[i]);
    }
    return 0;
}

```




#### 题目链接：[传送门](https://codeforces.com/problemset/problem/666/A)


##### 题意：


​ 给定串s，其由一个基本串后加任意多个长度为2或3的后缀串构成，要求基本串长度>4且相邻后缀串不相同。在基本串任意确定的情况下，求所有可能的后缀串。

##### 思路：


​ $dp[i][0]$表示第$a[i-1]$~$a[i]$组成的字符串是否可行，$dp[i][1]$表示第$a[i-2]$~$a[i]$组成的字符串是否可行。

​ 最后两个长度为2的后缀和长度为3的后缀如果可以取则可行。

​ $dp[i][0]=(dp[i+2][0]\&amp;\&amp;s1!=s2)~~||~~dp[i+3][1]$

​ $dp[i][1]=dp[i+2][0]~~||~~(dp[i+3][1]\&amp;\&amp;s1!=s2)$

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
#define x  first
#define y  second
using  namespace std;
typedef long long ll;
typedef  pair<int,int> _p;
const int MAX=100000;
const int inf=0x3f3f3f3f;
const double EPS=1e-10;
const int MOD=1e9+7;
int dp[10005][2];/*0 :2 ,1:3*/
set<string> mmp;
int main()
{
    string s;
    cin>>s;
    if(s.length()<6)
    {
        puts("0");
        return 0;
    }
    int ls=s.length();
    if(ls>6)
    {
        dp[ls-1][0]=1;
        mmp.insert(s.substr(ls-2,2));
    }
    if(ls>7)
    {
        dp[ls-1][1]=1;
        mmp.insert(s.substr(ls-3,3));
    }
    dp[ls-2][0]=dp[ls-2][1]=0;
    for(int i=ls-3; i>=4; --i)
    {
        if(i-2>=4)
        {
            if((i+3<ls&&dp[i+3][1]) || (dp[i+2][0]&&s.substr(i-1,2)!=s.substr(i+1,2) )) //0
            {
                dp[i][0]=1;
                mmp.insert(s.substr(i-1,2));
            }
        }
        if(i-3>=4)
        {
            if(dp[i+2][0]>0||( i+3<ls &&dp[i+3][1]&&s.substr(i-2,3)!=s.substr(i+1,3))) // 1
            {
                dp[i][1]=1;
                mmp.insert(s.substr(i-2,3));
            }
        }

    }
    cout<<mmp.size()<<endl;
    for(auto i:mmp)
        cout<<i<<endl;
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



#### 1159D - The minimal unique substring


链接：[1159D - The minimal unique substring](https://codeforces.com/contest/1159/problem/D)

思路：

令$a=(n-k)/2$ ， 接下来我们构造字符串s，a个0，1个1，a个0，1个1… (这道题还是暴力找规律靠谱点) **证明：**

这样字符串的周期为$a+1$.

更确切的说字符串$s$的组成是 ($a$个$0$)($1$个$1$)($a$个$0$)($1$个$1$) ($k-2$个字符) 四个部分

+ 如果 $l&gt;a+1$


​ 那么存在$l&#x27;=l-(a+1)$也是可行的

+ 如果 $1&lt;=l&lt;=a​$


​ 那么存在$l&#x27;=(l+a+1),l&#x27;\in[a+2,2*a+1]$ 可行的,因为所有$l&#x27;$满足 $l&#x27;+k&lt;=n$ （**即$l&#x27;$在第三部分**）

所以只有$l=a+1​$可能满足，下面我们来证明字符串 $s​$ 中以 $l​$ 为开始，长度为 $k​$ 的字符串只存在一个。

要想长度为k，那么$l’$只有可能在第1，2，3部分。但因为只有第二部分有 $1$ ，但是不能选( $l$ 就是在第二部分)

故不存在$l’ !=l$ 满足与字符串s相同

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;

int main()
{
    int n,k;
    cin>>n>>k;
    int a=(n-k)/2;
    for(int i=1;i<=n;++i)
        cout<<(i%(a+1)==0?'1':'0');
    cout<<endl;
    return 0;
}
```




## [1166D - Cute Sequences](https://codeforces.com/contest/1166/problem/D)


#### 题意：


​ 给一个序列的首项与末项a,b，现在要求我们怎么可以使得这个序列中的每个数$x_i=x_{i−1}+x_{i−2}+⋯+x_1+r_i,(x&gt;=2)$，其中$1≤ri≤m$。如果可行的话，请输出一种解。

#### 思路：


​ 因为每个r最少为1，所以我们先令所有的r=1，得到一个序列:$a$, $a+1$, $2*a+2$, $4*a+4,...$

我们发现$i&gt;=3$时，第$i$项是$i+1$项的二倍。所以这个序列增长很快！

​ 我们求只取这个序列中小于等于b的部分，那么我们得到一个序列A，长度为k (A为构造的序列)。

​ 我们令$rem=b-A[k]$, 那么rem就是我们需要往这个序列中增加某些位置的r值，让rem减少到0，从而让A[k]等于b

​ 我们假设第$i$位的r增加1，那数组A中第i+1位的值增加1，第$i+2$位的值增加$2$第$i+3$位的值增加$4$，向后的第q位的值增加$2^{q-1}$，那么我们可以算出来对数组A第k位的值增加多少。换句话说对rem减少的贡献是多少。

​ 所以我们可以贪心的从第2位一直到第k位，假设此时考虑第i位， $r$增加 $1$对 $rem$的贡献减少$val$，那么我们就让第 i 位的 $r$增加$y=min(m-1,rem/val)$.

​ 注意，当i=k的时候，对第rem减少的贡献也是1。

​ 如果最后rem为0，那么咱们构造的数组A就是解。

​ 否则一定无解。

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll A[105],r[105],rem;
ll getnext(ll last,ll th)
{
    if(th==1)
        return last+1;
    else
        return 2ll*last;
}
ll init(ll a,ll b,ll m)
{
    ll ta=0;
    A[++ta]=a;
    while(getnext(A[ta],ta)<=b){//构造出初始的A数组
        A[ta+1]=getnext(A[ta],ta);
        ta++;
    }
    for(ll i=2;i<=ta;++i) r[i]=1ll;
    rem=b-A[ta];
    return ta;
}
ll getval(ll t)//算出来第i位增加1，对rem的贡献是多少
{
    if(t<=2) return 1;
    t-=2;
    return (1ll<<t);
}
bool solve(ll ta,ll m)//remshi是全局变量
{
    for(ll i=2;i<=ta;++i){
        ll val=getval(ta-i+1);
        ll tot=min(m-1,rem/val);
        rem-=tot*val;
        r[i]+=tot;
    }
    if(rem!=0) return false;
    ll sum=A[1];
    for(ll i=2;i<=ta;++i){
        A[i]=sum+r[i];
        sum+=A[i];
    }
    return true;
}
int main(){
    ll q;
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>q;
    while(q--)
    {
        ll a,b,m;
        cin>>a>>b>>m;
        ll ta=init(a,b,m);//处理得到初始的A数组
        if(!solve(ta,m))//处理rem
        {
            cout<<-1<<endl;
        }
        else{
            cout<<ta;
            for(ll i=1;i<=ta;++i){
                cout<<" "<<A[i];
            }
            cout<<endl;
        }
    }
    return 0;
}
```


