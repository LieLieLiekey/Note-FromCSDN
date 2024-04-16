

### 

   归并排序求逆序数 
 


例题：nyoj117

+  
## 117-求逆序数
 


内存限制:64MB 时间限制:2000ms 特判: No

通过数:33 提交数:90 难度:5

### 题目描述:


在一个排列中，如果一对数的前后位置与大小顺序相反，即前面的数大于后面的数，那么它们就称为一个逆序。一个排列中逆序的总数就称为这个排列的逆序数。

现在，给你一个N个元素的序列，请你判断出它的逆序数是多少。

比如 1 3 2 的逆序数就是1。

### 输入描述:


```bash
第一行输入一个整数T表示测试数据的组数（1<=T<=5)
每组测试数据的每一行是一个整数N表示数列中共有N个元素（2〈=N〈=1000000）
随后的一行共有N个整数Ai(0<=Ai<1000000000)，表示数列中的所有元素。

数据保证在多组测试数据中，多于10万个数的测试数据最多只有一组。
```


### 输出描述:


```bash
输出该数列的逆序数
```


### 样例输入:


```bash
2
2
1 1
3
1 3 2
```


### 样例输出:


```bash
0
1
```


原理就是：

数学归纳法咳咳…

该区间的逆序数等于，**左区间的逆序数**加上**右区间的逆序数**加上**区间合并的时候逆序数(右边的数放在前面，前面区间的数比该数大)**

初始状态成立

递归过程成立

整个过程成立…

代码:

```cpp
#include<queue>
#include<iostream>
#include<string.h>
#include<cstdio>
#include<iostream>
#include<algorithm>
#define mset(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
const int maxn=5e5+100;
//marr中间储存的数组
//sum:记录逆序对的个数
//输入：arr[]
//结果：得到arr[]逆序对的个数
int arr[maxn],marr[maxn];
ll sum;
void mergeSort(int* arr,int l,int r) //左闭右闭
{
    if(l==r)
        return ;
    int mid=(l+r)/2;
    mergeSort(arr,l,mid);
    mergeSort(arr,mid+1,r);
    int tot=0;
    int ll=l,rr=mid+1;//开始需要比较的位置
    while(ll<=mid&&rr<=r) //next get date postion
    {
        if(arr[rr]<arr[ll])//逆序了，加上左边大于它的个数
        {
            sum+=mid-ll+1;
            marr[tot++]=arr[rr++];
        }
        else
        {
            marr[tot++]=arr[ll++];
        }
    }
    for(int i=ll; i<=mid; ++i)
        marr[tot++]=arr[i];
    for(int i=rr; i<=r; ++i)
        marr[tot++]=arr[i];
    for(int i=0; i<r-l+1; ++i)
        arr[l+i]=marr[i];
    return ;
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0; i<n; ++i)    scanf("%d",arr+i);;
    sum=0;
    mergeSort(arr,0,n-1);
    cout<<sum<<endl;
    return 0;
}


```




代码放在这里

 

时间复杂度与快排一样都为nlogn，但归并排序时间更为稳定。

相对于快排缺点是需要开一个临时数组用来存放临时数据。

```cpp
/*
归并排序
稳定的排序方法
key code
sort_combination()
*/
#include<cstdio>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<malloc.h>
#include<time.h>
using namespace std;
void merge_sort(int *arr,int Beg,int End)
{
    if(End-Beg<2)
        return;
    int mid=(Beg+End)/2;
    merge_sort(arr,Beg,mid);
    merge_sort(arr,mid,End);
    void merge_combination(int*,int,int,int);
    merge_combination(arr,Beg,mid,End);
}
void merge_combination(int *arr,int Beg,int mid,int End)
{
    int *marr=(int*)malloc(sizeof(int)*(End-Beg));
    int i=Beg,j=mid,k=0;
//    cout<<"merge combination function.\n";
    for(;i<mid&&j<End;)
        marr[k++]=(arr[i]<=arr[j])?arr[i++]:arr[j++];
    for(;i<mid;)
    marr[k++]=arr[i++];
    for(;j<End;)
        marr[k++]=arr[j++];
    k=0;
    for(int t=Beg;t<End;t++)
        arr[t]=marr[k++];
    free(marr);
}
const int maxn=1e3+10;
int arr[maxn];
int main()
{
    int n;
    cin>>n;
    srand(time(NULL));
    for(int i=0;i<n;i++)
        arr[i]=rand()%1000;
    for(int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<endl;
    cout<<"sort after.....\n";
    merge_sort(arr,0,n);
    for(int i=0;i<n;i++)
        cout<<arr[i]<<" ";
}
```


 



