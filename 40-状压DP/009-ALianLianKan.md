

### A - LianLianKan


I like playing game with my friend, although sometimes looks pretty naive. Today I invent a new game called LianLianKan. The game is about playing on a number stack. Now we have a number stack, and we should link and pop the same element pairs from top to bottom. Each time, you can just link the top element with one same-value element. After pop them from stack, all left elements will fall down. Although the game seems to be interesting, it’s really naive indeed. 
![./figures/791b82e30179bc1b498d58e6ad7733d3](./figures/791b82e30179bc1b498d58e6ad7733d3)
 To prove I am a wisdom among my friend, I add an additional rule to the game: for each top element, it can just link with the same-value element whose distance is less than 6 with it. Before the game, I want to check whether I have a solution to pop all elements in the stack.

**Input**

There are multiple test cases. The first line is an integer N indicating the number of elements in the stack initially. (1 <= N <= 1000) The next line contains N integer ai indicating the elements from bottom to top. (0 <= ai <= 2,000,000,000)

**Output**

For each test case, output “1” if I can pop all elements; otherwise output “0”.

**Sample Input**

```bash
2
1 1
3
1 1 1
2
1000000 1
```


**Sample Output**

```bash
1
0
0
```


##### 题意：


给你一个栈，栈中有n个元素，下面输入n个数，依此从栈底到栈顶。接下来你必须从找到一个**与栈顶距离小于等于5的位置**，若这个位置的数和栈顶相同，可以让**这个数**和**栈顶的数**从栈中消去。

问有没有一种方法是所有数字全部消去

##### 分析：


消去与栈底最远的或者最近的什么贪心都是不行的，都可以找出反例。这道题只有暴力来写

当然暴力的DP也是算是暴力?

第h高度**之前的数**全消去的时候最多能消去高度h之后的后4位，且最大距离与h不超过9，又因为h的后9位肯定有5个没有被消去的数，那么只要枚举h高度之后的9个状态压缩一下，模拟从从栈顶消去元素的所有的情况。

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
int dp[1100][1<<10],a[1100];
int dfs(int h,int state)//当前高度为h，状态为state
{//能将第一个消去则进入下个状态 不能则返回0
    if(!h)
        return 1;
    if(dp[h][state]!=-1)
        return dp[h][state];
    if((state&1)==0)//第h高度没有数字则整下个
    {
        int nextstate=state>>1;
        if(h>10)//第9位是否要添进去
        {
                nextstate|=(1<<9);
        }
        return dp[h][state]=dfs(h-1,nextstate);
    }
    /*
    枚举删除的位置
    */
    int dis=1;
    int ans=0;
    int i=1;
    while(i<=9&&dis<=5&&h-i>0)
    {

        if((state&(1<<i))==0)//这一位是消去过了
        {
             i++;
             continue;
        }
        if(a[h-i]==a[h])//这h的下i位相等
        {
            int nextstate=(state^(1<<i))>>1;
            if(h>10)//第9位是否要添进去
            {
                nextstate|=(1<<9);
            }
            ans+=dfs(h-1,nextstate);
            if(ans)
            {
                return dp[h][state]=1;
            }
        }
        i++;
        dis++;
    }
    return dp[h][state]=0;

}
int main()
{
    int n;
    while(~scanf("%d",&n))
    {
        for(int i=1; i<=n; ++i)
            scanf("%d",a+i);
        if(n&1)
        {
            printf("0\n");
            continue;
        }
        mset(dp,-1);
        int ans=0;
        if(n<=10)
        {
            ans=dfs(n,(1<<n)-1);
        }
        else{
            ans=dfs(n,(1<<10)-1);
        }
        printf("%d\n",ans);
    }
    return 0;
}
```


