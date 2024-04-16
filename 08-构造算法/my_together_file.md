

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




## [2013年NOIP全国联赛提高组](http://129.211.20.246/problemset.php?search=2013%E5%B9%B4NOIP%E5%85%A8%E5%9B%BD%E8%81%94%E8%B5%9B%E6%8F%90%E9%AB%98%E7%BB%84) ### 1039: 火柴排队


### 思路：


​ 我们只需保证交换后左边的第K大跟右边的第K大在同一个位置即可。对于左边数组A，右边的数组为B，数组B中第i个数是第k大，所以我们需要把A数组中第k大的数放到第i个。根据这样可以构造一个数组，数组中第 $i i$ 个值 $a [ i ] a[i]$ 代表数组A中第 $i i$ 个数是第k大，且B数组中第k大的位置是$a [ i ] a[i]$

故我们求逆序数即可。

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n;
ll A[100005],B[100005],pos[100005],seq[100005];
ll sa```




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




## codeforec 1208C Magic Grid（构造题）


题目链接：[传送门](https://codeforces.com/problemset/problem/1208/C)

**题意：**

​ 给你一个n，满足n是4的倍数。让你构造一个$n ∗ n n*n$的矩阵，满足该矩阵的元素分别为$0 0$ 到$n ∗ n − 1 n*n-1$。且不重复。还要满足矩阵每一行每一列元素的异或值都相同

**思路：**

​ 这两天发现了异或的另一个性质：



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


