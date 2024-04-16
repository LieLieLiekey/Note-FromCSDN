

## codeforces 1214E.Petya and Construction Set（构造）


#### 题目链接：[传送门](https://codeforces.com/contest/1214/problem/E)


#### 题意：


    现在有$2*n$个顶点，并且给一个长度为$n$的数组$d[]$，让我们构建一颗树，满足树上顶点$2*i-1$与顶点$2*i$之间的距离为$d[i]$。对于结果输出$2*n-1$条边。

#### 思路：



构造题，头脑风暴瞎想吧。


    其实我题目要求的就是构造出$2*n$个节点的树满足有不同的n对顶点之间的距离分别为$d[i]$。我们可以假设$d[]$中元素是非递增的（这可以通过排序后的顶点变换得到）。

    初始时有n个节点线性连接在一起：1-3-5…-2*n-1，并且d[1]>=d[2]>=d[3]。

    对于第 i 个节点，我们寻找对应的顶点 i+1所连接的节点，那么第i+d[i]-1个节点是可行的。如果他连接的是序列最后一个节点，那么就让该节点添加到序列结尾即可。（因为d[]是不递增的，所以总是有节点连接。

**代码**：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=1e5+20;
int V[2*N];
P seq[N];//d,id
vector<P> E;
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n;
    cin>>n;
    for(int i=1;i<=n;++i)
    {
        int d;
        cin>>d;
        seq[i].first=d;
        seq[i].second=i;
    }
    sort(seq+1,seq+n+1,greater<P>());
    for(int i=1;i<=n;++i){
        V[i]=2*seq[i].second-1;
        if(i!=1) E.push_back({V[i],V[i-1]});
    }
    int top=n;
    for(int i=1;i<=n;++i)
    {
        int d=seq[i].first;
        E.push_back({V[i]+1,V[i+d-1]});
        if(i+d-1==top)
            V[++top]=V[i]+1;
    }
    for(P e:E)
        cout<<e.first<<" "<<e.second<<endl;
    return 0;
}

```


