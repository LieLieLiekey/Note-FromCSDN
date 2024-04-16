

 

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




最近在看一本《c缺陷与陷阱》，意识到在大型程序时对象的声明与定义的重要性

普通变量的定义与声明

每个外部对象都必须在程序的某个地方进行定义。因此如果一个程序中包含了语句

```cpp
extern int a;//声明变量a
```


那么，这个程序就必须在别处的某个地方包括语句

```cpp
 int a;//代表定义外部int型变量a
```


或者 

```cpp
int a=10;//定义变量a并初始化```


这两个语句既可以在同一个源文件中，也可以不在同一源文件中

 

 

若一个变量前加了static修饰符

```cpp
static int a;//定义变量a，但变量a只在此文件中起作用```


static修饰符不仅适用于变量，也适用于函数。如果一个函数f()调用函数g()，且只有该函数f调用函数g，那么就可以把函数f函数g写在同一个文件中，并把函数g声明为static型的， 

 表明这个对象或者函数的作用域只在此文件中。

 

 

 

**函数的声明方式**

（作用域修饰符）返回值类型   函数名（参数表）

**函数的定义方式**

返回值类型  函数名 （参数表）

{

   函数体

}

 

 

对C++编译器而言，当调用函数的时候，编译器只需要看到函数的声明。当定义类类型的对象时，编译器只需要知道类的定义，而不需要知道类的实现代码。因此，因该将类的定义和函数声明放在头文件中，而普通函数和类成员函数的定义放在源文件中。

这样在用到对应的接口函数时只需包含xxx.h文件即可，在需要修改函数内容时只在xxx.cpp修改。如果需要修改接口则只需修改xx.h对应的接口，xxx.cpp对应的接口即可。

 



### 关于c++迭代器的一些讨论。


具体结论已经经过实验。

c++STL库封装了一些非常常用的数据结构，但是想要熟悉掌握这些就不能不熟悉迭代器。

主要说三个问题以及结论


+ 正向迭代器与反向迭代器的相互转化以及转化的效率问题: 转化是O(1)还是O(log)的不太清楚。
+ .删除迭代器指向的元素后，it++ 还有效吗？
+ 删除迭代器指向的元素后，it会自动移动到下一个位置吗？
+ 正向迭代器和反向迭代器同样能够 $− − ​ --​$吗？



### 1 . 正向迭代器与反向迭代器的相互转化以及转化的效率问题


这里以$s e t &lt; i n t &gt; set&lt;int&gt;$ 容器为例子，$i t it$表示其正向迭代器，$r i t rit$表示其反向迭代器。

1.正向迭代器转化为反向迭代器

```cpp
    rit=reverse_iterator<set<int>::iterator >(it);
```


2.反向迭代器转化为正向迭代器

```cpp
	it=rit.base();
```


效率不太确定，反正不是O(n)的。应该是O(1) 或者O(logn)


但是需要注意的是，



 

       最近再做一个系统时，写了一个基类4个派生类，基类中有虚函数，每次修改之后就将二级制信息存储进*.dat文件。

但是在再起启动程序时就出现这样的访问冲突问题，然后就一直困扰了3天，搜百度，博客，知乎等。最后还是在老师的提醒下发现问题出现在哪里。

      每个类每多一个虚函数，其内存大小就多4个字节用来存放改函数对应的地址，所以在用二进制存取的过程中也将虚函数的地址存入*.dat文件，接下来重启程序时，此时生成程序的虚函数地址可能已经改变，但是在二进制读取时还是读取的原来的函数地址，所以在使用基类时的数据就会出现访问错误，可能会访问位置内存，但没有访问权限，接下来就是程序异常退出。

 


![./figures/20180612194837703](./figures/20180612194837703)


 

 大概就是这样的问题，我试着换了还文本模式读取信息，成功！！！

 

还有需要注意一点的是 new开辟内存时会调用类的构造函数，但是malloc不会，后者只是在栈上非分配指定大小内存而已。

 



题目：

