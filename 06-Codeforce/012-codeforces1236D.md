

## codeforces1236D.Alice and the Doll(贪心模拟)


**题目链接**：[传送门](https://codeforces.com/contest/1236/problem/D)

思路：

题意感觉描述的有点模糊（至此我还不太清楚是每个格子只能进行走一次，还是走多次，但是走一次的话代码就能A，如果走多次的话下面出的样例也能hack出代码的错误，但目前来看应该每个格子只能走一次，且只能左转一次）

因为每个格子只能走一起，且只能右转一次，所以我们前进的时候要尽可能多的走，从当前位置计算直线走到哪个位置可以用二分O(logn)求出位置。（蛇皮走位


3 5 5

1 4

1 5

3 3

3 4

3 5

No


```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=1e5+10;
/*
模拟蛇皮走位
不能走：
1.转弯后还是原位置不能动
*/
int n,m,k;
vector<int> row[N],col[N];
void work(int x,int y,int d)//
{
    //朝该方向走,走不动停止
    //0 1 2 3
    long long sum=1;
    int r1=0,r2=n+1,c1=0,c2=m+1;
    while(true)
    {
        if(d==0)
        {
            auto it=upper_bound(row[x].begin(),row[x].end(),y);
            int yy=*it-1;
            yy=min(yy,c2-1);
            if(yy==y) break;
            sum+=yy-y;
            y=yy;
            r1=x;
            d=1;
        }
        if(d==1)
        {
            auto it=upper_bound(col[y].begin(),col[y].end(),x);
            int xx=*it-1;
            xx=min(xx,r2-1);
            if(xx==x) break;
            sum+=xx-x;
            x=xx;
            c2=y;
            d=2;
        }
        if(d==2)
        {
            auto it=upper_bound(row[x].begin(),row[x].end(),y);
            int yy=*(--it)+1;
            yy=max(yy,c1+1);
            if(yy==y)
                break;
            sum+=y-yy;
            y=yy;
            r2=x;
            d=3;
        }
        if(d==3)
        {
            auto it=upper_bound(col[y].begin(),col[y].end(),x);
            int xx=*(--it)+1;
            xx=max(xx,r1+1);
            if(xx==x)
                break;
            sum+=x-xx;
            x=xx;
            c1=y;
            d=0;
        }
    }
    long long en=1ll*n*m-1ll*k;
    if(sum==en)
        puts("Yes");
    else
        puts("No");
}
int main()
{
    scanf("%d%d%d",&n,&m,&k);
    int flag=0;
    for(int i=1;i<=k;++i)
    {
        int x,y;
        if(x==1&&y==2) flag=1;
        scanf("%d%d",&x,&y);
        row[x].push_back(y);
        col[y].push_back(x);
    }
    for(int i=1;i<=n;++i)
    {
        row[i].push_back(0);
        row[i].push_back(m+1);
    }
    for(int i=1;i<=m;++i)
    {
        col[i].push_back(0);
        col[i].push_back(n+1);
    }
    for(int i=1;i<=n;++i)
        sort(row[i].begin(),row[i].end());
    for(int i=1;i<=m;++i)
        sort(col[i].begin(),col[i].end());
    int d=0;
    if(m==1||flag)
        d=1;
    work(1,1,d);
    return 0;
}

```


