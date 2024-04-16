

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


