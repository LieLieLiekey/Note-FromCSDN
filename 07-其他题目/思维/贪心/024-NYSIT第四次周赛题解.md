

## NYIST–2018大一新生第四次周赛


链接：[https://cn.vjudge.net/contest/269128](https://cn.vjudge.net/contest/269128) 密码：nyist

### [A - 穆穆清风至](https://cn.vjudge.net/problem/HDU-2550) [HDU - 2550 ](https://cn.vjudge.net/problem/21474/origin)


画图，模拟一下即可

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
struct Node{
int len,num;
}node[110];
void Print(int len)//输出一行长度为len 的弓箭
{
    printf(">+");
    for(int i=0;i<len-2;++i)
        printf("-");
    printf("+>\n");
}
bool cmp(Node a,Node b)//将短的放前面
{
    return a.len<b.len;
}
int main()
{
    int t,n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;++i)
            scanf("%d %d",&node[i].len,&node[i].num);
        sort(node,node+n,cmp);
        for(int i=0;i<n;++i)
        {
            for(int j=0;j<node[i].num;++j)//每一种箭 输出num个
                Print(node[i].len);
            printf("\n");
        }
    }
    return 0;
}


```


### [B - 无法提交](https://cn.vjudge.net/problem/CodeForces-702A) [CodeForces - 702A ](https://cn.vjudge.net/problem/439225/origin)


```bash
求最大连续严格递增长度
```


思路：记录当前严格递增长度和上一个数，每输入一个数判断是否与前面那个数构成严格递增关系，更新变量即可。

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 110
using namespace std;
int main()
{
    int maxlen,n,val,lastval;
    while(~scanf("%d",&n))
    {
        lastval=-1;//上一个数
        maxlen=-1;//最长的连续递增长度
        int cnt=0;//现在当前有多少个连续的严格递增数
        /*
        每次在输入数时变量代表的意义
        val:现在输入的数
        lastval:上一个数(初始值为-1)
        cnt:现在当前有多少个连续的严格递增数
        maxlen:最大的cnt
        */
        while(n--)
        {
            scanf("%d",&val);
            if(val>lastval)//还保持严格递增
                cnt++;
            else//不能保持严格递增  
            {
                if(maxlen<cnt)//更新
                    maxlen=cnt;
                cnt=1;
            }
            lastval=val;
        }
        if(maxlen<cnt)
            maxlen=cnt;
        printf("%d\n",maxlen);
    }
}

```


### [C - 吹我罗衣裾](https://cn.vjudge.net/problem/HDU-2003) [HDU - 2003 ](https://cn.vjudge.net/problem/17551/origin)


题目都说了用double ，float的精度较低

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 1100
using namespace std;
int main()
{
    double k;
    while(~scanf("%lf",&k))
    {
        if(k<0.0)
            k=-1.0*k;
        printf("%.2lf\n",k);
    }
}

```


### [D - 青袍似春草](https://cn.vjudge.net/problem/HDU-1420) [HDU - 1420](https://cn.vjudge.net/problem/17360/origin)


快速幂模板，注意A,B,C<=1000000，A*A的过程可能会爆int(1e9)，所以用需要用long long

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 1100
using namespace std;
typedef long long ll;
ll quick_pow(ll a,ll b,ll mod)//快速幂板子，可以记下来
{
    ll ans=1;
    while(b)
    {
        if(b&1)
            ans=(ans*a)%mod;
        a=(a*a)%mod;
        b>>=1;
    }
    return ans;
}
int main()
{
    ll a,b,mod,ans;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld %lld %lld",&a,&b,&mod);
        printf("%lld\n",quick_pow(a,b,mod));
    }
}
```


### [E - 无法提交](https://cn.vjudge.net/problem/CodeForces-977A) [CodeForces - 977A](https://cn.vjudge.net/problem/1550001/origin)


