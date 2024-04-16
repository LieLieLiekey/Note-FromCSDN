

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


