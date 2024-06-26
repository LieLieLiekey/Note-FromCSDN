

 

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
    _Date *dateArr;//字符表（字符种类 已经对应出现的次数）
    HTnode *hufArr;//赫夫曼数组
    char **charCodeArr;//每类字符对应的编码
    int Allcodesize;//压缩后的bit位数目（因为可能不足一个字节要补成一个字节）
    char *codebitArr;
    HuffmanTree(char *str,int info_size)
    {
        /*
        需要:读入信息
        结果:输出字母表dateArr,记下原文件的字节数real_size,读入文件经过处理后的处理文件read_intArr,共ilen*4个字节,得到字符种类数charsize,
        */
        char *read_str;
        real_size=info_size;
        hufArr=NULL;
        charCodeArr=NULL;
        codebitArr=NULL;
        ilen=info_size/4+(bool)(info_size%4);
        read_intArr=new int[ilen+2];
        read_str=(char*)read_intArr;
        for(int i=0; i<real_size; ++i)//对每一个字节操作
            read_str[i]=str[i];
        for(int i=real_size;i<ilen*4;++i)
            read_str[i]='\0';
        /*
        再增加两个不同的字符  以保证字符表不止一种字符  防止只有一种字符没有编码
        */
        read_intArr[ilen]=0;
        read_intArr[ilen+1]=1;
        ilen+=2;
        map<int,int>mmp;
        map<int,int>::iterator it;
        for(int i=0; i<ilen; ++i)
        {
            it=mmp.find(read_intArr[i]);
            if(it==mmp.end())
                mmp.insert(pair<int,int>(read_intArr[i],1));
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
        /*
        计算字符串种类以及出现个数 存到dateArr数组里面  共charsize个ok //下标从0开始
        */
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
                {
                     midc[top++]='0';
                }

                else
                {
                     midc[top++]='1';
                }

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
        需要：读入的字符串 read_intArr ,字符表,每个字符对应的编码数组charcodeArr[][],
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
        map<int,int>mmp;//字符  对应索引
        for(int i=0;i<charsize;++i)
        {
            mmp.insert(pair<int,int>(dateArr[i].cc,i));
        }
        map<int,int>::iterator it;
        for(int i=0; i<ilen; ++i)
        {
            it=mmp.find(read_intArr[i]);
            index=it->second;
            int j=0;
            //将此字符对应的编码存储到codebitArr数组中
            while(charCodeArr[index][j])
            {
                ++top;
                Getbitpos(top,sizepos,bitpos);
//                printf("top=%d,sizepos=%d,bitos=%d\n",top,sizepos,bitpos);
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
        mmp.clear();
        while(top<mid*8)
        {
            ++top;
            Getbitpos(top,sizepos,bitpos);
            evalubit(&codebitArr[sizepos-1],bitpos,0);
        }
                cout<<endl;
        /*
        得到编码数组 codebitArr  共Allcodesize 编码总长度
        */
    }
    void Printcharcode()
    {
        for(int i=0;i<charsize;++i)
        {
            char *p=(char*)&dateArr[i].cc;
            printf("%c%c%c%c: ",*p,p[1],p[2],p[3]);
            printf("%s\n",charCodeArr[i]);
        }
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
        fp=fopen("../date2.txt","wb");
        fwrite(&charsize,4,1,fp);//写入 字符种类数目
        fwrite(&Allcodesize,4,1,fp);//写入  编码的bit位数目
        fwrite(&real_size,4,1,fp); //写入原来的字节数目
        fwrite(&ilen,4,1,fp);//写入  需要压缩的int数组的长度
        int *chartable;
        chartable=new int[charsize];
        for(int i=0; i<charsize; ++i)
            chartable[i]=dateArr[i].cc;
        fwrite(chartable,4,charsize,fp);//写入字母表
        delete []chartable;
        fwrite(hufArr,sizeof(HTnode),charsize*2-1,fp);//写入Huffman 数组
        fwrite(codebitArr,1,mid,fp);//写入 编码
        fclose(fp);
    }
    ~HuffmanTree()
    {
        delete []read_intArr;
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
    fp=fopen("../yuandoc.txt","rb");
    fseek(fp,0L,SEEK_END);
    info_size=ftell(fp);
    fseek(fp,0L,SEEK_SET);
    str=new char[info_size];
    fread(str,1,info_size,fp);
    HuffmanTree  huftree(str,info_size);
    //读取字符串到str
    huftree.BulidTree();
    huftree.Getcharcode();
//    huftree.Printcharcode();
    huftree.Getbitcode();
    huftree.save_date();
    fclose(fp);
    delete []str;
//over~~~~~
}

```


解压程序
```
/*
解压程序

*/
#include"head1.h"
void Compress_file(FILE *fp)//对文件进行解压  当成解压字符ASSIC码并存到文本里面（二进制存储）
{
    int charsize,Allcodesize,real_size,info_size;
    int sizepos,bitpos,now_index;
    int *codetable;
    char *codebitArr;
    int *InfoArr;//来存储解码后的信息
    HTnode* hufcodeArr;
    int mid;
    fread(&charsize,4,1,fp);//读取 charsize
    fread(&Allcodesize,4,1,fp);//读取  有用的编码位数
    fread(&real_size,4,1,fp);//读取 真正的字节数目
    fread(&info_size,4,1,fp);//读取  压缩的int个数
    mid=Allcodesize/8;
    if(Allcodesize%8)
        mid++;
    codetable=new int[charsize];//申请 字母表内存
    hufcodeArr=new  HTnode[2*charsize-1];//申请 hufmantree内存
    codebitArr=new char[mid];//申请编码内存
    fread(codetable,4,charsize,fp);//读取  字母表
    fread(hufcodeArr,sizeof(HTnode),charsize*2-1,fp);//读取哈夫曼树
    fread(codebitArr,1,mid,fp);//读取编码
    int top=0;
    int cnt=0;
    now_index=2*charsize-2;
    InfoArr=new int[info_size];
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
            now_index=2*charsize-2;
        }
    }
    FILE *fp2;
    fp2=fopen("../info2.txt","wb");
    fwrite(InfoArr,1,real_size,fp2);
    fclose(fp2);
    delete []codetable;
    delete []hufcodeArr;
    delete []codebitArr;
    delete []InfoArr;
}
int main()
{
    FILE *fp;
    fp=fopen("../date2.txt","rb");
    if(fp==NULL)
    {
        printf("error!\n");
        exit(1);
    }
    Compress_file(fp);
    fclose(fp);
}

```