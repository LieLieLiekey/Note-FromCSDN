

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


 

