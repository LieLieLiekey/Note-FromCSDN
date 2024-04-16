

## 1284D. New Year and Conference(思路)


##### 比赛链接：[传送门](https://codeforces.com/problemset/problem/1284/D)



总结：

如何快速的判断一个区间集合是否都与某区间Q相交？

如果区间集合内存在一个区间A不与区间Q相交，那么一定满足区间A的右端点 小于 区间Q的左端点，或区间A的左端点 大于 区间Q的右端点，所以我们只需维护区间集合内 右端点最小的位置sp 和 左端点最大的位置ep，如果满足ep > Q.r 或sp < Q.l ，证明区间集合内存在某区间不与区间Q相交。

证明：一个区间集合是否都与某区间Q相交的充分必要条件是…(代指上面的一短句子)

充分性：区间集合都与区间Q相交，那么集合内所有区间的右端点 $x\ge l$，左端点$x \le r$，故右端点的最小值$sp \ge l$，左端点的最大值$ep \le r$.

必要性：显然


##### 思路：


对于敏感集合，一定能归结到一对区间敏感。

证明：敏感集合内一定对于某个地点内所有区间都不相交，另一个地点所有区存在相交，那么我们只需找出那一对相交的区间即为敏感的一堆区间。

我们可以遍历所有相交的区间，那么如何遍历呢？我们对于时间点x，维护一个集合S，这个集合内存储满足地点A的时间区间包含时间点x 的**地点B的时间区间**。即如果$a\le x\le b$，那么集合S内存储$(c,d)$。这个集合S很容易维护到，我们可以对于每个event，将事件$(a,b,c,d)$ 变成在时间点 $a$ 加入 $(c,d)$，时间点 $b+1$ 删除 $(c,d)$ 即可。

那么此时集合S内都是在事件点 $x$ 相交的地点B的区间，如果集合S中存在两个区间不相交，那么存在敏感的区间。在维护的过程中，我们只需判断新加入的区间是否与集合S的区间都相交即可。如何判断呢？

我们另需维护集合S中左端点的最大值ep和右端点的最小值sp，如果新加入的区间Q与集合S内某个区间不相交，那么一定有ep > Q.r 或sp < Q.l 。


退役后长时间不刷题思路退化了QAQ。


##### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int inf=0x3f3f3f3f;
const int N=3e5+10;
multiset<P> table;
multiset<int> mxtable,mitable;
struct node
{
    int x,l,r,flag;
    node() {}
    node(int x,int l,int r,int flag):x(x),l(l),r(r),flag(flag) {}
    bool operator < ( const node &o)
    {
        if(x!=o.x)
            return x < o.x;
        return flag < o.flag;
    }
} t[N];
int data[N][4];
/*
按照端点排序
for端点，从而进行add和del maintain Set
*/
void addme(int l,int r)
{
    table.insert(make_pair(l,r));
    mxtable.insert(l);
    mitable.insert(r);
}
void delme(int l,int r)
{
    auto it=table.find(make_pair(l,r));
    table.erase(it);
    mxtable.erase(mxtable.find(l));
    mitable.erase(mitable.find(r));

}
bool work(int n,int tol)
{
    table.clear();
    mxtable.clear();
    mitable.clear();
    mxtable.insert(-1);
    mitable.insert(inf);
    for(int i=0; i<tol; ++i)
    {
        int mx=(*mxtable.rbegin()),mi=*mitable.begin();
        if(t[i].flag==1)
        {
            if(mx > t[i].r||mi < t[i].l)
                return false;
            else
                addme(t[i].l,t[i].r);
        }
        else
            delme(t[i].l,t[i].r);
    }
    return true;
}
int main()
{
    int n;
    bool isok=true;
    scanf("%d",&n);
    for(int i=1; i<=n; ++i)
    {
        for(int k=0; k<4; ++k) scanf("%d",&data[i][k]);
    }
    int tol=0;
    for(int i=1; i<=n; ++i)
    {
        int a=data[i][0],b=data[i][1],c=data[i][2],d=data[i][3];
        t[tol++]=node(a,c,d,1);
        t[tol++]=node(b+1,c,d,-1);
    }
    sort(t,t+tol);
    isok=work(n,tol);
    if(isok)
    {
        tol=0;
        for(int i=1; i<=n; ++i)
        {
            int a=data[i][0],b=data[i][1],c=data[i][2],d=data[i][3];
            t[tol++]=node(c,a,b,1);
            t[tol++]=node(d+1,a,b,-1);
        }
        sort(t,t+tol);
        isok=work(n,tol);
    }
    printf("%s\n",isok?"Yes":"No");
    return 0;
}

```


