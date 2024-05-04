


我写这个博客纯粹是让自己以后留着，按着自己的理解写一遍，让自己对之记忆更加深刻


百度百科上介绍的尤为详细 **强力推荐**

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
}
```