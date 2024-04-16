

### Game HDU - 6669(思维+DP)


##### 题目链接：[HDU - 6669 ](https://cn.vjudge.net/problem/2679386/origin)


##### 思路：


​ 对于区间$[ a , b ] [a,b]$，关键点有$a , a + 1 , b − 1 , b a,a+1,b-1,b$。我们首先处理出所有区间的关键点，然后去重。容易知道，对于每个任务完成的位置一定在某个区间的关键点上。

​ 那么我们用$d p [ i ] [ k ] ​ dp[i][k]​$代表站在关键点$k ​ k​$完成第$i ​ i​$个任务的最小步数。然后进行状态转移

​ 对于第$i ​ i​$个任务在关键点$k ​ k​$的最小步数，即$d p [ i ] [ k ] ​ dp[i][k]​$的转移如下。假设第$i ​ i​$个任务的完成区间为$[ a [ i ] , b [ i ] ] ​ [a[i],b[i]]​$，$p o s [ k ] ​ pos[k]​$代表第$k ​ k​$个关键点的位置.


+ $i f ：$





## P3953 逛公园


**题目：**[传送门](https://www.luogu.org/problem/P3953)

**思路：**

​ 定义⼀条路径 (X…Y) 的冗余度为它的长度减去 X…Y 的最短路长度，那么这题就是求1到N的冗余度小于k的路径的条数。我们定义$d p [ i ] [ j ] dp[i][j]$ 代表1到 i 的冗余度等于 j 的路径的条数。对于一条有u到v的边表示为W(u,v)，我们定义函数$p ( u , v ) = w ( u , v ) + d i s [ u ] + d i t [ v ] − d i s [ T ] p(u,v)=w(u,v)+dis[u]+dit[v]-dis[T]$ 。那么$d p [ v ] [ j ] = S U M ( d p [ u ] [ j − p ( u , v ) ] ) dp[v][j]=SUM(dp[u][j-p(u,v)])$ ,这个函数的意义是S到T的路径中走(u,v)这条边浪费的长度。其中 u 是后驱为v的边的前驱顶点，边权为w。

​ 这题我们主要注意两点，第一点即零环无解，第二点是确定DP顺序，使得DP顺序是DP图的一个拓扑序(满足无后效性)。

​ 第一点因为数据量较大，我们可以考虑把所有0边都提出来，判断是否存在环即可。

​ 第二点我们可以根据先从小到大枚举冗余度k，在排除第一点的条件下，因为冗余度为0的路径不可能是一个环，对于冗余度不为0的边，我们不用管(因为我们是枚举是k从大到小)，对于浪费度为0的边(这些边只可能是到v的最短路上的边，非零边和零边)，在最短路上的边我们可以根据dis值从小到大来确定dp顶点顺序。对于dis值相等且这两个顶点有一个冗余度为0的边，即零边。我们需要额外的用另一种方法确定他们的dp顺序，我们可以在前面第一点的时候求零的顶点拓扑序列设为id，这样的话得到了零边的更新方式。

​ So



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




### [I - Beautiful People](https://vjudge.net/problem/ZOJ-2319)


[ZOJ - 2319 ](https://vjudge.net/problem/16158/origin)

##题意：

​ 给出 m 个人，每个人有两个属性：强壮度（s），美丽度（b），如果a的s，b中任意一个属性大于等于y的对应属性，另一个属性小于y，两个人就会打架。现在要办一个party，要求邀请尽可能多的人，并且他们不能打架。输出人数和每个人的编号（编号从1开始）

### 思路：


​ 这道题不难想象邀请最多的人 满足他们的S，B序列都是严格递增的。那么我们只要从所有人的S，B序列中找出所有的严格递增的个数中的最多的即可。

​ 我们将所有人按照S从小到大排序，如果S相同 就让B大的排在前面，然后找出S的最长严格递增子序列即可，并记录路径即可。（这样的话可以保证我们选取过程中S相同 的所有B中，B最多选一个）

​ 题目中的数据为


m:4

S: 1 1 2 2

B: 1 2 1 2

我们按规定排序后

S: 1 1 2 2

B: 2 1 2 1

我们选取**排序后**的第二个人和第四个人即可


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int inf=0x3f3f3f3f;
const int maxn=1e5+100;
struct Data
{
    int a,b,id;
} data[maxn];
bool operator <(const Data &aa,const Data &bb)
{
    if(aa.a==bb.a)
        return aa.b>bb.b;
    return aa.a<bb.a;
}
int S[maxn],pre[maxn],dp[maxn],lcsid[maxn];
vector<int> V;
int main()
{
    int t,fa=0;
    scanf("%d",&t);
    while(t--)
    {
        if(fa) puts("");
        fa=1;
        int n;
        scanf("%d",&n);
        for(int i=1; i<=n; ++i)
        {
            scanf("%d%d",&data[i].a,&data[i].b);
            data[i].id=i;
        }
        sort(data+1,data+n+1);
        for(int i=1; i<=n; ++i) S[i]=data[i].b;
        int len=0;
        mset(pre,-1);
        dp[0]=-1;
        lcsid[0]=-1;
        for(int i=1; i<=n; ++i)
        {
            int th=lower_bound(dp,dp+len+1,S[i])-dp;//th就是该元素该插入的位置，且他从上一个地方过来
            pre[i]=lcsid[th-1];
            lcsid[th]=i;
            dp[th]=S[i];
            len=max(len,th);
        }//pre[lcsid[len]]一直王回溯即可
        V.clear();
        for(int v=lcsid[len]; v!=-1; v=pre[v])
            V.push_back(v);
        printf("%d\n",V.size());
        for(int i=0; i<V.size(); ++i)
            printf("%d ",data[V[i]].id);
        puts("");
    }

    return 0;
}

```




### [D - 度度熊与邪恶大魔王](https://vjudge.net/problem/HDU-6082)


​ [HDU - 6082 ](https://vjudge.net/problem/984092/origin)

#### 思路：


​ 数据很水，$1000*1000*10$的复杂度，多组输入都能过。

​ $dp[f][h]$ 表示防御力为 $f$ 血量为$h$被消灭所需的最小晶石数量。那么假设第$i$个技能造成的伤害为$K[i]$,晶石数量为$P[i]$

$dp[f][h]=min(dp[f][h+f-K[i]]+P[i]),i \in[1,m] \&amp;\&amp;K[i]&gt;f​$ 。 且$dp[f][0]=0​$

注意：$K[i]&lt;=f$的情况 和无解的情况即可。

​ 如果最大的防御$fmax&gt;_{All}P[i]$ 则无解。(其他形式的判断也行)

```cpp
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<string>
#include<queue>
#define mset(a,b) memset(a,b,sizeof(a))
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
using namespace std;
typedef long long ll;
const ll maxn=1e5+100;
const ll inf=0x3f3f3f3f3f3f3f3f;
ll H[maxn],F[maxn];
ll dp[11][1100];//初始化都为0
ll K[1100],P[1100];
int main()
{
    ll n,m;
    ll fmax=-1,hmax=-1;
    while(~scanf("%lld%lld",&n,&m))
    {
        fmax=hmax=-1;
        for(ll i=1; i<=n; ++i)
        {
            scanf("%lld%lld",H+i,F+i);
            fmax=fmax<F[i]?F[i]:fmax;
            hmax=hmax<H[i]?H[i]:hmax;
        }
        for(ll i=1; i<=m; ++i)
            scanf("%lld%lld",P+i,K+i);
        int flag=1;
        for(ll f=0; f<=fmax&&flag; ++f) //对于每个防御力 遍历生命值dp[f][0]=0
        {
            dp[f][0]=0;
            for(ll h=1; h<=hmax; ++h)
            {
                ll minn=inf;
                for(ll i=1; i<=m; ++i)
                {
                    if(K[i]<=f)
                        continue;
                    if(h+f<K[i])
                    {
                        minn=min(minn,P[i]);
                    }
                    else
                    {
                        minn=min(minn,dp[f][h-K[i]+f]+P[i]);
                    }
                }
                if(minn==inf)//不能够打死
                {
                    flag=0;
                    break;
                }
                dp[f][h]=minn;
            }
        }
        if(!flag)
        {
            printf("-1\n");
            continue;
        }
        ll ans=0;
        for(ll i=1; i<=n; ++i)
            ans+=dp[F[i]][H[i]];
        printf("%lld\n",ans);
    }
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