k的值较小，模拟一下过程即可

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 110
using namespace std;
int main()
{
    int n,k;
    scanf("%d %d",&n,&k);
    while(k)
    {
        if(n%10)
            n--;
        else
            n/=10;
        --k;
    }
    printf("%d\n",n);
}
```


### [F - 无法提交](https://cn.vjudge.net/problem/CodeForces-510A) [CodeForces - 510A ](https://cn.vjudge.net/problem/111960/origin)


简单画图题，模拟过程即可

```
/*
输出第k行:
k为奇数：       输出m个'#' (#####)
k为4的倍数：    输出一个'#'   m-1个'.'     (#..)
k是2的倍数但是不是4的倍数：输出 m-1个'.' 一个'#' (..#)
输出n行即可
*/
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 110
using namespace std;
int main()
{
    int n,m;
    scanf("%d %d",&n,&m);
    for(int i=1; i<=n; ++i)
    {
        if(i&1)//i为奇数
            for(int j=1; j<=m; ++j)
                printf("#");
        else
        {
            if(i%4==0)//i是4的倍数 输出#..
            {
                printf("#");
                for(int j=1; j<=m-1; ++j)
                    printf(".");
            }
            else
            {
                for(int j=1; j<=m-1; ++j)
                    printf(".");
                printf("#");
            }
        }
        printf("\n");
    }
}

```


### [G - 无法提交](https://cn.vjudge.net/problem/CodeForces-501A) [CodeForces - 501A ](https://cn.vjudge.net/problem/102946/origin)


我相信你读完这道题就能A

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 110
using namespace std;
int main()
{
    int a,b,c,d;
    int score1,score2;
    while(~scanf("%d %d %d %d",&a,&b,&c,&d))
    {
        score1=max(3*a/10,a-(a/250)*c);
        score2=max(3*b/10,b-(b/250)*d);
        if(score1==score2)
            printf("Tie\n");
        else
            printf("%s\n",score1>score2?"Misha":"Vasya");
    }
}

```


### [H - 安得抱柱信](https://cn.vjudge.net/problem/HihoCoder-1768) [HihoCoder - 1768 ](https://cn.vjudge.net/problem/1660336/origin)


​ 找规律题吧，我做这道题暴力了一遍，发现在5位数以内满足条件的只有2,3,5,7,23,37,53,73,373这9个数，所以就猜应该只有这9个数。因为一个5位数可以看作左边是一个1位数，右边是一个4位数，因为四位数中没有“真素数”所以五位数一定不会是一个“真素数”（因为“真素数“满足其左边和右边都是”真素数“）。然后扩展一下，得到超过5位数的数的都不会是“真素数”，所以”真素数“就只有这9个数了

AC代码：

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 1100000
using namespace std;
typedef long long ll;
int ans[]={2,3,5,7,23,37,53,73,373};
int main()
{
    int n;
    while(~scanf("%d",&n))
    {
        if(n<=9)
            printf("%d\n",ans[n-1]);
        else
            printf("-1\n");
    }

}

```


暴力过程的代码：

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 1100000
using namespace std;
typedef long long ll;
int prime[maxn];
int Solve(int k)//判断k是不是真正的素数
{
    int wis[10];
    int len=0;
    while(k)
    {
        wis[len++]=k%10;
        k/=10;
    }//注意数组中的数存的顺序是从低位到高位的
    for(int i=len-1;i>=0;--i)
    {
        for(int j=i;j>=0;--j)//取i  j之间的数字（包括i j下标）
        {
            int val=0;
            for(int k=i;k>=j;--k)//求 i  j之间的数字为多少
            {
                val*=10;
                val+=wis[k];
            }
            if(prime[val])
                return 0;
        }
    }
    return 1;
}
int main()
{
    prime[0]=prime[1]=1;//非素数用 1表示
    for(int i=2;i<=1000;++i)
    {
        if(!prime[i])
        {
            for(int j=i*i;j<=1000000;j+=i)
                prime[j]=1;
        }
    }
    for(int i=1;i<=1000000;++i)
    {
        if(Solve(i))
            printf("%d\n",i);
    }
}
```


### [I - 皎日以为期](https://cn.vjudge.net/problem/HihoCoder-1051) [HihoCoder - 1051 ](https://cn.vjudge.net/problem/505378/origin)


思路：

贪心问题，m次补签卡，求最长连续登陆天数，

补签卡够直接输出100.

如果不能全补签，就枚举m个补签卡的位置（一定是连续的）。

