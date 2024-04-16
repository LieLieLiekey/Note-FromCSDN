

#### 题目链接：[ Let Them Slide](https://codeforces.com/contest/1208/problem/E)


#### 题意：


现有n行w列的墙,每行有一排连续方块，一排方块可以左右连续滑动，且每个方块都有一个价值，第i 列的价值定义为这列的方块的价值和。求1到w列中每列的最大价值。注：如果一个位置没有方块，那么这个位置的价值为0

#### 思路：



我一直没想到可以这样实现，颠覆了我当时混乱的思想。


     对于第 $i$ 行的第 $j$ 个方块，如果这排方块的总长度为$cnt$，那么可以算出来该方块可以移动到$[j,w+j-cnt]$区间列，对于每一列（假设为 j ）我们可以使用两个vector分别记录第$j​$ 列添加的元素(行，值)，开始移除的元素(行,值)。

     那么我们就可以动态更新第 j 列每行的待选元素。 我们使用一个multiset[i]来表示当前列中第 $i$ 行待选的值，假设前面的已经维护好了，我们从第j列到第j+1列的时候，只需要对**j+1列中移除对应元素(行，值)**后更新对应的行对该列的贡献，第 **j+1列中添加对应元素(行，值)**后更新改行对该列的贡献即可，其他没有影响到的行还是上列的值。

#### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=1e6+20;
vector<P> add[N],rve[N];//row,val
multiset<int> nrow[N];
long long ans[N];
int main()
{
    int n,w;
    scanf("%d%d",&n,&w);
    for(int i=1; i<=n; ++i)
    {
        int cnt;
        scanf("%d",&cnt);
        for(int j=1; j<=cnt; ++j)
        {
            //[j,w+j-cnt]
            int x;
            scanf("%d",&x);
            add[j].push_back({i,x});
            rve[w+j-cnt+1].push_back({i,x});
        }
        if(cnt<w)
        {
            add[1].push_back({i,0});
            rve[w-cnt+1].push_back({i,0});
            add[cnt+1].push_back({i,0});
            rve[w+1].push_back({i,0});
        }
    }
    for(int i=1; i<=w; ++i) //第i列
    {
        for(P p:rve[i])
        {
            int id=p.first,v=p.second;
            ans[i]-=*nrow[id].rbegin();
            nrow[id].erase(nrow[id].find(v));
            ans[i]+=(nrow[id].empty()?0:*nrow[id].rbegin());
        }
        for(P p:add[i])
        {
            int id=p.first,v=p.second;
            ans[i]-=(nrow[id].empty()?0:*nrow[id].rbegin());
            nrow[id].insert(v);
            ans[i]+=(*nrow[id].rbegin());
        }
        if(i<w)
            ans[i+1]=ans[i];
    }
    for(int i=1; i<=w; ++i)
        printf("%lld ",ans[i]);
    return 0;
}

```


