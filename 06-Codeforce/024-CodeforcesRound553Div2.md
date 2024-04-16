

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


