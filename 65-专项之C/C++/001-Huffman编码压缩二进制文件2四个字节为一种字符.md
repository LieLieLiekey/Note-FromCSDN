

 

编码过程与与上一节相似


![./figures/20180928084503446](./figures/20180928084503446)


 

**不同的是初始文件需要处理一下转化成处理文件**

```cpp
#ifndef HEAD1_H_INCLUDED
#define HEAD1_H_INCLUDED

#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<map>
#include<set>
#include<fstream>
using namespace std;
struct HTnode
{
    int parent,lchild,rchild;
    int weight,index;
    HTnode()
    {
        parent=lchild=rchild=-1;
        weight=0;
        index=-1;
    }
};
bool operator <(HTnode b,HTnode a)//对节点结构体进行运算符重载
{
    return b.weight<a.weight;
}
bool Getbit(char *p,int k)//得到一个字节从左到右数的第k位
{

    if(*p&(1<<(8-k)))
        return 1;
    return 0;
}
void PrintBit(char*p)//输出p指针指向的一个字节
{
    for(int i=1; i<=8; ++i)
        printf("%d",Getbit(p,i));
}
void Getbitpos(int bitsize,int &sizepos,int &bitpos)//得到第几个字节的第几位
{
    int mid=bitsize/8;
    if(bitsize%8)
    {
        sizepos=mid+1;
        bitpos=bitsize%8;
        return;
    }
    sizepos=mid;
    bitpos=8;
    return;
}
void evalubit(char *p,int k,int flag)//给以一个字节的从左到右第k位赋0   1
{
    if(flag)
    {
        *p=*p|(1<<(8-k));
        return;
    }
    *p=*p&(~(1<<(8-k)));
}
#endif // HEAD1_H_INCLUDED
```


**储存到中间文件的方式**


![./figures/20180930141223723](./figures/20180930141223723)


 

下面中

**yuandoc.txt     需要压缩的文件**

**date2.txt      压缩后的文件**

**info2.txt       解压后的文件**

#### 压缩程序


```cpp

/*
原理：
if 前i个字符是周期性的
    then     i-next[i]==T[next[i]]
else    T[i]=i;
*/
/*
Huffman树
功能：
将TXT文本压缩
1.处理文件后计算字符编码权值
2.构建编码树
3.将字符串转化为编码
4.存储赫夫曼编码树

5.将编码转化为字符串

时间:2018-9-30日 14:05
*/
#include"head1.h"
struct _Date
{
    int cc;
    int cnt;
} ;
class HuffmanTree
{
public:
    int charsize;//字符种类数
    int ilen;//读入信息的整形数组大小
    int *read_intArr;//读入整形数组信息
    int real_size;//真实信息的字节数
    _Date *```


