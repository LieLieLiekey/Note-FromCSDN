

##[CodeForces - 949B ](https://vjudge.net/problem/1412027/origin)

题意：现在给你一个n，表示有2*n-1个方格，第奇数方格上会有一个数字 1-n按顺序放。第偶数个方格上是没有数字的。变动规则是排在最后一个位置的数字，移动到它前边最近的空位 。 直到数字之间没有空位。最终的数列是由n已经确定的。给你q，表示q次查询，每次查询输入一个x，问数列第x位上的数字是多少？ .
![./figures/01fef3d910f5d625885b73d8d9765452](./figures/01fef3d910f5d625885b73d8d9765452)


**Input**

The first line contains two integers *n* and *q* (1 ≤ *n* ≤ 1018, 1 ≤ *q* ≤ 200 000), the number of elements in the array and the number of queries for which it is needed to find the answer.

Next *q* lines contain integers *x**i* (1 ≤ *x**i* ≤ *n*), the indices of cells for which it is necessary to output their content after Dima’s algorithm finishes.

**Output**

For each of *q* queries output one integer number, the value that will appear in the corresponding array cell after Dima’s algorithm finishes.

**Examples**

**Input**

```bash
4 3
2
3
4
```


**Output**

```bash
3
2
4
```


**Input**

```bash
13 4
10
5
4
8
```


**Output**

```bash
13
3
8
9
```


**Note**

The first example is shown in the picture.

当n=13时，数列为[1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10, 7].

### 题意：


中文的我想大家都看得懂

### 分析:


假设现在询问的位置是$x,且（1&lt;=x&lt;=n）$


奇数位置的值一定能立马确定为$(x+1)/2$，因为奇数位置刚开始都有值且确定，往前移动只能移动到偶数位置上


+  如果$x$是奇数 $val=(x+1)/2​$ +  $x$是偶数 $假设最后x数的位置的数为val，那么我们回到val刚放到x这个位置的状态，此时位置x之前的偶数位置一定是空的$,$即位置x前面有x/2个数，又因为val刚放到x这个位置，故x后面的数一定是连续的数共有n-x/2-1个$, $那么val放到位置x之前一定在位置x+(n-x/2-1)+1的位置上$，$如果此时x是奇数，则val=(x+1)/2,否则重复x为偶数的状态$，$直到x为奇数即可​$ 


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
const int maxn=1e3+100;
const int branch=26;
const int inf=0x7fffffff;
int main()
{
    ll n,q,x;
    ios::sync_with_stdio(false);/*这语句加速cin输入，去了也没关系*/
    cin>>n>>q;
    while(q--)
    {
        cin>>x;
        while(x%2==0)
        {
            x=n+x/2;
        }
        cout<<(x+1)/2<<endl;
    }
    return 0;
}
```


