

先放get_nextval（）函数的代码

```cpp
void get_nextval(const char str[],int *net)
{
    net[0]=-1;
    int j=0,k=-1,len;
    len=strlen(str);
    while(j<len)
    {
        if(k==-1||str[j]==str[k])
            net[++j]=++k;
        else
            k=net[k];
    }
}//在这个函数内数组下标是0开始的 
```


在这个函数内数组下标是0开始的 

**首先你要明白next数组的含义**

**next[j]的意思就是在下标j之前的字符串上  得出该字符串大的最大匹配数**

就像这样
![./figures/20180919092310259](./figures/20180919092310259)


 要求k最大即匹配数最多(两条黑线内的对应相等)(图不好先凑合一下 有时间找大牛给补下图)

 

好的 现在咱们开始分析get_next函数

next[0]=-1（代表没有最大匹配 应该将i指针右移动）

假设next[j]=k成立  且0<=k<j (k！=j保证最大匹配数不为自己本身)

1.如果str[j]==str[k]的话str[j+1]=k+1

          因为如果还存在str[j+1]>k+1的话即 str[j]>k  这与假设不成立    所以 str[j+1]=k+1

2.如果str[j]!=str[k]的话 

          那就一直找k=next[k]直至 str[j]=str[k]  然后令str[j+1]=k+1


![./figures/20180919103801616](./figures/20180919103801616)


也许很多人对第二个条件不太明白，那么下面咱们来证明第二个条件的正确性，

**刚开始我一直有一个疑问 为什么next[j+1]的值一定会通过这个方法找出来呢  万一存在一个更长的字符串与之匹配呢**


![./figures/201809191101104](./figures/201809191101104)


好的  现在来看一下图  ， 假设我们通过第二个条件找到答案是k3即str[j]==str[k3] ，  但存在一个k'没有通过第二个条件找到（且k'>k3 要求k'更长）使得 str[0]......str[k']==str[j-k']......str[j]（前k'+1个字符相等） 即next[j+1]=k'+1   

**此时k'>k3  且k'没有被第二个条件所找到**

因为k3<k'<j    那么 k'的长度一定在找到的k之间

**假设在k'的长度在k1和k2之间 且k2<k'<k1,那么k1判断之后发现str[j]!=str[k1]，下一步k2=next[k1]， 但是因为k2<k'<k1,即k2并不是k1的最大匹配， k'的匹配比k2更大 next[k1]的值应该是k';**

与假设next[k1]==k2矛盾 


![./figures/201809191101104](./figures/201809191101104)


故不存在一个没有找到过的k'   使得k'>k3且 str[0]......str[k']==str[j-k']......str[j]str[j]==str[k']

所以next[j+1]的值肯定能从第二个条件找到。

 

get_nextval（）函数还有一点可能有人有疑问，为什么当k=-1时 也执行next[++j]=++k

因为当k==-1时 必定有过一次k=0且str[j]!=str[0]   即没有   以0为下标的字串 与  j之前的字符串 匹配 返回-1 此时因该让next[j+1]=0

 

数学归纳法

初始条件:next[0]=-1 符合题意  

假设当n<=j    时候next[j]符合题意 

又因为当n=j+1 时 由next[j+1]也符合题意

所以算法正确

 

```cpp
/*
字符串kmp
*/
#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=1010;
void get_nextval(const char str[],int *net)
{
    net[0]=-1;
    int j=0,k=-1,len;
    len=strlen(str);
    while(j<len)
    {
        if(k==-1||str[j]==str[k])
            net[++j]=++k;
        else
            k=net[k];
    }
}
int kmp(const char ss[],const char tt[])//参数传两个主川和模式串  返回值-1或者在主串中匹配的位置
{
    int *net=new int[maxn];
    int ls,lt,i=0,j=0;
    ls=strlen(ss);
    lt=strlen(tt);
    get_nextval(tt,net);
    while(i<ls&&j<lt&&(ls-i)>=(lt-j))
    {
        while(j!=-1&&ss[i]!=tt[j])
        {
            j=net[j];
        }
        i++;
        j++;
    }
    delete []net;
    if(j>=lt)
        return (i-j+1);
    return -1;
}
int main()
{
    char ss[maxn],tt[maxn];
    while(~scanf("%s %s",ss,tt))
    {
        int ans=kmp(ss,tt);
        if(ans==-1)
            cout<<"未匹配"<<endl;
        else
        {
            cout<<"从主串的第 "<<ans<<" 个存在匹配"<<endl;
        }
    }
}
```


 

