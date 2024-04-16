

刚做了一个搜索的专题，没做这个专题时只懂得搜索的思想（当然简单的搜索题也可以一波打AC） 写这个是为了总结一下，实际上只求自己能看懂就行。

做专题之后对广搜的理解又深了一步，

**多路搜索**：

think ： 每个源点开始搜索，期间用个辅助mapp 与map合作生效为真正的map，广搜最先到达的状态一定是最短路径，记录下该源点到每个状态的最短路径，然后找出每个源点都能到达的目的点的step，找出最小的即可。

eg: Find a way



**回溯搜索**：即 不仅可以找出最短路径，并且可以知道到这个路径的走法

think： 用father数组 根基这个数组的状态作为下标，存下父节点的状态即可

eg : H - Pots



**抽象搜索**：

毫无疑问  将抽象问题转化为易分析的问题

eg：M - 非常可乐



在搜索过程中 有许多可以简化的地方，简化代码 （熟练使用vis[][]，dir[][]）



  大家一定觉的运动以后喝可乐是一件很惬意的事情，但是seeyou却不这么认为。因为每次当seeyou买了可乐以后，阿牛就要求和seeyou一起分享这一瓶可乐，而且一定要喝的和seeyou一样多。但seeyou的手中只有两个杯子，它们的容量分别是N 毫升和M 毫升 可乐的体积为S （S<101）毫升　(正好装满一瓶) ，它们三个之间可以相互倒可乐 (都是没有刻度的，且 S==N+M，101＞S＞0，N＞0，M＞0) 。聪明的ACMER你们说他们能平分吗？如果能请输出倒可乐的最少的次数，如果不能输出"NO"。 
Input三个整数 : S 可乐的体积 , N 和 M是两个杯子的容量，以"0 0 0"结束。Output如果能平分的话请输出最少要倒的次数，否则输出"NO"。Sample Input 
7 4 3
4 1 3
0 0 0

Sample Output 
NO
3




抽象的搜索问题，

每次操作都有6个方向 （将三个杯子分别编号为0 ，1，2对应的Full的容量为S,N,M）

1.     0->1(0号杯子往1号杯子里面倒)

2.     2->1

3.     0->2

4.     1->2

5      1->0

6      2->0

将每次操作后杯子饮料的容量作为地图map[][]存放前两个杯子饮料的容量 。（三个杯子饮料总和一定，前两个确定，第三个也杯子内饮料的容量也就确定了，所以用两个杯子就可以了）

这样根据杯子倒水次数来广搜，杯子的饮料的容量作为路径去搜索

1.方向数组vis[6][3] 存每次操作对应的编号

2.Full[]数组存下对应编号杯子的最大容量

3.tiji[]数组表示此次倒水之后对应编号的饮料的容量

4.map[][]数组以前两个编号杯子的容量为下标，0表示出现过，1表示未出现过;

5.用个Turn（）函数来表示倒饮料的操作



map[i][j]=1，表示该状态已经存在，下次再出现i ,j的情况时就不用去搜索这种情况(未找到答案也是这因这种情况而停止的)





PS值得一提的是，没有答案时说明倒水操作一直在一个重复过的循环当中,//题外话，不要将这个看作解题的一部分(●'◡'●)



