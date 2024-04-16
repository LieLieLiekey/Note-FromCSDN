

## HDU6184 Counting Stars（三元环统计）


**题目链接**：[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=6184)

**思路：**

​ 可以看到A struct是有一个重复边的两个三元环组成的，我们可以使用三元环统计的方法，这样每个三元环就会计算一次，我们对每条边记录下在多少个三元环，那么答案就是每条边的$C(cnt,2)$ 之和

三元环计数链接：[this](https://www.cnblogs.com/Dance-Of-Faith/p/9759794.html)

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef P Edge;
Edge edge[200005];
int degree[100005];
bool cmp(int x,int y)
{
    return degree[x]!=degree[y]?degree[x]<degree[y]:x<y;
}
vector<int> adja[100005];

int color[100005];
map<P,int> cunt;//记录边的出现次数
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,m;
    while(cin>>n>>m)
    {
        for(int i=1; i<=n; ++i)
        {
            adja[i].clear();
            degree[i]=0;
            color[i]=0;
        }
        cunt.clear();
        for(int i=1; i<=m; ++i)
        {
            int u,v;
            cin>>u>>v;
            edge[i].first=u;
            edge[i].second=v;
            ++degree[u];
            ++degree[v];
        }
        for(int i=1; i<=m; ++i)//把无向边变为有向边
        {
            int u=edge[i].first,v=edge[i].second;
            if(cmp(u,v))
                adja[u].push_back(v);
            else
                adja[v].push_back(u);
        }
        for(int u=1; u<=n; ++u)
        {
            for(int v:adja[u])
                color[v]=u;
            for(int v:adja[u])//枚举第1条边
            {
                for(int vv:adja[v]){//枚举第2条边
                    if(color[vv]==u){//是个三元环
                        cunt[{u,v}]++;
                        cunt[{v,vv}]++;
                        cunt[{u,vv}]++;
                    }
                }
            }
        }
        ll ans=0;
        for(auto p:cunt)
        {
            ll cnt=p.second;
            if(cnt>=2){
                ans+=(cnt*(cnt-1))/2;
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}

```


