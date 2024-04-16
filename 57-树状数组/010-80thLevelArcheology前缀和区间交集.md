

### [I - 80-th Level Archeology](https://vjudge.net/problem/CodeForces-731D)（前缀和，区间交集）


[CodeForces - 731D ](https://vjudge.net/problem/525657/origin)

### 题意：


​ 给出n个串，一共有c种字母编号为1-c。然后描述每一个串。每一次可以使得所有串的所有字母编号+1（编号为c的变成1）.问最少多少次吼能够使得所有的串按照字典序递增

### 思路：


​ 我们只要保证相邻的两个串都递增即可。对于每两个串，我们求出假设我们旋转k次就可以使得着两个串递增。其中k的区间可以线性求出来。最后我们只要找出被区间覆盖n-1次的点即可。这个k就是答案。

​ 至于怎么线性求k的区间，因为两个串不管旋转多少次他们的大小都取决于最前面的不同的数。那么我们只要找到第一个不同的数字，分情况讨论从而得出k的区间。

### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int MAXN=1000000+20;
int MAX=1000000+10;
const int inf=0x3f3f3f3f;
int bt[MAXN];//  叶子存储相邻元素差
int num[2][500100];
int lowbit(int k)
{
    return k&-k;
}
void modify(int k,int val)
{
    while(k<=MAX)
    {
        bt[k]+=val;
        k+=lowbit(k);
    }
}
int getsum(int k)
{
    int ans=0;
    while(k>0)
    {
        ans+=bt[k];
        k-=lowbit(k);
    }
    return ans;
}
void addInterval(int l,int r)
{
//    if(l>r) return ;
    l++,r++;
    modify(l,1);
    modify(r+1,-1);
}
int main()
{
    int n,c,cur=0,flag=1;
    int lastcnt,cnt;
    scanf("%d%d",&n,&c);
    MAX=c+5;
    scanf("%d",&cnt);
    for(int i=0; i<cnt; ++i)
        scanf("%d",&num[cur][i]);
    lastcnt=cnt;
    cur^=1;
    for(int k=1; k<n; ++k)
    {
        scanf("%d",&cnt);
        for(int i=0; i<cnt; ++i)
            scanf("%d",&num[cur][i]);
        if(flag) //可能存在解
        {
            int sign=0;;
            for(int i=0; i<min(lastcnt,cnt); ++i)
            {
                if(num[cur][i]>num[cur^1][i])
                {
                    sign=1;
                    addInterval(0,c-num[cur][i]);
                    addInterval(c-num[cur^1][i]+1,c-1);
                    break;
                }
                else if(num[cur][i]<num[cur^1][i])
                {
                    sign=1;
                    addInterval(c-num[cur^1][i]+1,c-num[cur][i]);
                    break;
                }
            }
            if(sign==0)
            {
                if(lastcnt>cnt)//无解
                    flag=0;
                else
                    addInterval(0,c-1);
            }
        }
        lastcnt=cnt;
        cur^=1;
    }
    int ans=-1;
    if(flag)
    {
        for(int i=1; i<=c; ++i)
        {
            if(getsum(i)==n-1)
            {
                ans=i-1;
                break;
            }
        }
    }
    printf("%d\n",ans);
    return 0;
}

```