```cpp
#include<stdio.h>开三位数组会超时，但这道题开个二维数组就OK了，因为总量一定 前两个的体积知道 第三个也就确定了
#include<string.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<stdlib.h>
#define N 110
#include<string>
using namespace std;
int map[N][N],flag,s,n,m,ans,vis[6][3]={{1,0,0},{2,0,0},{0,1,1},{2,1,1},{0,2,2},{1,2,2}},Full[3],tiji[3];
double zhi;
struct node{
int v,a,b,step;
};
queue<struct node>mmp;
void turn(int *aa,int *bb,int full)//a->b
{
     int a,b;
     a=*aa;
     b=*bb;
     if(*aa+*bb>full)
     {
         a=*aa+*bb-full;
         b=full;
     }
     else
     {
         a=0;
         b=*aa+*bb;
     }
     *aa=a;
     *bb=b;
     return ;
}

void dfs()
{
    struct node mm;
    int ss,mod1,vv,aa,bb;//表示此时的状态 vv,aa,bb;
    mm=mmp.front();
    vv=mm.v;
    aa=mm.a;
    bb=mm.b;
    ss=mm.step;
    mod1=0;
    if(aa==zhi)
        mod1++;
    if(bb==zhi)
        mod1++;
    if(vv==zhi)
        mod1++;
    if(mod1==2)//是否为答案
    {
        flag=1;
        ans=ss;
        return;
    }
    mmp.pop();
    for(int i=0;i<6;i++)
    {
        tiji[0]=vv;//每次都初始化体积数组
        tiji[1]=aa;//
        tiji[2]=bb;//
        turn(&tiji[vis[i][0]],&tiji[vis[i][1]],Full[vis[i][2]]);//倒水操作
        if(!map[tiji[0]][tiji[1]])//用不用去搜索
        {
            struct node mm;
            mm.v=tiji[0];
            mm.a=tiji[1];
            mm.b=tiji[2];
            mm.step=ss+1;
            map[tiji[0]][tiji[1]]=1;
            mmp.push(mm);
        }
    }

}
void bfs()
{
    struct node qq;
    qq.v=s;
    qq.a=qq.b=qq.step=0;
    map[s][0]=1;
    mmp.push(qq);
    while(!mmp.empty())
    {
        dfs();
        if(flag)
            return;
    }
}
int main()
{
    while(scanf("%d %d %d",&s,&n,&m)&&s)
    {
        Full[0]=s;
        Full[1]=n;
        Full[2]=m;
        flag=0;
        zhi=s/2.0;
        memset(map,0,sizeof(map));
        while(!mmp.empty())
            mmp.pop();
        bfs();
        if(flag)
            printf("%d\n",ans);
        else
            printf("NO\n");
    }
}
```








  给你两个容器，分别能装下A升水和B升水，并且可以进行以下操作 


  FILL(i)        将第i个容器从水龙头里装满(1 ≤ i ≤ 2); 


  DROP(i)        将第i个容器抽干 


  POUR(i,j)      将第i个容器里的水倒入第j个容器（这次操作结束后产生两种结果，一是第j个容器倒满并且第i个容器依旧有剩余，二是第i个容器里的水全部倒入j中，第i个容器为空） 


  现在要求你写一个程序，来找出能使其中任何一个容器里的水恰好有C升，找出最少操作数并给出操作过程 
Input 

有且只有一行，包含3个数A,B,C（1<=A,B<=100,C<=max(A,B)）Output 

  第一行包含一个数表示最小操作数K 


  随后K行每行给出一次具体操作，如果有多种答案符合最小操作数，输出他们中的任意一种操作过程，如果你不能使两个容器中的任意一个满足恰好C升的话，输出“impossible” 
Sample Input 
3 5 4

Sample Output 
6
FILL(2)
POUR(2,1)
DROP(1)
POUR(2,1)
FILL(2)
POUR(2,1)




**回溯搜索**

**记下搜索路径的父亲即可.**

****

**此代码中（map[i][j][0],map[i][j][1]）代表父亲的坐标。 map[i][j][2]来表示父状态到此状态所经历的方法，map[i][j][2]=0也就表示没有从父状态到此状态的方法或者未出现过此路径**



