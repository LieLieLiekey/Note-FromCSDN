

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




## P4248 [AHOI2013]差异 （后缀数组+单调栈）


#### 题目链接：[传送门](https://www.luogu.org/problem/P4248)


#### 正文：


首先对于这个公式的前两项我们可以快速求出，为$(1+n)*n*(n-1)/2$。所以我们只需考虑最后一项的和，又因为每个$T_i$对应排序后的后缀的$rank[i]$位置，所以这步可以转化为在排序后的后缀数组上统计答案。

首先最后一项$lcp(T_i,T_j)$ 的值，设$x=rank[i],y=rank[j]$，不访假设$x<y$，那么$lcp(T_i,T_j)$等于$min\{height[x+1],height[x+2]....,height[y]\}$，即区间$[x+1,y]$的$height[]$数组中的最小的值$height[k]$ 的值是贡献。如果最小高度有多个，那么对规定最左边的最小高度起贡献。

因为最后一项的是所有元组，所以我们可以用单调栈维护每个$height[]$贡献的区间即可，

#### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b)   memset(a,b,sizeof(a))
typedef long long ll;
const int N=5e5+10;//下标从1开始
int rak[N],sa[N],tp[N],c[N],height[N];
//最后的rak[i]=p 与sa[p]=i ,11对应
void SA(char *s,int n)//这个基数排序的版本中桶的大小为第一关键词rak的最大值
{
    int m=128;//桶的大小,会慢慢变大,最大为n,但初始时是字符的最大值
    //首先基数排序初始化rak数组和sa数组
    //第一轮基数排序,如果s的最大值很大,可改用快速排序
    for(int i=0; i<=m; ++i) c[i]=0;
    for(int i=1; i<=n; ++i) c[rak[i]=s[i]]++;
    for(int i=1; i<=m; ++i) c[i]+=c[i-1];
    for(int i=n; i>=1; --i) sa[c[s[i]]--]=i; //所有后缀长度为1的字符串已求出

    for(int k=1,p ; k < n; k<<=1 ) //p是一个计数器，现在还没用。
    {
        /*tp[i]:第二关键词排名为i的位置为tp[i]*/
        p=0;
        for(int i=n-k+1; i<=n; ++i) tp[++p]=i;
        for(int i=1; i<=n; ++i) if(sa[i]>k) tp[++p]=sa[i]-k;
        /*基数排序求出2k长度的sa数组*/
        for(int i=0; i<=m; ++i) c[i]=0;
        for(int i=1; i<=n; ++i) c[rak[i]]++;
        for(int i=1; i<=m; ++i) c[i]+=c[i-1];
        for(int i=n; i>=1; --i) sa[ c[rak[tp[i]]]-- ]=tp[i];
        /*求该轮的rank数组*/
        //tp才是上一轮的rak,现在要利用上轮的rak和这轮的sa求这轮的rank
        std::swap(rak,tp);
        rak[sa[1]]=p=1;
        for(int i=2,a,b; i<=n; ++i)
        {
            a=sa[i],b=sa[i-1];
            if(tp[a]==tp[b]&&((a+k<=n&& b+k<=n&&tp[a+k]==tp[b+k])||(a+k > n&& b+k > n))) rak[a]=p;
            else rak[a]=++p;
        }
        if(p>=n) break;//可以提前退出
        m=p;
    }//计算高度
    int k=0;
    for(int i=1; i<=n; ++i)
    {
        if(k) k--;//i  ,
        int j=sa[rak[i]-1];
        if(j==0) continue;
        while(s[j+k]==s[i+k]) ++k;
        height[rak[i]]=k;
    }
}
char s[N];
int S[N],top;
int left[N],right[N];
int main()
{
    scanf("%s",s+1);
    int ls=strlen(s+1);
    SA(s,ls);
    top=0;
    for(int i=2;i<=ls;++i)
    {
        while(top > 0&& height[S[top]]> height[i]) top--;
        S[++top]=i;
        if(top==1) left[i]=2;
        else left[i]=S[top-1]+1;
    }
    top=0;
    for(int i=ls;i>=2;--i)
    {
        while(top>0 && height[S[top]] >=height[i]) top--;
        S[++top]=i;
        if(top==1) right[i]=ls;
        else right[i]=S[top-1]-1;
    }
    long long ans=(1ll+ls)*(ls-1)*(ls)/2ll;
    for(int i=2;i<=ls;++i)
    {
        ans-=2ll*height[i]*(right[i]-i+1)*(i-left[i]+1);
    }
    printf("%lld\n",ans);
}
```




### 后缀数组


后缀排序后的序列(信息：sa[],height[],rank[])有诸多性质，要灵活应用，并且一定要记得，**一个字符串的子串就是某个后缀的前缀，那么子串之间的关系在后缀数组上非常明显**！

后缀数组经典问题

##### 1.求两后缀的最长公共前缀——LCP(a,b)。


LCP(a,b)定义为后缀a与后缀b的最长相同前缀的长度，设$x = rank\left\lbrack a \right\rbrack,y = rank\left\lbrack b \right\rbrack$，$rank\lbrack i\rbrack$ 即后缀$i$ 在后缀数组中的排名。不访假设$x < y​$，那么 

$$\text{LCP}\left( a,b \right) = min(height\lbrack x + 1\rbrack,height\lbrack x + 2\rbrack\ldots,height\lbrack y\rbrack)$$



##### 2.比较一个字符串的两个子串的大小关系


假设需要比较的是$A = S\left\lbrack a\ldots b \right\rbrack$和$B = S\lbrack c\ldots d\rbrack$的大小关系。

若$\text{LCP}\left( a,c \right) \geq \min\left( \left| A \right|,\left| B \right| \right)$ ,$A < B \Leftarrow \Rightarrow \left| A \right| < |B|$

否则$A < B \Leftarrow \Rightarrow rank\left\lbrack a \right\rbrack < rank\lbrack b\rbrack$

##### 3.不同子串的数目


子串就是后缀的前缀，所以可以枚举每个后缀，计算前缀总数，再减掉重复，“前缀总数”其实就是子串个数，为 $\frac{n*(n+1)}{2}​$。

如果按后缀排序的顺序枚举后缀，每次新增的子串就是除了与上一个后缀的 LCP 剩下的前缀。这些前缀一定是新增的，否则会破坏$LCP(sa[i],sa[j])=min\{height[i+1...j]\}$的性质。只有这些前缀是新增的，因为 LCP 部分在枚举上一个前缀时计算过了。

所以答案为： $\frac{n*(n + 1)}{2} - \sum_{i = 2}^{n}{height[i]}$

##### 4.求在字符串中至少出现k次的最长子串的长度


即height[]中相邻k-1个的最小值的最大值。

答案为：$max\{ v\ |v = \min\left( \text{height}\left\lbrack i \right\rbrack,height\left\lbrack i + k - 2 \right\rbrack \right),i \in \left\lbrack 2,n + 2 - k \right\rbrack\}$。

可以使用RMQ 做到O(nlogn)预处理，O(1)查询。

##### 5.查询一个字符串在文本串的出现次数。


假设文本串为S，查询串为T，那么我们可以在串S的后缀数组上二分出字典序大于等于串T的最小排名（注意此时的二分只考虑前|T|个长度），然后二分字典序大于串T的最小排名，出现次数即这两个位置相减的值。

#### 6. 求两个字符串的最长相同子串 Poj2774


很容易想出答案是这两个字符串后缀中的最长相同前缀的长度。 我们假设这两个字符串分别为S1，S2，令S=S1+’#’+S2。 接下来求出S的后缀数组，因为对于S2（S1）的某个后缀t2，另一个串S1(S2)与它相同的最长子串一定是S的后缀数组中离后缀t2的最近的两侧的某个后缀串t1的lcp的值。(t1,t2分别是S1,S2的后缀串) 所以我们考虑这样做，从左到右依此遍历后缀数组，维护下S1后缀串的最近的出现过的排名位置p1，S2后缀串最近的出现过的排名位置p2，每遇到一个S1（S2）的后缀串，就求上个另一个后缀串与自己的最长前缀长度即min⁡{height[p+1],…height[i]} 更新答案即可。 注：区间min可以使用RMQ预处理，总体时间复杂度O((n+m)log(n+m))

#### 7. 某字符串最长重复子串问题


一个字符串t是S的重复子串当且仅当t在S中至少出现了两次(出现位置不同)

+ **求字符串可重叠最长重复子串的长度** 即height[]数组的最大值 注：DA算法时间复杂度O(nlogn),DC3时间复杂度O(n)+ **不可重叠最长重复子串的长度** 这里不可重叠是指要求字符串t在字符串S中至少两次出现的区间无重叠。 对于这个问题可改为判定性问题，我们可以二分t的长度，对于每个长度lt，我们可以将height数组分组，即在height[i]<lt的位置分开，这样每个区间的任意两个后缀串的相同前缀长度都>=lt,那么只要某个区间的sa[]的最大值和sa[]最小值相差只要>=lt即这个长度可以。（这里可以扩展一下，要求出现的重复子串相隔间距至少一定位置也可以） 注：二分O(logn)，judge O(n)，总体时间复杂度为O(nlogn) 这个二分+分组的技巧会经常常见。 *下面有关图片取自—2009年论文集之后缀数组——罗穗骞* 
![./figures/20191007154422462.png](./figures/20191007154422462.png)
 
![./figures/20191007154432438.png](./figures/20191007154432438.png)
+ **可重叠的k次最长重复子串（pku3261）** 
![./figures/20191007154507188.png](./figures/20191007154507188.png)



#### 8. 多字符串之间的关系问题


对于多个字符串，我们常常把这些字符串用特殊字符（比如char(1),char(2)等等，反正只要不出现在字符集里且连接所使用的字符不同即可）连接起来，然后在后缀数组上进行一些操作即可。这么做的作用是对于每个后缀串分隔符处的典序比较肯定出排名结果，这样分隔符处以及之后字符对于这个后缀串就不起作用了 注：通常也使用二分长度+分组的技巧，具体请看下面多字符串的关系

+ **给定 n 个字符串，求出现在不小于 k 个字符串中的最长子串。** 如果k=1的话就直接输出最长即可。 否则我们将这些字符串用特殊且不相等的字符连接起来，求他们的后缀数组，接下来二分满足要求的子串的长度（改成判定性问题），对于每个长度w，我们将height[]<w处分隔开从而将height[]数组分组，我们只需判断这些组内是否有k个不同字符串的后缀即可（因为每组后缀的最长相同前缀长度>=w，容易看出答案一定也在某个组中，所以该算法正确）。 注：时间复杂度O(nlogn) *下面有关图片取自—2009年论文集之后缀数组——罗穗骞* 
![./figures/2019100715473419.png](./figures/2019100715473419.png)
+ **每个字符串至少出现两次且不重叠的最长子串(spoj220)** *下面有关图片取自—2009年论文集之后缀数组——罗穗骞* 
![./figures/20191007154750828.png](./figures/20191007154750828.png)
+ **出现或反转后出现在每个字符串中的最长子串(PKU3294** *下面有关图片取自—2009年论文集后缀数组——罗穗骞* 
![./figures/2019100715480865.png](./figures/2019100715480865.png)




这篇文章大部分参考：https://wenku.baidu.com/view/ed1be61e10a6f524ccbf85fd.html###


##### DA算法


时间复杂度O(nlogn)，空间复杂度O(n)

后缀数组DA算法：

```cpp
//子串与子串的关系可以转化为两后缀的前缀的关系,所以后缀数组在字符串方面有很大用处
/*
注: 排名从1开始,后缀下标从1开始.

名词解释:下面后缀i代指原串下标i开始的后缀,排名指字典序从小到大的排名.
s[] :原串数组,下标从1开始,要在下标n+1处有一最小字符,比如'\0'.
n   :字符串长度.
sa[]:sa[i]代表排名为i的后缀下标为sa[i]
rank[]: 后缀i的排名为rank[i]
height[]: height[i]代表排名i与排名i-1后缀的最长相同前缀的长度.
空间复杂度O(n),时间复杂度O(nlogn)
*/
const int N=1e5+10;
int t1[N],t2[N],c1[N];//辅助数组
void SA(char *s,int n,int sa[],int rank[],int height[])//基数排序的版本中
{
    int m=128;//桶的大小,会在下面循环中变化,第一关键词r的最大值,初始时是字符的最大值,之后都<=n
    int *sb=t1,*r=t2,*c=c1;//辅助数组,分别为:基数排序所用的第二2,rak',cnt数组
    //用基数排序求出长度为1的sa[]和rank[],如果字符最大值较大,第一轮可以采用sort
    for(int i=0; i<=m; ++i) c[i]=0;
    for(int i=1; i<=n; ++i) c[r[i]=s[i]]++;
    for(int i=1; i<=m; ++i) c[i]+=c[i-1];
    for(int i=n; i>=1; --i) sa[c[s[i]]--]=i;

    for(int k=1,p ; k < n; k<<=1 ) //p是一个计数器，现在还没用。
    {
        //sb[i]:第二关键词排名为i的位置为sb[i]
        p=0;
        for(int i=n-k+1; i<=n; ++i) sb[++p]=i;
        for(int i=1; i<=n; ++i) if(sa[i]>k) sb[++p]=sa[i]-k;
        //基数排序求出2k长度的sa数组
        for(int i=0; i<=m; ++i) c[i]=0;
        for(int i=1; i<=n; ++i) c[r[i]]++;
        for(int i=1; i<=m; ++i) c[i]+=c[i-1];
        for(int i=n; i>=1; --i) sa[ c[r[sb[i]]]-- ]=sb[i];
        std::swap(r,sb);
        //现在要利用上轮的r和这轮的sa求这轮的r
        r[sa[1]]=p=1;
        for(int i=2,a,b; i<=n; ++i)
        {
            a=sa[i],b=sa[i-1];
            if(sb[a]==sb[b]&&(a+k<=n && b+k<=n&&sb[a+k]==sb[b+k]) ) r[a]=p;
            else r[a]=++p;
        }
        if(p>=n) break;//可以提前退出
        m=p;
    }
    /*计算高度数组*/
    int k=0;
    for(int i=1;i<=n;++i) rank[sa[i]]=i;
    for(int i=1; i<=n; ++i)
    {
        if(k) k--;
        int j=sa[rank[i]-1];
        if(j==0) continue;
        while(s[j+k]==s[i+k]) ++k;
        height[rank[i]]=k;
    }
}
int rank[N],sa[N],height[N];
char s[N];
int RMQ[N],mm[N],best[N][20];//rmq[]=height[]
void initRMQ(int n)
{
    for(int i=1; i<=n; ++i) RMQ[i]=height[i];
    mm[0]=-1;
    for(int i=1; i<=n; ++i) mm[i]=((i&(i-1))==0)?mm[i-1]+1:mm[i-1];
    for(int i=1; i<=n; ++i) best[i][0]=i;
    for(int j=1; j<=mm[n]; ++j)
        for(int i=1; i+(1<<j)-1<=n;++i){
            int a=best[i][j-1];
            int b=best[i+(1<<(j-1))][j-1];
            if(RMQ[a] < RMQ[b]) best[i][j]=a;
            else best[i][j]=b;
        }
}
int askRMQ(int a,int b)
{
    int t;
    t=mm[b-a+1];
    b-=(1<<t)-1;
    a=best[a][t],b=best[b][t];
    if(RMQ[a] < RMQ[b]) return a;
    else return b;
}
int lcp(int a,int b)
{
    a=rank[a],b=rank[b];
    if(a > b) std::swap(a,b);
    return height[askRMQ(a+1,b)];
}
```


如果传入的数组字符最大值太大，第一波可以使用快排（当然离散化也是可以的）

```cpp
const int N=1e6+10;
int t1[N],t2[N],c1[N];//辅助数组
void SA(int *s,int n,int sa[],int rank[],int height[])//基数排序的版本中
{
    int m=n;//桶的大小,会在之后循环变化,<=n
    int *sb=t1,*r=t2,*c=c1;
    /*串最大值较大,第一轮采用sort*/
    for(int i=1; i<=n; ++i) sa[i]=i;
    auto cmp=[&](int x,int y)
    {
        return s[x]<s[y]||(s[x]==s[y]&&x < y);
    };
    std::sort(sa+1,sa+n+1,cmp);
    int p;
    r[sa[1]]=p=1;
    for(int i=2; i<=n; ++i)
    {
        if(s[sa[i-1]]==s[sa[i]]) r[sa[i]]=p;
        else r[sa[i]]=++p;
    }
	
    for(int k=1,p ; k < n; k<<=1 ) //p是一个计数器，现在还没用。
    {

        p=0;
        for(int i=n-k+1; i<=n; ++i) sb[++p]=i;
        for(int i=1; i<=n; ++i) if(sa[i]>k) sb[++p]=sa[i]-k;

        for(int i=0; i<=m; ++i) c[i]=0;
        for(int i=1; i<=n; ++i) c[r[i]]++;
        for(int i=1; i<=m; ++i) c[i]+=c[i-1];
        for(int i=n; i>=1; --i) sa[ c[r[sb[i]]]-- ]=sb[i];
        std::swap(r,sb);

        r[sa[1]]=p=1;
        for(int i=2,a,b; i<=n; ++i)
        {
            a=sa[i],b=sa[i-1];
            if(sb[a]==sb[b]&&(a+k<=n && b+k<=n&&sb[a+k]==sb[b+k]) ) r[a]=p;
            else r[a]=++p;
        }
        if(p>=n) break;//可以提前退出
        m=p;
    }
    /*计算高度数组*/
    int k=0;
    for(int i=1; i<=n; ++i) rank[sa[i]]=i;
    for(int i=1; i<=n; ++i)
    {
        if(k) k--;
        int j=sa[rank[i]-1];
        if(j==0) continue;
        while(s[j+k]==s[i+k]) ++k;
        height[rank[i]]=k;
    }
}
```




## POJ 2774求两字符串的最长公共子串（后缀数组）


题目链接：[传送门](http://poj.org/problem?id=2774)

**思路**：

大概就是枚举s2(s1)的每个后缀，查看对应的s1(s2)的后缀与自己的最长前缀长度是多少。

我们可以把字符串s1和s2拼接到一起,中间用’#‘连接(’#'只是代表比字符集任意一个字符小的字符)，然后求出拼接后字符串的后缀数组，在排序后的后缀数组上排名从小到大遍历，并同时记下左边最近的s1(s2)的后缀的位置p1(p2)，然后对于每个s2(s1)的后缀，用RMQ求出p1(p2)位置的后缀串与自己后缀的最长前缀长度是多少（这一步可以RMQ预处理O(1)查询$height[]$区间最小值实现），更新最长前缀长度的最大值即可。

**代码**：

```cpp
//#include<bits/stdc++.h>
#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string.h>
#define mset(a,b)   memset(a,b,sizeof(a))
typedef long long ll;
const int N=2e5+10;
int t1[N],t2[N],c1[N];//辅助数组
void SA(char *s,int n,int sa[],int rank[],int height[])//基数排序的版本中
{
    int m=128;//桶的大小,会在下面循环中变化,第一关键词r的最大值,初始时是字符的最大值,之后都<=n
    int *sb=t1,*r=t2,*c=c1;//辅助数组,分别为:基数排序所用的第二2,rak',cnt数组
    //用基数排序求出长度为1的sa[]和rank[],如果字符最大值较大,第一轮可以采用sort
    for(int i=0; i<=m; ++i) c[i]=0;
    for(int i=1; i<=n; ++i) c[r[i]=s[i]]++;
    for(int i=1; i<=m; ++i) c[i]+=c[i-1];
    for(int i=n; i>=1; --i) sa[c[s[i]]--]=i;

    for(int k=1,p ; k < n; k<<=1 ) //p是一个计数器，现在还没用。
    {
        //sb[i]:第二关键词排名为i的位置为sb[i]
        p=0;
        for(int i=n-k+1; i<=n; ++i) sb[++p]=i;
        for(int i=1; i<=n; ++i) if(sa[i]>k) sb[++p]=sa[i]-k;
        //基数排序求出2k长度的sa数组
        for(int i=0; i<=m; ++i) c[i]=0;
        for(int i=1; i<=n; ++i) c[r[i]]++;
        for(int i=1; i<=m; ++i) c[i]+=c[i-1];
        for(int i=n; i>=1; --i) sa[ c[r[sb[i]]]-- ]=sb[i];
        std::swap(r,sb);
        //现在要利用上轮的r和这轮的sa求这轮的r
        r[sa[1]]=p=1;
        for(int i=2,a,b; i<=n; ++i)
        {
            a=sa[i],b=sa[i-1];
            if(sb[a]==sb[b]&&(a+k<=n && b+k<=n&&sb[a+k]==sb[b+k]) ) r[a]=p;
            else r[a]=++p;
        }
        if(p>=n) break;//可以提前退出
        m=p;
    }
    /*计算高度数组*/
    int k=0;
    for(int i=1; i<=n; ++i) rank[sa[i]]=i;
    height[1]=0;
    for(int i=1; i<=n; ++i)
    {
        if(k) k--;
        int j=sa[rank[i]-1];
        if(j==0) continue;
        while(s[j+k]==s[i+k]) ++k;
        height[rank[i]]=k;
    }
}
int rank[N],sa[N],height[N]; //height[1]的值为0
char s[N];
//预处理O(nlogn)—查询O(1)求height[]的连续最小值的RMQ代码
int RMQ[N],mm[N],best[N][20];//rmq[]=height[]
void initRMQ(int n, int height[])
{
    for(int i=1; i<=n; ++i) RMQ[i]=height[i];
    mm[0]=-1;
    for(int i=1; i<=n; ++i) mm[i]=((i&(i-1))==0)?mm[i-1]+1:mm[i-1];
    for(int i=1; i<=n; ++i) best[i][0]=i;
    for(int j=1; j<=mm[n]; ++j)
        for(int i=1; i+(1<<j)-1<=n; ++i)
        {
            int a=best[i][j-1];
            int b=best[i+(1<<(j-1))][j-1];
            if(RMQ[a] < RMQ[b]) best[i][j]=a;
            else best[i][j]=b;
        }
}
int askRMQ(int a,int b)//求区间[a,b]最小值的下标
{
    int t;
    t=mm[b-a+1];
    b-=(1<<t)-1;
    a=best[a][t],b=best[b][t];
    if(RMQ[a] < RMQ[b]) return a;
    else return b;
}
int lcp(int a,int b)
{
    a=rank[a],b=rank[b];
    if(a > b) std::swap(a,b);
    return height[askRMQ(a+1,b)];
}
char s1[N],s2[N];
int main()
{
    int n=0;
    scanf("%s%s",s1+1,s2+1);
    int ls1=strlen(s1+1),ls2=strlen(s2+1);
    for(int i=1; i<=ls1; ++i) s[++n]=s1[i];
    s[++n]='#';
    for(int i=1; i<=ls2; ++i) s[++n]=s2[i];
    s[n+1]='\0';
    SA(s,n,sa,rank,height);
    initRMQ(n,height);
    int lp1=-1,lp2=-1,ans=0;
    for(int i=1; i<=n; ++i)
    {
        if(sa[i]>ls1+1)//是串s2
        {
            if(lp1!=-1)
                ans=std::max(ans,height[askRMQ(lp1+1,i)]);
            lp2=i;
        }
        else if(sa[i]<=ls1)
        {
            if(lp2!=-1)
                ans=std::max(ans,height[askRMQ(lp2+1,i)]);
            lp1=i;
        }
    }
    printf("%d\n",ans);
}