```
 ```


我写这个博客纯粹是让自己以后留着，按着自己的理解写一遍，让自己对之记忆更加深刻

 

百度百科上介绍的尤为详细  **强力推荐**

[https://baike.baidu.com/item/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F/3229428?fr=aladdin](https://baike.baidu.com/item/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F/3229428?fr=aladdin)

 

**希尔排序也称 缩小增量排序**

希尔排序原理 ：分段排序将相隔len长度的元素都放在一组，进行插入排序，接下来缩小len的长度，直至len=1时整个数组排序完毕，其中分段进行排序的过程是减少远距离的逆序数，使得len=1时进行插入排序，不会发生最坏的情况o（n*n）

其中选取len的规则对希尔排序效率的影响也非常大 希尔排序的做法简单易操作，但是其中的时间复杂度的计算确是尤其的复杂。所以怎样选取希尔排序中len也成为现代研究的一部分。

一般选取len有集中常用的方法，

1.len=n 。      每次减半 len/=2；

2.Hibbard增量。 2^1-1，2^2-1   ,  2^3-1,    2^4-1 ..........log2（n+1）

等等。。。。。。

对shall_sort增量的研究[ http://www.docin.com/p-1176055304.html](http://www.docin.com/p-1176055304.html) //也是非常的详细可靠。

在上面几类中 .Hibbard增量的效率是最为可观的。

在下面的代码中函数shall_sort就是希尔排序 

 

```cpp
#include<stdio.h>//
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>
#include<windows.h>
int main()
{
    void shall_sort(int *a,int n);
    int a[10000],n;
    time_t t1,t2;
    scanf("%d",&n);
    srand(unsigned(time(NULL)));
    for(int i=0;i<n;i++)
    {
        a[i]=rand()%5000;
    }
    t1=clock();
    shall_sort(a,n);
    t2=clock();//获取时间点
    printf("sort after...,time=%ldms\n",t2-t1);
    for(int i=0;i<n;i++)
        printf("%d ",a[i]);
}
void shall_sort(int *a,int n)//希尔排序 a为数组名称，n为元素个数
{
    int len=n/2,t,k=0,mod;
    t=log10(n+1.0)/log10(2.0);
    printf("t=%d\n",t);
    while(k<=t)
    {
      k++;
      len=pow(2.0,t-k+1)-1;
      for(int i=len;i<n;i++)//一次排序
      {
        int j=i-len;
        mod=a[i];
        while(j>=0&&a[j]>mod)//插入排序
        {
            a[j+len]=a[j];
            j-=len;
        }
        a[j+len]=mod;
      }
    }
}```


 

 

 

 

 

 

 

 



操作

1.找到一个枢纽pivotkey ,对于一个一次操作让枢纽左边的值都小于等于pivotkey,枢纽右边的值都大于等于pivotkey

2.一个排序后将该区间分成两部分继续递归排序，直至不符合l<R；

注意对于默认枢纽为第一个元素，你也可以找到 low-high中人一个当作枢纽然后与第一个进行交换

 

 

```cpp
#include<stdio.h>
#include<cstring>
#include<string>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<time.h>
#define INF 0x3f3f3f3f
#define N 10010
using namespace std;
template<typename T>
void Oneqsort(T *arr,int low,int high)
{
    if(low>=high)
     return;
    T pivotkey;
    int l,r;
    l=low;
    r=high;
    pivotkey=arr[l];
    while(l<r)
    {
        while(l<r&&(!(arr[r]<pivotkey)))r--;
        arr[l]=arr[r];
        while(l<r&&(!(pivotkey<arr[l]))) l++;
        arr[r]=arr[l];
    }
    arr[r]=pivotkey;
    Oneqsort(arr,low,r-1);
    Oneqsort(arr,r+1,high);
}
template <typename T>
void QuickSort(T *arr,int la)//数组首地址 数组长度
{
    Oneqsort(arr,0,la-1);
}
template <typename T>
void Print(T* arr,int len)
{
    for(int i=0;i<len;i++)
        cout<<arr[i]<<" ";
    cout<<endl;
}
int arr[N];
int main()
{
    int n;
    while(~scanf("%d",&n))
    {
         srand(time(NULL));
         for(int i=0;i<n;i++)
         {
             arr[i]=rand()%1000;
         }


         Print(arr,n);
         printf("after......\n");
         QuickSort(arr,n);
         Print(arr,n);
    }
}
```


 



数据结构AOE网 和AOV-网一节 

 

意义就是：

**给出一些事件和活动** （图），**该事件进行的前提条件是，所有以该事件为后继的活动已经完成**（顶点进行的前提条件是，其作为后继的边全部完成）

**给这些事件排个序，使得事件进行过程不冲突**

**如果冲突  **

**         **存在一个环

**否则**

**  **   可以得到一个拓扑序列,并且还可以计算对应事件或者边的最早发生事件和最晚发生时间。

代码实现：

```cpp
/*
拓扑排序

*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<stack>
#define INF 0x3f3f3f3f
using namespace std;
const int maxn=1010;
struct Edge
{
    int v;
    int val;
    int next;
    Edge()
    {
        next=-1;
    }
} edge[maxn]; //边的个数
int head[maxn];
int Indegree[maxn];
int seque[maxn];
int beg_time[maxn],end_time[maxn];
bool GetTuopu(int n,struct Edge edge[],int head[],int Indegree[],int seque[])//给邻接表 和入度序列  得到拓扑序列
{
    stack<int>mmp;
    for(int i=0; i<n; i++)
        if(!Indegree[i])
            mmp.push(i);
    int  top=0;
    while(!mmp.empty())
    {
        int now_v=mmp.top();
        mmp.pop();
        seque[top++]=now_v;
        int to=head[now_v];
        while(~to)
        {
            Indegree[edge[to].v]--;
            if(!Indegree[edge[to].v])
            {
                mmp.push(edge[to].v);
            }
            to=edge[to].next;
        }
    }
    if(top!=n)
        return 0;
    return 1;
}
int main()
{
    int n,m,u,v,w;
    while(~scanf("%d %d",&n,&m))
    {
        /*----------------建立邻接表------------*/
        memset(head,-1,sizeof(head));
        memset(Indegree,0,sizeof(Indegree));
        for(int i=0; i<m; ++i)
        {
            scanf("%d %d %d",&u,&v,&w);
            Indegree[v]++;
            edge[i].v=v;
            edge[i].next=head[u];
            head[u]=i;
            edge[i].val=w;
        }
        /*----------------求拓扑序列------------*/
        if(!GetTuopu(n,edge,head,Indegree,seque))
        {
            printf("Tuop sequen not exit\n");
            continue;
        }
        /*----------------求事件的最早开始时间------------*/
        memset(beg_time,0,sizeof(beg_time));
        for(int i=0; i<n; i++)//
        {
            int now_v=seque[i];
            //        beg_time[k]=Max（前驱的最短时间+边权）
            int to=head[now_v];
            while(~to)
            {
                if(beg_time[now_v]+edge[to].val>beg_time[edge[to].v])
                    beg_time[edge[to].v]=beg_time[now_v]+edge[to].val;
                to=edge[to].next;
            }
        }
        /*----------------求事件的最晚开始时间------------*/
        for(int i=0; i<n; ++i)
            end_time[i]=beg_time[n-1];//给事件的结束时间赋初值
        for(int i=n-1; ~i; --i)//
        {
            int now_v=seque[i];
//            end_time[k]=Min(后继的最晚时间-边权)
            int to=head[now_v];
            while(~to)
            {
                if(end_time[now_v]>end_time[edge[to].v]-edge[to].val)
                    end_time[now_v]=end_time[edge[to].v]-edge[to].val;
                to=edge[to].next;
            }
        }
        for(int i=0; i<n; ++i)
            printf("%3d",i);
        printf("\n");
        printf("beg_time:\n");
        for(int i=0; i<n; ++i)
            printf("%3d",beg_time[i]);
        printf("\n");
        printf("end_time:\n");
        for(int i=0; i<n; ++i)
            printf("%3d",end_time[i]);
        printf("\n");
        /*
        边的最早开始时间:前驱的最早开始时间
        边的最晚开始时间:后继的最晚开始时间-边权
        */
    }
}
/*
测试数据
9 11
0 1 6
0 2 4
0 3 5
1 4 1
2 4 1
3 5 2
4 6 9
4 7 7
5 7 4
7 8 4
6 8 2
*/```


 

