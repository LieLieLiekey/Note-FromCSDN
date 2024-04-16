

## 1245F. Daniel and Spring Cleaning(数位DP)


##### 题目链接：[传送门](https://codeforces.com/problemset/problem/1245/F)


##### 题意：


给出$l,r​$，让求满足$a\in[l,r],b\in[l,r]​$ 且$a⊕b=a+b​$ 的$(a,b)​$对数。

##### 思路：


如果$a⊕b=a+b$ 那么有$a\&b=0$，我们用$f(l,r)$代表满足$a\in[0,l],b\in[0,r]$且满足$a\&b=0$的个数，那么题目等效于求$f(r,r)-f(l-1,r)-f(r,l-1)+f(l-1,l-1)$的值。


这种问题我就没往数位DP上想过。但是用数位DP处理起来真的是太巧妙了。

相似的题目链接：[牛客2019多校pair](https://ac.nowcoder.com/acm/contest/887/H)


因为位运算只与对应的位有关，前后的位无关系，所以我们可以用数位DP来解决这个问题。

为了求$f(l,r)$，我们先让$l,r$进行二进制分解，假设最低位是第1位，最高位为31位（因为 $l,r$ 是在int的数据范围内）。

我们用$dp[k][limt1][limt2]$ 来代表当前满足处理到 $k$ 位，此时 $l$ 和 $r$ 是否是顶位的满足条件的个数。处理到第k位时，前面的必定满足对应的位数**且运算**的值为0。然后我们枚举当前状态下两个数的第k位的所有情况dp即可。

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
ll dp[50][2][2];//dp[k][limt][limt] a&b=0
int ar[50],br[50];//[31...1]  top->down
ll dfs(int k,int limt1,int limt2)
{
    if(k==0)
        return 1;
    if(dp[k][limt1][limt2]!=-1) return dp[k][limt1][limt2];
    int up1=limt1?ar[k]:1;
    int up2=limt2?br[k]:1;
    ll ans=0;
    for(int i=0;i<=up1;++i)
    {
        for(int j=0;j<=up2;++j)
        {
            if((i&j)!=0) continue;
            ans+=dfs(k-1,limt1&&i==up1,limt2&&j==up2);
        }
    }
    return dp[k][limt1][limt2]=ans;
}
ll solve(ll a,ll b)
{
    if(a<0||b<0) return 0;
    mset(dp,-1);
    for(int i=1;i<=31;++i)
    {
        ar[i]=a&1;
        a>>=1;
        br[i]=b&1;
        b>>=1;
    }
    return dfs(31,1,1);
}
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        ll a,b;
        cin>>a>>b;
        cout<<solve(b,b)-2*solve(a-1,b)+solve(a-1,a-1)<<endl;
    }
    return 0;
}
```




### J - 吉哥系列故事――恨7不成妻


单身! 　　依然单身！ 　　吉哥依然单身！ 　　DS级码农吉哥依然单身！ 　　所以，他生平最恨情人节，不管是214还是77，他都讨厌！ 　　 　　吉哥观察了214和77这两个数，发现： 　　2+1+4=7 　　7+7=7*2 　　77=7*11 　　最终，他发现原来这一切归根到底都是因为和7有关！所以，他现在甚至讨厌一切和7有关的数！

什么样的数和7有关呢？

如果一个整数符合下面3个条件之一，那么我们就说这个整数和7有关—— 　　1、整数中某一位是7； 　　2、整数的每一位加起来的和是7的整数倍； 　　3、这个整数是7的整数倍；

现在问题来了：吉哥想知道在一定区间内和7无关的数字的平方和。

**Input**

输入数据的第一行是case数T(1 <= T <= 50)，然后接下来的T行表示T个case;每个case在一行内包含两个正整数L, R(1 <= L <= R <= 10^18)。

**Output**

请计算[L,R]中和7无关的数字的平方和，并将结果对10^9 + 7 求模后输出。

**Sample Input**


3 1 9 10 11 17 17


**Sample Output**


236 221 0


##### 参考博客：[http://www.cnblogs.com/kuangbin/archive/2013/05/01/3053233.html](http://www.cnblogs.com/kuangbin/archive/2013/05/01/3053233.html)


##### 分析 ：


当然，看完博客还是懵逼，因为我一开始的思路是错的。

首先这道题的状态是很好想的

$dp[pos][Pre\_sum][Pre\_Product\%7]$ 代表未知的pos位的前缀十进制位之和取余7为Pre_sum,前缀的值取余7为Pre_Product。

举个例子：54****对应的状态是$dp[4][9\%7][54\%7]$

**这个地方是我错的原因，不想看的可以跳过。**


然后就开始数位dp加递归求解了吗？，合并一下就像这样？

```cpp
ans+=dfs(pos-1,(PreSum+i)%7,PreProduct*10+i,istop&&i==endd);//这个合并的方法是错的