```cpp
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<stdlib.h>
#define N 300
#include<string>
using namespace std;
int a,b,c,ans,flag,map[110][110][3],res[100];
struct node
{
    int aa;
    int bb,step;
};
queue<struct node>mmp;
void dfs()
{
    int aa,bb,ss;
    struct node qq;
    qq=mmp.front();
    aa=qq.aa;
    bb=qq.bb;
    ss=qq.step;
    if(aa==c||bb==c)//判断是否为答案
    {
        flag=1;
        ans=ss;
        return;
    }
    mmp.pop();
    if(!map[a][bb][2])
    {
        struct node mm;
        mm.aa=a;
        mm.bb=bb;
        mm.step=ss+1;
        map[a][bb][0]=aa;
        map[a][bb][1]=bb;
        map[a][bb][2]=1;
        mmp.push(mm);
    }
    if(!map[aa][b][2])
    {
        struct node mm;
        mm.aa=aa;
        mm.bb=b;
        mm.step=ss+1;
        mmp.push(mm);
        map[aa][b][0]=aa;
        map[aa][b][1]=bb;
        map[aa][b][2]=2;
    }
    if(!map[0][bb][2])
    {
        struct node mm;
        mm.aa=0;
        mm.bb=bb;
        mm.step=ss+1;
        mmp.push(mm);
        map[0][bb][0]=aa;
        map[0][bb][1]=bb;
        map[0][bb][2]=3;
    }
    if(!map[aa][0][2])
    {
        struct node mm;
        mm.aa=aa;
        mm.bb=0;
        mm.step=ss+1;
        mmp.push(mm);
        map[aa][0][0]=aa;
        map[aa][0][1]=bb;
        map[aa][0][2]=4;
    }
    //方法5
    int ii,jj;
    if((aa+bb)>a)
    {
        jj=aa+bb-a;
        ii=a;
    }
    else
    {
        ii=aa+bb;
        jj=0;
    }
    if(!map[ii][jj][2])
    {
        struct node mm;
        mm.aa=ii;
        mm.bb=jj;
        mm.step=ss+1;
        mmp.push(mm);
        map[ii][jj][0]=aa;
        map[ii][jj][1]=bb;
        map[ii][jj][2]=5;
    }
    //方法6
    if((aa+bb)>b)
    {
        ii=aa+bb-b;
        jj=b;
    }
    else
    {
        ii=0;
        jj=aa+bb;
    }
    if(!map[ii][jj][2])
    {
        struct node mm;
        mm.aa=ii;
        mm.bb=jj;
        mm.step=ss+1;
        mmp.push(mm);
        map[ii][jj][0]=aa;
        map[ii][jj][1]=bb;
        map[ii][jj][2]=6;
    }
}
void bfs()
{
    struct node qq;
    qq.aa=qq.bb=qq.step=0;
    map[0][0][0]=map[0][0][1]=-1;
    map[0][0][2]=-1;
    mmp.push(qq);
    while(!mmp.empty())
    {
        dfs();
        if(flag)
            return ;
    }
}
int main()
{
    scanf("%d %d %d",&a,&b,&c);
    bfs();
    if(flag)
    {
        int ii,jj,mod1=1,mod2=2;
        struct node mm;
        mm=mmp.front();
        ii=mm.aa;
        jj=mm.bb;
        int k=0;
        while((ii!=-1)||(jj!=-1))
        {
            res[k++]=map[ii][jj][2];
            mod1=map[ii][jj][0];
            mod2=map[ii][jj][1];
            ii=mod1;
            jj=mod2;
        }
        printf("%d\n",ans);
        for(int i=k-1; i>=0; i--)
        {
            if(res[i]==1)
            {
                printf("FILL(1)\n");
                continue;
            }
            if(res[i]==2)
            {
                printf("FILL(2)\n");
                continue;
            }

            if(res[i]==3)
            {
                printf("DROP(1)\n");
                continue;
            }

            if(res[i]==4)
            {
                printf("DROP(2)\n");
                continue;
            }

            if(res[i]==5)
            {
                printf("POUR(2,1)\n");
                continue;
            }

            if(res[i]==6)
            {
                printf("POUR(1,2)\n");
                continue;
            }
        }
    }
    else
        printf("impossible\n");
}```








圣诞节要到了，坤神和瑞瑞这对基佬想一起去召唤师大峡谷开开车。百度地图一下，发现周围的召唤师大峡谷还不少，这对基佬纠结着，该去哪一个。。。坤神：我要去左边的这个（因为离自己比较近 哈哈~）。。瑞瑞：我要去右边的这个（因为离自己比较近 嘿嘿~） ........这对基佬闹矛盾了，开车有危险了！  为了不让他们去召唤师大峡谷坑人，riot决定让他们去X召唤师大峡谷，保证他俩所走的路程和最短。每走一个点需要花费11分钟，输出他们一共花费多少时间（最短时间噢）Input 

多组测试数据

每组数据，开始一行n，m (2<=n,m<=200)

接下来是个n x m的矩阵

'Y' 表示坤神所在的初始位置

'M' 表示瑞瑞所在的初始位置

'#' 该点禁止通行

'.' 该点可通行

'@' 召唤师大峡谷Output 

