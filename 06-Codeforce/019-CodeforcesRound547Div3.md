

### A. Game 23


思路：

深搜即可

```
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
typedef long long ll;
using namespace std;
const int maxn=120;
const int inf=0x3f3f3f3f;
ll m;
int dfs(ll val,int s)
{
    if(val==m)
        return s;
    if(val>m)
        return -1;
    int ans=dfs(val*2ll,s+1);
    if(ans!=-1)
        return ans;
    ans=dfs(val*3ll,s+1);
    return ans;
}
int main()
{
    ll n;
    cin>>n>>m;
    cout<<dfs(n,0);
    return 0;
}
```


B. Maximal Continuous Rest

思路：

把序列*2 ，找出最长连续1即可

```
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
typedef long long ll;
using namespace std;
const int maxn=4e5+100;
const int inf=0x3f3f3f3f;
int Tt[maxn];
int n;
int main()
{
    cin>>n;
    for(int i=0; i<n; ++i)
    {
        cin>>Tt[i];
        Tt[i+n]=Tt[i];
    }
    int ans=0,maxx=0;
    for(int i=0; i<2*n; ++i)
    {
        if(Tt[i]==0){
            ans=0;
            continue;
        }
        if(i==0||Tt[i]==Tt[i-1])
            ans++;
        else
            ans=1;
        maxx=max(maxx,ans);
    }
    cout<<maxx<<endl;
    return 0;
}
```


C. Polycarp Restores Permutation

思路：

将所有的$p i p_{i}$

