

## 1194E. Count The Rectangles（树状数组，离线扫描线）


##### 题目链接：[传送门](https://codeforces.com/problemset/problem/1194/E)


##### 思路：


首先看数据范围，$n\le5000$，我们首先处理出所有水平线段和垂直线段，然后将水平线段从低到高排序。

我们从低到高处理每条水平线段（计算出以该水平线段为底的矩形的数量）。

假设现在是第 i 条水平线段，首先我们 O(n) 处理出所有与该线段相交的垂直线段，然后记录与相交的垂直线段的最高点。我们现在维护这个最高点集合（用树状数组，用点的横坐标当下标，记录某一横坐标范围内点的数量）。

之后我们遍历**剩下的**水平线段（比 i 靠后的），假设现在遍历的是第 j 条水平线段，那么我们将集合中低于第 j 条水平线段的点从集合中删除，之后统计在第 j 条线段横坐标范围内的点的数量，这些点代表的垂直线段就与该两条水平线段相交，假设有cnt个，那么这两条水平线段围成的矩形就有 $cnt*(cnt-1)/2$ 个,我们遍历完所有剩下的水平线段并向上面那样维护就可以计算出所有以第 i 条线段为底的矩形的数量。

总的时间复杂度为 $O(n^2logn)$

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int N=5e3+10;
const int MAXN=1e4+10;
struct HorizontalLine{
    int x1,x2,y;
    HorizontalLine(){}
    HorizontalLine(int y,int x1,int x2):y(y),x1(x1),x2(x2){}
    bool operator <(const HorizontalLine &o) const
    {
        return y<o.y;
    }
};
vector<HorizontalLine> hl;
struct VerticalLine{
    int x,y1,y2;
    VerticalLine(){}
    VerticalLine(int x,int y1,int y2):x(x),y1(y1),y2(y2){}
    bool operator < (const VerticalLine &o) const
    {
        return y2<o.y2;
    }
};
vector<VerticalLine> vl;
struct Point{
    int x,y;
    Point(){}
    Point(int x,int y):x(x),y(y){}
    bool operator < (const Point &o) const
    {
        return y<o.y;
    }
}po[N];
struct BITtree{
    int bt[N*2];
    int lowbit(int k)
    {
        return k&-k;
    }
    void add(int k,int val)
    {
        while(k<=MAXN)
        {
            bt[k]+=val;
            k+=lowbit(k);
        }
    }
    int getpre(int k)
    {
        int ans=0;
        while(k)
        {
            ans+=bt[k];
            k-=lowbit(k);
        }
        return ans;
    }
    int getlr(int l,int r)
    {
        return getpre(r)-getpre(l-1);
    }
}ooo;
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;++i)
    {
        int x1,x2,y1,y2;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        x1+=5001;
        x2+=5001;
        if(x1 > x2)
            swap(x1,x2);
        if(y1 > y2)
            swap(y1,y2);
        if(x1==x2)
        {
            vl.push_back(VerticalLine(x1,y1,y2));
        }
        else{
            hl.push_back(HorizontalLine(y1,x1,x2));
        }
    }
    sort(hl.begin(),hl.end());
    sort(vl.begin(),vl.end());
    long long ans=0;
    for(int i=0;i<int(hl.size());++i)
    {
        int y=hl[i].y,x1=hl[i].x1,x2=hl[i].x2;
        int top=0;
        for(int j=0;j<int(vl.size());++j)
        {
            if(vl[j].x<=x2&&vl[j].x>=x1&&vl[j].y1<=y&&vl[j].y2>=y)
            {
                po[top++]=Point(vl[j].x,vl[j].y2);
                ooo.add(vl[j].x,1);
            }
        }
        int p=0;//未添加的位置
        for(int j=i+1;j<int(hl.size());++j)
        {
            while(p<top&&po[p].y<hl[j].y)
            {
                ooo.add(po[p].x,-1);
                ++p;
            }
            int cnt=ooo.getlr(hl[j].x1,hl[j].x2);
            ans+=1ll*cnt*(cnt-1)/2;
        }
        while(p<top)
        {
            ooo.add(po[p].x,-1);
            ++p;
        }
    }
    printf("%lld\n",ans);
    return 0;
}

```


