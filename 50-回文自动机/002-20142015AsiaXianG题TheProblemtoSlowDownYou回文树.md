

#### 题目链接：[传送门](https://codeforces.com/gym/100548)


#### 题意：


给出两个字符串A，B。求A的所有回文串在B中出现次数的和。

#### 思路：


我们可以分别对A，B字符串构建一颗回文树，根据回文树的结构，我们可以同时遍历两个回文树都有的回文串节点，然后计算贡献即可。 代码：

```cpp
#include <bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const int N=2e5+100;
struct PA_tree
{
    static const int branch=26;
    static const int MAXN=2e5+100;
    struct Node //每个节点代表一个回文串
    {
        int len;//回文串的长度,
        ll cnt;//回文串出现次数
        int next[branch],fail;
        //next[c]:该节点左右增加字符c的回文串节点位置,默认为0
        //fail :该节点非本身的最长回文后缀节点
    } node[MAXN];
    int ls,top=0;//长度,此时使用的节点个数
    char *s;//字符首指针,下标从1开始
    int initnode(int id)//需要手动初始化fail和len
    {
        node[id].cnt=0;
        mset(node[id].next,0);
        return id;
    }
    int getfail(int last,int i)
    {
        while(s[i-node[last].len-1]!=s[i]) last=node[last].fail;
        return last;
    }
    void init(char *s,int ls)
    {
        this->s=s;
        this->ls=ls;
        top=0;
        initnode(top++);
        initnode(top++);
        node[0].fail=node[1].fail=1;
        node[0].len=0,node[1].len=-1;
        s[0]=-1;
    }
    int gv(char c)
    {
        return c-'a';
    }
    void bulid_tree()
    {
        //目标,构建fail指针并生成回文树
        int last=0;
        for(int i=1; i<=ls; ++i)
        {
 
            int c=gv(s[i]);
            int cur=getfail(last,i);
            int now=node[cur].next[c];
 
            if(!now)
            {
                now=initnode(top++);//新建一个新的节点作为儿子
                node[now].len=node[cur].len+2;
                node[now].fail=node[getfail(node[cur].fail,i)].next[c];
                node[cur].next[c]=now;
            }
//            printf("c:%d,cur:%d,now:%d\n",c,cur,now);
            node[now].cnt++;
            last=now;
        }
    }
    void count()
    {
        //基于fail的节点标号一定比自身小,所以我们倒着累加
        for(int i=top-1; i; --i)
            node[node[i].fail].cnt+=node[i].cnt;
    }
 
};
char s1[N],s2[N];
PA_tree pa1,pa2;
ll res=0;
void dfs(int a,int b)
{
    if(a!=0&&a!=1)
        res+=(pa1.node[a].cnt)*(pa2.node[b].cnt);
    for(int i=0;i<26;++i){
        if(pa1.node[a].next[i]!=0&&pa2.node[b].next[i]!=0){
            dfs(pa1.node[a].next[i],pa2.node[b].next[i]);
        }
    }
    return ;
}
void solve()
{
    dfs(1,1);
    dfs(0,0);
}
int main()
{
    ios::sync_with_stdio(false);cin.tie(0);
    int t,cas=0;
    cin>>t;
    while(t--)
    {
        cin>>(s1+1)>>(s2+1);
//        scanf("%s%s",s1+1,s2+1);
        int ls1=strlen(s1+1),ls2=strlen(s2+1);
        pa1.init(s1,ls1);pa2.init(s2,ls2);
        pa1.bulid_tree();
 
        pa2.bulid_tree();
        pa1.count();
        pa2.count();
        res=0;
        solve();
        cout<<"Case #"<<++cas<<": "<<res<<endl;
//        printf("Case #%d: %lld\n",++cas,res);
    }
    return 0;
}
```