```


我们求的答案是满足条件的**数的平方和**，所以在进行状态合并的时时候相同状态对应的前缀可能是不同的，所以他们呢的平方和也是不同的，不能直接加上次计算结果。

就像23**与72**，对应的状态是一样的（先不考虑数位上存在7的条件），但是前者计算过了，在计算后者不能直接加前者计算的值。

**所以我们应该寻求一个新的解法!**


想一想，如果我们知道该状态下后pos位满足条件的数都是什么，我们应该怎么计算呢？

**假如说第pos位是i，后pos-1位满足条件的数都已经知道有n个，对应的数字分别为m1,m2,m3… mn**

**那么后pos位中满足条件的平方和我们可以计算出来**(这里的平方和中的数不包括前缀)。

设k位第pos位对应的权值$k=pow(10,pos-1)$

$(i*k+m_j)^2==(i*k)^2+m_j^2+2*i*k*m_j$

**枚举这n个数在第pos为i的情况下，在该状态下后pos位满足条件的数的平方和为**

$Product=n*(i*k)^2+\sum_{j=1} ^nm_j^2+2*i*k*\sum_{j==1}^nm_j$

**枚举第pos位就得到后pos位满足条件的数的平方和**，在上面的公式中用到了n（改状态下满足条件的数的个数），sum(该状态下满足条件的数的和)，Preduct（改状态下满足条件的数的平方和）。

在合并的时候需要把这三个值全都统计一下，以便递归求解，最后的答案在Preduct里面。

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x3f;
const ll MOD=1e9+7;
struct node{//(针对于后pos位未知位数的)
ll cnt;//满足条件的个数
ll sum;//满足条件的数的和
ll Product;//Product为满足条件的数的平方和
node(){
cnt=-1;
sum=Product=0ll;
}
node(ll a,ll b,ll c){
cnt=a,sum=b,Product=c;}
};
node dp[25][10][10];//dp[pos][Pre_sum][Pre_Product%7];
int num[25];
ll quick_pow(ll a,ll b)
{
    ll ans=1;
    while(b)
    {
        if(b&1)
            ans=(ans*a)%MOD;
        a=(a*a)%MOD;
        b>>=1;
    }
    return ans;
}
node dfs(int pos,int PreSum,int PreProduct,bool istop)
{
    if(!pos)
    {
        if(PreSum%7!=0&&PreProduct%7!=0)
            return node(1,0,0);
        else
            return node(0,0,0);
    }
    if(!istop&&dp[pos][PreSum%7][PreProduct%7].cnt!=-1)
        return dp[pos][PreSum%7][PreProduct%7];
    int endd=istop?num[pos]:9;
    node ans(0,0,0);
    ll powval=quick_pow(10ll,pos-1);
    for(int i=0;i<=endd;++i)
    {
        if(i==7)
            continue;
        //针对于每个位
        node mid=dfs(pos-1,(PreSum+i)%7,(PreProduct*10+i)%7,istop&&i==endd);
        ll k=i*powval%MOD;
        ans.cnt+=mid.cnt;
        ans.sum+=(mid.sum+(mid.cnt*k)%MOD)%MOD;
        ans.Product+=(mid.Product+(2*k*mid.sum)%MOD+((mid.cnt*k)%MOD)*(k%MOD))%MOD;
        ans.cnt%=MOD;
        ans.sum%=MOD;
        ans.Product%=MOD;
    }
    if(!istop)
        dp[pos][PreSum%7][PreProduct%7]=ans;
    return ans;
}
ll calc(ll val)
{
    int pos=0;
    do{
        num[++pos]=val%10;
        val/=10;
    }
    while(val);
    return dfs(pos,0,0,1).Product;
}
int main()
{
    int t;
    ll a,b;
    mset(dp,-1);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%I64d%I64d",&a,&b);
        printf("%I64d\n",(((calc(b)-calc(a-1))%MOD)+MOD)%MOD);
    }
    return 0;
}
```




