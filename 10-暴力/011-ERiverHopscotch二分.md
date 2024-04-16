

### E - River Hopscotch


Every year the cows hold an event featuring a peculiar version of hopscotch that involves carefully jumping from rock to rock in a river. The excitement takes place on a long, straight river with a rock at the start and another rock at the end, *L* units away from the start (1 ≤ *L*≤ 1,000,000,000). Along the river between the starting and ending rocks, *N* (0 ≤ *N* ≤ 50,000) more rocks appear, each at an integral distance *Di* from the start (0 < *Di* < *L*).

To play the game, each cow in turn starts at the starting rock and tries to reach the finish at the ending rock, jumping only from rock to rock. Of course, less agile cows never make it to the final rock, ending up instead in the river.

Farmer John is proud of his cows and watches this event each year. But as time goes by, he tires of watching the timid cows of the other farmers limp across the short distances between rocks placed too closely together. He plans to remove several rocks in order to increase the shortest distance a cow will have to jump to reach the end. He knows he cannot remove the starting and ending rocks, but he calculates that he has enough resources to remove up to *M* rocks (0 ≤ *M* ≤ *N*).

FJ wants to know exactly how much he can increase the shortest distance **before** he starts removing the rocks. Help Farmer John determine the greatest possible shortest distance a cow has to jump after removing the optimal set of *M* rocks.

**Input**

Line 1: Three space-separated integers: *L*, *N*, and*M* Lines 2… *N*+1: Each line contains a single integer indicating how far some rock is away from the starting rock. No two rocks share the same position.

**Output**

Line 1: A single integer that is the maximum of the shortest distance a cow has to jump after removing *M* rocks

**Sample Input**

```bash
25 5 2
2
14
11
21
17
```


**Sample Output**

```bash
4
```


**Hint**

Before removing any rocks, the shortest jump was a jump of 2 from 0 (the start) to 2. After removing the rocks at 2 and 14, the shortest required jump is a jump of 4 (from 17 to 21 or from 21 to 25).

##### 题意：


一条河的长度为L，中间有n个石头，我现在可以去掉其中的m个石头，使得最小相邻石头距离的最大.

求最大是多少

##### 分析：


枚举最小距离，每个最小距离可以确定去除石头的和数，且最小距离与去除石头的个数之间正相关，所以枚举最小距离二分求解即可。

```cpp
#include<cstdio>
#include<algorithm>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=5e4+10;
int a[maxn];
int n,m,L;
int f(int x)
{
    int l,r;
    l=0,r=1;
    int ans=0;
    while(r<n+2)
    {
        if(a[r]-a[l]<x)//若最后的end都不满足 就把l所在去了，代码没写那个因为效果一样
        {
            r++;
            ans++;
        }
        else
        {
            l=r;
            r++;
        }
    }
    return ans;
}
int solve()
{
    int l=0,r=L,ans,mid;
    while(l<=r)
    {
        mid=(l+r)/2;
        if(f(mid)<=m)
        {
            ans=mid;
            l=mid+1;
        }
        else
            r=mid-1;
    }
    return ans;
}
int main()
{
    while(~scanf("%d %d %d",&L,&n,&m))
    {
        a[0]=0;
        a[n+1]=L;
        for(int i=1;i<=n;++i)
            scanf("%d",a+i);
        sort(a,a+n+2);
        printf("%d\n",solve());
    }
    return 0;
}
```


