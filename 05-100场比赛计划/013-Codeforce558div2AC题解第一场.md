

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

