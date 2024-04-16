

 

### 先放题目


A supermarket has a set Prod of products on sale. It earns a profit px for each product x∈Prod sold by a deadline dx that is measured as an integral number of time units starting from the moment the sale begins. Each product takes precisely one unit of time for being sold. A selling schedule is an ordered subset of products Sell ≤ Prod such that the selling of each product x∈Sell, according to the ordering of Sell, completes before the deadline dx or just when dx expires. The profit of the selling schedule is Profit(Sell)=Σ x∈Sellpx. An optimal selling schedule is a schedule with a maximum profit. For example, consider the products Prod={a,b,c,d} with (pa,da)=(50,2), (pb,db)=(10,1), (pc,dc)=(20,2), and (pd,dd)=(30,1). The possible selling schedules are listed in table 1. For instance, the schedule Sell={d,a} shows that the selling of product d starts at time 0 and ends at time 1, while the selling of product a starts at time 1 and ends at time 2. Each of these products is sold by its deadline. Sell is the optimal schedule and its profit is 80.


![./figures/f9d071d9c472cbda044241e92bee7393](./figures/f9d071d9c472cbda044241e92bee7393)


 Write a program that reads sets of products from an input text file and computes the profit of an optimal selling schedule for each set of products. Input

A set of products starts with an integer 0 <= n <= 10000, which is the number of products in the set, and continues with n pairs pi di of integers, 1 <= pi <= 10000 and 1 <= di <= 10000, that designate the profit and the selling deadline of the i-th product. White spaces can occur freely in input. Input data terminate with an end of file and are guaranteed correct.

Output

For each set of products, the program prints on the standard output the profit of an optimal selling schedule for the set. Each result is printed from the beginning of a separate line.

Sample Input

```
4  50 2  10 1   20 2   30 1

7  20 1   2 1   10 3  100 2   8 2
   5 20  50 10
```


Sample Output

```
80
185```


题意：

给你n个商品，每个商品都有两个参数 v t ，v为该商品卖出后的利润，t表明该商品只能在这个期限卖出。

问你这批商品最多能获得多少利润

 

 

 

 

若不是当时刷的专题是并查集，还真不知道这个题能用并查集嘞！（话说并查集也真是厉害）

刚开始看这个题，自己先想了一波思路，思路中只用了贪心，然后算了下时间复杂度为O（n*n）  ，题中n=1w ,肯定会超时

 

想了半天也不知道怎么用并查集，后来搜了搜博客,,ԾㅂԾ,,，有了并查集的思想，并且认识到这种思想是多么的强大（可以看成树，但是看成链状更容易理解）

 

 

这道题你必须将时间看作离散状的，假设0~7的天数分作 第1天 ，第2天，第 3天， 第4天..................第7天。

分析：

将每个商品数据储存在结构体中，输入数据以后，所有商品按利润从大到小的顺序排列,利润相等的期限长的排在前面.

这样所有商品经这种规则排序后储存在结构体数组中（编号为0~(n-1)），从左到右开始遍历，根据每个商品的期限，找到**离这个期限最近**的且**可占用**的时间，去占用这个时间， 你可以想象一下“占用”后的该时间用一个数组标记一下，表示该时间已“占用”。这样保证每个被占用的时间段它所在的商品都是最佳的。

 

那么怎么实现快速找到 "**离这个期限最近的且可占用的"**时间呢? 假设用一个fahther[]数组来存放这个你所想要的时间，初始状态

father[x]=x，都为自己树上的根，当这个时间用过以后就把这个father[x]=x-1（这个时间用过之后，离这个时间期限最近的时间就是左边的那一个）表示这个时间已经用过，并且把这棵树与左边的一棵树连接起来，

**只有满足father[x]=x，才表明x这个时间段可占用 ()**

 

 

```cpp
#include<stdio.h>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#define N 10000
using namespace std;
int father[N+10];
struct node{
int v,t;
}a[N+10];
void up_date(int n)
{
    for(int i=0;i<=n;i++)
        father[i]=i;
}
int _find(int x)
{
    if(x==father[x])
        return x;
    return father[x]=_find(father[x]);//路径压缩
}
bool cmp(node q,node qq)
{
    if(q.v==qq.v)
        return q.t>qq.t;
    return q.v>qq.v;
}
int main()
{
    int n,ans,maxx=0,root;
    while(~scanf("%d",&n))
    {
        maxx=ans=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d %d",&a[i].v,&a[i].t);
            maxx=maxx>a[i].t?maxx:a[i].t;
        }
        up_date(maxx);
        sort(a,a+n,cmp);
        for(int i=0;i<n;i++)//核心代码
        {
            root=_find(a[i].t);//找这棵树的根，即可用的时间。
            if(root>0)//有可用时间
            {
                ans+=a[i].v;
                father[root]=root-1;
            }
        }
        printf("%d\n",ans);
    }
}
```


 

 



