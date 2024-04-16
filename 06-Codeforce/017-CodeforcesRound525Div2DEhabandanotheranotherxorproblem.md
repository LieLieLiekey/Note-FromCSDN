

Codeforces Round #525 (Div. 2) D. Ehab and another another xor problem

链接：[https://codeforces.com/contest/1088/problem/D](https://codeforces.com/contest/1088/problem/D)

题意：


让你猜两个整数a b的值是多少。

你可以给出最多62次提问，

其中0<=a,b<230(也就是说二进制位最多30位)



提问方法就是你给他两个数c，d他会返回 1或-1或0

+ **1 if a⊕c>b⊕d**+ **0 if a⊕c=b⊕d**+ **-1 if a⊕c<b⊕d**



交互题


首先异或的性质

针对每个二进制位

1.与0异或之后 结果为本身

2.与1异或之后 相当于取反

3.自身与自身异或为0


如果正在判断从高位到低位的第k位,进行两次猜测，第一次将c d**第k位** 置为1 0异或后比较，第二次c,d**第k位**置为0 1异或后进行比较（c，d第k位前面的全置为对应a b已经确定过了，第k位后面的置为0）

a b此时的位有四种情况

a b

1 1 返回值分别为 -1 1

0 0 返回值分别为1 -1

1 0 返回值相同 由剩下的位确定

0 1 返回值相同 由剩下的位确定

由此可见

+  如果两个数对应的位相同就可以猜测两次确定出来 +  如果两个数对应的位不同 ，我们需要计算a，b的大小才能确定答案。


那么我们可以先开始的时候确定都异或0 0 判断ab的大小，如果出现位不同的，就可以根据ab的大小来确定位是多少，然后在根据当前返回值来确定剩下的位的大小关系。如果位相同就可以直接判断位是多少。每次分别异或1 0，异或0 1 结合上面判断就可确定30位的值，总共需要提问61次
 


```cpp
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<map>
#include<vector>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e3+10;
const int branch=26;
const int inf=0x3f3f3f3f;
int ask(int c,int d)
{
    printf("? %d %d\n",c,d);
    fflush(stdout);
    int ans;
    scanf("%d",&ans);
    return ans;
}
int main()
{
    int a,b;
    int aIsBiger=1;
    a=0,b=0;
    aIsBiger=ask(0,0);
    for(int i=29;~i;--i)
    {
            int x=ask(a|1<<i,b);//第i位为 1 0
            int y=ask(a,b|1<<i);//第i位为 0 1
            if(x==-1&&y==1)//同为1
            {
                if(x==-1)// 1 -1
                {
                    a|=1<<i;
                    b|=1<<i;
                }
            }
            else if(x==y)
            {
                if(aIsBiger==1)
                    a|=1<<i;
                else
                    b|=1<<i;
                aIsBiger=(x==1);
            }
    }
    printf("! %d %d\n",a,b);
    return 0;
}
```