第一行输入一个数N（0<N<=100）,表示有N组测试数据。后面的N行输入多组输入数据，每组输入数据都是一个字符串S(S的长度小于10000，且S不是空串）， 测试数据组数少于5组。数据保证S中只含有"[","]","(",")"四种字符

   解决这道题，首先要知道括号配对满足的条件是什么。   1.左括号与右括号个数相等   2.左右括号配对次序正确   解决这道题要用到“栈”  

**输入字符串   从开始往后查 当遇到左括号时将之进入栈，继续往后查 当遇到右括号时就要与“栈”的首个比较看是否配对  **

**当配对时 将配对的符号从栈中取出，不配对时即break；  ** 以下两种情况还需特判一下    1.字符最后一个判断完了  但最后栈里是否还有。   2.栈里没有了 但查到了右括号即无法找到栈中左括号  

上代码

```cpp
#include<stdio.h>  
#include<string.h>  
char zhan[10010];进栈  
char s[10010];  
int main()  
{  
    int t,k,len,sign;//len用于判断是否停止  
    scanf("%d",&t);  
    while(t--)  
    {  
       scanf("%s",s);  
       len=strlen(s);  
       k=-1;sign=1;  
       for(int i=0;i<len;i++)  
       {  
           if(s[i]=='['||s[i]=='(')//入栈  
                zhan[++k]=s[i];  
           else  if((s[i]==']'&&k!=-1&&zhan[k]=='[')||(s[i]==')'&&k!=-1&&zhan[k]=='('))进栈查找  
                   zhan[k--]='\0';  
           else//查找不符合  
                 {  
                     sign=0;  
                      break;  
                 }  
             if(i==len-1&&k!=-1)//最后一个查完 了但栈里还有的情况  
             {  
                 sign=0;  
                 break;  
             }  
       }  
       if(sign==1)  
        printf("Yes\n");  
       else  
        printf("No\n");  
       memset(s,0,sizeof(s));  
    }  
}  
```


 

如有细节错误请在下方评论指出，本人将不胜感激。

 

 



**在吸收用键盘输入的数据时gets（）与scanf（）函数都有读取字符串的功能。但是他们吸收字符串除了gets（）能吸收空格而scanf（）不能吸收空格的区别之外。他们还是有很大的区别的。若能掌握这些细节，那么用这些函数时就能更加灵活**

**咱们先看课本中对gets（）和scanf（）吸收字符串的介绍。**

**gets（）函数用法:**

gets（）函数可以接受输入包含空格的完整句子，知道遇到换行符结束。   功能:接受用户键盘输入，将输入的字符串保存在字符数组中，如果接受到【enter】键则返回，并在字符串的末尾加上字符串结束字符'\0'；

```cpp
char str[100];
gets(str);
puts(str);
```


 

输入字符串 ''how are you''【回车】输出str字符串 结果为how are you,当然字符串结尾str[11]='\0'；（回车键当然也不会吸收）

**gets（）函数可以吸收空格，但遇见回车不吸收，并且把把回车当作该字符串的结束标志，在字符串末尾补'\0'；**

**scanf（）函数用法：**

scanf（）函数吸收字符串时使用格式控制符%s，与%s对应的是字符数组的名称，此时空格和回车符号均作为输入数据的分隔符而不能读入。

eg:

```cpp
#include<stdio.h>
int main()
{
char s1[100],s2[100],s3[100];
scanf("%s%s%s",s1,s2,s3);
printf("s1=*%s*,s2=*%s*,s3=*%s*",s1,s2,s3);
}```


 输入字符串 ''how are you''【回车】输出：s1=*hello*,  s2=*are*,s3=*you*;

**即scanf（）吸收字符串时，不吸收空白符，遇见空白符停止吸收，在字符串末尾补'\0'，并且scanf（）吸收字符时会自动略过开头的空白符，直至遇见一个非空白符才开始它的吸收过程。**

 

**那么咱们再进一步详细的思考**

相信打过一段时间的代码的人都知道，用scanf（）吸收字符串时，如果scanf（）后面还有一个字符变量，为了不让字符变量被被回车或者空格影响，都会在中间加个getchar（）；

```cpp
#include<stdio.h>
int main()
{
    char a,s[100];
    scanf("%s",s);
    getchar();
    scanf("%c",&a);
    printf("string s=*%s*，char a=*%c*",s,a);
}
```


 

输入：abcd e【回车】

输出：string s=*abcd*,char a=*c*; 

若不加getchar（）；

```cpp
#include<stdio.h>
int main()
{
    char a,s[100];
    scanf("%s",s);
    scanf("%c",&a);
    printf("string s=*%s*\nchar c=*%c*",s,a);
}
```


 

输出应该就是：string s=*abcd*,char a=* *;                      可见空格被字符a吸收了。 

这个测试说明：scanf（）在接受字符串的时候，遇见字符串结束符号 也就是空白符，不吸收并且将之留在输入缓存缓存区内（stdin文件中），使得下一个字符在吸收时先遇见的便是空白符。所以一般情况下用getchar（）把该空白符吸收了，防止对后面的字符吸收数据有影响。

 

那么gets（）函数吸收字符串时对结束标志的处理跟scanf（）一样吗？   不知道，那么就测试一下呗。

```cpp
#include<stdio.h>
int main()
{
    char a,s[100];
    gets(s);
    a=getchar();
    printf("string s=*%s*，char a=*%c*",s,a);
}```


输入：abcd【回车】e

输出：string s=*abcd*,a=*e*  

什么 ∑( 口 ||   gets（）竟然可以不用getchar（）；就把回车符号给吸收了

 

那么再测试一个开头就是回车的数据

输入：【回车】a

输出：string s=**,a=*a*

∑( 口 || gets（）竟然也可以吸收只有一个回车的空字符串。。。。

 

 

**其实gets（）在吸收字符串时遇见回车就把回车从输入缓存区内吸收，并且结束吸收，把吸收的回车符号变为字符串结束标志'\0'**

**所以gets（）吸收字符串时不会在输入缓存区内留下吸收过的任何东西，而且开头的空字符串gets（）也会将之看作字符串吸收。**

 

**而scanf（）在吸收字符串时会自动掠过开头的空白符（也就是对于他的来说的空字符串），而直至遇见一个非空白符才开始吸收， 并且遇见它的结束标志后，停止吸收字符，并且将该结束标志留在输入缓存区内。**

 

 

 

 

总结：

**gets（）吸收字符串时，会吸收空字符串（只有一个回车的字符串），并且吸收完字符串后将回车符号吸收变为'\0'，不在输入缓存区内留下该回车符号。**

**scanf（）吸收字符串时，会自动掠过开头的空白符，直至遇见第一个非空白符才开始吸收，并且吸收完字符串后，会自动在吸收的字符串后加上'\0'。将遇见的结束标志（空白符）还留在输入缓存区内。  **

 

 

 

每种函数都有自己特殊的用法，要将之灵活运用。

PS：puts（）输出字符串时会自动加上换行。

 

 

 

如果该文章有错误，请在下方评论区补充，我将不胜感激。



 

Youtube网址[https://www.youtube.com/watch?v=z0v6hmumCFU](https://www.youtube.com/watch?v=z0v6hmumCFU)

如下写了一个程序


![./figures/20181011082246571](./figures/20181011082246571)


 

点击解决方案->添加->新建项目（注意要在需要打包的程序的解决方案里面新建该项目）


![./figures/20181011082500569](./figures/20181011082500569)


选择其他项目类型-> Visual Studio installer 里面 Setup Project

如果没有这一项请点此网址[https://www.jb51.net/article/128869.htm](https://www.jb51.net/article/128869.htm)按照教程下载安装此组件


![./figures/20181011082624560](./figures/20181011082624560)


之后点Application Folder右键ADD  项目输出 点击主输出确定

 


![./figures/20181011082950246](./figures/20181011082950246)



![./figures/20181011083049428](./figures/20181011083049428)


意思就是把你exe程序输出道这个文件中，（**注意如果exe程序需到某些dll组件需要把该组件和dll放在同一目录**）（**并且如果这个exe有相对路径使用一些资源的话，需要在这个文件夹内创建文件夹使得这个相对路径成立**） 

然后


![./figures/20181011083607433](./figures/20181011083607433)


意思就是创建一个快捷方式（桌面图标）名字自己起（在这里我重命名为dch测试）  


![./figures/20181011083708325](./figures/20181011083708325)


然后把这个图标放在桌面的哪个文件夹里（拖过去就行）


![./figures/20181011083813472](./figures/20181011083813472)


整完之后就是这样的效果


![./figures/20181011083917320](./figures/20181011083917320)


然后再在User's Programs Menu菜单创建一个文件夹


![./figures/20181011084041679](./figures/20181011084041679)


就像这样


![./figures/20181011084100817](./figures/20181011084100817)


然后再在这里点击创建新的快捷方式就像这样


![./figures/20181011084312513](./figures/20181011084312513)


点击里面的


![./figures/20181011084337780](./figures/20181011084337780)


双击


![./figures/20181011084354668](./figures/20181011084354668)


确认

就像这样（名字我给重命名了，看自己）


![./figures/20181011084443806](./figures/20181011084443806)


 这步的意思就是创建一个快捷方式在控制面板上 

然后就OK了

点击setup 重新生成 就像这样


![./figures/20181011084620343](./figures/20181011084620343)


就像这样


![./figures/2018101108470089](./figures/2018101108470089)


成功 然后你在解决方案里找到这个文件夹内的文件就OK 

就像这样


![./figures/20181011084841936](./figures/20181011084841936)


第一个是安装程序

 

 

 

 

如果OK了记得评论点赞哦 



### C语言课程设计作业–图书馆系统


这系统功能挺强大的，管理员密码：666666

```cpp
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<time.h>
#include<malloc.h>
#include<conio.h>
struct _BOOK//只有价钱 和状态 已经借书人性别是整形
{
   char book_name[20];
   char book_num[15];
   double book_prices;
   char author_name[20];
   int _state;
   char Borrower_name[20];
   char Borrower_num[15];
   int Borrower_sex;
   struct _BOOK  *next;
};
struct _VIP//借书人的信息
{
    char vip_name[20];
    char vip_num[15];
    char vip_mm[19];
    int vip_sex;
    int many;
    struct _VIP *next;
};
struct _BOOK *head_book;
struct _VIP *head_vip,*vip=NULL;//该vip是间接地址指针
int login_state,book_many,vip_many;
char _num[20],_mm[20],admin_mm[]="123456";//记录用户的登录信息
int main()
{

    struct _BOOK *creat_book();//ok
    struct _VIP* creat_vip();//ok
    bool check_name(char *s);//
    struct _BOOK* look_book0(char *str);
    void* p_malloc(int a);
    bool add_book();
    void delete_book(struct _BOOK *p,int);
    void revise_book1(struct _BOOK *p,int);
    bool revise_book2(struct _BOOK *p,int);
    void revise_book3(struct _BOOK *p,int);
    void revise_book4(struct _BOOK *p,int);
    bool revise_book5(struct _BOOK *p,int);
    bool revise_book0(struct _BOOK *p,int);
    void look_book1(struct _BOOK *p,int);
    void look_book2(char *name,int);
    void look_book3(char *title,int);
    struct _VIP* look_vip0(char *num);
    void revise_vip1(struct _VIP *p,int);
    void revise_vip2(struct _VIP *p,int);
    void revise_vip3(struct _VIP *p,int);
    void add_vip();
    bool vip_login();
    bool _continue();
    bool borrow_book();
    bool back_book();
    void book_updated();
    void vip_updated();
    void all_book(int);
    void all_vip();
    void reset_book();
    void reset_vip();
    void revise_color();
    head_book=creat_book();//ok
     head_vip=creat_vip();//ok
     void welcome_op();
    void identity_op();
    welcome_op();
    identity_op();
}
struct _BOOK *creat_book()//创建一个book信息的链表~导入图书信息//OK//
{
    struct _BOOK *h,*p,*s;
    void* p_malloc(int);
    int n;//n为图书的个数
    FILE *fp;
    if((fp=fopen("book.txt","rb"))==NULL)
    {
        fp=fopen("book.txt","wb");
        int a=0;
        fwrite(&a,4,1,fp);
        fclose(fp);
        printf("未找到book.txt文件，已经自动创建!，请重新启动该程序\n");
        exit(1);
    }
    fread(&n,sizeof(int),1,fp);
    book_many=n;
    h=(struct _BOOK*)p_malloc(sizeof(struct _BOOK));
    h->author_name[0]='\0';
    h->book_name[0]='\0';
    h->book_num[0]='\0';
    h->Borrower_name[0]='\0';
    h->Borrower_num[0]='\0';
    h->_state=0;
    h->next=NULL;
    p=h;
    for(int i=0;i<n;i++)//
    {
      if((s=(struct _BOOK*)malloc(sizeof(struct _BOOK)))==NULL)
      {
        printf("error!\n");
        exit(1);
      }
      p->next=s;
      if(fread(s,sizeof(struct _BOOK),1,fp)==EOF)
          break;
      s->next=NULL;
      p=s;
    }//文件读入完成
    fclose(fp);
    head_book=h;
    return h;
}
struct _VIP* creat_vip()//~导入vip信息
{
    void* p_malloc(int);
    struct _VIP *h,*p,*s;
    int n;//n为注册VIP个数
    FILE *fp;
    if((fp=fopen("vip.txt","rb"))==NULL)//准备读取文件
    {
        fp=fopen("vip.txt","wb");
        int a=0;
        fwrite(&a,4,1,fp);
        printf("未找到vip.txt文件，已经自动创建!，请重新启动该程序\n");
        exit(1);
    }
    fread(&n,sizeof(int),1,fp);
    vip_many=n;
    h=(struct _VIP*)p_malloc(sizeof(struct _VIP));
    h->many=0;
    h->vip_mm[0]='\0';
    h->vip_name[0]='\0';
    h->vip_num[0]='\0';
    h->vip_sex=0;
    h->next=NULL;
    p=h;
    for(int i=0;i<n;i++)
    {
      s=(struct _VIP*)p_malloc(sizeof(struct _VIP));
      p->next=s;
      if(fread(s,sizeof(struct _VIP),1,fp)==EOF)
      {
           break;
      }
       s->next=NULL;
      p=s;
    }//文件读入完成
    fclose(fp);
    head_vip=h;
    return h;
}
bool check_mm(char *s)//检查mm是否合法,并且带不符合时的警告
{
    int len,flag=0;
    len=strlen(s);
    if(len>=18||len<10)
    {
        printf("\t*密码长度在10~17位之间!!\n");
        getch();
        return 1;
    }
    for(int i=0;i<len;i++)
    {
        if( (s[i]>='a'&&s[i]<='z') || (s[i]>='A'&&s[i]<='Z') || s[i]=='_' || (s[i]>='0'&&s[i]<='9') || s[i]=='.')
            continue;
        else
        {
             flag=1;
             break;
        }
    }
    if(flag)
    {
        printf("所用密码不合法! 请重新输入\n");
        getch();
        return 1;
    }
    return 0;
}
bool check_name(char *s)//检查名字是否合格，不允许出现空白符就行
{
    int len,flag=0;
    len=strlen(s);
    if(len>20||len<2)
    {
        printf("\t*****名字太短或太长！\n");
        getch();
        return 1;
    }
    for(int i=0;i<len;i++)
    {
        if(s[i]==' '||s[i]=='\t')
        {
            flag=1;
            break;
        }
    }
    if(flag)
    {
        printf("\t*****名字不能包含空白符\n");
        getch();
        return 1;
    }
    return 0;
}
bool check_num(char *s)//检查编号是否符合
{
    int len;
    len=strlen(s);
    if(len!=10)
    {
        printf("\t*编号只能是一串十位的数字编号!\n");
        getch();
        return 1;
    }
    for(int i=0;i<len;i++)
    {
        if(s[i]>='0'&&s[i]<='9')
            continue;
        printf("\t*编号只能是一串十位的数字编号!\n");
        getch();
        return 1;
    }
    return 0;
}
struct _BOOK* look_book0(char *str)//通过*编号*,查找对应书编号结构体所在地址的前一个*地址*,如s的前一个地址//没找到对应编号则返回NULL
{
    bool flag=1;
    struct _BOOK *p,*s;
    p=head_book;
    s=p->next;//对s进行判断
    while(s!=NULL)
    {
        flag=strcmp(s->book_num,str);//0是找到了
        if(!flag)
            break;
        p=s;
        s=p->next;
    }
    if(!flag)
        return p;
    return NULL;
}
void * p_malloc(int a)//带警告的malloc
{
    void *p;
    if((p=malloc(a))==NULL)
    {
        printf("\t\t*****error!\n");
        getch();
        exit(1);
    }
    return p;
}
bool add_book()//书名 作者 编号 价钱//
{
    bool revise_book0(struct _BOOK *p,int);
    void delete_book(struct _BOOK *p,int);
    void reset_book();
    void reset_vip();
    char *num;
    struct _BOOK *p,*s;
    num=(char*)p_malloc(15);
    s=head_book->next;
    p=(struct _BOOK*)p_malloc(sizeof(struct _BOOK));
    head_book->next=p;
    p->next=s;
    do
    {
        fflush(stdin);
        printf("\t请输入新输入书的编号:");
        gets(num);
    }
    while(check_num(num));
    if(look_book0(num)!=NULL)
    {
        printf("\t*该书编号已经存在!!\n");
        getch();
        free(num);
        free(p);
        return 0;
    }
    strcpy(p->book_num,num);
    free(num);
    if(!revise_book0(head_book,1))
    {
        delete_book(head_book,1);
        return 0;
    }
    book_many++;
    reset_book();
    reset_vip();
    printf("\t\t书籍添加成功\n");
    getch();
    return 1;
}
void delete_book(struct _BOOK *p,int sign)//*删除*对应地址的书的信息//间接指针
{
    void reset_book();
    struct _BOOK *s;
    s=p->next;
    p->next=s->next;
    free(s);//释放s指向的区域//未测试不知道是否会死机;
    book_many--;
    if(!sign)
    {
       printf("\t\t删除成功\n");
       getch();
    }
}
void revise_book1(struct _BOOK *p,int sign)//通过地址*修改*book的书名//参数的对应编号的地址的前一个地址//sign为1时表明在注册 2表示修改的全体参数
{
    struct _BOOK *s;
    s=p->next;
    char *mod;
    mod=(char*)p_malloc(20);
    fflush(stdin);
    if(sign==1)
        printf("\t请输入该书的书名:");

    else
        printf("\t请输入修改后的书名:");
    do
    {
        gets(mod);
    }
    while(check_name(mod));
    strcpy(s->book_name,mod);
    if(!sign)
    {
        printf("\t\t修改信息成功\n");
        getch();
    }

    free(mod);
}
bool revise_book2(struct _BOOK *p,int sign)//通过地址*修改*借书的状态//进入按提示输入/ 0为不在书架
{
    struct _BOOK *s;
    bool revise_book5(struct _BOOK *p,int);
    s=p->next;
    if(sign==1)
        printf("\t请确定所添加的该书的状态0/1(1为在书架,0为不在书架):");
    else
         printf("\t请输入修改后的状态0/1(1为在书架,0为不在书架):");
    scanf("%d",&s->_state);
    if(s->_state)
    {
        s->Borrower_name[0]='\0';
        s->Borrower_num[0]='\0';
        s->Borrower_sex=0;
        if(!sign)
        {
           printf("\t\t状态信息修改成功\n");
           getch();
        }
        return 1;
    }
    else
    {
        if(!revise_book5(p,1))
            return 0;
        else
        {
            if(!sign)
            {
              printf("状态信息修改成功\n");
              getch();
            }
            return 1;
        }
    }

}
void revise_book3(struct _BOOK *p,int sign)//通过地址*修改*书的作者名称
{
    char *mod;
    mod=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        if(sign==1)
        printf("\t请输入所进该书的作者名:");
    else
        printf("\t请输入该书修改后的作者名:");

        gets(mod);
    }
    while(check_name(mod));
    p=p->next;
    strcpy(p->author_name,mod);
    if(!sign)
    {
        printf("\t\t修改成功\n");
        getch();
    }
    free(mod);
}
void revise_book4(struct _BOOK *p,int sign)//通过地址*修改*书的价格
{
    p=p->next;
    if(sign==1)
        printf("\t请输入该进图书的价格:");
    else
        printf("\t请输入新的价格:");
    scanf("%lf",&p->book_prices);
    if(!sign)
    {
        printf("\t\t价格修改成功\n");
        getch();
    }

}
bool revise_book5(struct _BOOK *p,int sign)//通过地址修改书的状态信息//改变该间接指向的用户信息
{
    struct _VIP *pp,*ss;
    struct _BOOK *s;
    char *mod;
    struct _VIP* look_vip0(char *num);
    mod=(char*)p_malloc(20);//输入用户的号码
    fflush(stdin);
    printf("\t请输入该用户的号码:");
    do
    {
        gets(mod);
    }
    while(check_num(mod));
    if((pp=look_vip0(mod))==NULL)//所要操作的VIP的间接指针
    {
        printf("\t*****抱歉,该用户编号不存在(返回原来的界面)\n");
        getch();
        free(mod);
        return 0;
    }
       ss=pp->next;
       s=p->next;
       strcpy(s->Borrower_name,ss->vip_name);
       strcpy(s->Borrower_num,ss->vip_num);
       s->Borrower_sex=ss->vip_sex;
       if(!sign)
       {
          printf("该书用户信息修改成功\n");
          getch();
       }
       free(mod);
       return 1;
}
bool revise_book0(struct _BOOK *p,int sign)//通过地址*修改*书的所有参数//sign 在此中要么为1要么为2
{
    revise_book1(p,sign);
    revise_book4(p,sign);
    revise_book3(p,sign);
    if(!revise_book2(p,sign))
        return 0;
    return 1;
}
void look_book1(struct _BOOK *p,int sign)//通过地址*输出*书的基本*信息*//0代表基本信息 1代表详细信息***************
{
    p=p->next;
    printf("《%-20s》\t%-18s\t%-20s\t%-20.2lf\t",p->book_name,p->book_num,p->author_name,p->book_prices);
    if(p->_state)
        printf("%-20s","在架");
    else
        printf("%-20s","不在架");
    if(!sign)
        printf("\n");
    else
    {
        printf("%-20s\t%-20s\n",p->Borrower_name,p->Borrower_num);
    }
}
void look_book2(char *name,int sign)//通过作者名*输出*书的基本*信息*
{
    int flag=0;
    struct _BOOK *p,*s;
    p=head_book;
    s=p->next;
    while(s!=NULL)
    {
        if(!strcmp(s->author_name,name))
        {
            look_book1(p,sign);
            flag++;
        }
        p=s;
        s=p->next;
    }
    if(!flag)
      printf("\n\n抱歉,此书库没有该作者所创作的书...................................\n");
    else
      printf("\n\n以上共有%d个查询结果.....................................\n",flag);
    getch();
}
void look_book2_(int sign)//带提示输入 book2//OK
{
    char *mod;
    mod=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        printf("\t请输入作者名:");
        gets(mod);
    }
    while(check_name(mod));
    look_book2(mod,sign);
    free(mod);
}
void look_book3(char *title,int sign)//通过书名*输出*书的基本*信息*//OK
{
    struct _BOOK *p,*s;
    int flag=0;
    p=head_book;
    s=p->next;
    while(s!=NULL)
    {
        if(!strcmp(s->book_name,title))
        {
            look_book1(p,sign);
            flag++;
        }
        p=s;
        s=p->next;
    }
    if(!flag)
        printf("\n\n抱歉，此书库没有该书......................\n");
    else
        printf("\n\n以上共有%d个查询结果......................\n",flag);
    getch();
}
void look_book3_(int sign)//带提示的 书名 信息//OK
{
    char *mod;
    mod=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        printf("\t请输入书名:");
        gets(mod);
    }
    while(check_name(mod));
    look_book3(mod,sign);
    free(mod);
}
void look_book4(int sign)//带提示的 编号找到信息//OK
{
    struct _BOOK *p;
    char *mod;
    mod=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        printf("\t请输入该书的编号:");
        gets(mod);
    }
    while(check_num(mod));
    p=look_book0(mod);
    if(p==NULL)
    {
        printf("\t*该书编不存在！！！\n");
        getch();
        free(mod);
        return;
    }
    look_book1(p,sign);
    getch();
    free(mod);

}
struct _VIP* look_vip0(char *num)//通过*vip号码* *找到*对应地址的*前一个地址*
{
    struct _VIP *p,*s;
    int flag=0;
    p=head_vip;
    s=p->next;
    while(s!=NULL)
    {
        if(!strcmp(s->vip_num,num))
        {
            flag=1;
            break;
        }
        p=s;
        s=p->next;
    }
    if(flag)
        return p;
    else
        return NULL;
}
void revise_vip1(struct _VIP *p,int sign)//通过地址*修改*vip性别
{
    p=p->next;
    printf("\t请确认您的性别0/1(0男 1女):");
    scanf("%d",&p->vip_sex);
    fflush(stdin);
    if(!sign)
    {
      printf("\t\t性别修改成功\n");
      getch();
    }

}
void revise_vip2(struct _VIP *p,int sign)//通过地址*修改*密码
{
    char *mod;
    mod=(char*)p_malloc(20);
    p=p->next;
    fflush(stdin);
    do
    {
      if(sign)
        printf("\t请设置您的密码:");
      else
        printf("\t请输入您要设置的密码:");
      gets(mod);
    }
    while(check_mm(mod));
    strcpy(p->vip_mm,mod);
    strcpy(_mm,mod);
    if(!sign)
    {
     printf("\t\t密码修改成功\n");
     getch();
    }
    free(mod);

}
void revise_vip3(struct _VIP *p,int sign)//通过地址*修改*昵称
{
    p=p->next;
    char *mod;
    mod=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        printf("\t请输入您要设置的昵称:");
        gets(mod);
    }
    while(check_name(mod));
    strcpy(p->vip_name,mod);
    if(!sign)
    {
    printf("\t\t昵称修改成功\n");
    getch();
    }
    free(mod);
}
void add_vip()//账号 密码 性别 昵称
{
    char *num;
    void reset_book();
    void reset_vip();
    struct _VIP *p,*s;
    num=(char*)p_malloc(20);
    s=head_vip->next;
    p=(struct _VIP*)p_malloc(sizeof(struct _VIP));
    head_vip->next=p;
    p->next=s;
    fflush(stdin);
    do
    {
        printf("\t请输入您的学号(工号):");
        gets(num);
    }
    while(check_num(num));
    if(look_vip0(num)!=NULL)
    {
        printf("\t*此号码已经存在！！\n");
        getch();
        free(num);
        free(p);
        return ;
    }
    strcpy(p->vip_num,num);
    free(num);
    revise_vip1(head_vip,1);
    revise_vip2(head_vip,1);
    revise_vip3(head_vip,1);
    p->many=0;
    vip_many++;
    reset_book();
    reset_vip();
    printf("\t\t账号注册成功请注意保管\n");
    getch();
}
bool vip_login()//登陆 登陆成功返回1 失败返回0//没有该账号//密码错误,
{
    struct _VIP *p,*s;
    fflush(stdin);
    do
    {
      printf("\t请输入您的账号:");
      gets(_num);
    }
    while(check_num(_num));
    do
    {
    printf("\t请输入您的密码:");
    gets(_mm);
    }
    while(check_mm(_mm));
    if((p=look_vip0(_num))==NULL)
    {
        login_state=0;
        printf("\t*****没有该账号\n");
        getch();
        return 0;
    }
    else//找到对应的账号
    {
        s=p->next;
        if(strcmp(s->vip_mm,_mm))
        {
           login_state=0;
           printf("密码错误\n");
           getch();
           return 0;
        }
        login_state=1;
        printf("登陆成功\n");
        getch();
        vip=p;//信息导入
        return 1;
    }
}
bool _continue()//通过发送是否继续,并且加以用户的判断返回对应值
{
    char mod;
    fflush(stdin);
    printf("\t\t\tcontinue(y/n)?:");
    mod=getchar();
    if(mod=='y'||mod=='Y')
        return 1;
    return 0;
}
bool borrow_book()//借书 借书成功返回1 失败返回0  ///*通过提示输入编号来借书*//不在书架，或者编号不存在返回0
{
    char *num;
    struct _BOOK *p;
    struct _VIP *vvip;
    void reset_book();
    void reset_vip();
    void login_state2();
    int flag=0;
    num=(char*)p_malloc(20);
    do
    {
        fflush(stdin);
        printf("\t请输入所借书的索书号:");
        gets(num);
        if(!check_num(num))
        {
            flag=1;
            break;
        }
        printf("\t*****您输入的编号不合法!\n");
        getch();
    }
    while(_continue());
    if(!flag)
    {
        free(num);
        return 0;
    }
    if((p=look_book0(num))==NULL)
    {
        printf("\t\t抱歉没有找到该编号对应的书\n");
        getch();
        free(num);
        return 0;
    }
    p=p->next;//找到对应编号对应的书
    vvip=vip->next;
    if(!p->_state)
    {
         printf("\t\t抱歉该编号对应的书不在书架\n");
         getch();
         free(num);
         return 0;
    }
    p->_state=0;//借书成功
    strcpy(p->Borrower_name,vvip->vip_name);
    strcpy(p->Borrower_num,vvip->vip_num);
    p->Borrower_sex=vvip->vip_sex;
    vvip->many++;
    reset_book();
    reset_vip();
    login_state2();
    printf("\t\t借书成功\n");
    getch();
    free(num);
    return 1;
}
bool back_book()//还书 通过对应的编号还书//如果用户不想输入或者书编对应的借书人不是自己//或者在书架 /
{
    struct _BOOK *p;
    struct _VIP *vvip;//中间用一下
    void login_state2();
    void reset_book();
    void reset_vip();
    char *num;
    int flag=0;
    num=(char*)p_malloc(20);
    do
    {
        fflush(stdin);
        printf("\t请输入所还书的书编号:");
        gets(num);
        if(!check_num(num))
        {
            flag=1;
            break;
        }
    }
    while(_continue());
    if(!flag)
    {
        free(num);
        return 0;
    }
    if((p=look_book0(num))==NULL)
    {
        printf("\t*此书编不存在！！！\n");
        getch();
        free(num);
        return 0;
    }
    p=p->next;//有该书
    vvip=vip->next;
    if(strcmp(p->Borrower_num,vvip->vip_num))
    {
       printf("抱歉，您未借此编号的书\n");
       getch();
       free(num);
       return 0;
    }
    p->_state=1;
    p->Borrower_name[0]='\0';
    p->Borrower_num[0]='\0';
    vvip->many--;
    free(num);
    reset_book();
    reset_vip();
    login_state2();
    printf("\t\t还书成功\n");
    getch();
    return 1;
}
void book_updated()//把所有数据保存
{
    struct _BOOK *p,*s;
    FILE *fp;
    p=head_book;
    s=p->next;
    if((fp=fopen("d:\\bookinformation\\book.txt","wb"))==NULL)
    {
       printf("open file:book error!!\n");
       exit(1);
    }
    fwrite(&book_many,sizeof(int),1,fp);
    while(s!=NULL)
    {
        fwrite(s,sizeof(struct _BOOK),1,fp);
        p=s;
        s=p->next;
    }
    fclose(fp);
}
void vip_updated()//vip数据保存
{
    struct _VIP *pp,*ss;
    FILE *fp;
    pp=head_vip;
    ss=pp->next;
    if((fp=fopen("d:\\bookinformation\\vip.txt","wb"))==NULL)//准备读取文件
    {
        printf("open file:vip error!!\n");
        exit(1);
    }
    fwrite(&vip_many,sizeof(int),1,fp);
    while(ss!=NULL)
    {
        fwrite(ss,sizeof(struct _VIP),1,fp);
        pp=ss;
        ss=pp->next;
    }
    fclose(fp);
}
void all_book(int sign)//输出所有书的基本信息
{
    system("cls");
    struct _BOOK *p,*s;
    void print_biao();
    void print_biao2();
    p=head_book;
    s=p->next;
    if(!sign)
      print_biao();
    else
      print_biao2();
     while(s!=NULL)
    {
        look_book1(p,sign);
        p=s;
        s=p->next;
    }
    printf("\n\n以上共有%d个结果......................\n",book_many);
    getch();
}
void print_biao()//输出一个book信息表头
{
    printf("%-247s\t%-20s\t%-20s\t%-20s\t%-20s\n\n","书名","编号","作者","价格","状态");
}
void print_biao2()//输出一个详细书籍信息的表头
{
    printf("%-24s\t%-20s\t%-20s\t%-20s\t%-20s%-20s\t%-20s\n\n","书名","编号","作者","价格","状态","Borrow name","Borrow num");
}
void all_vip()//输出所有VIP的基本信息 测试用
{
    struct _VIP *pp,*ss;
    pp=head_vip;
    ss=pp->next;
    while(ss!=NULL)
    {
        printf("nick:%20s\tnum:%20s\tmm:%20s\tsex: ",ss->vip_name,ss->vip_num,ss->vip_mm);
        if(ss->vip_sex)
            printf("女\n");
        else
            printf("男\n");
        pp=ss;
        ss=pp->next;
    }
    puts("—————————————————————————————————————————————————————");
    printf("\n\n以上共有%d个结果.........................\n",vip_many);
    getch();
}//2
void free_book()//释放book 链表内存
{
    struct _BOOK *p,*s;
    p=head_book;
    s=p->next;
    while(s!=NULL)
    {
        free(p);
        p=s;
        s=p->next;
    }
    free(p);
}
void free_vip()//释放vip链表内存
{
    struct _VIP *pp,*ss;
    pp=head_vip;
    ss=pp->next;
    while(ss!=NULL)
    {
        free(pp);
        pp=ss;
        ss=pp->next;
    }
    free(pp);
    login_state=0;
}
void reset_book()//用在已经打开链表的情况
{
    book_updated();
    free_book();
    creat_book();
}
void reset_vip()
{
    vip_updated();
    free_vip();
    creat_vip();
}
void welcome_op()//OK  欢迎界面
{
    system("cls");
    puts("\t\t\t-----------------------------------------\n");
    puts("\t\t\t----------欢迎进入图书信息管理系统-------\n");
    puts("\t\t\t-----------------------------------------\n");
    getch();
}
void identity_op()// //选择用户界面
{
    void _tourist();
    void _vip();
    void _administrator();
    void revise_color();
    char flag=0;
    do
    {
    system("cls");
    puts("\t\t\t-----------------------------------------\n");
    puts("\t\t\t① 游客    \n");
    puts("\t\t\t② 会员    \n");
    puts("\t\t\t③ 管理员  \n");
    puts("\t\t\t④ 调色人员\n");
    puts("\n\n\n");
    fflush(stdin);
    printf("\t\t请确认您的身份:[ ]\b\b");
    flag=getchar();
    switch(flag)
    {
    case '1':_tourist();break;
    case '2':if(vip_login()) _vip();break;//登陆成功才可进入vip页面
    case '3':_administrator();break;
    case '4':revise_color();break;
        default : fflush(stdin);puts("\t\t您的输入有误,请重新输入.\n");puts("plese enter any key return \n");getch();
    }
    }
    while(1);//为了减少空间复杂度
}
void _tourist()//OK//游客身份的界面//有BUg  同时输入123时只取第一个
{
   char flag=0;
    do
   {
    system("cls");
    puts("\t尊敬的游客您好:\n");
    puts("\n\n");
    puts("\t\t\t1.查看所有书籍信息\n");
    puts("\t\t\t2.根据书名查看信息\n");
    puts("\t\t\t3.根据作者名查看书籍信息\n");
    puts("\t\t\t4.根据编号查看书籍信息\n");
    puts("\t\t\t5.返回上一界面\n");
    puts("\t\t\t6.注册会员\n");
    puts("\t\t\t7.退出系统\n");
    puts("\n\n\n");
    fflush(stdin);
    printf("\t\t请输入您要选的功能:[ ]\b\b");
    flag=getchar();
    switch(flag)
    {
    case '1':all_book(0);break;
    case '2':look_book3_(0);break;
    case '3':look_book2_(0);break;
    case '4':look_book4(0);break;
    case '5':return;
    case '6':add_vip();break;
    case '7':exit(0);
        default : fflush(stdin);puts("\t*****您的输入有误,请重新输入.\n");getch();
    }
   }
   while(1);
}
void _vip()//会员身份的界面//进入就已经登陆 //ok
{
    char flag=0;
   void revise_vip();
   void look_vip(struct _VIP *pp,int);
   do
   {
    system("cls");
    puts("\t尊敬的会员您好:\n");
    puts("\t\t\t1.查看所有书籍信息\n");
    puts("\t\t\t2.根据书名查看信息\n");
    puts("\t\t\t3.根据作者名查看书籍信息\n");
    puts("\t\t\t4.根据编号查看书籍信息\n");
    puts("\t\t\t5.借书\n");
    puts("\t\t\t6.还书\n");
    puts("\t\t\t7.查看个人信息\n");
    puts("\t\t\t8.个人信息修改\n");
    puts("\t\t\t9.退出登陆\n");
    fflush(stdin);
    printf("\t\t请输入您要选的功能:[ ]\b\b");
    flag=getchar();
    switch(flag)
    {
    case '1':all_book(0);break;
    case '2':look_book3_(0);break;
    case '3':look_book2_(0);break;
    case '4':look_book4(0);break;
    case '5':borrow_book();break;
    case '6':back_book();break;
    case '7':look_vip(vip,0);break;
    case '8':revise_vip();break;
    case '9':login_state=0;vip=NULL;return;
        default : fflush(stdin);puts("\t****您的输入有误,请重新输入.\n");getch();
    }
   }
   while(1);
}
void _administrator()//管理员身份
{
    char mod[20];
    void revise_book_();
    void look_vip1();
    void delete_vip1();
    void delete_vip(struct _VIP *pp);
    void delete_book1();
    printf("请输入管理员密码：");
    scanf("%s",mod);
    if(strcmp(mod,admin_mm))
    {
        puts("\t\t密码错误!");
        getch();
        return ;
    }
    do
   {
    char flag=0;
    system("cls");
    puts("\t管理员您好:\n");
    puts("\n\n");
    puts("\t\t\t1.查看所有书籍的详细信息\n");
    puts("\t\t\t2.根据书名查看详细信息\n");
    puts("\t\t\t3.根据作者名查看书籍详细信息\n");
    puts("\t\t\t4.根据编号查看书籍详细信息\n");
    puts("\t\t\t5.查看所有vip会员信息\n");
    puts("\t\t\t6.查看某一会员的信息\n");
    puts("\t\t\t7.删除某一会员的信息\n");
    puts("\t\t\t8.添加书籍\n");
    puts("\t\t\t9.删除书籍\n");
    puts("\t\t\ta.修改某一书籍的信息\n");
    puts("\t\t\tb.返回上一界面\n");
    puts("\t\t\tc.退出系统\n");
    fflush(stdin);
    printf("\t\t请输入您要选的功能:[ ]\b\b");
    flag=getchar();
    switch(flag)
    {
    case '1':all_book(1);break;
    case '2':look_book3_(1);break;
    case '3':look_book2_(1);break;
    case '4':look_book4(1);break;
    case '5':all_vip();break;
    case '6':look_vip1();break;
    case '7':delete_vip1();break;
    case '8':add_book();break;
    case '9':delete_book1();break;
    case 'a':revise_book_();break;
    case 'b':return;
    case 'c':exit(0);
        default : fflush(stdin);puts("\t*****您的输入有误,请重新输入.\n");getch();
    }
   }
    while(1);
}
void revise_vip()//修改vip的所有信息
{
    void look_vip(struct _VIP *pp,int);
    void login_state2();
    struct _VIP *pp;
    pp=vip;
    look_vip(pp,1);
    revise_vip1(pp,1);
    revise_vip2(pp,1);
    revise_vip3(pp,1);
    reset_book();
    reset_vip();
    login_state2();
    puts("\t\t信息修改成功\n");
    getch();
}
void look_vip(struct _VIP *pp,int sign)//间接地址查看信息
{
    pp=pp->next;
    if(!sign)
       printf("您的个人信息:\n\n");
    else if(sign==1)
        printf("您此时的个人信息:\n\n");
    else
        printf("该用户的个人信息:\n\n");
    printf("nick:%20s\tnum:%20s\tmm:%20s\t性别: ",pp->vip_name,pp->vip_num,pp->vip_mm);
    if(pp->vip_sex)
        printf("女\n\n");
    else
        printf("男\n\n");
    if(!sign)
        getch();
}
void login_state2()//不带提示信息的重新登陆VIP
{
    struct _VIP *pp,*ss;
    pp=head_vip;
    ss=pp->next;
    while(ss!=NULL)
    {
        if(!strcmp(ss->vip_num,_num))
        {
            login_state=1;
            vip=pp;
            return;
        }
        pp=ss;
        ss=pp->next;
    }
}
void look_vip1()//带查看某一会员信息
{
    struct _VIP *pp;
    char *num;
    num=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        printf("\t\t请输入所要查看会员的账号:");
        gets(num);
    }
    while(check_num(num));
   if((pp=look_vip0(num))==NULL)
      {
        printf("\t*****该会员不存在!\n");
        getch();
        free(num);
        return ;
      }
    else
    {
        pp=pp->next;
        printf("nick:%20s\tnum:%20s\tmm:%20s\tsex: ",pp->vip_name,pp->vip_num,pp->vip_mm);
        if(pp->vip_sex)
            printf("女\n");
        else
            printf("男\n");
        getch();
        free(num);
        return;
    }
}
void delete_vip1()//带提示删除会员信息
{
    struct _VIP *pp;
    char *num;
    void delete_vip(struct _VIP *pp);
    num=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        printf("\t\t请输入所要删除会员的账号:");
        gets(num);
    }
    while(check_num(num));
   if((pp=look_vip0(num))==NULL)
      {
        printf("\t*****该会员不存在!\n");
        getch();
        free(num);
        return ;
      }
    else
    {
        look_vip(pp,2);
        delete_vip(pp);
        printf("\t\t删除成功\n");
        getch();
        free(num);
        return;
    }
}
void delete_vip(struct _VIP *pp)//根据间接地址删除会员信息
{
    struct _VIP *ss;
    ss=pp->next;
    pp->next=ss->next;
    free(ss);
    vip_many--;
    reset_vip();
}
void delete_book1()//带提示的删除某一书籍 1表示还书 0表示删除书的操作
{
    struct _BOOK *p;
    char *num;
    num=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        printf("请输入所要删除的书编号:");
        gets(num);
    }
    while(check_num(num));
    if((p=look_book0(num))==NULL)
    {
        free(num);
        return;
    }
    else
    {
        printf("该书的信息为:\n\n");
        print_biao2();
        look_book1(p,2);
        delete_book(p,1);
        reset_book();
        reset_vip();
        printf("该书已从书库移除\n");
        getch();
        free(num);
        return;
    }
}
void revise_book_()//带提示的修改书的全部参数
{
    struct _BOOK *p;
    char *num;
    num=(char*)p_malloc(20);
    fflush(stdin);
    do
    {
        printf("\t请输入所修改书的编号:");
        gets(num);
    }
    while(check_num(num));
    if((p=look_book0(num))==NULL)
    {
        printf("\t*该书编号不存在！！!\n");
        getch();
        free(num);
        return;
    }
    else
    {
        printf("该书的信息:\n\n");
        print_biao2();
        look_book1(p,1);
        if(!revise_book0(p,2))
        {
            free(num);
            return;
        }
        else
        {
            free(num);
            reset_book();
            reset_vip();
            printf("\t\t该书的所有参数修改成功\n");
            getch();
            return;
        }
    }
}
void revise_color()
{
    system("cls");
    char a[2],b[2],color[10]="color ";
    puts("\t\t\t0 = 黑色\n");
    puts("\t\t\t1 = 蓝色\n");
    puts("\t\t\t2 = 绿色\n");
    puts("\t\t\t3 = 湖蓝色\n");
    puts("\t\t\t4 = 红色\n");
    puts("\t\t\t5 = 紫色\n");
    puts("\t\t\t6 = 黄色\n");
    puts("\t\t\t7 = 白色\n");
    puts("\t\t\t8 = 灰色\n");
    puts("\t\t\t9 = 淡蓝色\n");
    puts("\t\t\tA = 淡绿色\n");
    puts("\t\t\tB = 淡浅绿色\n");
    puts("\t\t\tC = 淡红色\n");
    puts("\t\t\tD = 淡紫色\n");
    puts("\t\t\tE = 淡黄色\n");
    puts("\t\t\tF = 亮白色\n\n\n");
    puts("\t原色   窗口色选0,字体颜色选7");
    puts("\t白枫色 窗口色选f,字体颜色选4");
    puts("\t请输入窗口背景色  窗口字体颜色(用空格隔开)：\n");
    scanf("%s",a);
    scanf("%s",b);
    if(((a[0]>='0'&&a[0]<='9')||(a[0]>='A'&&a[0]<='F')||(a[0]>='a'&&a[0]<='f'))&&((b[0]>='0'&&b[0]<='9')||(b[0]>='A'&&b[0]<='F')||(b[0]>='a'&&b[0]<='f')))
    {
        if(a[0]==b[0])
        {
            printf("You can't choose the same color\n");
            getch();
        }

        else
        {
            color[6]=a[0];
            color[7]=b[0];
            color[8]='\0';
            system(color);
        }
    }
    else
    {
        printf("输入格式错误\n");
        getch();
    }
    return;
}


```




函数名：freopen 函数，以指定模式重新指定到另一个文件。模式用于指定新文件的访问方式。 头文件：stdio.h C89函数声明：

```bash
FILE *freopen( const char *filename, const char *mode, FILE *stream );
```


C99函数声明：

```bash
FILE *freopen(const char * restrict filename, const char * restrict mode, FILE * restrict stream);
```


形参说明：

```bash
filename：需要重定向到的文件名或文件路径。
mode：代表文件访问权限的字符串。例如，"r"表示“只读访问”、"w"表示“只写访问”、"a"表示“追加写入”。
stream：需要被重定向的文件流。
返回值：如果成功，则返回该指向该输出流的文件指针，否则返回为NULL。
```


eg:

```bash
freopen("../1.in","r",stdin);
freopen("../1.out","r",stdout);
```


1.代表输入流 变为从指定文件输入 2.代表输出流 变为输出道指定文件内 **默认情况下cin cout与之保持一致**

简单写东西的话 相对于fscanf（） 和fprintf（） 还是比较方便的 但是不能替代



c++类关于类静态成员和方法和类的普通成员和方法的关系以及区别

下面把静态属性(方法)称为类的属性(方法) ，普通属性(方法)称为对象的属性(方法)

#### 调用类成员和属性的几种方法


```cpp
/*

调用类成员和属性的几种方法:
    类名::属性或方法名
    对象.属性或对象名
*/
#include<cstdio>
#include<iostream>
using namespace std;
class Cat{
   
public:
    static int tot;
    static void Comemet(){
   
    tot=100;
    }
    static void Print(){
   
    cout<<tot<<endl;
    }
};
int Cat::tot=0;
int main(```




思路：

编码


![./figures/20180928084503446](./figures/20180928084503446)


 

所需头文件：

 

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
struct _Date
{
    char cc;
    int cnt;
} ;
bool Getbit(char *p,int k)//得到一个字节从左到右数的第k位
{

    if(*p&(1<<(8-k)))
        return 1;
    return 0;
}
void printbit(char*p)
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


 

 

 

编码代码：（因为是雏形 所以这里采用的是以每一个字节当作一个字符）

文件名称说明:

**yuandoc.txt     需要压缩的文件**

**date1.txt      压缩后的文件**

**info1.txt       解压后的文件**

 

 

 

 

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
1.计算字符编码权值
2.构建编码树
3.将字符串转化为编码
4.存储赫夫曼编码树

5.将编码转化为字符串

程序缺陷 ：
只有一种字符编码时  该字符的编码为空
*/
#include"head1.h"
class HuffmanTree
{
public:
    int charsize;//字符种类数
    int slen;//读入的字节数
    char *read_str;//读入的字符串
    _Date *dateArr;//字符表（字符种类 已经对应出现的次数）
    HTnode *hufArr;//赫夫曼数组
    char **charCodeArr;//每类字符对应的编码
    int Allcodesize;
    char *codebitArr;
    HuffmanTree(char *str,int info_size)
    {
        /*
        需要:读入字符，和字节数
        结果:输出字母表dateArr,存储读入字符,得到字符种类数charsize,
        */
        hufArr=NULL;
        charCodeArr=NULL;
        codebitArr=NULL;
        slen=info_size;
        read_str=new char[slen];
        for(int i=0;i<slen;++i)
            read_str[i]=str[i];
        map<char,int>mmp;
        map<char,int>::iterator it;
        for(int i=0; i<slen; ++i)
        {
            it=mmp.find(read_str[i]);
            if(it==mmp.end())
                mmp.insert(pair<char,int>(read_str[i],1));
            else
                it->second++;
        }
        charsize=mmp.size();
        dateArr=new  _Date[charsize];
        int top=0;
        for(it=mmp.begin(); it!=mmp.end(); ++it)
        {
            dateArr[top].cc=it->first;
            dateArr[top++].cnt=it->second;
        }
        mmp.clear();
    }
    void BulidTree()
    {
        /*
        需要:字符表,字符个数,
        输出：哈夫曼数组,
        */
        hufArr=new HTnode[2*charsize-1];
        multiset<HTnode>hufset;
        for(int i=0; i<charsize; ++i)
        {
            hufArr[i].weight=dateArr[i].cnt;
            hufArr[i].index=i;
            hufset.insert(hufArr[i]);

        }//前n个节点存储树节点兵器人加入set容器中
        int top=charsize;
        int lc,rc;
        multiset<HTnode>::iterator it;
        while(top!=2*charsize-1)
        {
            it=hufset.begin();
            lc=it->index;
            hufset.erase(it);
            it=hufset.begin();
            rc=it->index;
            hufset.erase(it);
            hufArr[top].lchild=lc;
            hufArr[top].rchild=rc;
            hufArr[top].weight=hufArr[lc].weight+hufArr[rc].weight;
            hufArr[top].index=top;
            hufArr[lc].parent=top;
            hufArr[rc].parent=top;
            hufset.insert(hufArr[top]);
            top++;
        }
        /*
        二叉树构建完成
        数组为hufArr  根节点为2*charsize-2
        对应的字符在dateArr.cc里面
        */
    }
    void Getcharcode()
    {
        /*
        需要：哈夫曼节点数组hufArr[],字符表种类数charsize
        输出：字符对应的编码 存到charcodeArr[][]
        */
        charCodeArr=new char*[charsize];
        char *midc=new char[charsize+1];//作为中间字符串
        int top,now_node,next_node;
        Allcodesize=0;
        for(int i=0; i<charsize; ++i)
        {
            top=0;
            now_node=i;
            while(hufArr[now_node].parent!=-1)
            {
                next_node=hufArr[now_node].parent;
                if(hufArr[next_node].lchild==now_node)
                    midc[top++]='0';
                else
                    midc[top++]='1';
                now_node=next_node;
            }
            midc[top]=0;
            Allcodesize+=top*dateArr[i].cnt;//计算总共需要的比特位数
            charCodeArr[i]=new char[top+1];
            for(int j=0; j<top; ++j) //将第i个字符对应的吧编码存储进去
            {
                charCodeArr[i][j]=midc[top-1-j];
            }
            charCodeArr[i][top]='\0';
        }
        delete []midc;
        /*
        得到字符对应的编码
        */
    }
    void Getbitcode()
    {
        /*
        需要：读入的字符串 read_str ,字符表,每个字符对应的编码数组charcodeArr[][],
        输出:编码
        */
        int index;//找到字符对应的索引
        int mid;//存这些二进制数需要的字节数
        int sizepos,bitpos;
        mid=Allcodesize/8;
        if(Allcodesize%8)
            mid++;
        codebitArr=new char[mid];//申请编码内存
        int top=0;
        for(int i=0; i<slen; ++i)
        {
            for(int j=0; j<charsize; ++j)
                if(dateArr[j].cc==read_str[i])
                {
                    index=j;
                    break;
                }
            int j=0;
            //将此字符对应的编码存储到codebitArr数组中
            while(charCodeArr[index][j])
            {
                ++top;
                Getbitpos(top,sizepos,bitpos);
                if(charCodeArr[index][j]=='0')
                {
                    evalubit(&codebitArr[sizepos-1],bitpos,0);
                }
                else
                {
                    evalubit(&codebitArr[sizepos-1],bitpos,1);
                }
                j++;
            }
        }
        cout<<endl;
        while(top<mid*8)//不够一个字节的补上0补够一个字节
        {
            ++top;
            Getbitpos(top,sizepos,bitpos);
            evalubit(&codebitArr[sizepos-1],bitpos,0);
        }
        /*
        得到编码数组 codebitArr  共Allcodesize 编码总长度
        */
    }
    void Printcharcode()
    {
        /*
        输出字符表对应的编码
        */
    }
    void save_date()
    {
        /*
        初始：字符表种类数 ，bit位的数目, 字母表, Huffman树 ,编码
        输出：保存
        */
        int mid;
        mid=Allcodesize/8;
        if(Allcodesize%8)
            mid++;
        FILE *fp;
        fp=fopen("../date.txt","wb");
        fwrite(&charsize,4,1,fp);//写入 字符种类数目
        fwrite(&Allcodesize,4,1,fp);//写入  bit位数目
        fwrite(&slen,4,1,fp); //写入原来的字节数目
        char *chartable;
        chartable=new char[charsize];
        for(int i=0; i<charsize; ++i)
            chartable[i]=dateArr[i].cc;
        fwrite(chartable,1,charsize,fp);//写入字母表
        delete []chartable;
        fwrite(hufArr,sizeof(HTnode),charsize*2-1,fp);//写入Huffman 数组
        fwrite(codebitArr,1,mid,fp);//写入 编码
        fclose(fp);
    }
    ~HuffmanTree()
    {
        delete []read_str;
        delete []dateArr;
        if(hufArr)
            delete []hufArr;
        if(codebitArr)
            delete []codebitArr;
        if(charCodeArr)
        {
            for(int i=0; i<charsize; ++i)
                delete []charCodeArr[i];
            delete []charCodeArr;
        }
    }
};
//编码程序
int main()
{
    char *str;
    int info_size;
    FILE *fp;
    fp=fopen("../yuandoc.txt","rb");//读取需要压缩的文件
    fseek(fp,0L,SEEK_END);
    info_size=ftell(fp);//计算需要压缩文件的字节
    fseek(fp,0L,SEEK_SET);
    str=new char[info_size];
    fread(str,1,info_size,fp);
    HuffmanTree  huftree(str,info_size);
    //读取字符串到str
    huftree.BulidTree();
    huftree.Getcharcode();
    huftree.Getbitcode();
    huftree.save_date();
    fclose(fp);
    delete []str;
//over~~~~~
}
```


 

 

此代码储存到文本时按照如下方式储存

 

 


![./figures/20180928090600280](./figures/20180928090600280)


 

 

译码就比较简单了：


![./figures/2018092809110234](./figures/2018092809110234)


 

代码：

```cpp
/*
解压程序

*/
#include"head1.h"
void Compress_file(FILE *fp)//对文件进行解压  当成解压字符ASSIC码并存到文本里面（二进制存储）
{
    int charsize,Allcodesize,info_size;
    int sizepos,bitpos,now_index;
    char *codetable;
    char *codebitArr;
    char *InfoArr;
    HTnode* hufcodeArr;
    int mid;
    fread(&charsize,4,1,fp);//读取 charsize
    fread(&Allcodesize,4,1,fp);//读取  有用的编码位数
    fread(&info_size,4,1,fp);//读取 原来的字节数目
    codetable=new char[charsize];//申请 字母表内存
    hufcodeArr=new  HTnode[2*charsize-1];//申请 hufmantree内存
    fread(codetable,1,charsize,fp);//读取  字母表
    fread(hufcodeArr,sizeof(HTnode),charsize*2-1,fp);//读取哈夫曼树
    mid=Allcodesize/8;
    if(mid%Allcodesize)
        mid++;
    codebitArr=new char[mid];//申请编码内存
    fread(codebitArr,1,mid,fp);//读取编码
    int top=0;
    int cnt=0;
    now_index=2*charsize-2;
    InfoArr=new char[info_size];
    while(top<Allcodesize)
    {
        ++top;
        Getbitpos(top,sizepos,bitpos);
        if(Getbit(&codebitArr[sizepos-1],bitpos))
        {
            now_index=hufcodeArr[now_index].rchild;
        }
        else
        {
            now_index=hufcodeArr[now_index].lchild;
        }

        if(hufcodeArr[now_index].lchild==-1)
        {
            InfoArr[cnt++]=codetable[now_index];
//            printf("now index=%d\n",now_index);
            now_index=2*charsize-2;
//            printf(" cnt=%d, char=%c,ASSIC=%d\n",cnt,InfoArr[cnt-1],(int)InfoArr[cnt-1]);
        }
    }
    FILE *fp2;
    fp2=fopen("../info.txt","wb");
//    printf("infoArr=%s\n",InfoArr);
    fwrite(InfoArr,1,info_size,fp2);
    fclose(fp2);
    delete []codetable;
    delete []hufcodeArr;
    delete []codebitArr;
    delete []InfoArr;
}
int main()
{
    FILE *fp;
    fp=fopen("../date.txt","rb");
    if(fp==NULL)
    {
        printf("error!\n");
        exit(1);
    }

    if(!fp)
        exit(1);
    Compress_file(fp);
    fclose(fp);
}
```


 

缺陷：

1.只有一种字符无编码

2.把一个字节当作一个一种字符   压缩力度小

后续跟更新4个字节为以一个字符的编码代码



## 深入理解函数指针和函数数组


理解函数指针首先理解它的类型，首先**函数指针是个指针，他指向一个函数**。其次与普通变量指针相同重要的一点是函数指针的类型，**如果两个函数的参数个数、参数表、返回值类型都相同，则这两个函数是同一个类型**。换句话说同一类型的函数指针可以指向这两个函数
我们先看一个例子：

```cpp
#include<iostream>
using namespace std;
typedef int f2(int,int);
int fa(int a,int b)
{
    return a+b;
}
int main()
{
    f2 *c1=&fa;//函数指针c1指向的类型是f2,与fa的类型相同。c1的值是fa的地址
    cout<<(*c1)(5,6)<<endl;//*c1==fa  ,输出fa(5,6)的值。输出11
    return 0;
}

```


上面的 typedef int f2(int,int); 代表f2是一个函数，函数的类型是 接受两个int类型的参数，返回int类型的值


如果对上面的typedef int f2(int,int); 不理解可以进一步看介绍 typedef的博客[https://blog.csdn.net/Dch19990825/article/details/81024419](https://blog.csdn.net/Dch19990825/article/details/81024419)


现在定义一个函数fa，他的类型与 f2 相同，那么我们就可以定义一个 **指向f2类型** 的指针c1指向fa。

那么 *c1就是 fa 了，即(*c1)== fa。所以(*c1)(5,6) 就等效于 fa(5,6)了


另一个特别之处是在c语言中 **函数指针的指针** 就等效于 **函数指针本身**。直接的说

fa与&fa相同， *fa与fa相同
我们看这个例子：

```cpp
#include<iostream>
using namespace std;
typedef int f2(int,int);
int fa(int a,int b)
{
    return a+b;
}
int main()
{
    f2 *c1=&fa;
    f2 *c2=fa;//等效于fa等效与fa的地址即&fa
    cout<<(*c1)(5,6)<<endl;//输出11
    cout<<c2(5,6)<<endl;//输出11
    cout<<(*c2)(5,6)<<endl;//输出11
    return 0;
}
```


那么指针作为函数的参数又是怎样呢？

```cpp
#include<iostream>
using namespace std;
typedef int f2(int,int);
int fa(int a,int b)
{
    return a+b;
}
void show(int a,int b,f2* c)
{
    cout<<c(a,b)<<endl;
}
int main()
{
    show(1,2,fa);//输出3
    return 0;
}
```


上面的把fa函数的地址赋给 函数指针c，然后调用c指向的函数。

想了解函数指针数组吗？这个例子满足你

```cpp
#include<iostream>
using namespace std;
typedef int f2(int,int);
int fa(int a,int b)
{
    return a+b;
}
int fb(int a,int b)
{
    return a-b;
}
int fc(int a,int b)
{
    return a*b;
}
f2* func[3];
int main()
{
    func[0]=fa;
    func[1]=fb;
    func[2]=fc;
    for(int i=0; i<3; ++i) 
        cout<<func[i](5,6)<<endl;
    // 分别输出  11 -1 30
    return 0;
}
```


**最后是一个扩展阅读，c++11的lambda表达式**

```cpp
#include<iostream>
using namespace std;
typedef int f2(int,int);
int main()
{
    auto fa=[](int a,int b){return a+b;};
    cout<<fa(5,6)<<endl;
    return 0;//输出11
}

```



c++ lambda表达式博客链接 [https://www.cnblogs.com/DswCnblog/p/5629165.html](https://www.cnblogs.com/DswCnblog/p/5629165.html)


### 最后总结重要的几点


+ 首先函数指针是一个指针，它指向一个函数（指针的值是函数的地址）.+ 两个函数类型相同的充分必要条件是这两个函数的参数表和返回值类型相同.+ 在C语言中，函数名称等效函数的地址.