每组测试数据，输出坤神和瑞瑞到达同一个召唤师大峡谷所花费的最短时间。Sample Input 
4 4
Y.#@
....
.#..
@..M
4 4
Y.#@
....
.#..
@#.M
5 5
Y..@.
.#...
.#...
@..M.
#...#Sample Output 
66
88
66



****

**这个题也可以将召唤师峡谷看作路走。（当时就因为这一点一直wa）;**

**简单的多路搜索**

每个源点Y  M 搜索到每个召唤师峡谷  ,,ԾㅂԾ,,  的最短路径 ， 接下来遍历召唤师峡谷 ，找出都能到此处并且最短路径和最小的步数。

过程实现的细节:

1.vis[4][2]作为搜索的方向的增量

2.用map存输入数据的地图，数组bbj[][]将走过的坐标记作1，  所以搜索过程中坐标能走的必要条件是map中该坐标能走且bbj[i][j]==0（这个坐标未搜过）

3.其中存放答案的mapp[][][]数组    mapp[i][j][0],中  i ,j表示map地图对应的坐标，而mapp[i][j][0]存的是**所有源点中能到达此坐标**的**最短路径和。**

mapp[i][j][1]表示全部源点中能到此坐标的数量.（**在此题中map[i][j]=2才有效**）



```cpp
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<queue>
#define N 200
#define inf 0x1f1f1f1f//使得能更新ans
using namespace std;
char map[N+10][N+10];
int bbj[N+10][N+10],n,m;
int vis[4][2]={{-1,0},{0,-1},{0,1},{1,0}},mapp[N+10][N+10][2];//存放答案的
struct node{
    int i,j,step;
};
typedef struct node Node;
queue<Node>mmp;
void dfs()//与bfs分开写纯属个人喜好
{
    Node mm;
    int ii,jj,ss,aa,bb;
    mm=mmp.front();
    ii=mm.i;
    jj=mm.j;
    ss=mm.step;
    mmp.pop();
    for(int i=0;i<4;i++)
    {
        aa=ii+vis[i][0];
        bb=jj+vis[i][1];
        if((!bbj[aa][bb])&&aa>=1&&aa<=n&&bb>=1&&bb<=m&&map[aa][bb]!='#')//这个方向能走
        {
            bbj[aa][bb]=1;//使这个坐标已经在搜索的队列中,不让其他路搜索
            mapp[aa][bb][0]+=ss+1;//加上此源点到这个坐标的step
            mapp[aa][bb][1]++;//该源点已经到达该坐标
            Node mm;
            mm.i=aa;
            mm.j=bb;
            mm.step=ss+1;
            mmp.push(mm);
        }
    }
}
void bfs(int a,int b)//开始坐标
{
    while(!mmp.empty())
        mmp.pop();
  Node qq;
  qq.i=a;
  qq.j=b;
  qq.step=0;
  mmp.push(qq);
  while(!mmp.empty())
        dfs();
}
int main()
{
    int ans,x1,x2,y1,y2;
    while(~scanf("%d %d",&n,&m))
    {
        memset(bbj,0,sizeof(bbj));
        memset(mapp,0,sizeof(mapp));
        for(int i=1;i<=n;i++)//输入地图
            scanf("%s",map[i]+1);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(map[i][j]=='Y')
                {
                    x1=i,y1=j;
                }
                if(map[i][j]=='M')
                {
                    x2=i,y2=j;
                }
            }
        }
        bfs(x1,y1);
        memset(bbj,0,sizeof(bbj));//重置bbj
        bfs(x2,y2);
        ans=inf;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(map[i][j]=='@' && mapp[i][j][1]==2)//两个源点都能到的召唤师峡谷
                    ans=mapp[i][j][0]>ans?ans:mapp[i][j][0];
            }
        }
        printf("%d\n",ans*11);
    }
}```





简单的多路搜索





+  
## H 幻方变换(puzzle)（NYIST 2019年校赛）
 



如果一个 3 × 3 的矩阵中，整数 1-9 中的每个都恰好出现一次，我们称这个矩阵为一个幻 方。

我们可以对一个幻方进行一些操作。具体来说，我们可以

• 选择幻方的一行，整体向右移动一格，并将最右侧的数字移到最左边；或者

• 选择幻方的一列，整体向下移动一格，并将最下侧的数字移到最上面。

