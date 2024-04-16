

For each prefix of a given string S with N characters (each character has an ASCII code between 97 and 126, inclusive), we want to know whether the prefix is a periodic string. That is, for each i (2 <= i <= N) we want to know the largest K > 1 (if there is one) such that the prefix of S with length i can be written as A K , that is A concatenated K times, for some string A. Of course, we also want to know the period K. 

Input

The input file consists of several test cases. Each test case consists of two lines. The first one contains N (2 <= N <= 1 000 000) – the size of the string S. The second line contains the string S. The input file ends with a line, having the number zero on it. 

Output

For each test case, output “Test case #” and the consecutive test case number on a single line; then, for each prefix with length i that has a period K > 1, output the prefix size i and the period K separated by a single space; the prefix sizes must be in increasing order. Print a blank line after each test case. 

Sample Input

```
3
aaa
12
aabaabaabaab
0```


Sample Output

```
Test case #1
2 2
3 3

Test case #2
2 2
6 2
9 3
12 4```


 

 

题意：

给你一个长度为n的字符串  让你分别计算下标为0长度为1........n的字符串的周期字符串的出现次数k  

如果k大于1  输出长度i 和周期字符串的次数k

KMP扩展

**原理：**

**设T[i]为前i个字符串最小周期为T[i]  eg：aabaab   T[1]=1 ,T[2]=1,T[3]=3**

**设next[i]为前i个字符最多匹配前next[i]个字符（不包括自身  这里的next函数与KMP中函数意思有些更改  这里的next[i]等效于书上的nextval[i+1]-1）  eg:aabaab next[1]=0  next[2]=1  next[3]=0  next[4]=1 next[5]=2 next[6]=3**

**用语言来表达就是 **

**         如果i是个周期字符串必定有 I-next[i]=T[next[i]]   其周期T[i]=T[next[i]]**

**         并且如果i-next[i]=****T[next[i]]**** 那么  i必定是个周期字符周期为T[i]=****T[next[i]]**

**数学逻辑表达**

**if ** i-next[i]=T[next[i]]        命题A 

    **then**   i有不为自身的周期 即T[i]=T[next[i]]   命题B          //逻辑表达式 A->B;

**if  ** i有不为自身的周期  

     **then**    i-next[i]=T[next[i]]                                               //逻辑表达式B->A

(得出A==B)

第二个的逆否命题即为

if      i-next[i]!=T[next[i]]

     then I的周期为自身             //^A->^B

代码：

```cpp
#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;
const int maxn=1001000;
int net[maxn];//net[j] 下标为j的失配后 匹配到下标net[j]  即前j个字符串最大匹配为net[j]个
int T[maxn];//T[i]代表最小周期为T[i]
void Get_nextval(int *net,char *str)//这是求i以及i之前的最大匹配数目
{
    int len=strlen(str);
    net[0]=-1;
    int j=0,k=-1;
    while(j<len)//j为字符串的下标
    {
        if(k==-1||str[j]==str[k])
            net[++j]=++k;
        else
            k=net[k];
    }
}
int main()
{
    char str[maxn];
    int cas=0;
    int len;
    while(scanf("%d",&len)&&len)
    {
        scanf("%s",str);
        Get_nextval(net,str);
        printf("Test case #%d\n",++cas);
        T[0]=0;
        T[1]=1;
        int k;
        for(int i=2;i<=len;i++)
        {
            k=net[i];
            if(i-k==T[k])
            {
                 T[i]=T[k];
                 cout<<i<<" "<<i/T[i]<<endl;
            }
            else
                  T[i]=i;
        }
        cout<<endl;
    }
}```


 

 

