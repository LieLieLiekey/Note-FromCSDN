

## HDU6184 Counting Stars（三元环统计）


**题目链接**：[传送门](http://acm.hdu.edu.cn/showproblem.php?pid=6184)

**思路：**

​ 可以看到A struct是有一个重复边的两个三元环组成的，我们可以使用三元环统计的方法，这样每个三元环就会计算一次，我们对每条边记录下在多少个三元环，那么答案就是每条边的$C(cnt,2)$ 之和

三元环计数链接：[this](https://www.cnblogs.com/Dance-Of-Faith/p/9759794.html)

**代码：**

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef P Edge;
Edge edge[200005];
int degree[100005];
bool cmp(int x,int y)
{
    return degree[x]!=degree[y]?degree[x]<degree[y]:x<y;
}
vector<int> adja[100005];

int color[100005];
map<P,int> cunt;//记录边的出现次数
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n,m;
    while(cin>>n>>m)
    {
        for(int i=1; i<=n; ++i)
        {
            adja[i].clear();
            degree[i]=0;
            color[i]=0;
        }
        cunt.clear();
        for(int i=1; i<=m; ++i)
        {
            int u,v;
            cin>>u>>v;
            edge[i].first=u;
            edge[i].second=v;
            ++degree[u];
            ++degree[v];
        }
        for(int i=1; i<=m; ++i)//把无向边变为有向边
        {
            int u=edge[i].first,v=edge[i].second;
            if(cmp(u,v))
                adja[u].push_back(v);
            else
                adja[v].push_back(u);
        }
        for(int u=1; u<=n; ++u)
        {
            for(int v:adja[u])
                color[v]=u;
            for(int v:adja[u])//枚举第1条边
            {
                for(int vv:adja[v]){//枚举第2条边
                    if(color[vv]==u){//是个三元环
                        cunt[{u,v}]++;
                        cunt[{v,vv}]++;
                        cunt[{u,vv}]++;
                    }
                }
            }
        }
        ll ans=0;
        for(auto p:cunt)
        {
            ll cnt=p.second;
            if(cnt>=2){
                ans+=(cnt*(cnt-1))/2;
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}

```




## Prufer序列（无根树与序列的互相转化及其性质）


##### 什么是Prufer序列？


Prufer序列是将一个带有节点编号的无根树转化为一个序列的过程，且每一个无根树唯一的确定一个prufer序列。反过来也成立。


##### Prufer序列的性质



+ 原树中顶点 $v v$ 的度数$− 1 = - 1=$ 序列中顶点v的出现次数
+ n个顶点的无根树的Prufer序列的长度为n-2
+ 一个Prufer序列与一个无根树一一对应




##### 将无根树转化为Prufer序列


**方法：**

一棵树要得到普吕弗序列，方法是逐次去掉树的顶点，直到剩下两个顶点。考虑树*T*，其顶点为{1, 2, …, *n*}。在第*i*步，去掉标号最小的叶，并把普吕弗序列的第*i*项设为这叶的邻顶点的标号。

一棵树的序列明显是唯一的，而且长为*n* − 2。

**算法：**

**使用的数据结构**：维护一个度数为1的set集合即可.


+ 初始度数为1的集合（所有叶子）.
+ 每次从度数为1的叶子顶点集合中找到编号最小的顶点u，并将其从度数为1的集合中删去。将u连接的顶点v加入prufer序列，删除u连接的所有边。
+ 更新u和v的度数，v的度数为1则加入度数为1的集合。
+ 当加入序列的数的个数为n-2时候停止。否则返回到第二步。



**具体实现：**


时间复杂度为O(nlogn)。代码经过自己的部分测试是正确的，若有人发现bug请在评论区指出，我将尽快进行修改


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
const int N=1e5+10;
vector<int> prufer;
vector<int> g[N];
int du[N];
/*
输入:顶点个数n和树g[]
输出:prufer序列
*/
void TreeToPrufer(int n,vector<int> g[])//g[]中存储的是无向边,共有n个顶点
{
   
    set<int> leaf;
    mset(du,0);
    prufer.clear();
    for(int u=1;u<=n;++u)
        for(int v:g[u]) du[v]++;
    for(int i=1;i<=n;++i) if(du[i]==1) leaf.insert(i);
    while(prufer.size()!=n-2)
    {
   
        int u=*leaf.begin();
        du[u]=0;
        leaf.erase(leaf.begin());
        for(int v:g[u])
        {
   
            if(!du[v]) continue;
            prufer.push_back(v);
            du[v]--;
            if(du[v]==1) leaf.insert(v);
        }
    }
    printf("following is prufer sequence of tree:\n");
    for(int```




## 洛谷P2624 [HNOI2008]明明的烦恼（Prufer序列+组合数学）


**题目：**给你n个节点的树中某些节点的度数，其他节点的度数任意，问有多少种满足题意的树。

**思路：**

​ 假设给出n个节点的K个节点度数确定，且分别为$d_1,d_2,d_3...d_k​$。我们令$a_i=d_i-1$, 且设$sum= \sum _{i=1} ^{k}a_i​$。

那么有$ans=C {a_1 \choose n-2}*C {a_2 \choose n-2-a_1}*...C {a_k \choose n-2-a_1-a_2..-a_{k-1}}=\frac{(n-2)!}{(n-2-sum)!*\Pi_{i=1} ^{k}a_i!}*(n-k)^{(n-2-sum)}$

**代码：**

```python
def quick_pow(a,b):
    ans=1
    while b>0:
        if (b&1)>0 :
            ans*=a
        a*=a
        b>>=1
    return ans
def init(n):
    fac = [0 for i in range(n + 1)]
    fac[0]=1
    for i in range(1,n+1):
        fac[i]=fac[i-1]*i
    return fac
if __name__ == '__main__':
    # a,b=[int(i) for i in (input().split())]
    # print(a,b)
    # print(quick_pow(a,b))
    n=int(input())
    du=[]
    for i in range(n):
        x=int(input())
        du.append(x)
    if n==1:
        if du[0]>0:
            print(0)
        else:
            print(1)
        exit()
    sum=0
    for i in du:
        if i==0:
            print(0)
            exit()
        if i==-1:
            continue
        sum+=i-1
    if sum>n-2:
        print(0)
        exit()
    #此时n>=2且du[]>1,且sum<=n-2
    fac=init(n)
    ans=fac[n-2]//fac[n-2-sum]
    k=0
    for i in du:
        if i==-1:
            continue
        ans//=fac[i-1]
        k+=1
    ans*=quick_pow(n-k,n-2-sum)
    print(int(ans))



```


