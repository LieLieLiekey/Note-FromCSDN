

       吉哥又想出了一个新的完美队形游戏！  　　假设有n个人按顺序站在他的面前，他们的身高分别是h[1], h[2] ... h[n]，吉哥希望从中挑出一些人，让这些人形成一个新的队形，新的队形若满足以下三点要求，则就是新的完美队形：  　　1、挑出的人保持原队形的相对顺序不变，且必须都是在原队形中连续的；  　　2、左右对称，假设有m个人形成新的队形，则第1个人和第m个人身高相同，第2个人和第m-1个人身高相同，依此类推，当然如果m是奇数，中间那个人可以任意；  　　3、从左到中间那个人，身高需保证不下降，如果用H表示新队形的高度，则H[1] <= H[2] <= H[3] .... <= H[mid]。  　　现在吉哥想知道：最多能选出多少人组成新的完美队形呢？

 

 

这道题正确解决方案就是manacher 判断下单调递增即可

```cpp
#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<stdlib.h>
#include<string.h>
using namespace std;
const int maxn=101000;
int  num[maxn];
int nn[maxn<<1];
int Lis[maxn<<1];
int Proprocess(const int* str,int len,int *p)//0 代表＃
{
    int top=0;
    p[top++]=-1;
    for(int i=0;i<len;++i)
    {
        p[top++]=0;
        p[top++]=str[i];
    }
    p[top++]=0;
    p[top]=-2;
    return top;
}
int  Mannacher(const int* str,int len)//经过预处理的字符串
{
    int r;//r为上一个中心对应的半径
    int mid=0;//中心
    memset(Lis,0,sizeof(Lis));
    for(int i=1;i<len;++i)//计算以i为中心的字符串的
    {
        if(i<=mid+r)
        {
            r=min(Lis[2*mid-i],mid-i+r);
        }
        else
            r=0;
        while(str[i+r+1]==str[i-r-1]&&str[i+r+1]<=str[i+r-1])//相等的情况下 保持递增
             r++;
        Lis[i]=r;
        mid=i;
    }
    int ans=-1;
    for(int i=1;i<len;++i)
        ans=ans>Lis[i]?ans:Lis[i];
    return ans;

}
int main()
{
    int t,n;
    scanf("%d",&t);
    while(t--)
    {
       scanf("%d",&n);
       for(int i=0;i<n;i++)
            scanf("%d",num+i);
       n=Proprocess(num,n,nn);
       int ans=Mannacher(nn,n);
       cout<<ans<<endl;
    }
}```


 

但是这道题我一次做的时候做错了  当时也想了一个o（n）的方法,  直接让下一个判断的中心为上一个回文串的右

边缘+1。因为疏忽上一个回文串可能全相等的情况 所以错了

放一个数据

1

12 50 50 50 50 50 50 50 50 50 50 50 50

 

错误代码（给自己提个醒）

```cpp
#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<stdlib.h>
#include<string.h>
using namespace std;
const int maxn=101000;
int  num[maxn];
int nn[maxn<<1];
int Lis[maxn<<1];
int Proprocess(const int* str,int len,int *p)//0 代表＃
{
    int top=0;
    p[top++]=-1;
    for(int i=0;i<len;++i)
    {
        p[top++]=0;
        p[top++]=str[i];
    }
    p[top++]=0;
    p[top]=-2;
//    for(int i=0;i<=top;++i)
//        cout<<p[i]<<" ";
//    cout<<endl;
    return top;
}
int  Mannacher(const int* str,int len)//经过预处理的字符串
{
    int mid,r,maxx;
    mid=0,r=0;
    memset(Lis,0,sizeof(Lis));
    for(int i=1;i<len;)//计算以i为中心的字符串的
    {
        maxx=str[i]?str[i]:300;//作为首先最大字符
        r=0;
        while(str[i+r+1]==str[i-r-1])
        {
             if(str[i+r+1])
             {
                 if(str[i+r+1]>maxx)//不符合
                    break;
                maxx=str[i+r+1];//符合 并且更换最大值
             }
             r++;
        }
        Lis[i]=r;
        mid=i;
        if(r)
           i=mid+r;
        else
            i=mid+r+1;//需要从0处开始
    }
    int ans=-1;
    for(int i=1;i<len;++i)
        ans=ans>Lis[i]?ans:Lis[i];
    return ans;

}
int main()
{
    int t,n;
    scanf("%d",&t);
    while(t--)
    {
       scanf("%d",&n);
       for(int i=0;i<n;i++)
            scanf("%d",num+i);
       n=Proprocess(num,n,nn);
       int ans=Mannacher(nn,n);
       cout<<ans<<endl;
    }
}```


 

