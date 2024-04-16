

### POJ - 3294 - Life Forms(后缀数组，二分+分组技巧)


#### 题目链接：[传送门](http://poj.org/problem?id=3294)


#### 思路：


+  part1 +  对于n个字符串，我们只需要找至少在n/2+1个字符串出现过的最长子串即可。 +  part2 +  如果k=1，我们只需输出最长的字符串即可（这里n肯定等于1，即本身） +  否则我们首先将这n个字符串用**不相同**的**特殊字符**连接成一个字符串S，并记录每个下标位置属于哪个字符串。 +  二分所求子串的长度w，然后在$height[]$数组上进行分组，即$height[]<w$的位置分割开，这样我们就得到了许多组，我们只需判断是否存在一组内有k个字符串的后缀即可。（因为后缀的最长相等前缀$>=w$不会跨越组，所以如果存在，答案一定在某个组内，否则也不存在，某个组存在最少k个字符串的后缀串，所以算法正确） +  part3 +  现在我们找到了这个最长子串长度w，我们只需模仿上面分组，如果组内有解就输出这个组的最长相同前缀即可。 


代码：

```cpp
#include<string>
#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string.h>
#define mset(a,b)   memset(a,b,sizeof(a))
typedef long long ll;
using namespace std;
const int N=2e5+10;
int t1[N],t2[N],c1[N];//辅助数组
void SA(int *s,int n,int sa[],int rnk[],int height[])//基数排序的版本中
{
    int m=300;
    int *sb=t1,*r=t2,*c=c1;
    for(int i=0; i<=m; ++i) c[i]=0;
    for(int i=1; i<=n; ++i) c[r[i]=s[i]]++;
    for(int i=1; i<=m; ++i) c[i]+=c[i-1];
    for(int i=n; i>=1; --i) sa[c[s[i]]--]=i;

    for(int k=1,p ; k < n; k<<=1 )
    {
        p=0;
        for(int i=n-k+1; i<=n; ++i) sb[++p]=i;
        for(int i=1; i<=n; ++i) if(sa[i]>k) sb[++p]=sa[i]-k;
        for(int i=0; i<=m; ++i) c[i]=0;
        for(int i=1; i<=n; ++i) c[r[i]]++;
        for(int i=1; i<=m; ++i) c[i]+=c[i-1];
        for(int i=n; i>=1; --i) sa[ c[r[sb[i]]]-- ]=sb[i];
        std::swap(r,sb);
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
    int k=0;
    for(int i=1; i<=n; ++i) rnk[sa[i]]=i;
    height[1]=0;
    for(int i=1; i<=n; ++i)
    {
        if(k) k--;
        int j=sa[rnk[i]-1];
        if(j==0) continue;
        while(s[j+k]==s[i+k]) ++k;
        height[rnk[i]]=k;
    }
}
int rnk[N],sa[N],height[N]; //height[1]的值为0
int w[N];
string s[105];
int n,book[105],belong[N];
bool judge(int v,int ls,int k)//出现的长度为v,至少出现在k个字符串中
{
    mset(book,0);
    int c=0;
    if(belong[sa[1]]!=-1)   book[belong[sa[1]]]=1,c=1;
    int l=1;
    for(int i=2; i<=ls; ++i)
    {
        if(height[i]>=v)//i not is se
        {
            if(book[belong[sa[i]]]==0)//
            {
                book[belong[sa[i]]]=1;
                c++;
            }
        }
        else
        {
            l=i;
            if(c>=k) return true;
            mset(book,0);
            c=0;
            if(belong[sa[i]]!=-1)   book[belong[sa[i]]]=1,c=1;
        }
    }
    if(c>=k) return true;
    else return false;
}
void ptans(int v,int ls,int k)
{
    mset(book,0);
    int c=0;
    if(belong[sa[1]]!=-1)   book[belong[sa[1]]]=1,c=1;
    for(int i=2; i<=ls; ++i)
    {
        if(height[i]>=v)//i not is se
        {
            if(book[belong[sa[i]]]==0)//
            {
                book[belong[sa[i]]]=1;
                c++;
            }
        }
        else
        {
            if(c>=k)  //sa[i-1],len:v
            {
                for(int j=0; j<v; ++j)
                    printf("%c",char(w[sa[i-1]+j]-100));
                puts("");
            }
            mset(book,0);
            c=0;
            if(belong[sa[i]]!=-1)   book[belong[sa[i]]]=1,c=1;
        }
    }
    if(c>=k)  //sa[i-1],len:v
    {
        for(int j=0; j<v; ++j)
            printf("%c",char(w[sa[ls]+j]-100));
        puts("");
    }
}
int main()
{
    bool have=false;
    while(scanf("%d",&n),n)
    {
        if(have) puts("");
        have=true;
        int ls=0;
        for(int i=1; i<=n; ++i)
        {
            cin>>s[i];
            for(int j=0;j<s[i].size();++j)
            {
                w[++ls]=int(s[i][j])+100;
                belong[ls]=i;
            }
            w[++ls]=int(i);
            belong[ls]=-1;
        }
        if(n==1)
            cout<<s[1]<<endl;
        w[ls+1]=0;
        SA(w,ls,sa,rnk,height);
        int l=1,r=ls,ans=-1,k=(n+2)/2;
        while(l<=r)
        {
            int m=l+r>>1;
            if(judge(m,ls,k))
            {
                ans=m;
                l=m+1;
            }
            else r=m-1;
        }
        if(ans==-1)
            printf("?\n");
        else
            ptans(ans,ls,k);
    }
}
```


