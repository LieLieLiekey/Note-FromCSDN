### 1159D - The minimal unique substring

链接：[1159D - The minimal unique substring](https://codeforces.com/contest/1159/problem/D)

思路：

令$a=(n-k)/2$  ， 接下来我们构造字符串s，a个0，1个1，a个0，1个1......
(这道题还是暴力找规律靠谱点)
**证明：**

这样字符串的周期为$a+1$.

更确切的说字符串$s$的组成是 ($a$个$0$)($1$个$1$)($a$个$0$)($1$个$1$) ($k-2$个字符) 四个部分

- 如果 $l>a+1$

​	那么存在$l'=l-(a+1)$也是可行的 

- 如果 $1<=l<=a​$

​	那么存在$l'=(l+a+1),l'\in[a+2,2*a+1]$ 可行的,因为所有$l'$满足  $l'+k<=n$ （**即$l'$在第三部分**）

所以只有$l=a+1​$可能满足，下面我们来证明字符串 $s​$ 中以 $l​$ 为开始，长度为 $k​$ 的字符串只存在一个。

要想长度为k，那么$l’$只有可能在第1，2，3部分。但因为只有第二部分有 $1$ ，但是不能选( $l$ 就是在第二部分)

故不存在$l’ !=l$ 满足与字符串s相同

代码：

```cpp
#include<bits/stdc++.h>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;

int main()
{
    int n,k;
    cin>>n>>k;
    int a=(n-k)/2;
    for(int i=1;i<=n;++i)
        cout<<(i%(a+1)==0?'1':'0');
    cout<<endl;
    return 0;
}
```
