

**（1）二次项定理**

根据此定理，可以将$x + y x + y$ 的任意次幂展开成和的形式



$$( a + b ) n = C n 0 a 0 b n + C n 1 a 1 b n − 1 . . . + C n k a k b n − k . . . + C n n a n b 0 (a + b)^{n} = C_{n}^{0}a^{0}b^{n} + C_{n}^{1}a^{1}b^{n - 1}... + C_{n}^{k}a^{k}b^{n - k}... + C_{n}^{n}a^{n}b^{0}$$



也可以表示为



$$( a + b ) n = ∑ k = 0 n C n k a k b n − k = ∑ k = 0 n C n k a n − k b k (a + b)^{n} = \sum_{k = 0}^{n}C_{n}^{k}a^{k}b^{n - k} = \sum_{k = 0}^{n}C_{n}^{k}a^{n - k}b^{k}$$





容斥的几种写法


容斥公式本身就是 **枚举出状态的组合**，算其乘积，奇数个值为负，偶数个值为正

原理：

对于组合中每个状态有 **在**或**不在**两种，求其组合，可以用二进制枚举，也可以用递归

+ 二进制+ 两层for循环+ 递归



```cpp
#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<map>
#include<vector>
#include<time.h>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
//假设有tot个数，存储在num数组中
int num[20];//存放数字种类
int rc[maxn];//存放容斥的组合
int tot;//数字种类数
int cnt;//容斥组合的个数
void rc_for()//求出num中 tot个数的所有组合
{
    cnt=0;
    rc[cnt++]=1;//初始状态
    for(int i=0; i<tot; ++i)
    {
        int k=cnt;//下标为i的数与前k个数的所有组合的组合
        for(int j=0; j<k; ++j)
        {
            rc[cnt++]=num[i]*rc[j]*-1;//奇数个为负
        }
    }
}
void rc_bit()//用二进制来写
{
    int top=1<<tot;//共tot个数字
    cnt=0;
    for(int i=0; i<top; ++i)
    {
        int val=1;
        for(int k=0; k<tot; ++k) //枚举每个位是否为1 为1的组合整上去
        {
            if((1<<k)&i)
            {
                val*=-1*num[k];
            }
        }
        rc[cnt++]=val;
    }
}
void dfs(int k,int val)//正在枚举下标为k的状态, 之前组合乘积为-1
{
    if(k==tot)
    {
        rc[cnt++]=val;
        return ;
    }
    dfs(k+1,val*-1*num[k]);//下标为k的状态在组合中
    dfs(k+1,val);
}
void rc_dfs()
{
    cnt=0;
    dfs(0,1);//
}
int main()
{
    //主要是枚举这些数的所有组合(不能重复)
    /*
    测试
    */
    scanf("%d",&tot);
    for(int i=0; i<tot; ++i)
        scanf("%d",num+i);
    rc_for();
    printf("\nrc_for.........\n");
    cout<<"cnt:"<<cnt<<endl;
    for(int i=0; i<cnt; ++i)
        printf("%d ",rc[i]);
    puts("");
    printf("rc_bit.........\n");
    rc_bit();
    cout<<"cnt:"<<cnt<<endl;
    for(int i=0; i<cnt; ++i)
        printf("%d ",rc[i]);
    puts("");
    rc_dfs();
    cout<<"cnt:"<<cnt<<endl;
    for(int i=0; i<cnt; ++i)
        printf("%d ",rc[i]);
    return 0;
}

```




## 排列组合



根本思想还是组合数学的加法原则，将一个状态分成几个不相交的状态，然后用加法原则加起来即可


#### 1.球同，盒不同，无空箱


如果：n>=m $C(n-1,m-1)$

否则 n<m $0$

**分析** :

使用插板法：n个球中间有n-1个间隙，现在要分成m个盒子，而且不能有空箱子，所以只要在n-1个间隙选出m-1个间隙即可。

#### 2.球同，盒不同，允许空箱


$C(n+m-1,m-1)$

我们在第1类情况下继续讨论，我们可以先假设m个盒子里都放好了1个球，所以说白了就是，现在有m+n个相同的球，要放入m个不同的箱子，没有空箱。也就是第1种情况

#### 3.球不同，盒相同，无空箱