题目

 

Now and then you play the following game with your friend. Your friend writes down a sequence consisting of zeroes and ones. You choose a continuous subsequence (for example the subsequence from the third to the fifth digit inclusively) and ask him, whether this subsequence contains even or odd number of ones. Your friend answers your question and you can ask him about another subsequence and so on. Your task is to guess the entire sequence of numbers. You suspect some of your friend's answers may not be correct and you want to convict him of falsehood. Thus you have decided to write a program to help you in this matter. The program will receive a series of your questions together with the answers you have received from your friend. The aim of this program is to find the first answer which is provably wrong, i.e. that there exists a sequence satisfying answers to all the previous questions, but no such sequence satisfies this answer.

Input

The first line of input contains one number, which is the length of the sequence of zeroes and ones. This length is less or equal to 1000000000. In the second line, there is one positive integer which is the number of questions asked and answers to them. The number of questions and answers is less or equal to 5000. The remaining lines specify questions and answers. Each line contains one question and the answer to this question: two integers (the position of the first and last digit in the chosen subsequence) and one word which is either `even' or `odd' (the answer, i.e. the parity of the number of ones in the chosen subsequence, where `even' means an even number of ones and `odd' means an odd number).

Output

There is only one line in output containing one integer X. Number X says that there exists a sequence of zeroes and ones satisfying first X parity conditions, but there exists none satisfying X+1 conditions. If there exists a sequence of zeroes and ones satisfying all the given conditions, then number X should be the number of all the questions asked.

Sample Input

```
10
5
1 2 even
3 4 odd
5 6 even
1 6 even
7 10 odd```


Sample Output

```
3```


 

 

 

 问你那个问题与前面的有冲突， %99是并查集 

题意：长度为n的字符串，给你k个问题，每个问题数据为  x, y ，vn，分别表示其字串的**开始位置**，**结束位置**，**该字符串内1的个数是偶数还是奇数**。

问你在提出k个问题的过程中，有几个是正确的，（假设第k+1能推翻前面的，则正确的为k个）

 

 

参考博客：[http://blog.csdn.net/hi_just_do_it/article/details/52002836](http://blog.csdn.net/hi_just_do_it/article/details/52002836/)（看我的不如看他的ヽ(*。>Д<)o゜，这篇是留给自己看的）

题中N 是10亿，所以直接用编号作为数组的下标显然是不合适的，题中问题最多有5000个，即是最多有5000*2个不重复的数。

所以我们可以把题目中所有出现过的数离散化，假设每个数离散化后都对应一个“编号”那么将出现过的数放进数组排序，数组的下标与数组内的值一一对应，也就是将数离散化了，

**怎么查找该数离散化后的编号呢，二分查找，时间复杂度0 log2（n）**

然后开始带权并查集的过程 ，这道带权并查集的过程跟前面题           How Many Answers Are Wrong  差不多，这里就不详细说了。

代码

 

```cpp
#include<stdio.h>
#include<string>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<stdlib.h>
#define N 10000
#include<map>
using namespace std;
map<int,int>mmp;//表示一个数有没有出现过
int father[N+10],rela[N+10],num[N+10],ll,rr;//分别表示查找区域的左右端点
struct node {
    int l,r,vn;//分别是问题的左端点 ，右端点，奇偶性
}ques[N];
int _find(int x)
{
    int team;
    if(x==father[x])
        return x;
    team=father[x];
    father[x]=_find(father[x]);//压缩路径
    rela[x]=(rela[x]+rela[team])%2;
    return father[x];
}
int _seach(int x)
{
    int mid;
    int l,r;
    l=ll;r=rr;
    mid=(l+r)/2;
    while(l<r)
    {
      if(x>num[mid])
          l=mid+1;
      else
          r=mid;
      mid=(l+r)/2;
    }
    return l;
}
int  _judge(int a,int b,int relax)//对a  b进行操作
{
    int root1,root2;
    root1=_find(a);
    root2=_find(b);
    if(root1==root2)
    {
        if(((rela[a]-rela[b]+2)%2)!=relax)
            return 0;//假的
        else
            return 1;
    }
    if(root1<root2)
    {
        father[root1]=root2;
        rela[root1]=(relax+rela[b]-rela[a]+2)%2;
    }
    else
    {
        father[root2]=root1;
        rela[root2]=(rela[a]-relax-rela[b]+2)%2;
    }
    return 1;
}
int main()
{
    int n,k,cnt,ans,flag=1,a,b,relax;
    char vn[20];
    cnt=ans=0;;
    scanf("%d%d",&n,&k);
    for(int i=0;i<k;i++)
    {
        scanf("%d %d %s",&ques[i].l,&ques[i].r,vn);
        ques[i].l--;
        if(vn[0]=='e')
            ques[i].vn=0;
        else
            ques[i].vn=1;
        if(!mmp[ques[i].l])
        {
            mmp[ques[i].l]=1;
            num[cnt++]=ques[i].l;
        }
        if(!mmp[ques[i].r])
        {
            mmp[ques[i].r]=1;
            num[cnt++]=ques[i].r;
        }
    }
    sort(num,num+cnt);//将不重复的的离散化的数储存起来并且排序  //离散化 标号对应的值为实际值
//    printf("cnt=%d\n",cnt);
//    for(int i=0;i<cnt;i++)
//        printf("num[%d]=%d\n",i,num[i]);
    ll=0;rr=cnt-1;
    for(int i=0;i<cnt;i++) //更新树
        father[i]=i;
    for(int i=0;i<k;i++)//判断答案的时候
    {
        a=_seach(ques[i].l);
        b=_seach(ques[i].r);
        relax=ques[i].vn;
        flag=_judge(a,b,relax);
        ans=i;
        if(!flag)
        {
            printf("%d\n",i);break;
        }

    }
    if(flag)
        printf("%d\n",k);
}```


 

 

 

 

 



昨天做了个POJ-食物链的带权并查集，那可把我难为死了，看了几个博客，都是一个公式解决，并没有详细解说为什么这样做，所以喜欢寻根问底的我(●'◡'●)苦思冥想，终于从中得到了启发，这个题的解题思路也相似。

 

**解决这种带权并查集问题，与并查集问题（father[N]）只是多加了个关系，这个关系表示与他父亲的关系，我把他记作relat[N],**

**关键就是怎样通过关系，来构建一个关系表达式，使得求两个数的关系可以通过其他关系来间接求出**。

上面的就是基本的思想，下面咱们来就题论题。

先放题目：

 

TT and FF are ... friends. Uh... very very good friends -________-b FF is a bad boy, he is always wooing TT to play the following game with him. This is a very humdrum game. To begin with, TT should write down a sequence of integers-_-!!(bored).


![./figures/956a59c85e195b555e72de064fd5a563](./figures/956a59c85e195b555e72de064fd5a563)


Then, FF can choose a continuous subsequence from it(for example the subsequence from the third to the fifth integer inclusively). After that, FF will ask TT what the sum of the subsequence he chose is. The next, TT will answer FF's question. Then, FF can redo this process. In the end, FF must work out the entire sequence of integers. Boring~~Boring~~a very very boring game!!! TT doesn't want to play with FF at all. To punish FF, she often tells FF the wrong answers on purpose. The bad boy is not a fool man. FF detects some answers are incompatible. Of course, these contradictions make it difficult to calculate the sequence. However, TT is a nice and lovely girl. She doesn't have the heart to be hard on FF. To save time, she guarantees that the answers are all right if there is no logical mistakes indeed. What's more, if FF finds an answer to be wrong, he will ignore it when judging next answers. But there will be so many questions that poor FF can't make sure whether the current answer is right or wrong in a moment. So he decides to write a program to help him with this matter. The program will receive a series of questions from FF together with the answers FF has received from TT. The aim of this program is to find how many answers are wrong. Only by ignoring the wrong answers can FF work out the entire sequence of integers. Poor FF has no time to do this job. And now he is asking for your help~(Why asking trouble for himself~~Bad boy) 

Input

Line 1: Two integers, N and M (1 <= N <= 200000, 1 <= M <= 40000). Means TT wrote N integers and FF asked her M questions. Line 2..M+1: Line i+1 contains three integer: Ai, Bi and Si. Means TT answered FF that the sum from Ai to Bi is Si. It's guaranteed that 0 < Ai <= Bi <= N. You can assume that any sum of subsequence is fit in 32-bit integer. 

Output

A single line with a integer denotes how many answers are wrong.

Sample Input

```
10 5
1 10 100
7 10 28
1 3 32
4 6 41
6 6 1```


Sample Output

```
1```


题意：

 

给出一个n，和m，表示总共有n个数组成的数列，下面问m个回复，每个问题由三部分组成，p q v，表示数列中从第p个数到第q个数的元素的和v。

要你找出其中错误回复的个数--也就是这个回答与上面的冲突。

**根据题意，思考，构建模型。确定下来用构建并查集，**

**因为 a b的v中包含a b，所以用并查集向量的方式不容易得出其中的线性关系**，**但是如果我让a表示p-1，b表示q ,那么此时的a b v ****就表示不带左端点的从a到b的元素和v**，那么其中就可以表示一些线性关系了

**********************                                                             做个标识-----------  A->B 表示 A到其父节点B的 V。**

 

**当a<b, b<c时   有下面的关系成立**


![./figures/20180110110422478](./figures/20180110110422478)


**即    a->b+b-c=a->c **                     方程式  ①


![./figures/20180110111716432](./figures/20180110111716432)


**好好斟酌一下就可以理解这个关系式   **

 

**————————————————————————————————————————————**

**那么当b>c是还符合吗 ?**

**NO！！      当 a<b b>c时  a->b+b->c并不等于a->c 看下面的证明过程**

(●'◡'●)  画的不好凑合着先用

  
![./figures/20180110114735194](./figures/20180110114735194)


**a->b 包含端点b 但是b->c不包含端点b **

**故在计算时a->b+b->c 其实等于 a->(c-1 )+b  可见并不等同于a->c         (你可以试着计算一下a->b+c->b)**

**-----------------------------————————————————————————————————————————————————————————————————**

 

 

**所以要想保证该模型有方程式①的线性关系，那么就必须保证a<b  b<c 。这样才能得出 a->c**

**所以咱们构建的并查集要想实现这种线性关系 必须保证每个子节点的序号小于父子节的序号，这样相减也符合**

 

其实到这里这道题就没什么问题了，下面的都是思想实现过程

**此类只需保证 1.子节点的序号比父节点的序号小**

压缩路径注意改变与父亲的关系

 

 

```cpp
#include<stdio.h>/carefly
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
#define N 200110
using namespace std;
int father[N],relat[N],sum;//sum声明成全局变量保证在下面更新父子关系时 关系值的变化
void up_date(int n)
{
    for(int i=0;i<=n;i++)
    {
         father[i]=i;
         relat[i]=0;
    }
}
int _find(int x)//找根//压缩路径//找到关系//线性压缩
{
    int team;
    if(father[x]==x)
        return x;
    team=_find(father[x]);//最终节点
    sum=sum+relat[x];//向量关系计算
    father[x]=team;//压缩路径
    relat[x]=sum;//改变与父节点的relat值量
    return team;
}
int main()
{
    int n,m,p,q,summ,root1,root2,ans,mod;
    while(~scanf("%d %d",&n,&m))
    {
    up_date(n);
    ans=0;
    for(int i=1;i<=m;i++)
    {
        scanf("%d %d %d",&q,&p,&summ);//注意q<=p;
        q--;//这里我把q看作起点
        sum=0;
        root1=_find(q);
        sum=0;
        root2=_find(p);
        if(root1!=root2)//合并集合 //注意小的要并到大的上面
        {
            if(root1<root2)
            {
                father[root1]=root2;
                relat[root1]=summ+relat[p]-relat[q];
            }
            else
            {
                father[root2]=root1;
                relat[root2]=relat[q]-summ-relat[p];
            }

        }
        else//判断是否合理
        {
            mod=relat[q]-relat[p];
            if(summ!=mod)//no合理
                ans++;

        }
    }
    printf("%d\n",ans);
    }
}```


这道题上面没说多组输入，但是只能多组输入才能过

 

**参考的博客：**

**[http://blog.csdn.net/backforward/article/details/51889011](http://blog.csdn.net/backforward/article/details/51889011)**  

