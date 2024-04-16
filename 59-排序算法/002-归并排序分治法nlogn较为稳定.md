

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


 