### B - XHXJ’s LIS


define xhxj (Xin Hang senior sister(学姐)) If you do not know xhxj, then carefully reading the entire description is very important. As the strongest fighting force in UESTC, xhxj grew up in Jintang, a border town of Chengdu. Like many god cattles, xhxj has a legendary life: 2010.04, had not yet begun to learn the algorithm, xhxj won the second prize in the university contest. And in this fall, xhxj got one gold medal and one silver medal of regional contest. In the next year’s summer, xhxj was invited to Beijing to attend the astar onsite. A few months later, xhxj got two gold medals and was also qualified for world’s final. However, xhxj was defeated by zhymaoiing in the competition that determined who would go to the world’s final(there is only one team for every university to send to the world’s final) .Now, xhxj is much more stronger than ever，and she will go to the dreaming country to compete in TCO final. As you see, xhxj always keeps a short hair(reasons unknown), so she looks like a boy( I will not tell you she is actually a lovely girl), wearing yellow T-shirt. When she is not talking, her round face feels very lovely, attracting others to touch her face gently。Unlike God Luo’s, another UESTC god cattle who has cool and noble charm, xhxj is quite approachable, lively, clever. On the other hand,xhxj is very sensitive to the beautiful properties, “this problem has a very good properties”，she always said that after ACing a very hard problem. She often helps in finding solutions, even though she is not good at the problems of that type. Xhxj loves many games such as，Dota, ocg, mahjong, Starcraft 2, Diablo 3.etc，if you can beat her in any game above, you will get her admire and become a god cattle. She is very concerned with her younger schoolfellows, if she saw someone on a DOTA platform, she would say: “Why do not you go to improve your programming skill”. When she receives sincere compliments from others, she would say modestly: "Please don’t flatter at me.(Please don’t black)."As she will graduate after no more than one year, xhxj also wants to fall in love. However, the man in her dreams has not yet appeared, so she now prefers girls. Another hobby of xhxj is yy(speculation) some magical problems to discover the special properties. For example, when she see a number, she would think whether the digits of a number are strictly increasing. If you consider the number as a string and can get a longest strictly increasing subsequence the length of which is equal to k, the power of this number is k… It is very simple to determine a single number’s power, but is it also easy to solve this problem with the numbers within an interval? xhxj has a little tired，she want a god cattle to help her solve this problem,the problem is: Determine how many numbers have the power value k in [L，R] in O(1)time. For the first one to solve this problem，xhxj will upgrade 20 favorability rate。

**Input**

First a integer T(T<=10000),then T lines follow, every line has three positive integer L,R,K.( 0<L<=R<2 63-1 and 1<=K<=10).

**Output**

For each query, print “Case #t: ans” in a line, in which t is the number of the test case starting from 1 and ans is the answer.

**Sample Input**


1 123 321 2


**Sample Output**


Case #1: 139


这题比较有意思，在把前面的状态压缩时用了一个非常巧妙的办法。

##### 参考博客：[https://www.cnblogs.com/dilthey/p/8525413.html](https://www.cnblogs.com/dilthey/p/8525413.html)


##### 题意：


在区间【a,b】找有多少个数满足下列。条件：这个数的十进制位的最长递增长度等于K.

##### 分析：


数位dp的时候把前缀的数的状态记录下即可，但是该怎么记录呢？

在nlogn的最长递增子序列的求法中每一个序列都确定一个数组d,d[top]就是长度为top的子序列的最大值是多少，

这里面top的范围是1~10,所有出现的最大值的范围是0~9,所以这里可以采用一个十个2进制位的形式进行压缩。肯定有点迷吧，让我慢慢解释…

对于一个上面的数组d[top]，其里面的值随着下标的增大是逐渐递增的，所以如果咱们知道数组d中的所有值，那么这个数组d就确定了，换句话就是说前缀的数的状态确定了。

这里咱们采用十个2进制位进行压缩，如果num位为1，就代表这个num数字在数组d中出现过，这样就用一个二进制数来表示前缀的数的状态了。

举个栗子：


