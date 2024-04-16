

## codeforces 1207F. Remainder Problem(平方启发)


#### 题目链接：[传送门](https://codeforces.com/contest/1207/problem/F)


#### 题意：


现在有一个大小为500000的数组，初始每个元素都为0，索引从1开始，现有两个操作：

1 x y–代表将索引为x的元素值加y

2 x y–代表求数组中所有索引满足**取余x等于y**的的元素值和。

#### 思路：


对于每个查询如果采用暴力的方式话时间复杂度为$O(N/x)$，其中N为数组大小。这对x较大的时候可以使用这种方法。

对于 $x$ 较小时，假设 $x\le K$，那么查询有$K^2$种，假如我们维护每组查询的结果，那么对于每次1操作，我们需要$O(K)$维护较小的$x\le K$的查询。

我们让$K$取$sqrt(N)$，那么总的时间复杂度为$O(N*sqrt(N))$

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
int a[750][750],b[500005];//<=720处理,>720暴力
int main()
{
    int q;
    scanf("%d",&q);
    while(q--)
    {
        int cmd,x,y;
        scanf("%d%d%d",&cmd,&x,&y);
        if(cmd==1)
        {
            b[x]+=y;
            for(int i=1;i<=720;++i)
                a[i][x%i]+=y;
        }
        else{
            if(x<=720){
                printf("%d\n",a[x][y]);
            }
            else{
                int ans=0;
                for(int k=0;k*x+y<=500000;++k){
                    ans+=b[k*x+y];
                }
                printf("%d\n",ans);
            }
        }
    }
    return 0;
}

```


