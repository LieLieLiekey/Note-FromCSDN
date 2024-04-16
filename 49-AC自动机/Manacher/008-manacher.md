

先放下代码：

时间2018-4-9-19-58

 

```cpp
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#define N 2010000
#define INF 0x3f3f3f3f
#define MOD 10000
using namespace std;
char s[N],t[N];
int p[N];
void Preprocess(char* s)
{
    int s_len,cnt=0;
    s_len=strlen(s);
    t[cnt++]='$';
    for(int i=0; i<s_len; i++)
    {
        t[cnt++]='#';
        t[cnt++]=s[i];
    }//对s的处理变为t
    t[cnt++]='#';
    t[cnt++]='\0';
}
int manacher(char* t)
{
    int t_len,C,R,ans;
    t_len=strlen(t);
    p[0]=0,C=0,R=0;
    for(int i=1; i<t_len-1; i++) //求没一点为中心的最长回文串的半径
    {
        if(i<R)//利用回文特性
        {
            int j=2*C-i;
            p[i]=min(p[j],R-i);
            while(t[i+p[i]+1]==t[i-p[i]-1])
                    p[i]++;
            if(p[i]+i>=R)
            {
                C=i;
                R=p[i]+i;
            }
        }
        else//不能利用回文的特性
        {

            p[i]=0;
            while(t[i+p[i]+1]==t[i-p[i]-1])
                p[i]++;
            C=i;
            R=i+p[i];
        }
    }
    ans=-1;
    for(int i=1; i<t_len-1; i++)
    {
        ans=ans>p[i]?ans:p[i];
    }
    return ans;
}
int main()
{
    int k=0;
    while(~scanf("%s",s))
    {
        if(!strcmp(s,"END"))
        {
            return 0;
        }
        Preprocess(s);
        printf("Case %d: %d\n",++k,manacher(t));
    }
    return 0;
}```


 

