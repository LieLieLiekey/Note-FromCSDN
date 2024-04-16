

## 2018 CCPC Final B - Balance of the Force


##### 题目链接：[传送门](https://codeforces.com/gym/102055/status)


##### 题意：


给定 $N$个人，每个人可以选择加入黑暗 DarkDark 或者光明 LightLight 两种阵营，他们加入不同的阵营之后获得的力量值是不同的，即 $D_i$ 和 $L_i$ 。然后有些人之间有矛盾，是不能加入同一阵营的，矛盾的对数共有 MM 对，现在给出所有的矛盾和所有的 $L_i,D_i$，问在所有可能存在的最终阵营分配情况中，力量值最大的人和力量值最小的人之间的差**最小**可能是多少？如果说不可能分配的话输出IMPOSSIBLE。其中 $1\le N\le 2*10^5,,0\le M\le 2*10^5,,1\le L_i D_i \le 10^9$ ,共20组test，时限4S

##### 思路：


因为每个联通块内对立的状态已经给出，首先很容易想到对每个联通块进行二分图染色，如果存在奇环就impossible，否则我们对二分图赋予状态（染色0的赋予状态L和染色0的赋予状态D），每种状态会产生一个最大值和最小值。

如果没有奇环，那么现在问题就转化为有k堆物品，每堆物品有要么取(maxx1,minn1)或(maxx2,minn2)，现在要求如何对每堆物品赋予状态使得k堆物品中maxx的最大值减去minn的最小值的差最小。

##### **这个问题与另一个问题相似**：


**n个物品，每个物品价值要么取$a_i$,要么取$b_i$ ，你对这n个物品赋值，求这n堆物品中的最大值减最小值最大为多少**。

这个问题的做法：我们首先称$a_i$和$b_i$是孪生的，即同一种类，但不可同时取。然后我们把所有$a_i$和 $b_i$ 从小到大排序，然后依次枚举最大值，然后用数据结构维护当前所有前面所有值的集合，更新答案。

我们从小到大遍历价值：

+ 首先把该值插入到数据结构中+ 如果至此出现种类数不够n的话，就不更新答案，然后进行下面操作。 
  
+ 如果该物品的孪生物品出现过的话，对孪生物品进行选择,因为现在只有最小值才能影响答案，从数据结构中删除孪生物品中最小的那个，只留下大的那个.+ 否则什么也不做
 + 如果至此出现种类数够n的话，更新答案 
  
+ 如果孪生物品在前面出现过，那么先将孪生物品从数据结构中删除，然后更新答案（该值减去数据结构中的最小值），然后再将孪生物品插入进数据结构+ 然后对孪生物品进行选择，从数据结构中删除孪生物品中最小的那个，只留下大的那个。
 


我们现在回到这个题，这个题跟上面基本一样，枚举最大值，更新答案，当出现孪生的话，我们选择最小值大的那个。

+ 按照maxx值从小到大排序，然后用数据结构维护至此出现的minn+ 每遍历到一个物品就加入minn，如果出现孪生物品就选择minn较大的那个（因为之后的maxx，只有minn会影响答案）


代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> P;
const int N=2e5+10;
const int inf=0x3f3f3f3f;
vector<int> g[N];
int prices[N][2],color[N];
vector<int> seq;
struct State
{
    int maxx,minn,id;
    State() {}
    State(int maxx,int minn,int id):maxx(maxx),minn(minn),id(id) {}
    bool operator < (const State &o) const
    {
        return maxx<o.maxx;
    }
};
vector<State> t;
bool dfs(int u,int c)
{
    seq.push_back(u);
    color[u]=c;
    for(int v:g[u])
    {
        if(color[v]==-1)
        {
            if(!dfs(v,c^1))
                return false;
        }
        else
        {
            if(color[v]==c)
                return false;
        }
    }
    return true;
}
int lastpos[N];//lastpos[id], 种类id出现的数组下标pos
void set_delete(multiset<int> & mst,int v)
{
    auto it=mst.find(v);
    mst.erase(it);
}
void work(int n,int cas)//n种物品,每种物品两个状态，每个状态属性(maxx,minn)
{
    int cnt=0;
    fill(lastpos,lastpos+n+1,-1);
    multiset<int> mst;
    int ans=inf;
    for(int i=0; i<int(t.size()); ++i)
    {
        int tmaxx=t[i].maxx,tminn=t[i].minn,tid=t[i].id;
        mst.insert(tminn);
        if(lastpos[tid]==-1)
        {
            cnt++;//孪生没有出现
            lastpos[tid]=i;
            if(cnt==n)
            {
                ans=min(ans,tmaxx-*mst.begin());
            }
        }
        else //孪生出现了
        {
            if(cnt==n)
            {
                set_delete(mst,t[lastpos[tid]].minn);
                ans=min(ans,tmaxx-*mst.begin());
                mst.insert(t[lastpos[tid]].minn);
            }
            set_delete(mst,min(t[lastpos[tid]].minn,tminn));
        }
    }
    printf("Case %d: %d\n",cas,ans);
}
int main()
{
    int T,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=1; i<=n; ++i)  g[i].clear();
        for(int i=1; i<=m; ++i)
        {
            int u,v;
            scanf("%d%d",&u,&v);
            g[u].push_back(v);
            g[v].push_back(u);
        }
        for(int i=1; i<=n; ++i)
            scanf("%d%d",&prices[i][0],&prices[i][1]);
        fill(color,color+n+1,-1);
        int kinds=0;
        bool isok=true;
        t.clear();
        for(int i=1; i<=n; ++i)
        {
            if(color[i]==-1)
            {
                seq.clear();
                kinds++;
                isok=dfs(i,0);
                if(!isok) break;
                int minn=inf,maxx=-1;
                for(int sign=0; sign<=1; ++sign)
                {
                    minn=inf,maxx=-1;
                    for(int a:seq)
                    {
                        if(color[a]==sign)
                        {
                            minn=min(minn,prices[a][0]);
                            maxx=max(maxx,prices[a][0]);
                        }
                        else
                        {
                            minn=min(minn,prices[a][1]);
                            maxx=max(maxx,prices[a][1]);
                        }
                    }
                    t.push_back(State(maxx,minn,kinds));
                }
            }
        }
        if(!isok)
        {
            printf("Case %d: IMPOSSIBLE\n",++cas);
            continue;
        }
        sort(t.begin(),t.end());
        work(kinds,++cas);
    }
}
```


