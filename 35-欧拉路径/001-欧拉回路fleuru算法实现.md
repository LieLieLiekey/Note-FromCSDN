

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
    for(int i=1;i<=n;i++)
    {
        if(map[beg][i])
        {
            map[beg][i]--;
            map[i][beg]--;
            dfs(i);
        }
    }
    ans[top++]=beg;//放入栈中
}
void Print_road()//输出路径
{
    for(int i=top-1;i>=0;i--)
    {
        printf("%d",ans[i]);
        if(i)
            printf("-->");
    }
    puts("");
}
int main()
{
    int beg;
    while(~scanf("%d %d",&n,&m))//共有n个点，m个边   //欧拉回路所有边只走一次
    {
            memset(book,0,sizeof(book));
            memset(map,0,sizeof(map));

            for(int i=0;i<m;i++)
            {
                int u,v;
                scanf("%d %d",&u,&v);
                book[u]++;
                book[v]++;
                map[u][v]=map[v][u]=1;
            }//构建数组链表
            beg=1;
            int cnt=0;
            for(int i=1;i<=n;i++)
            {
                if(book[i]&1)
                {
                    cnt++;
                    beg=i;
                }
            }
            if(!cnt||cnt==2)//找出beg
            {
                fleury(beg);
                Print_road();
            }
            else
            {
                printf("不存在欧拉回路\n");
                continue;
            }
    }
} 
```




```
/*

fleury 有向边
用了邻接表实现
*/

#include<stdio.h>
#include<cstring>
#include<string>
#include<algorithm>
#include<math.h>
using namespace std;
const int maxn=1e3+10;
struct Node
{
    int v;
    int next,index,flag;
} node[maxn];
int head[maxn];//存放每个u节点的第一个指向
int ans[maxn];//存放点的顺序
int rbook[maxn],cbook[maxn];//表示每个点的度数
int top;
void dfs(int);
void fleury(int beg)
{
    top=0;
    dfs(beg);
}
void dfs(int beg)
{
    int to;
    to=head[beg];
    while(to!=-1)
    {
        if(node[to].flag)
        {
            node[to].flag=0;
            dfs(node[to].v);
        }
        to=node[to].next;
    }
    ans[top++]=beg;
}
void Print_road()//输出路径
{
    for(int i=top-1;i>=0;i--)
    {
        printf("%d",ans[i]);
        if(i)
            printf("-->");
    }
    puts("");
}
int main()
{
    int n,m,beg;
    while(~scanf("%d %d",&n,&m))//共有n个点，m个边   //欧拉回路所有边只走一次
    {
            memset(rbook,0,sizeof(rbook));
            memset(cbook,0,sizeof(cbook));
            memset(head,-1,sizeof(head));

            for(int i=0;i<m;i++)
            {
                int u,v;
                scanf("%d %d",&u,&v);
                cbook[u]++;
                rbook[v]++;
                node[i].v=v;
                node[i].flag=1;
                node[i].index=i;
                node[i].next=head[u];
                head[u]=i;
            }//构建数组链表
            beg=1;
            int cnt=0;
            for(int i=1;i<=n;i++)
            {
                if(rbook[i]!=cbook[i])//计算出度不等于入读的个数
                {
                    cnt++;
                    if(cbook[i]>rbook[i])//因为总的出度与总的入度个数是相同的，所有必有一大一小
                        beg=i;
                }
            }
            if(!cnt||cnt==2)//找出beg
            {
                fleury(beg);
                Print_road();
            }
            else
            {
                printf("不存在欧拉回路\n");
                continue;
            }
    }
}
```