我们化用一下这个数组d，用0~9十个位的0 or 1来表示，这个d数组里存了啥，比如说假设d[1]=1，d[2]=3，d[3]=5，d[4]=6，那么在本题下的形式就是sta = 0001101010


十个2进制位1有多少个 ，就代表这个状态最长递增子序列的长度为几。

**初始情况 ：**

​ sta



### G - B-number


A wqb-number, or B-number for short, is a non-negative integer whose decimal form contains the sub- string “13” and can be divided by 13. For example, 130 and 2613 are wqb-numbers, but 143 and 2639 are not. Your task is to calculate how many wqb-numbers from 1 to n for a given integer n.

**Input**

Process till EOF. In each line, there is one positive integer n(1 <= n <= 1000000000).

**Output**

Print each answer in a single line.

**Sample Input**


13 100 200 1000


**Sample Output**


1 1 2 2


**分析 ：**

做了这么长时间的数位dp，这题套路太老了！

So，怎么做呢，任何一个数位dp只要只要pre****的求法，找出其中的状态，题目自然就迎刃而解了！

这题求pre****，主要注意三个东西

+ pre的值是多少(为了取余13用)+ pre最后一位是否为1+ pre中是否含有串13


所以着要题的状态就这三个，当然还得再加上一个pos，表用来求的位数是几位

试试能不能写出dp方程？



$$dp[pos][PreSum][Is1][Have13]=\sum _{i==0}^{9}dp[pos-1][(PreSum*10+i)\%Mod][i==1][Have13||(Is1\&amp;\&amp;i==3)])$$



代码：

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x3f;
const int MOD=13;
int dp[15][14][2][2];//dp[pos][PreSum%mod][is_1][have_13]
int num[20];
int dfs(int pos,int PreSum,bool Is1,bool Have13,bool Istop)//前缀是否为1，是否是含有13
{
    if(!pos)
        return ((PreSum%MOD==0)&&Have13);
    if(!Istop&&dp[pos][PreSum][Is1][Have13]!=-1)
        return dp[pos][PreSum][Is1][Have13];
    int endd=Istop?num[pos]:9;
    int res=0;
    for(int i=0;i<=endd;++i)
    {
        res+=dfs(pos-1,(PreSum*10+i)%MOD,i==1,Have13||(Is1&&i==3),Istop&&i==endd);
    }
    if(!Istop)
        dp[pos][PreSum][Is1][Have13]=res;
    return res;
}
int calc(int val)
{
    int pos=0;
    do{
     num[++pos]=val%10;
     val/=10;
    }
    while(val);
    return dfs(pos,0,0,0,1);
}
int main()
{
    int a;
    mset(dp,-1);
    while(~scanf("%d",&a))
    {
        printf("%d\n",calc(a));
    }
    return 0;
}

