

### [I - Beautiful People](https://vjudge.net/problem/ZOJ-2319)


[ZOJ - 2319 ](https://vjudge.net/problem/16158/origin)

##题意：

​ 给出 m 个人，每个人有两个属性：强壮度（s），美丽度（b），如果a的s，b中任意一个属性大于等于y的对应属性，另一个属性小于y，两个人就会打架。现在要办一个party，要求邀请尽可能多的人，并且他们不能打架。输出人数和每个人的编号（编号从1开始）

### 思路：


​ 这道题不难想象邀请最多的人 满足他们的S，B序列都是严格递增的。那么我们只要从所有人的S，B序列中找出所有的严格递增的个数中的最多的即可。

​ 我们将所有人按照S从小到大排序，如果S相同 就让B大的排在前面，然后找出S的最长严格递增子序列即可，并记录路径即可。（这样的话可以保证我们选取过程中S相同 的所有B中，B最多选一个）

​ 题目中的数据为


m:4

S: 1 1 2 2

B: 1 2 1 2

我们按规定排序后

S: 1 1 2 2

B: 2 1 2 1

我们选取**排序后**的第二个人和第四个人即可


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int inf=0x3f3f3f3f;
const int maxn=1e5+100;
struct Data
{
    int a,b,id;
} data[maxn];
bool operator <(const Data &aa,const Data &bb)
{
    if(aa.a==bb.a)
        return aa.b>bb.b;
    return aa.a<bb.a;
}
int S[maxn],pre[maxn],dp[maxn],lcsid[maxn];
vector<int> V;
int main()
{
    int t,fa=0;
    scanf("%d",&t);
    while(t--)
    {
        if(fa) puts("");
        fa=1;
        int n;
        scanf("%d",&n);
        for(int i=1; i<=n; ++i)
        {
            scanf("%d%d",&data[i].a,&data[i].b);
            data[i].id=i;
        }
        sort(data+1,data+n+1);
        for(int i=1; i<=n; ++i) S[i]=data[i].b;
        int len=0;
        mset(pre,-1);
        dp[0]=-1;
        lcsid[0]=-1;
        for(int i=1; i<=n; ++i)
        {
            int th=lower_bound(dp,dp+len+1,S[i])-dp;//th就是该元素该插入的位置，且他从上一个地方过来
            pre[i]=lcsid[th-1];
            lcsid[th]=i;
            dp[th]=S[i];
            len=max(len,th);
        }//pre[lcsid[len]]一直王回溯即可
        V.clear();
        for(int v=lcsid[len]; v!=-1; v=pre[v])
            V.push_back(v);
        printf("%d\n",V.size());
        for(int i=0; i<V.size(); ++i)
            printf("%d ",data[V[i]].id);
        puts("");
    }

    return 0;
}

```


