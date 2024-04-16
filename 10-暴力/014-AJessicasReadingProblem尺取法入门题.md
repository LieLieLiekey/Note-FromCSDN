

### A - Jessica’s Reading Problem（尺取法入门题）


Jessica’s a very lovely girl wooed by lots of boys. Recently she has a problem. The final exam is coming, yet she has spent little time on it. If she wants to pass it, she has to master all ideas included in a very thick text book. The author of that text book, like other authors, is extremely fussy about the ideas, thus some ideas are covered more than once. Jessica think if she managed to read each idea at least once, she can pass the exam. She decides to read only one contiguous part of the book which contains all ideas covered by the entire book. And of course, the sub-book should be as thin as possible.

A very hard-working boy had manually indexed for her each page of Jessica’s text-book with what idea each page is about and thus made a big progress for his courtship. Here you come in to save your skin: given the index, help Jessica decide which contiguous part she should read. For convenience, each idea has been coded with an ID, which is a non-negative integer.

Input

The first line of input is an integer *P* (1 ≤ *P* ≤ 1000000), which is the number of pages of Jessica’s text-book. The second line contains *P* non-negative integers describing what idea each page is about. The first integer is what the first page is about, the second integer is what the second page is about, and so on. You may assume all integers that appear can fit well in the signed 32-bit integer type.

Output

Output one line: the number of pages of the shortest contiguous part of the book which contains all ideals covered in the book.

Sample Input

```bash
5
1 8 8 8 1
```


Sample Output

```cpp
2
```


####题意：

给你一个n，下面有n个数。求一个最短的区间，这n个数都在这个区间出现过。

##### 分析：



尺取法的原理：就像尺取虫一样，求解，《挑战程序设计竞赛》提出尺取法是建立在这样的一个模型上:

+ 找连续区间的问题，如果对于左端点s，第一个满足条件的右端点是t，那么对于左端点s+1,第一个满足条件的右端点是t’>=t


那么求所有的满足条件的区间就可以像尺取虫爬行的方式求解。


必须用O（n）的方法求解，又符合尺取法的条件

看代码理解：

```cpp
#include<cstdio>
#include<algorithm>
#include<map>
#include<set>
using namespace std;
const int maxn=1e6+10;
set<int>All;
map<int,int> times;
int a[maxn];
int main()
{
    int p,n,minn;
    scanf("%d",&p);
    for(int i=0;i<p;++i)
    {
        scanf("%d",a+i);
        All.insert(a[i]);
    }
    n=All.size();
    minn=p;
    int l=0,r=0;
    int sum=0;
    for(;;)
    {
        while(r<p&&sum<n)//不停的向右延申 直到出现的页数==N
        {
            if(times[a[r]]==0)
                sum++;
            times[a[r++]]++;
        }
        if(sum<n)//sum<n r延申出去了
            break;
        minn=min(minn,r-l);
        times[a[l]]--;//l右移动
        if(times[a[l++]]==0)//当l肯定没答案的时候
            sum--;
        if(p-l<n)
            break;
    }
    printf("%d\n",minn);
    return 0;
}
```


