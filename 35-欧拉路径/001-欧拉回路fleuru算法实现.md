

书上的欧拉回路定义不在重复，[欧拉回路定义](https://baike.baidu.com/item/%E6%AC%A7%E6%8B%89%E5%9B%9E%E8%B7%AF/10036484?fr=aladdin)，

弗洛莱走边的方法也不再细讲，[弗洛莱算法描述](https://blog.csdn.net/guomutian911/article/details/42105127/)

这里只说怎么进行代码实现。

圈套圈算法可以在O(n)时限内解决欧拉回路问题

```cpp
/*
无向图的欧拉回路 
邻接矩阵存图

原理：
dfs走边，当走不动时就将其放入栈中,最后将顶点从栈中取出的顺序就是欧拉路径。
如果走错边则必定会堵，那么就会将堵的放入栈中，从栈中取出的话就看作是最后走的割边，符合弗洛来算法；
如果走的边正确了，那么放入栈中的边取出时也与弗洛莱算法的顺序一致。

代码实现：
dfs 无路可走则放入栈中，最后栈就是一个欧拉路径
*/
#include<stdio.h>
#include<cstring>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;
const int maxn=1e3+10;
int ans[maxn];//存放点的顺序
int book[maxn];//表示每个点的度数
int map[maxn][maxn];
int top;
void dfs(int);
int n,m;
void fleury(int beg)
{
    top=0;
    dfs(beg);
}
void dfs(int beg)
{
    for(int i=1;i<=```


