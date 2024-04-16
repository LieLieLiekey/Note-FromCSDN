

### E - Mondriaan’s Dream


Squares and rectangles fascinated the famous Dutch painter Piet Mondriaan. One night, after producing the drawings in his ‘toilet series’ (where he had to use his toilet paper to draw on, for all of his paper was filled with squares and rectangles), he dreamt of filling a large rectangle with small rectangles of width 2 and height 1 in varying ways. 
![./figures/91cd2a849209448a71d50fa577e5d5ed](./figures/91cd2a849209448a71d50fa577e5d5ed)
 Expert as he was in this material, he saw at a glance that he’ll need a computer to calculate the number of ways to fill the large rectangle whose dimensions were integer values, as well. Help him, so that his dream won’t turn into a nightmare!

**Input**

The input contains several test cases. Each test case is made up of two integer numbers: the height h and the width w of the large rectangle. Input is terminated by h=w=0. Otherwise, 1<=h,w<=11.

**Output**


![./figures/9275391b5c2fd4e3cb556e4ab10140b5](./figures/9275391b5c2fd4e3cb556e4ab10140b5)
For each test case, output the number of different ways the given rectangle can be filled with small rectangles of size 2 times 1. Assume the given large rectangle is oriented, i.e. count symmetrical tilings multiple times.

**Sample Input**

```bash
1 2
1 3
1 4
2 2
2 3
2 4
2 11
4 11
0 0
```


**Sample Output**

```bash
1
0
1
2
3
5
144
51205
```


#### 题意：


一个h*w规格的地方，用1*2的砖铺满，有多少种方法

#### 分析：



可跳过此处…

闲聊一下:

这题其实我是一开始就有思路的，并且思路是对的。但是我想看其他人的代码是怎么写的。

然后就发生了我看了20多篇博客（先看的他们的思路,一会一个用0，1一会一个用1，0表示）,

把我给整迷了，觉得大部分博客并没有说到重点，状态压缩谁都会，这题重点是判断上一行与此行的状态兼容。


**先从第一行说起**，对于每一列，1代表这个位置不**暂时**不铺砖。0代表这个位置铺 **横着的砖块**。则用w位的0，1的二进制数来表示砖块的情况，

​ 很容易看出 **连着的0**的**个数**必须**是偶数**

从第i(i>=2)行说起，对于每一列

+ 如果这一列的上一行是1，那么这个位置必须要是0，代表我铺上砖了,（且这个砖是竖着的）+ 如果这一列的上一行是0，但是这个位置可以是0，也可以是1。 但是要求这一行的状态与上一行的状态兼容，怎么兼容呢，如果对于每一列**出现（1，0）或者（0,1）代表这这砖是竖着的**，如果是**(0，0)代表这个砖是横着的**，**且不允许出现(1,1)的状态**(即上一行不铺，这一行也不铺)


可以看出此时需要满足两个条件

+ 不允许出现（1,1）的状态+ 竖着的砖之间的横着的地方是偶数个


然后针对每个状态，遍历上一行的所有状态，进行状态转移即可，答案在$dp[h][0]$里面

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x7fffffff;
int h,w;
//1代表不铺 0代表铺砖
ll dp[12][1<<11];
bool JudgeOne(int s)//判断这一行状态是否成立，1代表这个是竖着的，否则就是0(横着放的)
{
    //保证竖着的砖之间的0的个数是偶数个
    int cnt=0;
    for(int i=0; i<w; ++i)
    {
        if(s&1)
        {
            if(cnt&1)
                return 0;
        }
        else
            cnt++;
        s>>=1;
    }
    if(cnt&1)
        return 0;
    return 1;
}
/*
从第行开始需要两行结合到一起判断
1.(0 1)或者(1 0)都算作1
2.(1,1)不允许此状态
3.竖着放的之前的横着放的位置一定有偶数个
*/
int main()
{
    int top;
    while(~scanf("%d %d",&h,&w)&&h|w)
    {
        if(h<w)
            swap(h,w);
        if((h*w)&1)
        {
            printf("0\n");
            continue;
        }
        mset(dp,0);
        top=(1<<w);
        for(int s=0; s<top; ++s)
        {
            if(JudgeOne(s))
                dp[1][s]=1;
        }
        for(int i=2; i<=h; ++i)
        {
            for(int s=0; s<top; ++s)
            {
                for(int ss=0; ss<top; ++ss)
                {
                    if((s&ss)==0&&JudgeOne(s^ss))
                    {
                        dp[i][s]+=dp[i-1][ss];
                    }
                }
            }
        }
        printf("%I64d\n",dp[h][0]);
    }
    return 0;
}

```


