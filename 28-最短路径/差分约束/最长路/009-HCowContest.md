

解释在代码里，（题中找突破点，就可以有思路了）

 

*N* (1 ≤ *N* ≤ 100) cows, conveniently numbered 1..*N*, are participating in a programming contest. As we all know, some cows code better than others. Each cow has a certain constant skill rating that is unique among the competitors.

The contest is conducted in several head-to-head rounds, each between two cows. If cow *A* has a greater skill level than cow *B* (1 ≤ *A* ≤ *N*; 1 ≤ *B* ≤ *N*; *A* ≠ *B*), then cow *A* will always beat cow *B*.

Farmer John is trying to rank the cows by skill level. Given a list the results of *M* (1 ≤ *M* ≤ 4,500) two-cow rounds, determine the number of cows whose ranks can be precisely determined from the results. It is guaranteed that the results of the rounds will not be contradictory.

Input

* Line 1: Two space-separated integers: *N* and *M* * Lines 2..*M*+1: Each line contains two space-separated integers that describe the competitors and results (the first integer, *A*, is the winner) of a single round of competition: *A* and *B*

Output

* Line 1: A single integer representing the number of cows whose ranks can be determined 　

Sample Input

```
5 5
4 3
4 2
3 2
1 2
2 5
```


Sample Output

```
2```


 

 

 

 

 

```cpp
/*s u意思为对应编号的牛
若s能打败u就令map[s][u]=1，否则map[s][u]=负无穷（可以理解为路不通）
初始化：map数组所有都为负无穷 map[i][i]=0
输入数据  s u证明s能打败u 令map[s][u]=1
那么所有数据输入完成后就构成一个图，在这个图中只看s到u的路径      
若存在一条路使得这条路所有权值之和>0 证明s能打败u（等于0表明这是
同一个牛）（并且s->u有路与u->s有路 不能同时存在，否则就有歧义了） 

那么我们选s到u的路径肯定选能确定s与u关系即map[s][u]>=0,
这样我们用floyd来找所有两个牛之间的最长”路径“，若这个最长路径>=0 表明s能击败u 即s u关系确定
如果两个牛的关系确定就有map[s][u]>=0成立 或者map[u][s]>=0成立,


一个牛的等级确定也就说明这条牛与其他所有牛的强弱关系都确定了,即这个牛与其他所有牛都存在上面的关系，

这样遍历n个牛就可以知道有几个牛的等级确定。


此代码时间复杂度：o{(n^3)(Floyd)+n*(2n)(遍历关系)}
*/

#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
#define N 100
#define INF -99999999
using namespace std;
int map[N+10][N+10];
int main()
{
    int n,m,a,b,cnt,sign;//floyd//找最长路径
    scanf("%d %d",&n,&m);
    for(int i=1; i<=n; i++) //init map
        for(int j=1; j<=n; j++)
            map[i][j]=INF;
    for(int i=1; i<=n; i++)
        map[i][i]=0;
    for(int i=1; i<=m; i++)
    {
        scanf("%d %d",&a,&b);//a b的关系确定
        map[a][b]=1;
    }
    for(int k=1; k<=n; k++) //通过第K个刷新最长的
        for(int i=1; i<=n; i++)
            for(int j=1; j<=n; j++)
            {
                if(map[i][k]+map[k][j]>map[i][j])
                   map[i][j]=map[i][k]+map[k][j];
            }
    cnt=0;
    for(int i=1;i<=n;i++)
    {
        sign=0;
        for(int j=1;j<=n;j++)
        {
            if(map[i][j]>=0||map[j][i]>=0)
            {
                 sign++;
                 continue;
            }
            break;
        }
        if(sign==n)
            cnt++;
    }
    printf("%d\n",cnt);
}
```


 

 

