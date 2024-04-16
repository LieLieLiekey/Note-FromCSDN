

看代码解释

```cpp
/*
求逆元
费马小定理
a^(p-1)=1(mod p)
故
a^(p-2)=1/a(mod p)
inv(a)(a关于p的逆元)=a^(p-2)
*/

#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<string>
#include<iostream>
#include<cstdlib>
#define N 1010
#define INF 0x3f3f3f3f
#define WC 1e-6
typedef long long LL;
using namespace std;
LL ksm(LL a,LL b,LL MOD)
{
    LL ans=1;
    while(b)
    {
        if(b&1)
            ans=(ans*a)%MOD;
        a=(a*a)%MOD;
        b/=2;
    }
    return ans;
}
LL inv(LL a,LL p)
{
    return ksm(a,p-2,p);
}
int main()
{
    LL n,p;
    while(~scanf("%lld %lld",&n,&p))
    {
        printf("inv( %lld )of %lld=%lld\n",n,p,inv(n,p));
    }
}```