第二类斯特林数dp[n][m]


dp[n][m]表示n个球 m个盒子的方法数

分两种状态

1.第n个球单独在一个盒子里 有dp[n-1][m-1]

2.第n个球不单独在一个盒子里 有m*dp[n-1][m]


$dp[n][m]=m * dp[n-1][m]+dp[n-1][m-1]$

边界条件：

dp[k][k]=1, k>=0

dp[k][0]=0,k>=1

0,n<m

#### 4.球不同，盒相同，允许空箱



枚举使用箱子的个数即可 此时的dp[n][m]是情况三的第二类的斯特林数


$ans=\sum_{i=0}^m dp[n][i]$

#### 5.球不同，盒不同，无空箱


$ans=dp[n][m]*m!$

因为球是不同的，所以dp[n][m]得到的盒子相同的情况，只要再给盒子定义顺序，就等于现在的答案了

#### 6.球不同，盒不同，允许空箱


power(m,n) 表示m的n次方

每个球都有m种选择，所以就等于m^n

#### 7.球同，盒同，允许空箱



n个球m个盒子，分两种情况

dp[n][m]代表n个球m个盒子允许空箱的个数

两种状态

1.每个盒子至少有一个球 有dp[n-m][m]种情况

2.至少有一个盒子没有球 有dp[n][m-1]种情况



n-m>=0:


$dp[n][m]=dp[n][m-1]+dp[n-m][m]$


n<m:


$dp[n][m]=dp[n][m-1]$

#### 8.球同，盒同，无空箱


dp[n-m][m],dp同第7种情况,n>=m 0, n<m

因为要求无空箱，我们先在每个箱子里面放1个球，然后还剩下n-m个球了，再根据情况7答案就出来了



### [C - Glenbow Museum](https://cn.vjudge.net/problem/UVALive-4123)


