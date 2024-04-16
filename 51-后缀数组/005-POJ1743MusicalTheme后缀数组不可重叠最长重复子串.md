

## POJ1743 Musical Theme (后缀数组，不可重叠最长重复子串)


#### 题目链接：[传送门](https://vjudge.net/problem/19231/origin)


### 思路：


​ 首先可以知道对于两个相同旋律的拍子(即两个拍子全部增加某个值后会相同)，假设长度为k，那么拍子的后k-1个数与他们的前一个数的差都是相同的。

​ 所以我们可以将数组转化为差数组，$d[1]=$无效值，然后要求从差数组中找到长度最长的两个子序列满足，子序列不重叠且间隔为至少1（如果这两个子序列挨着的话，那么对应的拍子就重叠了）

​ 所以我们可以二分这个子序列的长度，对于每个长度，我们根据$height[]$是否小于长度来进行分组，对于每个分组，如果这个组的下标最大值与最小值满足$max-min>=len+1​$,则这个解可以。

```cpp
#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string.h>
#define mset(a,b)   memset(a,b,sizeof(a))
typedef long long ll;
const int N=2e4+10;
int t1[N],t2[N],c1[N];//辅助数组
void SA(int *s,int n,int sa[],int rank[],int height[])//基数排序的版本中
{
    int m=200;//桶的大小,会在下面循环中变化,第一关键词r的最大值,初始时是字符的最大值,之后都<=n
    int *sb=t1,*r=t2,*c=c1;//辅助数组,分别为:基数排序所用的第二2,rak',cnt数组
    //用基数排序求出长度为1的sa[]和rank[],如果字符最大值较大,第一轮可以采用sort
    for(int i=0; i<=m; ++i) c[i]=0;
    for(int i=1; i<=n; ++i) c[r[i]=s[i]]++;
    for(int i=1; i<=m; ++i) c[i]+=c[i-1];
    for(int i=n; i>=1; --i) sa[c[s[i]]--]=i;

    for(int k=1,p ; k < n; k<<=1 ) //p是一个计数器，现在还没用。
    {
        //sb[i]:第二关键词排名为i的位置为sb[i]
        p=0;
        for(int i=n-k+1; i<=n; ++i) sb[++p]=i;
        for(int i=1; i<=n; ++i) if(sa[i]>k) sb[++p]=sa[i]-k;
        //基数排序求出2k长度的sa数组
        for(int i=0; i<=m; ++i) c[i]=0;
        for(int i=1; i<=n; ++i) c[r[i]]++;
        for(int i=1; i<=m; ++i) c[i]+=c[i-1];
        for(int i=n; i>=1; --i) sa[ c[r[sb[i]]]-- ]=sb[i];
        std::swap(r,sb);
        //现在要利用上轮的r和这轮的sa求这轮的r
        r[sa[1]]=p=1;
        for(int i=2,a,b; i<=n; ++i)
        {
            a=sa[i],b=sa[i-1];
            if(sb[a]==sb[b]&&(a+k<=n && b+k<=n&&sb[a+k]==sb[b+k]) ) r[a]=p;
            else r[a]=++p;
        }
        if(p>=n) break;//可以提前退出
        m=p;
    }
    /*计算高度数组*/
    int k=0;
    for(int i=1; i<=n; ++i) rank[sa[i]]=i;
    height[1]=0;
    for(int i=1; i<=n; ++i)
    {
        if(k) k--;
        int j=sa[rank[i]-1];
        if(j==0) continue;
        while(s[j+k]==s[i+k]) ++k;
        height[rank[i]]=k;
    }
}
int rank[N],sa[N],height[N]; //height[1]的值为0
int w[N],d[N];
/*
搞成差分数组 前缀相同长度至少为4的不重叠
*/
bool judge(int v,int n)//在v数组中能否构成长度>=v的不重叠子串
{
    //分成几个不相交的区间,求每个区间的
    int l=1,minn=sa[1],maxx=sa[1];
    for(int i=2;i<=n;++i)
    {
        if(height[i]>=v) {
            minn=std::min(minn,sa[i]);
            maxx=std::max(maxx,sa[i]);
        }
        else{
            if(maxx-minn>=v) return true;
            else minn=sa[i],maxx=sa[i];
        }
    }
    if(maxx-minn>=v+1) return true;
    else return false;
}
int main()
{
    int n;
    while(scanf("%d",&n),n)
    {
        for(int i=1;i<=n;++i) scanf("%d",w+i),d[i]=w[i]-w[i-1]+100;
        d[1]=0;
        d[n+1]=-1;
        SA(d,n,sa,rank,height);
        int l=4,r=n;
        int ans=-1;
        while(l<=r)
        {
            int m=l+r>>1;
            if(judge(m,n))
            {
                ans=m;
                l=m+1;
            }
            else r=m-1;
        }
        if(ans==-1)
            printf("0\n");
        else
            printf("%d\n",ans+1);
    }
    return 0;
}
```


