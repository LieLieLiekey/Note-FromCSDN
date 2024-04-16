

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

