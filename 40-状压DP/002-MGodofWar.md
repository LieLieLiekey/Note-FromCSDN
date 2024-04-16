

### M - God of War


At 184~280 A.D ,there were many kingdoms in China. Three strongest among them are “Wei”, “Shu”, “Wu”. People call this period as “Three Kingdoms”. HH is a super “Three Kingdoms” fan, because at this period there were many heroes and exciting stories. Among the heroes HH worships LvBu most. LvBu is the God of War and is also intelligent, but his ambition is too big while enemies are too powerful .Many monarchs wanted to kill him. At 198 A.D ,CaoCao fought with LvBu at Xuzhou.Though Lvbu is the God of War ,CaoCao had so many generals: Xuchu,DianWei XiahouChun……Facing so many heroes ,could LvBu beat all of them? [外链图片转存失败(img-6OdICLXg-1567489110593)(https://vj.e949.cn/4bb2034f502de1d3b2505bd22cd22e5d?v=1547513997)] Given the LvBu’s ATI, DEF, HP, and enemies’ ATI, DEF,HP, experience (if LvBu killed one of his enemies, he can get that experience ,and if his experience got more than or equal to 100*level,he would level-up and become stronger) and the In_ATI,In_DEF,In_HP(indicating when LvBu levels up,his ability will increase this point). Each turn LvBu will choose an enemy to fight. Please help LvBu find a way to beat all of enemies and survive with the max HP. Here’s a fight between LvBu and A: **If LvBu attack A, A will lose Max(1,LvBu’s ATI- A’s DEF) hp;If A survived, he will give LvBu Max(1,A’ATI- LvBu’DEF) injury.If LvBu is still alive, repeat it untill someone is dead(hp <= 0).** LvBu’s initial level is 1 and experience is 0,and he can level up many times.

**Input**

The input contains at most 20 test cases. For each case , the first line contains six intergers ,indicating LvBu’s ATI,DEF,HP and In_ATI,In_DEF,In_HP. The next line gives an interger N(0<N<=20),indicating the number of the enemies . Then N lines followed, every line contains the name(the length of each name is no more than 20),ATI,DEF,HP, experience(1<experience<=100).

**Output**

If LvBu is dead output “Poor LvBu,his period was gone.” Or output the maximum HP left.

**Sample Input**

```bash
100  80  100  5  5  5
2
ZhangFei 95  75  100  100 
XuChu 90  90  100  90

100 75 100 5 5 5
1
GuanYu 95 85 100 100
```


**Sample Output**

```bash
30
Poor LvBu,his period was gone.
```


### 题意：


吕布要单挑n位英雄，每个英雄有四个属性，即攻击力，防御力，生命值，经验值，

吕布刚开始有初始的三个基本属性（攻击力，防御力，生命值），每打死一个英雄就会获得相应的经验值

如果经验值达到100*level就会升级，升级或会增加自身的属性值，问吕布打死n个英雄后最大生命值为多少？

### 分析：


用n个二进制位代表打死对应的英雄，为1代表把此英雄打死了。所以用$dp[state]​$表示此时吕布的状态，这个状态可以从打败过的英雄的状态过来，枚举所有前继状态，因为同一个状态获得的经验值肯定是相同的，即等级相同，,取血量最大的即可。初始化其他状态血量为0，代表打不过。

简单dp，可能中间需要注意升级啥的。

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<set>
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
const int inf=0x7fffffff;
int Ina,Inb,Inhp;// up lever get shuxing
int a,b,hp;//lvbu of init state
struct Peo
{
    int a,b,hp,jy;
} peo[20];
struct Node
{
    int lev,hp,jy;//等级，血量 经验
    Node()
    {

    }
    Node(int l,int h,int j):lev(l),hp(h),jy(j)
    {

    }
};//等级和血量
int Getlev(int jy)//根据经验 算出来应该到第几个等级
{
    return jy/100+1;
}
Node judge(Node aa,Peo bb)//吕布的状态和 一个英雄 b 打完之后吕布的状态
{
    int hackb=max(1,a+(aa.lev-1)*Ina-bb.b);
    int hacka=max(1,bb.a-b-(aa.lev-1)*Inb);
    int tb=bb.hp/hackb+bool(bb.hp%hackb);
    int ta=aa.hp/hacka+bool(aa.hp/hacka);
    if(ta>=tb)//吕布胜利
    {
        int cc=Getlev(aa.jy+bb.jy)-aa.lev;
        return Node(aa.lev+cc,aa.hp-(tb-1)*hacka+cc*Inhp,aa.jy+bb.jy);
    }
    else
    {
        return Node(1,0,0);
    }
}
Node dp[1<<20];//处于该状态的最大血量
int main()
{
    int n;
    while(~scanf("%d %d %d %d %d %d",&a,&b,&hp,&Ina,&Inb,&Inhp))
    {
        scanf("%d",&n);
        for(int i=0; i<n; ++i)
        {
            scanf("%*s%d%d%d%d",&peo[i].a,&peo[i].b,&peo[i].hp,&peo[i].jy);
        }
        dp[0]=Node(1,hp,0);//初始状态
        int top=1<<n;
        for(int i=1; i<top; ++i)
        {
            dp[i].hp=0;
            for(int j=0; j<n; ++j)
            {
                if((1<<j)&i)//i的第j位为1 从上一个状态过来
                {
                    int lasts=i^(1<<j);
                    if(dp[lasts].hp>0)//上一个状态没死
                    {
                        Node mm=judge(dp[lasts],peo[j]);
                        if(mm.hp>dp[i].hp)
                            dp[i]=mm;
                    }
                }
            }
        }
        if(dp[top-1].hp==0)
            cout<<"Poor LvBu,his period was gone."<<endl;
        else
            cout<<dp[top-1].hp<<endl;
    }
    return 0;
}

```


#### 


