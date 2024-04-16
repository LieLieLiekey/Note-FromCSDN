

## 计蒜客- 2019计蒜之道D. “星云系统”（单调队列/单调栈）


**题意：**

​ 现在给定你一个字符串 $s$ 以及一个整数 $k$，请求出 $s$的字典序最小的长度为 $k$的子序列。

**数据范围：**

$0&lt;k≤∣s∣≤5000000$

**样例输入：**

```bash
helloworld
5
```


**样例输出：**

```bash
ellld
```


**思路：**

**假如我们先不考虑长度为k的限制我们应当怎么做？**

​ 我们以样例为例子。从左到右扫描字符串一遍：h、然后e，因为e的字典序比h小所以h不应该在e前面，所以把h删去，此时待选序列只有e；然后扫描l、l、o、r，此时待选序列中有ellor；然后扫描l，因为r比l大，所以r不应该在l之前，把r删除，同样o也是如此，现在待选序列就只剩elll；然后扫描d。按照前面的原理，所以elll都删去，现在待选序列中只有d。

不过前面的部分是否有些似曾相识，这不是符合单调栈的性质吗。所以前面的问题我们可以用单调栈来解决。

**那么现在有了长度为k的限制，我们应该怎么做？**

首先我们发现，假如字符串长度为n，那么想要答案最优就要从第1~(n-k+1)中取一个最小的字母。这个就相当于从单调栈中取栈底的元素，并删去（这个位置以及这个位置之前的都不能用了，但因为这个位置之前的在单调栈中不存在，故只删除这一个即可）。接下来取第二个字符，那么就是将第（n-k+2）加入单调栈，然后从单调栈中栈底元素并从单调栈删去。从单调栈中取栈底元素其实就是单调队列。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int inf=0x3f3f3f3f;
char s[5000000+10],st[5000000+10],ans[5000000+10];
int main()
{
    int k,p,top,ls;
    scanf("%s%d",s+1,&k);
    p=0,top=0;//p指向st队头
    ls=strlen(s+1);
    int w=ls-k+1;
    for(int i=1;i<=w;++i){//初始化，先找出(1~n-k+1)中字典序最小的字符串
        while(top>0&&s[i]<st[top-1]) top--;
        st[top++]=s[i];
    }
    int cnt=0;
    ans[cnt++]=st[p++];//取出栈底字符作为答案的第一个字符。
    for(int i=w+1;i<=ls;++i){//取剩下的k-1个字符
        while(top>p&&s[i]<st[top-1]) top--;
        st[top++]=s[i];
        ans[cnt++]=st[p++];
    }
    ans[cnt]='\0';
    printf("%s\n",ans);
    return 0;
}
```


单调队列用deque实现：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int inf=0x3f3f3f3f;
string s,ans;
deque<char> st;
int main()
{
    int k;
    ios::sync_with_stdio(false);cin.tie(0);
    cin>>s>>k;
    int w=s.length()-k;
    for(int i=0;i<=w;++i)
    {
        while(!st.empty()&&s[i]<st.back()) st.pop_back();
        st.push_back(s[i]);
    }
    ans+=st.front();
    st.pop_front();
    for(int i=w+1;i<s.length();++i){
        while(!st.empty()&&s[i]<st.back()) st.pop_back();
        st.push_back(s[i]);
        ans+=st.front();
        st.pop_front();
    }
    cout<<ans<<endl;
    return 0;
}
```




## HDU - 3706 Second My Problem First （单调队列）



这题与洛谷的滑动窗口那题比较像,不过那题是维护两个单调队列，不过这题只能用线性的方法做。而且还不能开1e7的数组，会MLE.


**题目：**

**题意：**

​ 给出一个n，A，B。其中$S_i=A^i \% B$ ,$T_i=Min(S_k), i-A &lt;= k &lt;= i, k &gt;= 1$ ,

**思路：**