例如，下面两个操作分别是一种合法的行操作和列操作：


![./figures/9b9944d4e8b854f3bd0fddb13ef3d196.png](./figures/9b9944d4e8b854f3bd0fddb13ef3d196.png)


显然，一个合法的幻方经过一次操作后一定还是合法的幻方。

给定幻方的初始状态，请问，最少要经过多少次变换，才能变成最终状态？

### 输入描述:


```bash
第一行一个整数 T (1 ≤ T ≤ 200000)，表示测试用例的数量。

接下来有 T 组测试用例，每组测试用例前有一个空行。每组样例的前 3 行为幻方的初始状态，后 3 行为幻方的最终状态。每行的数字之间没有空格。

保证初始状态和最终状态都是合法的幻方。
```


### 输出描述:


```bash
对于每组测试用例在一行内输出一个整数，表示答案。如果不可能从起始状态转变为最终状态，输出 impossible。
```


### 样例输入:


```bash
4

1```




### [Q - 水陆距离](https://vjudge.net/problem/HihoCoder-1478)


[HihoCoder - 1478 ](https://vjudge.net/problem/708796/origin)

给定一个N x M的01矩阵，其中1表示陆地，0表示水域。对于每一个位置，求出它距离最近的水域的距离是多少。

矩阵中每个位置与它上下左右相邻的格子距离为1。

Input

第一行包含两个整数，N和M。

以下N行每行M个0或者1，代表地图。

数据保证至少有1块水域。

对于30%的数据，1 <= N, M <= 100

对于100%的数据，1 <= N, M <= 800

Output

输出N行，每行M个空格分隔的整数。每个整数表示该位置距离最近的水域的距离。

Sample Input

```bash
4 4  
0110  
1111  
1111  
0110
```


Sample Output

```bash
0 1 1 0  
1 2 2 1  
1 2 2 1  
0 1 1 0
```


### 思路：


​ 广搜。将所有水域$0 0$全部放入队列并将离水域的距离设$0 0$。接下来$b f s bfs$周围的所有未计算过Mindis的点，先被广搜到的点的状态就是离水域的最短距离，标记已经计算过并加入队列。


刚好一年前做过的题，现在比赛不会做，我真是太菜了


### 代码：


```cpp
#include<queue>
#include<iostream>
#include<string.h>
#include<cstdio>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
const int maxn=```




## [2000年NOIP全国联赛普及组] 1019: 单词接龙


题目链接：[http://129.211.20.246/problem.php?id=1019](http://129.211.20.246/problem.php?id=1019)

##### 题目描述


单词接龙是一个与我们经常玩的成语接龙相类似的游戏，现在我们已知一组单词，且给定一个开头的字母，要求出以这个字母开头的最长的“龙”（每个单词都最多在“龙”中出现两次），在两个单词相连时，其重合部分合为一部分，例如beast和astonish，如果接成一条龙则变为beastonish，另外相邻的两部分不能存在包含关系，例如at和atide间不能相连。

##### 输入


每个测试文件只包含一组测试数据，每组输入的第一行为一个单独的整数n（n<=20）表示单词数，以下n行每行有一个单词，输入的最后一行为一个单个字符，表示“龙”开头的字母。你可以假定以此字母开头的“龙”一定存在。

##### 输出


对于每组输入数据，输出以此字母开头的最长的“龙”的长度。

下面的测试样例最后连成的“龙”为atoucheatactactouchoose。

##### 样例输入 [Copy](javascript:CopyToClipboard($(’#sampleinput’).text()))


```bash
5
at
touch
cheat
choose
tact
a
```


##### 样例输出 [Copy](javascript:CopyToClipboard($(’#sampleoutput’).text()))


```bash
23
```


### 思路：


​ 暴力深搜即可。（比赛中以为会超时，毕竟复杂度O(n!) ,赛后才知道这么简单。

​ 需要注意的一点是：


+  组合的单词不可互相包含


例如：ac与acc，或者abc与bc
 
+  两个单词可以组合则取**重合长度最小**的组合


例如:accc与cccc组合，组合后为acccccc ,而不是acccc
 



### 代码：


```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
#define x first
#define y second
using namespace std;
typedef long long ll;
const int maxn=1e6+10;
string S[22];
int n,ps[22][22],book```


