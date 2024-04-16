

### [H - Keywords Search](https://cn.vjudge.net/problem/HDU-2222)


 [HDU - 2222 ](https://cn.vjudge.net/problem/16403/origin)

In the modern time, Search engine came into the life of everybody like Google, Baidu, etc.  Wiskey also wants to bring this feature to his image retrieval system.  Every image have a long description, when users type some keywords to find the image, the system will match the keywords with description of image and show the image which the most keywords be matched.  To simplify the problem, giving you a description of image, and some keywords, you should tell me how many keywords will be match. 

**Input**

First line will contain one integer means how many cases will follow by.  Each case will contain two integers N means the number of keywords and N keywords follow. (N <= 10000)  Each keyword will only contains characters 'a'-'z', and the length will be not longer than 50.  The last line is the description, and the length will be not longer than 1000000. 

**Output**

Print how many keywords are contained in the description.

**Sample Input**

```
1
5
she
he
say
shr
her
yasherhs```


**Sample Output**

```
3```


 

AC自动机模板题

```cpp
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<queue>
using namespace std;
const int maxn=5e5+7;
struct AcTireNode
{
    int next[26];
    int fail,cnt;//要保证fail指针不能为自己
    AcTireNode()
    {
        memset(next,-1,sizeof(next));
        fail=cnt=0;//初始化
    }
    void clear()
    {
        memset(next,-1,sizeof(next));
        fail=cnt=0;//初始化
    }
};
class AcTire{
    /*
AC 自动机
1.输入模式串 构建字典树
2.构建fail指针
3.匹配文本串
4.初始化树
*/
    public:
        AcTireNode *node;
        int top;//使用了多少个节点
    AcTire()
    {
        top=0;
        node=new AcTireNode[maxn];
    }
    inline int hash_letter(char c)
    {
        return c-'a';
    }
    void insert(char *p)
    {
        int now=0;
        while(*p)
        {
            if(node[now].next[hash_letter(*p)]==-1)
                node[now].next[hash_letter(*p)]=++top;
            now=node[now].next[hash_letter(*p)];
            ++p;
        }
        node[now].cnt++;
    }
    void bulid_fail()
    {
        int now=0;
        int to;
        /*
        保证队列里的fail指针全部OK
        从队列中取一个 把其下面的fail指针OK 并且加入队列
        */
        queue<int> mmp;
        for(int i=0;i<26;++i)//将根节点的所有儿子加入队列
        {
            if(node[0].next[i]!=-1)
                mmp.push(node[0].next[i]);
        }
        while(!mmp.empty())//
        {
            now=mmp.front();
            mmp.pop();
            for(int i=0;i<26;++i)//将此节点的儿子的 fail指针计算出来并加入队列
            {
                if(node[now].next[i]!=-1)
                {
                    mmp.push(node[now].next[i]);
                    /*   计算now的 第i个儿子的fail指针   */
                    to=node[now].fail;
                    while(to>0&&node[to].next[i]==-1)
                        to=node[to].fail;
                    /* 直至根节点 或者fail的父节点*/
                    if(node[to].next[i]!=-1)//否则没有最大匹配  即为空
                        node[node[now].next[i]].fail=node[to].next[i];
                }
            }
        }

    }
    int Find_words(char *tx)
    {
        int ans=0;
        int now=0;//当前最大匹配下标
        int to,i;
        while(*tx)
        {
            i=hash_letter(*tx);
            //没有下面的匹配，则找跟此字符的最大匹配
            while(now>0&&node[now].next[i]==-1)
                    now=node[now].fail;
            if(node[now].next[i]!=-1)
                now=node[now].next[i];
            /* 开始计算以now为后缀的单词出现数*/
            to=now;
            while(to&&node[to].cnt!=-1)/*精髓之处，匹配过后设为-1代表该后缀对应所有的字符串都匹配过了，避免后来重复匹配已经匹配过的单词*/
            {
                ans+=node[to].cnt;
                node[to].cnt=-1;//标记该单词已经加过了  就算这个单词没出现 标记为-1代表这个字符串的后缀节点全扫描过了
                to=node[to].fail;
            }
            ++tx;
        }
        return ans;
    }
    void clear()
    {
        for(int i=0;i<=top;++i)
            node[i].clear();
        top=0;
    }
    ~AcTire()
    {
        delete []node;
    }

};
char tx[1000007],words[55];
int main()
{
    AcTire dch;
    int t;
    int n;

    scanf("%d",&t);
    while(t--)
    {
        dch.clear();
        scanf("%d",&n);
        for(int i=0;i<n;++i)
        {
            scanf("%s",words);
            dch.insert(words);
        }
        dch.bulid_fail();
        scanf("%s",tx);
        printf("%d\n",dch.Find_words(tx));
    }
}```


 

