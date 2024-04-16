

### B - Bound Found


Signals of most probably extra-terrestrial origin have been received and digitalized by The Aeronautic and Space Administration (that must be going through a defiant phase: “But I want to use feet, not meters!”). Each signal seems to come in two parts: a sequence of n integer values and a non-negative integer t. We’ll not go into details, but researchers found out that a signal encodes two integer values. These can be found as the lower and upper bound of a subrange of the sequence whose absolute value of its sum is closest to t.

You are given the sequence of n integers and the non-negative target t. You are to find a non-empty range of the sequence (i.e. a continuous subsequence) and output its lower index l and its upper index u. The absolute value of the sum of the values of the sequence from the l-th to the u-th element (inclusive) must be at least as close to t as the absolute value of the sum of any other non-empty range.

**Input**

The input file contains several test cases. Each test case starts with two numbers n and k. Input is terminated by n=k=0. Otherwise, 1<=n<=100000 and there follow n integers with absolute values <=10000 which constitute the sequence. Then follow k queries for this sequence. Each query is a target t with 0<=t<=1000000000.

**Output**

For each query output 3 numbers on a line: some closest absolute sum and the lower and upper indices of some range where this absolute sum is achieved. Possible indices start with 1 and go up to n.

**Sample Input**


5 1 -10 -5 0 5 10 3 10 2 -9 8 -7 6 -5 4 -3 2 -1 0 5 11 15 2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 15 100 0 0


**Sample Output**


5 4 4 5 2 8 9 1 1 15 1 15 15 1 15


##### 题意：


给你n个数，q次询问，每次询问给出一个t，让你从中找出一个**非空区间**，使得**区间和的绝对值**与t最接近。

##### 分析：


题目中重点是**区间绝对值**与t接近！

对尺取法有自己好的理解可以跳过


尺取法的原理：就像尺取虫一样，求解，《挑战程序设计竞赛》提出尺取法是建立在这样的一个模型上:

+ 找连续区间的问题，如果对于左端点s，第一个满足条件的右端点是t，那么对于左端点s+1,第一个满足条件的右端点是t’>=t


那么求所有的满足条件的区间就可以像尺取虫爬行的方式求解。


所以我们可以求出前缀和数组，对前缀和数组排序，对于一个左端点l，找出第一个右端点r，满足区间对应的值>=t，对于左端点 l 区间和绝对值最接近t的就在此时的r和r-1处中取，只需要在r在递增的过程中不停的更新最小值即可。

**没疑问的可以跳过**


可能会产生这个疑问

找到第一个l对应的r之后，对于l+1他的右端点是r’>=r，那么左端点逼近之后(l++)为什么不更新下此时的l与r-1区间是否可能是答案？

答：因为l与r-1已经更新过答案，又因为l+1与r-1的区间的绝对值肯定比t小，而且比l与r-1的区间的绝对值更小，所以答案不可能在l+1与r-1对应的区间。

所以l++即可，不用在此时判断与r-1的区间的绝对值有无可能在答案。


代码：

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
const ll MOD=1e9+7;
struct Node{
    int val,id;
}a[maxn];
bool operator <(Node a,Node b)
{
    return a.val<b.val;
}
int main()
{
    int n,q,t;
    int nval;
    while(scanf("%d%d",&n,&q)&&(n|q))
    {
        a[0].val=0;
        a[0].id=0;
        for(int i=1;i<=n;++i)
        {
            int val;
            scanf("%d",&val);
            a[i].val=a[i-1].val+val;
            a[i].id=i;
        }
        sort(a,a+n+1);
        int al,ar,sum,l,r,minn;
        while(q--)
        {
            scanf("%d",&t);
            l=0,r=1;
            minn=inf;//区间绝对值与t之差的绝对值
            for(;;)
            {
                while(r<=n)
                {
                    nval=a[r].val-a[l].val;
                    if(abs(nval-t)<minn)
                    {
                        minn=abs(nval-t);
                        al=min(a[r].id,a[l].id)+1;
                        ar=max(a[r].id,a[l].id);
                        sum=nval;
                    }
                    if(nval<t)
                        r++;
                    else
                        break;
                }
                if(r>n)
                    break;
                else
                {
                    l++;
                    if(l==r)
                        r++;
                }
            }
            printf("%d %d %d\n",sum,al,ar);
        }
    }
    return 0;
}

```