​ 求对于$T_i$，求S中下标$[i-A,i]$中的最小值，我们那么前面大于$S_i$就可以舍去。这刚好符合单调队列的性质。所以可以为维护一个最小值单调队列。如果队首的下标小于i-A，就出队。

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
deque<P> q;
const int maxn=1e7+10;
ll S[maxn];
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    ll n,A,B;
    while(cin>>n>>A>>B)
    {
        q.clear();
        ll pdt=1,lasts=1ll;;//lasts记录上一次s的值
        for(ll i=1;i<=n;++i){
         ll val=lasts*A%B;
         lasts=val;
         ll l=max(i-A,1ll);
         while(!q.empty()&&q.back().second>=val) q.pop_back();
         q.push_back({i,val});
         while(!q.empty()&&q.front().first<l) q.pop_front();
         pdt=pdt*q.front().second%B;
        }
        cout<<pdt<<endl;
    }
    return 0;
}
```




题目：

题意：

给你一个长度为n的数组，要求一段**连续的子序列**满足子序列中最大值减去最小值在$[m,k]$范围内。求该子序列的最大长度。

思路：我们假设区间右边界为$i$，然后求下标$[1,i]$中满足最大值减去最小值在[m,k]范围内的最小左边界。我们可以用单调队列维护一个当前前缀最大值序列和最小值序列。可以用下列步骤描述：

+ 将下标为$i$的值加入单调队列。+ 查看**最大值单调队列队首**减去**最小值单调队列队首**<=k是否满足， 
  
+ 如果不满足，我们让其下标最靠左边的出队，再次判断，直至队列为空或满足<=k停止。+ 满足则进行令i=i+1继续进行第3步。
 + 在前面出队的时候记录下出队的最大下标即为now，那么now就是区间不能取的最大位置。+ 查看**最大值单调队列队首**减去**最小值单调队列队首**>=m是否满足，如果满足用此时最长满足的区间下标为$[now+1,i]$,更新答案。否则对于$i$不可能有满足条件的区间左端点，不更新答案，并判断i+1


代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
deque<int> q1,q2;
int A[100000+10];
int main()
{
    int n,m,k;
    while(~scanf("%d%d%d",&n,&m,&k))
    {
        q1.clear();q2.clear();
        for(int i=1;i<=n;++i) scanf("%d",A+i);
        int ans=0,no=0;//no为对于当前左边界
        for(int i=1;i<=n;++i){
            while(!q1.empty()&&A[i]>=A[q1.back()]) q1.pop_back();
            q1.push_back(i);
            while(!q2.empty()&&A[i]<=A[q2.back()]) q2.pop_back();
            q2.push_back(i);
            //去掉无效的值
            while(!q1.empty()&&!q2.empty()&&A[q1.front()]-A[q2.front()]>k)
            {
                if(q1.front()<q2.front()){
                    no=q1.front();
                    q1.pop_front();
                }
                else{
                    no=q2.front();
                    q2.pop_front();
                }
            }
            if(!q1.empty()&&!q2.empty()&&A[q1.front()]-A[q2.front()]>=m)
                ans=max(ans,i-no);
        }
        cout<<ans<<endl;
    }
}
```




## 洛谷1886滑动窗口（单调队列）


**题目：**

可以使用线段树或mulitset，时间复杂度是O(nlogn)。使用单调队列时间复杂度为O(n)

**思路：**