```

#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 110
using namespace std;
int day[maxn];
int main()
{
    int t,n,m;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&n,&m);
        day[0]=0;
        for(int i=1;i<=n;++i)
        {
            scanf("%d",day+i);
        }
        if(m>=n)//可以全部补签
        {
            printf("100\n");
            continue;
        }
        int ans=-1;
        for(int i=0;i<=n-m;++i)//枚举范围即可
        {
            if(day[m+i+1]-day[i]-1>ans)//第i 和第m+i+1之间的补签 得到连续的天数=day[m+i+1]-day[i]-1
                ans=day[m+i+1]-day[i]-1;
        }
        printf("%d\n",ans);
    }
}

```


### [J - 新加题1](https://cn.vjudge.net/problem/HihoCoder-1712) [HihoCoder - 1712 ](https://cn.vjudge.net/problem/1445422/origin)


思路：

"一般我们在对字符串排序时，都会按照字典序排序。当字符串只包含小写字母时，相当于按字母表"abcdefghijklmnopqrstuvwxyz"的顺序排序。现在我们打乱字母表的顺序，得到一个26个字母的新顺序。例如"bdceafghijklmnopqrstuvwxyz"代表’b’排在’d’前，'d’在’c’前，'c’在’e’前…… "

将给出的26个小写字母依此当成a~z即可，进行排序即可，因为要输出字符串，所以需要记下未转化前的字符串

给定一个结构体：里面有两个元素s1 s2都为char数组,s1为输入字符串，s2为转化后的字符串，然后结构体排序即可。

```
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 110
using namespace std;
struct Node{
    char s1[maxn],s2[maxn];
}node[1100];
int bm[30];
bool cmp(Node a,Node b)
{
   int val=strcmp(a.s2,b.s2);
   return val<0;//代表排序过后 字符串小的在前面
}
int main()
{
    int n;
    scanf("%d",&n);
    char ss[30];
    scanf("%s",ss);
    for(int i=0;i<26;++i)
        bm[ss[i]-'a']=i;//bm[k]的意思k+'a'对应的字符为bm[k]+‘a’
    for(int i=0;i<n;++i)
    {
        scanf("%s",node[i].s1);
        int len=strlen(node[i].s1);
        for(int j=0;j<len;++j)
            node[i].s2[j]=bm[node[i].s1[j]-'a']+'a';
        node[i].s2[len]='\0';
    }
    sort(node,node+n,cmp);//排序
    for(int i=0;i<n;++i)
    {
        printf("%s\n",node[i].s1);
    }
}

```


### [K - 新加题2](https://cn.vjudge.net/problem/HihoCoder-1562) [HihoCoder - 1562](https://cn.vjudge.net/problem/1044043/origin)


思路：

根据当前时间和过的秒数，计算出最后的时间，根据**最后时间**的**小时** **分钟** **秒** 计算出**时针的角度**和**分针角度** 即可

代码:

```
/*
K - 新加题2
*/
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#define maxn 110

/*
1.计算最后的 h m s
2.计算此时的时针与分针夹角
因为夹角只与最后针的位置与关，所以保证h m s在一定范围内，用公式求出夹角即可
时针： 1h 转60° 1min转0.5°   1s转 （0.5/60）°
分针： 60min转360  1min转 6°  1s转0.1°
*/
using namespace std;
int main()
{
    int bh,bm,bs;//开始时钟的时刻
    int hh,mm,ss;//最后时钟的时刻
    int t,T;
    float mines_angle,hour_angle;
    float ans;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %d %d",&bh,&bm,&bs);
        scanf("%d",&t);
        ss=bs+t%60;
        t/=60;
        mm=bm+t%60;
        t/=60;
        hh=bh+t;
        mm+=ss/60;
        ss=ss%60;//保证秒针的值在0~59
        hh+=mm/60;
        mm=mm%60;//保证分针的值在0~59即可
        hh%=12;//保证时针在0~11之内
        mines_angle=(float)mm*6.0+(float)ss*0.1;
        hour_angle=(float)hh*30.0+(float)mm*0.5+(float)ss*(0.5/60.0);
        ans=hour_angle-mines_angle;
        if(ans<0.0)
            ans*=-1.0;
        if(ans>180.0)
            ans=360.0-ans;
        printf("%.4f\n",ans);
    }
}
```


