

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

+  首先每个第 $i$个数作为三元组的第三个元素，满足条件的$x,y$的组合最多有 $\lfloor \frac {i-1} 2\rfloor$ 个，这样就可以确定n个元素的数组最多可能由多少个三元组。 +  **注意到**自然数序列是满足三元组数量最多的序列。 +  所以我们找到一个k满足前k个数是自然数，即 $\sum_{i=1}^{k}\lfloor \frac {i-1}{2} \rfloor \le m$的最大的$k$ ，即前k+1个数是自然数的时候组成的三元组必定大于m 即 $\sum_{i=1}^{k+1}\lfloor \frac {i-1}{2} \rfloor > m$ ，令 $rem=m-\sum_{i=1}^{k}\lfloor \frac {i-1}{2}\rfloor$ ，如果 $rem!=0$ 且 $k==n$ 时无解。 +  我们让前k个全为自然数，那么剩余的还需的三元组的个数为rem，且满足 $rem<\lfloor \frac k 2 \rfloor$ ，即 $2*rem\le k$  +  根据前面的 $1$ 很容易想到让 $a[k+1]=k+k-2*rem+1=2*k-2*rem+1$ ，这样第k+1个数与前k个组组成的三元组的个数是rem。 +  我们要让剩下的 $k+2....n$ 全部填充为奇数，这样后边的序列不会组成三元组（因为奇数与奇数的和等于偶数），为了还不满足 $x\in[1,k+1],y,z\in[k+2,n]$  的三元组成立，我们让后边部分的数间隔大点，比如 $a[k+1]+1$ ，还不让满足 $x,y\in[1,k+1],z\in[k+2,n]$ 的三元组成立，让后半部分的每个值都大于 $a[k]+a[k+2]$



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