```




### F - Balanced Number


A balanced number is a non-negative integer that can be balanced if a pivot is placed at some digit. More specifically, imagine each digit as a box with weight indicated by the digit. When a pivot is placed at some digit of the number, the distance from a digit to the pivot is the offset between it and the pivot. Then the torques of left part and right part can be calculated. It is balanced if they are the same. A balanced number must be balanced with the pivot at some of its digits. For example, 4139 is a balanced number with pivot fixed at 3. The torqueses are 4*2 + 1*1 = 9 and 9*1 = 9, for left part and right part, respectively. It’s your job to calculate the number of balanced numbers in a given range [x, y].

**Input**

The input contains multiple test cases. The first line is the total number of cases T (0 < T ≤ 30). For each case, there are two integers separated by a space in a line, x and y. (0 ≤ x ≤ y ≤ 10 18).

**Output**

For each case, print the number of balanced numbers in the range [x, y] in a line.

**Sample Input**

```bash
2
0 9
7604 24324
```


**Sample Output**

```bash
10
897
```


**题意 ：**

求a~b之间有多少平衡数字，所谓平衡数就是可以从其十进制位中找到一个支点，使得力矩为0。例如4139 ，找支点3，满足4*2 + 1*1 ==9*1 =9。故4139就是平衡数。

**分析：**

对于非0数字，若存在支点，那么他的支点只有一个。

所以，枚举所有支点，知道在每个支点下的平衡数，加起来减去多计算的0就是答案。

**对于每个支点0 ：**

我们还是按照传统的方法dp数位，

设$dp[pos][o][k]$ pos为待定的位，o为支点，k为在该支点下前缀的力矩是k。满足条件的数有$dp[pos][o][k]$ 个.

**那么在支点o下dp方程为：**

$dp[pos][o][k]=\sum _{i==0} ^9dp[pos-1][o][k+(pos-o)*i]$

在这个过程中，如果k<0就肯定没有满足条件的数，直接返回0（在支点左边肯定为0，在支点右边如果为负，就肯定不满足）

**代码：**

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x3f;
ll dp[20][20][1500];
int num[20];
ll dfs(int pos,int o,int pre,bool istop)
{
    /*
    1.jianzhi  pre<0 return 0;
    2.记忆话
    */
    if(!pos)
        return pre==0;
    if(pre<0)
        return 0;
    if(!istop&&dp[pos][o][pre]!=-1)
        return dp[pos][o][pre];
    int endd=istop?num[pos]:9;
    ll ans=0;
    for(int i=0;i<=endd;++i)
    {
        ans+=dfs(pos-1,o,pre+(pos-o)*i,istop&&i==endd);
    }
    if(!istop)
        dp[pos][o][pre]=ans;
    return ans;
}
ll calc(ll val)
{
    if(val==-1)
        return 0;
    int pos=0;
    do{
        num[++pos]=val%10;
        val/=10;
    }
    while(val);
    ll ans=0;
    for(int i=1;i<=pos;++i)
    {
        ans+=dfs(pos,i,0,1);
    }
    return ans+1-pos;//数字0支点多加了pos-1个
}
int main()
{
    ll a,b;
    int t;
    scanf("%d",&t);
    mset(dp,-1);
    while(t--)
    {
        scanf("%lld %lld",&a,&b);
        printf("%lld\n",calc(b)-calc(a-1));
    }
    return 0;
}

```




### E - Round Numbers


The cows, as you know, have no fingers or thumbs and thus are unable to play Scissors, Paper, Stone’ (also known as ‘Rock, Paper, Scissors’, ‘Ro, Sham, Bo’, and a host of other names) in order to make arbitrary decisions such as who gets to be milked first. They can’t even flip a coin because it’s so hard to toss using hooves.

They have thus resorted to “round number” matching. The first cow picks an integer less than two billion. The second cow does the same. If the numbers are both “round numbers”, the first cow wins, otherwise the second cow wins.

A positive integer *N* is said to be a “round number” if the binary representation of *N* has as many or more zeroes than it has ones. For example, the integer 9, when written in binary form, is 1001. 1001 has two zeroes and two ones; thus, 9 is a round number. The integer 26 is 11010 in binary; since it has two zeroes and three ones, it is not a round number.

Obviously, it takes cows a while to convert numbers to binary, so the winner takes a while to determine. Bessie wants to cheat and thinks she can do that if she knows how many “round numbers” are in a given range.

Help her by writing a program that tells how many round numbers appear in the inclusive range given by the input (1 ≤ *Start* < *Finish* ≤ 2,000,000,000).

**Input**

Line 1: Two space-separated integers, respectively *Start* and *Finish*.

**Output**

Line 1: A single integer that is the count of round numbers in the inclusive range*Start*… *Finish*

**Sample Input**


2 12


**Sample Output**


6


**分析 ：**

有组合数学和数位dp两种方法，组合数学比较简单，这里只说数位dp。

dp能解决大部分区间计数问题，用枚举位数和动规来解决问题 dp[0][pos][k]代表000****中满足0-1>=k的种类数 dp[1][pos][k]代表 (1)****中满足0-1>=k的种类数前缀是1 **所以状态三个：** 1.前缀是否全为0 2.随便的有几位 3.这几位满足0-1>=k的个数

+ 当前缀有1时候，枚举第pos位是0是1即可。




$$dp[1][pos][k]=dp[1][pos-1][k-1]+dp[1][pos][k+1]$$



+ 当前缀前全位0时，枚举第pos位0，1即可


