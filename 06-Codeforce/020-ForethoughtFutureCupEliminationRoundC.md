

## [Forethought Future Cup - Elimination Round](https://codeforces.com/contest/1146) C. Tree Diameter( 树的直径的性质)


### 题意：


```bash
		交互题，最多问9次，求一棵树的直径。每次给他两个不重复的顶点集合，后台返回这两个顶点集合的之间的最短距离
```


### 思路


​ 我们可以随便找一个顶点a，找出a顶点到的最远距离顶点假设为X，那么X必定为树的直径两端的一个顶点，然后求X到其他顶点的最大距离即为树的直径即可。

```cpp
#include<bits/stdc++.h>
using namespace std;
const int inf =0x3f3f3f3f;
int ask(int th,vector<int>& V)//第th个顶点  跟V顶点集合的询问
{
    printf("%d %d %d",1,V.size(),th);
    for(int i:V)
        printf(" %d",i);
    puts("");
    fflush(stdout);
    int ans;
    scanf("%d",&ans);
    return ans;
}
int main()
{
    int t,n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        vector<int> V;
        for(int i=2;i<=n;++i) V.push_back(i);
        int maxx=ask(1,V),l=2,r=n;
        V.clear();
        while(l!=r){
            int mid=(l+r)/2;
            for(int i=l;i<=mid;++i) V.push_back(i);
            int val=ask(1,V);
            if(val==maxx){
                r=mid;
            }
            else
                l=mid+1;
            V.clear();
        }
        int th=l;
        for(int i=1;i<=n;++i) if(i!=th) V.push_back(i);
        int ans=ask(th,V);
        printf("-1 %d\n",ans);
        fflush(stdout);
    }
}

```