​ 用两个单调队列分别维护最大值和最小值。并记录下每个数的id，取时如果不在窗口范围则舍去。

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
deque<P> swmax;
deque<P> swmin;
vector<int> ansmax,ansmin;
vector<int> A(1000000+10);
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int n,k;
    cin>>n>>k;
    for(int i=1;i<=n;++i) cin>>A[i];
    for(int i=1;i<=k;++i){
        //维护max windows
        while(!swmax.empty()&&A[i]>=swmax.back().second) swmax.pop_back();
        swmax.push_back({i,A[i]});

        while(!swmin.empty()&&A[i]<=swmin.back().second) swmin.pop_back();
        swmin.push_back({i,A[i]});
    }
    ansmax.push_back(swmax.front().second);
    ansmin.push_back(swmin.front().second);
    for(int i=k+1;i<=n;++i){
        while(!swmax.empty()&&A[i]>=swmax.back().second) swmax.pop_back();
        swmax.push_back({i,A[i]});

        while(!swmin.empty()&&A[i]<=swmin.back().second) swmin.pop_back();
        swmin.push_back({i,A[i]});
        int l=i-k+1;

        while(swmax.front().first<l) swmax.pop_front();
        ansmax.push_back(swmax.front().second);

        while(swmin.front().first<l) swmin.pop_front();
        ansmin.push_back(swmin.front().second);
    }
    for(int i:ansmin){
        cout<<i<<" ";
    }
    cout<<endl;
    for(int i:ansmax){
        cout<<i<<" ";
    }
    cout<<endl;
}