```




## POJ1743 Musical Theme (后缀数组，不可重叠最长重复子串)


#### 题目链接：[传送门](https://vjudge.net/problem/19231/origin)


### 思路：


​ 首先可以知道对于两个相同旋律的拍子(即两个拍子全部增加某个值后会相同)，假设长度为k，那么拍子的后k-1个数与他们的前一个数的差都是相同的。

​ 所以我们可以将数组转化为差数组，$d[1]=$无效值，然后要求从差数组中找到长度最长的两个子序列满足，子序列不重叠且间隔为至少1（如果这两个子序列挨着的话，那么对应的拍子就重叠了）

​ 所以我们可以二分这个子序列的长度，对于每个长度，我们根据$height[]$是否小于长度来进行分组，对于每个分组，如果这个组的下标最大值与最小值满足$max-min>=len+1​$,则这个解可以。

```cpp
#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string.h>
#define mset(a,b)   memset(a,b,sizeof(a))
typedef long long ll;
const int N=2e4+10;
int t1[N],t2[N],c1[N];//辅助数组
void SA(int *s,int n,int sa[],int rank[],int height[])//基数排序的版本中
{
    int m=200;//桶的大小,会在下面循环中变化,第一关键词r的最大值,初始时是字符的最大值,之后都<=n
    int *sb=t1,*r=t2,*c=c1;//辅助数组,分别为:基数排序所用的第二2,rak',cnt数组
    //用基数排序求出长度为1的sa[]和rank[],如果字符最大值较大,第一轮可以采用sort
    for(int i=0; i<=m; ++i) c[i]=0;
    for(int i=1; i<=n; ++i) c[r[i]=s[i]]++;
    for(int i=1; i<=m; ++i) c[i]+=c[i-1];
    for(int i=n; i>=1; --i) sa[c[s[i]]--]=i;

    for(int k=1,p ; k < n; k<<=1 ) //p是一个计数器，现在还没用。
    {
        //sb[i]:第二关键词排名为i的位置为sb[i]
        p=0;
        for(int i=n-k+1; i<=n; ++i) sb[++p]=i;
        for(int i=1; i<=n; ++i) if(sa[i]>k) sb[++p]=sa[i]-k;
        //基数排序求出2k长度的sa数组
        for(int i=0; i<=m; ++i) c[i]=0;
        for(int i=1; i<=n; ++i) c[r[i]]++;
        for(int i=1; i<=m; ++i) c[i]+=c[i-1];
        for(int i=n; i>=1; --i) sa[ c[r[sb[i]]]-- ]=sb[i];
        std::swap(r,sb);
        //现在要利用上轮的r和这轮的sa求这轮的r
        r[sa[1]]=p=1;
        for(int i=2,a,b; i<=n; ++i)
        {
            a=sa[i],b=sa[i-1];
            if(sb[a]==sb[b]&&(a+k<=n && b+k<=n&&sb[a+k]==sb[b+k]) ) r[a]=p;
            else r[a]=++p;
        }
        if(p>=n) break;//可以提前退出
        m=p;
    }
    /*计算高度数组*/
    int k=0;
    for(int i=1; i<=n; ++i) rank[sa[i]]=i;
    height[1]=0;
    for(int i=1; i<=n; ++i)
    {
        if(k) k--;
        int j=sa[rank[i]-1];
        if(j==0) continue;
        while(s[j+k]==s[i+k]) ++k;
        height[rank[i]]=k;
    }
}
int rank[N],sa[N],height[N]; //height[1]的值为0
int w[N],d[N];
/*
搞成差分数组 前缀相同长度至少为4的不重叠
*/
bool judge(int v,int n)//在v数组中能否构成长度>=v的不重叠子串
{
    //分成几个不相交的区间,求每个区间的
    int l=1,minn=sa[1],maxx=sa[1];
    for(int i=2;i<=n;++i)
    {
        if(height[i]>=v) {
            minn=std::min(minn,sa[i]);
            maxx=std::max(maxx,sa[i]);
        }
        else{
            if(maxx-minn>=v) return true;
            else minn=sa[i],maxx=sa[i];
        }
    }
    if(maxx-minn>=v+1) return true;
    else return false;
}
int main()
{
    int n;
    while(scanf("%d",&n),n)
    {
        for(int i=1;i<=n;++i) scanf("%d",w+i),d[i]=w[i]-w[i-1]+100;
        d[1]=0;
        d[n+1]=-1;
        SA(d,n,sa,rank,height);
        int l=4,r=n;
        int ans=-1;
        while(l<=r)
        {
            int m=l+r>>1;
            if(judge(m,n))
            {
                ans=m;
                l=m+1;
            }
            else r=m-1;
        }
        if(ans==-1)
            printf("0\n");
        else
            printf("%d\n",ans+1);
    }
    return 0;
}
```




### POJ - 3294 - Life Forms(后缀数组，二分+分组技巧)


#### 题目链接：[传送门](http://poj.org/problem?id=3294)


#### 思路：


+  part1 +  对于n个字符串，我们只需要找至少在n/2+1个字符串出现过的最长子串即可。 +  part2 +  如果k=1，我们只需输出最长的字符串即可（这里n肯定等于1，即本身） +  否则我们首先将这n个字符串用**不相同**的**特殊字符**连接成一个字符串S，并记录每个下标位置属于哪个字符串。 +  二分所求子串的长度w，然后在$height[]$数组上进行分组，即$height[]<w$的位置分割开，这样我们就得到了许多组，我们只需判断是否存在一组内有k个字符串的后缀即可。（因为后缀的最长相等前缀$>=w$不会跨越组，所以如果存在，答案一定在某个组内，否则也不存在，某个组存在最少k个字符串的后缀串，所以算法正确） +  part3 +  现在我们找到了这个最长子串长度w，我们只需模仿上面分组，如果组内有解就输出这个组的最长相同前缀即可。 


代码：

```cpp
#include<string>
#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string.h>
#define mset(a,b)   memset(a,b,sizeof(a))
typedef long long ll;
using namespace std;
const int N=2e5+10;
int t1[N],t2[N],c1[N];//辅助数组
void SA(int *s,int n,int sa[],int rnk[],int height[])//基数排序的版本中
{
    int m=300;
    int *sb=t1,*r=t2,*c=c1;
    for(int i=0; i<=m; ++i) c[i]=0;
    for(int i=1; i<=n; ++i) c[r[i]=s[i]]++;
    for(int i=1; i<=m; ++i) c[i]+=c[i-1];
    for(int i=n; i>=1; --i) sa[c[s[i]]--]=i;

    for(int k=1,p ; k < n; k<<=1 )
    {
        p=0;
        for(int i=n-k+1; i<=n; ++i) sb[++p]=i;
        for(int i=1; i<=n; ++i) if(sa[i]>k) sb[++p]=sa[i]-k;
        for(int i=0; i<=m; ++i) c[i]=0;
        for(int i=1; i<=n; ++i) c[r[i]]++;
        for(int i=1; i<=m; ++i) c[i]+=c[i-1];
        for(int i=n; i>=1; --i) sa[ c[r[sb[i]]]-- ]=sb[i];
        std::swap(r,sb);
        r[sa[1]]=p=1;
        for(int i=2,a,b; i<=n; ++i)
        {
            a=sa[i],b=sa[i-1];
            if(sb[a]==sb[b]&&(a+k<=n && b+k<=n&&sb[a+k]==sb[b+k]) ) r[a]=p;
            else r[a]=++p;
        }
        if(p>=n) break;//可以提前退出
        m=p;
    }
    int k=0;
    for(int i=1; i<=n; ++i) rnk[sa[i]]=i;
    height[1]=0;
    for(int i=1; i<=n; ++i)
    {
        if(k) k--;
        int j=sa[rnk[i]-1];
        if(j==0) continue;
        while(s[j+k]==s[i+k]) ++k;
        height[rnk[i]]=k;
    }
}
int rnk[N],sa[N],height[N]; //height[1]的值为0
int w[N];
string s[105];
int n,book[105],belong[N];
bool judge(int v,int ls,int k)//出现的长度为v,至少出现在k个字符串中
{
    mset(book,0);
    int c=0;
    if(belong[sa[1]]!=-1)   book[belong[sa[1]]]=1,c=1;
    int l=1;
    for(int i=2; i<=ls; ++i)
    {
        if(height[i]>=v)//i not is se
        {
            if(book[belong[sa[i]]]==0)//
            {
                book[belong[sa[i]]]=1;
                c++;
            }
        }
        else
        {
            l=i;
            if(c>=k) return true;
            mset(book,0);
            c=0;
            if(belong[sa[i]]!=-1)   book[belong[sa[i]]]=1,c=1;
        }
    }
    if(c>=k) return true;
    else return false;
}
void ptans(int v,int ls,int k)
{
    mset(book,0);
    int c=0;
    if(belong[sa[1]]!=-1)   book[belong[sa[1]]]=1,c=1;
    for(int i=2; i<=ls; ++i)
    {
        if(height[i]>=v)//i not is se
        {
            if(book[belong[sa[i]]]==0)//
            {
                book[belong[sa[i]]]=1;
                c++;
            }
        }
        else
        {
            if(c>=k)  //sa[i-1],len:v
            {
                for(int j=0; j<v; ++j)
                    printf("%c",char(w[sa[i-1]+j]-100));
                puts("");
            }
            mset(book,0);
            c=0;
            if(belong[sa[i]]!=-1)   book[belong[sa[i]]]=1,c=1;
        }
    }
    if(c>=k)  //sa[i-1],len:v
    {
        for(int j=0; j<v; ++j)
            printf("%c",char(w[sa[ls]+j]-100));
        puts("");
    }
}
int main()
{
    bool have=false;
    while(scanf("%d",&n),n)
    {
        if(have) puts("");
        have=true;
        int ls=0;
        for(int i=1; i<=n; ++i)
        {
            cin>>s[i];
            for(int j=0;j<s[i].size();++j)
            {
                w[++ls]=int(s[i][j])+100;
                belong[ls]=i;
            }
            w[++ls]=int(i);
            belong[ls]=-1;
        }
        if(n==1)
            cout<<s[1]<<endl;
        w[ls+1]=0;
        SA(w,ls,sa,rnk,height);
        int l=1,r=ls,ans=-1,k=(n+2)/2;
        while(l<=r)
        {
            int m=l+r>>1;
            if(judge(m,ls,k))
            {
                ans=m;
                l=m+1;
            }
            else r=m-1;
        }
        if(ans==-1)
            printf("?\n");
        else
            ptans(ans,ls,k);
    }
}
```