[UVALive - 4123 ](https://cn.vjudge.net/problem/12130/origin)

题意：


​ **对于一个边平行于坐标轴的多边形，我们可以用一个由R或者O组成的序列来描述他，从一个顶点开始按照逆时针顺序走，碰到一个90°的内角记作R；碰到一个270°的内角记作O。这样的序列称为角度序列。**

​ **给定正整数L，有多少个长度为L的角度序列至少可以对应一个星形多边形（即多边形中存在一个点，可以看到多边形边界上的每一个点）？多边形的每条边长度任意。注意一个多边形有多条角度序列与之对应，RRORRR与ORRRRR是不同序列，但可以描述同一个多边形。**


输入描述：


​ **输入包含多组数据，每组数据仅占一行，即角度序列的长度L（1<=L<=1000）输入结束标志（L=0）**


输出描述：


​ **对于每组数据，输出满足条件的角度序列的个数。**


分析：


​ 长度为L的多边形的内角和是一定的，且270°的内角与90°的内角的个数是恒定为L。所以设90°的个数为x个，270°的个数为y个。

$x+y=L$

$90*x+270*x=(L-2)*180$

解得

$x=(l+4)/2$

$y=(l-4)/2$

故可知 90°的序列比270°的多4个，且L必须为偶数，且L >=4

​



**还有那些限制条件呢？**

题目描述的形状由上 下 左 右 四条边，即由4个RR的连续的串， 且OO不能连在一起，最左边是O，最右边是O也不行

那么可以用插空法

1.最左（右）边是O的方法数目 C（x-1，y-1）

2.左右两边有没有O的方法数目 C（x-1，y ）

故答案 

$$ans=C(x-1,y-1)*2+C(x-1,y)$$




```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=10000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
ull l;
int main()
{
    ull ans;
    int kcas=0;
    while(cin>>l,l)
    {
        if(l<=3||l&1)
        {
            ans=0;
        }
        else
        {
            ull x=(l+4)/2;
            ans=(x*(x-1)*(x-2)*(x-3))/24+((x-1)*(x-2)*(x-3)*(x-4))/24;
        }
        printf("Case %d: ",++kcas);
        cout<<ans<<endl;

    }
    return 0;
}
```




### [D - Series-Parallel Networks](https://cn.vjudge.net/problem/UVA-10253)


[UVA - 10253 ](https://cn.vjudge.net/problem/34527/origin)

题意就不描述了

输入格式：


​ 输入包含多组式布局，每组数据仅包含一个整数，即边数n（1<=n<=30）。输入结束标志为n=0。


输出格式：


​ 对于每组数据，输出一行，即包含m条边的串并联网络的数目。


这是白皮书上117页的内容，其中给出了两个算法，第一个算法理解但是有点难实现，第二个算法是真心不懂（但是第二个算法代码确实很简单dp吧）

第一个算法：


​ 把串并联网络看作一个树，因为每个串联网络一个分成**多个并联网络或者单边** 串联，并联网络可以分成

**多个串联网络或者单边** 并联。可以想想成一棵树的形式，假设刚开始有一个根是一个串连网络（并联网络），下一层全是并联网络（串联网络），就这样交替出现，当然每一棵树的最少得有两个儿子，如果这个棵数是个单边，那么他就是个叶子节点，没有儿子，这样问题就转化为了“共n个叶子，且每个非叶子节点至少有两个子节点”的树的数目f（n）,再乘以2就是本题的答案。

即找出n个叶子的树有多少种。


因为题目中说串联在一起（并联在一起）的各个部分可以相互调换顺序，相当于每一层的树交换顺序后 属于同一种，所以我们只要保证从**左到右节点数**是**递增或者递减的就可以了**。

假设对于5个叶子的节点，子树可以分为

1 1 1 1 1

1 1 1 2

1 1 3

1 4

1 2 2

2 3

**把每种的情况全加起来即可**

对于24个叶子的树：

2 10 12 的情况共有 $f ( 2 ) ∗ f ( 10 ) ∗ f ( 12 ) f(2)*f(10)*f(12)$种方法

对于 6 6 6有多少种方法吗？难道是$f ( 6 ) ∗ f ( 6 ) ∗ f ( 6 ) f(6)*f(6)*f(6)$



带标号的连通图计数

题目描述：


带标号的连通图计数。统计有n ( n<=50)个顶点的连通图有多少个。图的顶点有编号。例如n=3时有4个不同的图， n=4时有38个图；n=5,6时分别有728，26704个图


分析：


设f（n）为所求答案，g（n）为由n个顶点的非连通图，则f（n）+g（n）=h（n）=2n(n-1)/2 。

g（n）可以这样计算：先考虑1所在连通分量包含哪些顶点。假设1所在连通分量有k(k<n)个顶点，就有C（n-1，k-1）中取法，剩下的n-k的顶点随便共有h（n-k）中方法，根据加法原理

​ 

$$g （ n ） = ∑ k = 1 n − 1 C ( n − 1 , k − 1 ) ∗ f ( k ) ∗ h ( n − k ) g（n）= \sum_{k=1}^{n-1}C(n-1,k-1)*f(k)*h(n-k)$$



​ 

$$f ( n ) = h ( n ) − g ( n ) f(n)=h(n)-g(n)$$



初始状态

f（0）=1；算是一个空图

f（1）=1，h（1）=1，g（1）=0


因为数据较大，所以涉及到高精度乘法减法加法。

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#```




### [F - Ingenuous Cubrency](https://vjudge.net/problem/UVA-11137)


[UVA - 11137 ](https://vjudge.net/problem/19454/origin)

**题目描述** ：


​ 立方数之和。输入正整数n( n<=10000) ，求将n写成若干个正整数的立方和有多少种方法。

比如21有3种写法：21=13+13 …+13=23+13+13…13=23+23+13…13 。

77有22种写法，9999有440 022 018 293中写法。


**多组输入** ：


​ 每组输入一个n.


**输出描述** ：


​ 输出有多少种方法.


**分析** ：

​ 可以用多重背包写，也可以建立多段图（后者时间复杂度高），


多重背包

dp（i，j）表示最多不超过i，立方和为j的方法数目

初始状态：dp（0，0）=1

递推关系：dp （i，j）=dp（i-1，j）+dp（i，j - i*i*i*i ） (i>=1)


多段图：


初始状态：dp （0，0）=1

状态转移：对于每个dp（i，j） for k=0 to j+k*i*i*i<=maxn: dp（i，j+k*i*i*i）+=dp（i，j）

表示i，j这个状态可以加上一个i3 或者加上多个i3 转移到 i+1这个状态中


代码1：

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=10000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
ll dp[26][maxn+10];
void Preprocess()
{
    mset(dp,0ll);
    dp[0][0]=1;
    for(int i=1; i<=21; ++i) //最大不超过i
    {
        for(int j=0; j<=maxn; ++j) //递推关系  实际从dp[i-1]行求dp[i]行
        {
            dp[i][j]=dp[i-1][j];
            if(j-i*i*i>=0)
              dp[i][j]+=dp[i][j-i*i*i];
        }
    }
}
int main()
{
    int n;
    Preprocess();
    while(~scanf("%d",&n))
    {
        cout<<dp[21][n]<<endl;
    }
}
```


代码2：

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=10000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
ll dp[26][maxn+10];
void Preprocess()
{
    mset(dp,0);
    dp[0][0]=1;
    for(int i=1; i<=21; ++i)
    {
        for(int j=0; j<=maxn; ++j) //从 i-1  j状态转移
        {
            for(int a=0; j+a*i*i*i<=maxn; ++a)
            {

                dp[i][j+a*i*i*i]+=dp[i-1][j];
            }
        }
    }
}
int main()
{
    int n;
    Preprocess();
    while(~scanf("%d",&n))
    {
        cout<<dp[21][n]<<endl;
    }
}

```




### [E - Matches](https://cn.vjudge.net/problem/UVA-11375)


[UVA - 11375 ](https://cn.vjudge.net/problem/22967/origin)

**题目描述** ：


​ 火柴，用n (1<=n<=2000棍能组成多少个非负整数？火柴不必用完，组成的整数不能有前导零（但蒸整数0是可以的）。比如你有三根火柴，可以组成1或者7；如果有四根，除了可以组成1和7之外，还可以组成4和77。


**分析：**


​ 可以用加法原理，n根火柴组成的种类数，可以分解成只用1，2，3…n根火柴组成的种类数之和。

假设计算dp[i]是只用i根火柴可以组成的种类数。



**有个状态转移的过程，假设c[j]代表数字j需要花费的火柴数目。那么**

​ dp[i+c [ j ] ]=dp[i+ c [ j ] ]+dp[i]

对于dp[k],只能由前一个状态后加一个数字转移过来的（前一个状态都是独立的，没有重复），那么只要保证k之前的都进行上面的状态转移，那么此时的dp[ k ] 就是花费k个火柴可以组成的种类数

需要注意的是，因为没有前导0，所以刚开始从0状态不能经过数字0转移到dp[6],不然会导致后面计算的状态都包含前导0。 最后只要判断如果n>=6 就加上0这个种类即可


**当然写状态转移的时候也需要注意几点 ：**

1.初始状态 //dp[0]设为1，代表从0状态由一种方法到达，所以可以由0状态加数字到其他状态。

2.状态的转移过程//

因为数据量较大，用高精度的方式写

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=2000;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
/*
给你n个火柴棍,最多能组成几个非负数(不含前导零)

*/
struct BigNum{
    int a[2000];//储存 低位到高位   10000进制
    int len;//代表有效长度
    BigNum()
    {
         mset(a,0);
         len=1;
    }
    BigNum(int n)
    {
        mset(a,0);
        len=1;
        a[0]=n%10000;
        n/=10000;
        while(n)
        {
            a[len++]=n%10000;
            n/=10000;
        }
    }
    BigNum operator + (const BigNum &k)
    {
        BigNum  ans;
        ans.len=max(len,k.len);
        for(int i=0;i<ans.len;++i)
        {
            ans.a[i]+=a[i]+k.a[i];
            ans.a[i+1]+=ans.a[i]/10000;
            ans.a[i]%=10000;
        }
        if(ans.a[ans.len]>0)
        {
            ans.len++;
        }
        return ans;
    }
    BigNum(const BigNum &aa)//习惯用构造函数啥的，怕指针乱指
    {
        len=aa.len;
        mset(a,0);
        for(int i=0;i<len;++i)
            a[i]=aa.a[i];
    }
    BigNum operator = (const BigNum &aa)//也是上面的原理，怕指针乱指
    {
        len=aa.len;
        mset(a,0);
        for(int i=0;i<len;++i)
            a[i]=aa.a[i];
        return *this;
    }
    void out()
    {
        /*先输出最高位*/
        /*底位按5个长度输出*/
        printf("%d",a[len-1]);
        for(int i=len-2;i>=0;--i)
        {
            printf("%04d",a[i]);
        }
        printf("\n");
    }
};
int c[]={6,2,5,5,4,5,6,3,7,6};
BigNum dp[maxn+10];//dp[i] 表示*只用*i个柴火棍可以组成多少数组
void Preprocess()//需要用到高精度
{
    dp[0]=BigNum(1);//代表0 ~0有一步 初始状态
    for(int i=0;i<=maxn;++i)
    {
        for(int j=0;j<10;++j)
        {
            //第一个数字不能为0 如果n大于k 自动加上1
            if(!(!i&&!j)&&i+c[j]<=maxn)//i=0是不能走0
            {
                dp[i+c[j]]=dp[i+c[j]]+dp[i];
            }

        }
    }
}
int main()
{
    int n;
    Preprocess();
    while(~scanf("%d",&n))
    {
        BigNum ans;
        for(int i=1;i<=n;++i)
        {
            ans=ans+dp[i];
        }
        if(n>=6)
        {
            ans=ans+BigNum(1);
        }
        ans.out();
    }
}

```




**题目大意：**

```bash
在一个m行n列的矩形网格里放k个相同的石子，问有多少中方法？每个格子最多放一个石子，
所有石子都要用完，并且第一行，最后一行，第一列，最后一列都得有石子.```


 

**输入格式：**

   

```bash
输入第一行为数据组数 T（T<=50）每组数据包含三个整数 m,n,k（2<=m,n<=20 ,k<=500）。```


**输出格式：**

 

```bash
 对于每组数据，输出方案总数除以1 000 007的余数。```


 

**分析：**

如果题目的问题转化为  “**某行某列都没有石子的种类数**”  该多好 ，直接求C(r*c,k)就行了（代表从剩余的r行 c列中选k个位置放石子）

其实一点的都不难办

设全集为S  代表从n行m列中选k个位置的方案数

那么S=**答案+其中有一个或多个**（第一行，最后一行，第一列，最后一列）**没有石子方案数**

P：**其中有一个或多个**（第一行，最后一行，第一列，最后一列）**没有石子方案数**

**A：第一行没有石子的状态**

**B：最后一行没有石子的状态**

**C：第一列没有石子的状态**

**D:  最后一列没有石子的状态**

**P可以运用容斥原理求出**

 

**另外吐槽一点，n^2的复杂度求出 C(n,n)以内的所有组合数的方法也很妙！**

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=500;
const int branch=26;
const int inf=0x3f3f3f3f;
const int MOD=1e6+7;
int C[maxn+100][maxn+100];
void Preprocess()
{
    mset(C,0);
    for(int i=0; i<=maxn; ++i)
    {
        C[i][0]=C[i][i]=1;//边界条件
        for(int j=1; j<i; ++j)
        {
            C[i][j]=(C[i-1][j]+C[i-1][j-1])%MOD;
        }
    }
    //根据排列组合公式来求 C(i,j)
    //可以根据C(i,j)求C(i,j+1)   C(i,j)=(C(i,j+1)*(j+1))/(i-j)         在求二项式系数的时候很有用 求某一行的组合
}
int main()
{
    int n,m,nn,mm,k,num;
    int kase=0;
    Preprocess();
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d %d",&n,&m,&k);
        int ans=0;
        for(int i=0; i<16; ++i)//利用容斥原理求不在 状态A B  C D的个数
        {
            num=0,nn=n,mm=m;
            if(i&1)
            {
                nn--;
                num++;
            }
            if(i&2)
            {
                nn--;
                num++;
            }
            if(i&4)
            {
                mm--;
                num++;
            }
            if(i&8)
            {
                mm--;
                num++;
            }
            if(num&1)
            {
                ans=(ans-C[nn*mm][k]+MOD)%MOD;
            }
            else
            {
                 ans=(ans+C[nn*mm][k])%MOD;
            }
        }
        printf("Case %d: %d\n",++kase,ans);//求的是至少一个地方没有的状态
    }
    return 0;
}```


 

