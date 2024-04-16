

### [Codeforces Round #552 (Div. 3)](https://codeforces.com/contest/1154) E Two Teams


#### 题意：


​ n个人排成一排，每个人都有一个iq，且iq不重复。现在给你一个k，且有两个教练编号为分别为1，2轮流进行以下操作

​ 该教练从排成的一行中找出iq最大的人加入自己的团队，且让iq最大的人左边的k个人和右边的k个人都加入自己的团队（如果人数不够k个，则只把剩余的加入即可）。

​ 现在问所有的人都被选出之后所处的团队编号。

#### 思路：


​ 我们需要维护两个信息

+ 一行人的编号的顺序，以及对应的iq.+ 此时所有人的iq最大的人的编号。


​ 我们第一个可以采用set容器实现；第二个使用map容器实现（也可以采用线段树维护），即让一个iq对应一个编号。

​ 那么每次删除中只要找到最大的iq对应的编号，然后在set容器中删除他左边和右边的信息，同时在map中删除对应的记录即可。 每次删除和查找的时间复杂度为logn，总体时间复杂度为nlogn 代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const ll MAXN=2e5+20;
const int MAX=100000;
const int inf=0x3f3f3f3f;
set<int> seq;
map<int,int> maxIQ;//val id
int n,k;
int ansb[MAXN],iq[MAXN];
int delleft(int id,int sign)
{
    int tot=0;
    set<int>::iterator it=seq.find(id);
    if(it==seq.begin())
        return tot;
    it--;
    while(tot<k)
    {
        tot++;
        if(it==seq.begin())
        {
            int id=*it;
            ansb[id]=sign;
            seq.erase(it--);
            maxIQ.erase(iq[id]);
            return tot;
        }
        else{
            int id=*it;
            ansb[id]=sign;
            seq.erase(it--);
            maxIQ.erase(iq[id]);
        }
    }
    return tot;
}
int delright(int id,int sign)
{

    int tot=0;
    set<int>::iterator it=seq.find(id);
    it++;
    while(it!=seq.end()&&tot<k)
    {
        int nowid=*it;
        int nowiq=iq[nowid];
        ansb[nowid]=sign;
        seq.erase(it++);
        maxIQ.erase(nowiq);
        tot++;;
    }
    return tot;
}
int main()
{
    scanf("%d %d",&n,&k);
    for(int i=1; i<=n; ++i)
    {
        scanf("%d",iq+i);
        seq.insert(i);
        maxIQ[iq[i]]=i;
    }
    int sign=0;
    mset(ansb,-1);
    int tot=n;
    while(tot)
    {
        int maxid=(maxIQ.rbegin()->second);
        int maxiq=maxIQ.rbegin()->first;
        tot-=delleft(maxid,sign);
        tot-=delright(maxid,sign);
        ansb[maxid]=sign;
        seq.erase(maxid);
        maxIQ.erase(maxiq);
        tot--;
        sign^=1;
    }
    for(int i=1;i<=n;++i)
        printf("%d",ansb[i]+1);
    puts("");
    return 0;
}

```