```




## 单调队列和单调栈


我所认为的单调队列就是单调栈+取操作。


刚开始学单调栈的时候，翻开一篇单调栈的博客就能看到单调队列。后来才发现单调队列=单调栈+取栈底(出栈底)


### 单调栈


##### **什么是单调栈？**



来自某b乎：

**单调栈是**一种理解起来很容易，但是运用起来并不那么简单的数据结构。 一句话解释**单调栈**，就是一个**栈**，里面的元素的大小按照他们所在**栈**内的位置，满足一定的**单调**性。


**栈**这样的数据结构满足**先进后出**。假设一个数组从左到右依此进栈和出栈操作，我们令数组元素的值等于它在数组中的下标。那么在这个过程中栈中元素始终满足**栈底到栈顶的下标递增**。

**而单调栈是在栈的基础上有栈底到栈顶满足一定的单调性**。

##### 单调栈的性质是什么？


经过前面描述，我们可以知道，单调栈满足该栈中**栈底到栈顶元素的id递增且元素满足一定的单调性**

**而且必须保证随着时间的推移，栈内元素还满足单调栈的性质。**

数组中的元素只能进栈和出栈至多一次。所以时间复杂度为O(n)

##### 用到单调栈的场景？


说实话用到的都是单调的性质，一般都是用单调队列。


给你一个数组S。数组T的值$T_i=min(S_k) k\in(p_i,i)$,其中$p_i$小于$i$,且满足随着$i$的增大$p_i$不减小。

比如洛谷的滑动窗口题目



### 单调队列


如果把一个**单调栈的栈底看作单调队列的队首**，**单调栈的栈顶看作单调队列的队尾**，那么这个新的数据结构就是单调队列了。

单调队列与普通的队列有些不同，单调队列支持从队首删除，队尾添加和删除，故单调队列多使用deque实现。
**插入操作：**

​ 将元素插入单调队列中总是与队尾的元素比较，队尾元素不是更优就将队尾元素删除，**直到队列为空或该元素没队尾元素优**，**就将该元素加入队列**。
取操作：

​ 当需要取的时候就从队首取元素，如果队首元素的id不在要求的范围内就删除队首元素，然后再次进行取操作。

要求：

​ 而且必须保证随着时间的推移，栈内元素还满足单调栈的性质。

**下面举一些例题：**

洛谷的滑动窗口：[传送门](https://blog.csdn.net/Dch19990825/article/details/95009389)

2019计蒜之道复赛D题 “星云系统”：[传送门](https://blog.csdn.net/Dch19990825/article/details/95009147)

HDU - 3706 Second My Problem First :[传送门](https://blog.csdn.net/Dch19990825/article/details/95009206)

HDU3530 Subsequence 单调队列:[传送门](https://blog.csdn.net/Dch19990825/article/details/95009268) HDU-4122 Alice’s mooncake shop :[传送门](https://blog.csdn.net/Dch19990825/article/details/95032699)



### HDU-4122 Alice’s mooncake shop 单调队列


**题目：** [HDU - 4122 ](https://cn.vjudge.net/problem/25789/origin)

**题意：**

**输入：**

第一行两个数n,m. 代表n份订单 m小时制作月饼.

接下来有n行，每一行有订单的时间 （月 日 年 小时） 和 需要月饼的数量cnt .

接下来一行两个数T,timecost. 代表每个月饼的保质期为T 放冰箱每小时需要timecost的代价.

接下来有 $m$ 行，第$i$行代表第 $i-1$ 小时制作月饼的代价求完成所有月饼所需的代价.

**输出：**

求将所有订单完成的最小花费。

注：2000年1月1日0小时代表第0小时。

**思路：**

比较暴力的方法是

+ 处理出每个订单的时间和数量+ 对于每个订单期望找出时间(nowt-T,nowt)的最小花费。+ 每个订单用最小花费 $*$ 订单内月饼的个数来得到该订单的总最小花费。


显然这种方法时间复杂度为$T*m$,过大，不过看到这里都应该理解题意了。

我们使用单调队列，优先队列存储{时间,该时间的成本}。那么对于时间t，如果队尾处没有比此时更优，就删除队尾一个元素。如果此时有订单，就使用队首部处理该订单。

**代码：**

```cpp
/*
思路：
1.处理出每个订单的时间和数量
2.对于每个订单期望找出时间(T-nowt,nowt)的最小单位花费
3.处理出最小单位花费
或：代码是使用此种类方法
1.处理出每个订单的时间和数量,保证时间递增
2.遍历每个时间，处理出当当前时间的最小花费。然后查看该时间是否为下一个订单，如果是就从最小花费单调队列中出队至符合条件的一个。
*/#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
P order[2500+10];
deque<P> q;
map<string,ll> mmp;
ll getDay(ll y,ll m,ll d)//第y年m月d天
{
    ll sum=0;
    ll yy=y-1;
    sum=yy*365+(yy/4-yy/100+yy/400);
    for(ll i=1;i<m;++i){
        if(i==2) sum+=28+(((y%4==0&&y%100!=0)||y%400==0)?1:0);
        else if(i==1||i==3||i==5||i==7 ||i==8 ||i==10 ||i==12) sum+=31;
        else sum+=30;
    }
    sum+=d;
    return sum;
}
ll gethours(string mouth,ll day,ll year,ll hour)//2000-1-1 0是第0小时
{
    ll m=mmp[mouth],t=0;
    ll sum=getDay(year,m,day)-getDay(2000,1,0)-1;//从2000年开始到现在纯共有sum天
    sum*=24;
    sum+=hour;
    return sum;
}
void init()
{
    mmp["Jan"]=1,mmp["Feb"]=2,mmp["Mar"]=3,mmp["Apr"]=4,mmp["May"]=5,mmp["Jun"]=6,mmp["Jul"]=7,mmp["Aug"]=8;
    mmp["Sep"]=9,mmp["Oct"]=10,mmp["Nov"]=11,mmp["Dec"]=12;
}
int main()
{
    ll T,sum,timecost,n,m;
    ios::sync_with_stdio(false);cin.tie(0);
    init();
    while(cin>>n>>m,n)
    {
        q.clear();
        sum=0ll;
        string mouth;
        ll day,year,hour,cnt;
        for(ll i=1;i<=n;++i){
            cin>>mouth>>day>>year>>hour>>cnt;
            order[i].first=gethours(mouth,day,year,hour);
            order[i].second=cnt;
        }
        cin>>T>>timecost;
        ll p=1;
        for(ll i=0;i<m;++i){
            ll x;
            cin>>x;//第i次的花费
            while(!q.empty()&&((q.back().second+(i-q.back().first)*timecost)>=x)) q.pop_back();
                q.push_back({i,x});
            while(order[p].first==i){
                while(!q.empty()&&(q.front().first+T<i)) q.pop_front();
                ll cnt=order[p].second;
                sum+=cnt*(q.front().second+(i-q.front().first)*timecost);
                ++p;
            }
        }
        cout<<sum<<endl;
    }
    return 0;
}
```