$dp[0][pos][k]=dp[0][pos-1][k]+dp[1][pos-1][k+1]$

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x3f;
const int MOD=2520;
int dp[2][40][70];//dp[0/1]第一维意思：满足后pos位数中0-1>=k的个数中，pos位之前是否全为0。      最高31位
int num[40];
int GetDp(int flag,int pos,int k)//-31<=k<=31
{
    return dp[flag][pos][k+31];
}
void  enDp(int flag,int pos,int k,int val)
{
    dp[flag][pos][k+31]=val;
}
int dfs(int pos,int flag,int k,bool Istop)
{
    if(!pos)
        return k<=0;
    if(!Istop&&GetDp(flag,pos,k)!=-1)
        return GetDp(flag,pos,k);
    int endd=Istop?num[pos]:1;
    int res=0;
    for(int i=0;i<=endd;++i)
    {
        if(i==1)
            res+=dfs(pos-1,1,k+1,Istop&&i==endd);
        else
        {
            if(flag==0)
                    res+=dfs(pos-1,0,0,Istop&&i==endd);
            else
                res+=dfs(pos-1,1,k-1,Istop&&i==endd);
        }
    }
    if(!Istop)
        enDp(flag,pos,k,res);
    return res;
}
int calc(int val)//如果前导全为0，就是0 否则为1
{
    int pos=0;
    do{
        num[++pos]=val%2;
        val/=2;
    }
    while(val);
    return dfs(pos,0,0,1);
}
int main()
{
    mset(dp,-1);
    int a,b;
    while(~scanf("%d %d",&a,&b))
    {
        printf("%d\n",calc(b)-calc(a-1));
    }
    return 0;
}
```




### C - 不要62


杭州人称那些傻乎乎粘嗒嗒的人为62（音：laoer）。 杭州交通管理局经常会扩充一些的士车牌照，新近出来一个好消息，以后上牌照，不再含有不吉利的数字了，这样一来，就可以消除个别的士司机和乘客的心理障碍，更安全地服务大众。 不吉利的数字为所有含有4或62的号码。例如： 62315 73418 88914 都属于不吉利号码。但是，61152虽然含有6和2，但不是62连号，所以不属于不吉利数字之列。 你的任务是，对于每次给出的一个牌照区间号，推断出交管局今次又要实际上给多少辆新的士车上牌照了。

**Input**

输入的都是整数对n、m（0<n≤m<1000000），如果遇到都是0的整数对，则输入结束。

**Output**

对于每个整数对，输出一个不含有不吉利数字的统计个数，该数值占一行位置。

**Sample Input**

```bash
1 100
0 0
```


**Sample Output**

```bash
80
```


这是我第一个数位dp入门题，首先用自己动归的代码打出来了，虽然谁说代码贼丑，但是还是完美地解决这个问题，而且时间复杂度可观，接下来看别人的这道题的代码，可以说dfs深搜加记忆化的代码是真的简洁(当然还是动归的思想)

这是我学完之后的代码

```cpp
#include<cstdio>
#include<algorithm>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x3f;
const int MOD=1e5+7;
int n,m;
ll dp[20][2];//dp[k][0/1]k位，前位有无限制6的符合条件的种类数
int num[20];
ll dfs(int pos,bool limit,bool istop)//前面是否限制位6，是否到顶端
{
    /*如果没有到顶端即前一位没有到最大num[pos+1],那么这个过程就相当在求dp[pos][limit]
      否则就会枚举0~num[pos]，dp求所有值，
      注释：limit=1则表示前一位为6，istop=1表示前一位已经到顶端
    */
    if(!pos)
        return 1;
    if(!istop&&dp[pos][limit]!=-1)
        return dp[pos][limit];
    ll res=0ll;
    int rmax=istop?num[pos]:9;
    for(int i=0;i<=rmax;++i)
    {
        if(i==4||(limit&&i==2))
            continue;
        res+=dfs(pos-1,i==6,istop&&i==rmax);
    }
    if(!istop)
        dp[pos][limit]=res;
    return res;
}
ll solve(ll val)
{
    if(val==0)
        return 1;
    int pos=0;
    while(val)//分解数位，位置从1~pos
    {
        num[++pos]=val%10;
        val/=10;
    }
    return dfs(pos,0,1);
}
int main()
{
    mset(dp,-1);
    ll a,b;
    while(~scanf("%lld %lld",&a,&b))
    {
        if(a==0&&b==0)
            break;
        printf("%lld\n",solve(b)-solve(a-1));
    }
    return 0;
}
```




### A - Beautiful numbers


Volodya is an odd boy and his taste is strange as well. It seems to him that a positive integer number is beautiful if and only if it is divisible by each of its nonzero digits. We will not argue with this and just count the quantity of beautiful numbers in given ranges.

**Input**

The first line of the input contains the number of cases t (1 ≤ t ≤ 10). Each of the next *t* lines contains two natural numbers li and ri (1 ≤ \li≤ ri≤ 9 ·1018).

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d).

**Output**

Output should contain t numbers — answers to the queries, one number per line — quantities of beautiful numbers in given intervals (from li to ri, inclusively).

Examples

**Input**

```bash
1
1 9
```


**Output**

```bash
9
```


**Input**

```bash
1
12 15
```


**Output**

```bash
2
```


**分析：**

刚学dp，这dp搞我一天了，不过还真有意思的，里面又悟出来一点东西，dp方程要敢想

**状态：**

$dp[pos][PreSum][PreLcm]$ 是值pre*****(pos个*号，*号代表这个数随便取。这个数的前缀是pre),这个dp代表前缀为PreSum且前缀的lcm为PreLcm后pos个数满足条件的个数是多少。

举个例子：520***就是PreSum为520，PreLcm为10，其对应的dp方程为$dp[3][520][10]$

**故dp方程为：**

$dp[pos+1][PreSum][PreLcm]=\sum_{i==0}^{9}dp[pos][PreSum*10+i][LCM(PreLcm,i)]$

当pos==0时候（递归边界）

若满足PreSum%PreLcm==0就返回1，否则返回0

**这个需要注意两个点：**

+ 第三个参数最大为2520，但是真正能取的都是2520的因数（2520从哪来的呢，2520是LCM(1,2,3…9)），也就那48个，所以可以将第三个参数映射一下（相当于离散化），减少空间+ 第二个参数会很大吧，但是第三个参数是来干什么的？不是最后的时候取余第三个参数的吗！，又因为2520是所有可能第三个参数的倍数，故$PreSum\%PreLcm==0$等效于$PreSum\%2520\%PreLcm==0$(当然取余后的值可不相等)，所以可以让第二个参数取余2520，控制范围，减少空间


详情看代码

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<vector>
#include<cstring>
#include<string>
#include<iostream>
#include<iomanip>
#define mset(a,b)   memset(a,b,sizeof(a))
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
const int maxn=1e5+10;
const int branch=26;
const int inf=0x3f;
const int MOD=2520;
ll dp[30][MOD+10][50];
int index[MOD+10];
int num[30];
void init()
{
    mset(dp,-1);
    int tot=0;
    /*将MOD仅有的因子离散化 每个值对应于一个下标*/
    for(int i=1;i<=MOD;++i)
        if(MOD%i==0)
            index[i]=++tot;
}
int Gcd(int a,int b)
{
    int temp;
    while(a%b)
    {
        temp=a%b;
        a=b;
        b=temp;
    }
    return b;
}
int Lcm(int a,int b)
{
    return a/Gcd(a,b)*b;
}
ll dfs(int pos,int pre_sum,int pre_lcm,bool is_top);
ll calc(ll val)
{
    int pos=0;
    do{
        num[++pos]=val%10;
        val/=10;
    }
    while(val);//位数从下标1开始存
    return dfs(pos,0,1,true);
}
ll dfs(int pos,int pre_sum,int pre_lcm,bool is_top)
{
    if(!pos)
        return pre_sum%pre_lcm==0;
    if(!is_top&&dp[pos][pre_sum][index[pre_lcm]]!=-1)
        return dp[pos][pre_sum][index[pre_lcm]];
    int endd=is_top?num[pos]:9;
    ll res=0ll;
    for(int i=0;i<=endd;++i)
    {
        int lcm,sum;
        lcm=pre_lcm;
        if(i)
            lcm=Lcm(lcm,i);
        sum=(pre_sum*10+i)%MOD;
        res+=dfs(pos-1,sum,lcm,is_top&&i==endd);
    }
    if(!is_top)
        dp[pos][pre_sum][index[pre_lcm]]=res;
    return res;
}
int main()
{
    int t;
    ll a,b;
    init();
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld %lld",&a,&b);
        printf("%lld\n",calc(b)-calc(a-1));
    }
    return 0;
}
```


