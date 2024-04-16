

## 1243E - Sum Balance（状压DP，图）

题目链接：[1243E - Sum Balance](https://codeforces.com/problemset/problem/1243/E)
题意：

给一个K，代表有K个箱子。第 $i$ 个箱子有 $n_i$ 个物品，价值分别为$a_{i,1},a_{i,2}...a_{i,n_i}$。

现在分别从K个箱子中取精确的一个物品，并放回K个箱子（每个箱子精确放一个），要求最后的所有箱子内物品价值相等。并输出方案。**保证所有物品的价值唯一**。

$k\in[1,15],n_i\in[1,5000],a_{i,j}\in[-1e9,1e9]$
思路：

每个箱子取出一个物品，并放入一个箱子，若此刻我们将箱子看成顶点，取放的过程看作一条有向边，那么这里有K个箱子K条边，且每个顶点的出度和入度都等于1，显然这个图是由若干个简单环组成的。

首先如果所有物品的总和不是 $K$ 的倍数，那么无解。否则我们将物品总和除以K，结果设为 $ave$。

因为保证所有的价值唯一，那么我们将所有物品看作顶点，我们记录第 $i$ 个箱子的总和是 $sum[i]$ ,对于第 $i$ 个箱子的物品 $a$ ,我们令 $b=ave-(sum[i]-a)$，即将物品 a 拿走后，将物品 b 放到箱子 $i$ 中可保证箱子总和为 $ave$，

**此时若物品 b 存在**且（（**物品b不在箱子 $i$ 中**）或（**在箱子 $i$ 中且是物品a** ））。我们就让 $a$ 向 $b$ 连接一条边。

这样我么形成了一个图，且每个顶点的出度为1，现在我们给顶点覆上颜色，颜色为所属箱子，然后求出图中所有的环，且环内颜色互不相同。

如果我们能组合出一组环，使得所有环的所有颜色互不相同且总颜色种类等于K，那么这个就是答案。对于这一步，我们实现的时候可以使用状压DP，记录每个环的状态和每个环内的边，然后状压DP即可，状态转移的时候用状态的枚举子集优化，时间复杂度可以达到$3^k$。

记录每个顶点的颜色可以使用map，这样总体的时间复杂度为$O(k*alln+alln*log(alln))+3^k$

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const int N=18;
vector<ll> box[N];
ll sum[N];
unordered_map<ll,ll> color;
int dp[1<<N];
vector<P> take[1<<N];
unordered_map<ll,ll> to;
/*
记录每个点的颜色，以及箱子的和
1.建图
2.找环 并记录过程
3.dp并记录过程
*/
P ans[N];
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin>>n;
    ll allsum=0;
    for(int i=0; i<n; ++i)
    {
        ll k;
        cin>>k;
        box[i].resize(k);
        sum[i]=0;
        for(int j=0; j<k; ++j)
        {
            cin>>box[i][j];
            allsum+=box[i][j];
            sum[i]+=box[i][j];
            color[box[i][j]]=i;
        }
    }
    if(allsum%n!=0)
    {
        cout<<"No"<<'\n';
        return 0;
    }
    allsum/=n;
    for(int i=0; i<n; ++i)
    {
        for(ll v:box[i])
        {
            ll need=allsum-(sum[i]-v);
            auto it=color.find(need);
            if(it!=color.end())
            {
                ll w=it->second;
                if(w!=i||need==v)
                    to[v]=need;
            }
        }
    }
    for(int i=0; i < n; ++i)
    {
        for(ll v:box[i])
        {
            int S=0;
            bool isok=true;
            ll cur=v;
            vector<P> place;
            do
            {
                if( (S&(1<<color[cur])) !=0){
                    isok=false;
                    break;
                }
                S|=1<<color[cur];
                auto it=to.find(cur);
                if(it!=to.end())
                {
                    place.push_back(make_pair(it->second,color[cur]));//什么物品放到哪个箱子
                    cur=it->second;
                }
                else
                {
                    isok=false;
                    break;
                }

            }
            while(cur!=v);
            if(isok==true)
            {
                dp[S]=1;
                take[S]=place;
            }
        }
    }
    for(int i=0;i<(1<<n);++i){
        if(dp[i])
            continue;
        for(int sub=i;sub!=0;sub=(sub-1)&i)
        {
            int o=i^sub;
            if(dp[sub]&&dp[o])
            {
                dp[i]=1;
                take[i]=take[sub];
                take[i].insert(take[i].end(),take[o].begin(),take[o].end());
                break;
            }
        }
    }
    if(!dp[(1<<n)-1]){
        cout<<"No"<<'\n';
        return 0;
    }
    cout<<"Yes"<<'\n';
    for(P &p:take[(1<<n)-1]){
        ll val=p.first, id=p.second;
        ans[color[val]]=make_pair(val,id);
    }
    for(int i=0;i<n;++i)
        cout<<ans[i].first<<" "<<ans[i].second+1<<endl;
    return 0;
}

```


