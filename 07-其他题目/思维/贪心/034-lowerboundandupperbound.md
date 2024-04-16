

lower_bound()返回这个有序序列中**第一个大于等于**value的位置

upper_bound（）返回这个有序序列中**第一个大于**vlaue的位置



具体STL库好像用的二分查找

举个例子

代码

```cpp
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<map>
#define N 4020
#define INF 0x3f3f3f3f
#define MOD 10000
using namespace std;
int main()
{
    int arr[20];
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>arr[i];
    sort(arr,arr+n);
    for(int i=0;i<n;i++)
        printf("%3d ",i);
    puts("");
    for(int i=0;i<n;i++)
        printf("%3d ",arr[i]);
    puts("");
    int l,u,t=10;
    while(t--)
    {
        int val;
        scanf("%d",&val);
        l=lower_bound(arr,arr+n,val)-arr;//如果都在这个数大于所有数，则返回的是最后一个加1
        u=upper_bound(arr,arr+n,val)-arr;
        printf("l=%d ,u=%d\n",l,u);
    }
}```





输入数据

10 

1 2 8 6 7 56 75 32 12 92

下标 0     1    2    3    4     5       6     7      8       9

序列 1     2    6    7    8    12    32    56    75    92



查找 98

返回l=10  r=10

查找92

返回l=92  r=10

查找0

返回l=0     r=0

查找8

返回l=4    r=5；

这个数据表明若查找的值在有序序列最大值之外 会返回一个指向（数组末尾+1）指针



