

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


