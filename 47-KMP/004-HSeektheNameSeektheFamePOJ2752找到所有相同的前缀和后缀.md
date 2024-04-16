

题目链接[http://poj.org/problem?id=2752](http://poj.org/problem?id=2752)

题意：

给你一个字符串str  找到一个字符串集合S  ，集合内的字符串都为str的前缀和后缀

 

 

思路：

如果这个字符串s在这个集合的话，那么s肯定是字符串str的一个匹配(⊙﹏⊙)能理解我意思吧

 

So KMP模板

```cpp
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#define INF 0x3f3f3f3f
using namespace std;
const int maxn=1010000;
int ans[maxn],net[maxn];
char str[maxn];
void GetNextval(char *str,int *net)
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
int main()
{
    int top;
    while(~scanf("%s",str))
    {
        int len=strlen(str);
        top=0;
        int k=len;
        GetNextval(str,net);
        while(k)
        {
            ans[top++]=k;
            k=net[k];
        }
        for(int i=top-1;~i;--i)
            printf("%d ",ans[i]);
        printf("\n");
    }
}
```


 

