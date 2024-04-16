

One day, Nobita found that his computer is extremely slow. After several hours' work, he finally found that it was a virus that made his poor computer slow and the virus was activated by a misoperation of opening an attachment of an email.

Nobita did use an outstanding anti-virus software, however, for some strange reason, this software did not check email attachments. Now Nobita decide to detect viruses in emails by himself.

To detect an virus, a virus sample (several binary bytes) is needed. If these binary bytes can be found in the email attachment (binary data), then the attachment contains the virus.

Note that attachments (binary data) in emails are usually encoded in base64. To encode a binary stream in base64, first write the binary stream into bits. Then take 6 bits from the stream in turn, encode these 6 bits into a base64 character according the following table:

That is, translate every 3 bytes into 4 base64 characters. If the original binary stream contains 3k + 1 bytes, where k is an integer, fill last bits using zero when encoding and append '==' as padding. If the original binary stream contains 3k + 2 bytes, fill last bits using zero when encoding and append '=' as padding. No padding is needed when the original binary stream contains 3k bytes.

 
**Value**012345678910111213141516171819202122232425262728293031**Encoding**ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef**Value**3233343536373839404142434445464748495051525354555657585960616263**Encoding**ghijklmnopqrstuvwxyz0123456789+/

 

For example, to encode 'hello' into base64, first write 'hello' as binary bits, that is: 01101000 01100101 01101100 01101100 01101111 Then, take 6 bits in turn and fill last bits as zero as padding (zero padding bits are marked in bold): 011010 000110 010101 101100 011011 000110 1111**00** They are 26 6 21 44 27 6 60 in decimal. Look up the table above and use corresponding characters: aGVsbG8 Since original binary data contains 1 * 3 + 2 bytes, padding is needed, append '=' and 'hello' is finally encoded in base64: aGVsbG8=

Section 5.2 of RFC 1521 describes how to encode a binary stream in base64 much more detailedly:

[Click here to see Section 5.2 of RFC 1521 if you have interest](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3430)

Here is a piece of ANSI C code that can encode binary data in base64. It contains a function, *encode (infile, outfile)*, to encode binary file *infile* in base64 and output result to *outfile*.

[Click here to see the reference C code if you have interest](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3430)

**Input**

Input contains multiple cases (about 15, of which most are small ones). The first line of each case contains an integer N (0 <= N <= 512). In the next N distinct lines, each line contains a sample of a kind of virus, which is not empty, has not more than 64 bytes in binary and is encoded in base64. Then, the next line contains an integer M (1 <= M <= 128). In the following M lines, each line contains the content of a file to be detected, which is not empty, has no more than 2048 bytes in binary and is encoded in base64.

There is a blank line after each case.

**Output**

For each case, output M lines. The ith line contains the number of kinds of virus detected in the ith file.

Output a blank line after each case.

**Sample Input**

```
3
YmFzZTY0
dmlydXM=
dDog
1
dGVzdDogdmlydXMu

1
QA==
2
QA==
ICAgICAgICA=
```


**Sample Output**

```
2

1
0

```


**Hint**

In the first sample case, there are three virus samples: base64, virus and t: , the data to be checked is test: virus., which contains the second and the third, two virus samples.

 

 

**思路：**

**1.**将病毒字符串反编码为原来字符串

2.AC自动机，判断文本串中出现多少个模式串

 

**注意：**

**1.**Segmentation Fault    段错误，节点字符开512*64，（因为最多原来的字符串最多有64个字节，也就是深度最多为64）

2.反编码后的字符串用unsignde char 或者int 来存储，因为反编码后的字符串值为0~255之间,（不要问我为什么字符串ASSIC的值还有负的）,每个节点的branch开256个，

 

AC代码：

```cpp
#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<iostream>
using namespace std;
const int maxn=5e4+7;
const int branch=   ;
int get_charcode(char c)
{
    if(c>='A'&&c<='Z')
        return c-'A';
    else if(c>='a'&&c<='z')
        return c-'a'+26;
    else if(c>='0'&&c<='9')
        return c-'0'+52;
    else if(c=='+')
        return 62;
    else
        return 63;
}
void put_bit(unsigned char &val,int k,int bit)//右边到左边的bit位  1~8 只限
{
    if(bit)
        val|=(1<<(k-1));
    else
        val&=(~(1<<(k-1)));
}
int get_bit(unsigned char &val,int k)//地位到高位的第 k 个位
{
    if(val&(1<<(k-1)))
        return 1;
    return 0;
}
int convertion(char *p,int *str)//将p反编码转化为 str 和cnt
{
    string coding="";
    int lp=strlen(p);
    for(int i=0; i<lp; ++i)
    {
        if(p[i]!='=')
        {
            unsigned char val=(unsigned char)get_charcode(p[i]);
            for(int i=6; i>=1; --i)
            {
                if(get_bit(val,i))
                    coding+='1';
                else
                    coding+='0';
            }
        }
    }

    int top=0;
    while(top< coding.length()/8)
    {
        unsigned char val;
        for(int i=8; i>=1; --i)
        {
            if(coding[top*8+8-i]=='1')
                put_bit(val,i,1);
            else
                put_bit(val,i,0);
        }
        str[top++]=(int)val;
    }
    return top;
}
struct Node
{
    int  fail;
    int  cnt;
    int  is_calu;//是否被该标号计算过
    int net[branch];
    void clear()
    {
        is_calu=-1;
        memset(net,0,sizeof(net));
        fail=0;
        cnt=0;
    }
};
class AcTree
{
private:
    Node* node;
    int top;
public:
    AcTree()
    {
        node=new Node[maxn];
        top=0;
        node[0].clear();
    }
    void init()
    {
        node[0].clear();
        top=0;
    }
    int hash_letter(int c)
    {
        return (int)c;
    }
    void insert(int *p,int total)
    {
        int now=0;
        for(int j=0; j<total; ++j)
        {
            int i=hash_letter(p[j]);
            if(!node[now].net[i])
            {
                node[now].net[i]=++top;
                node[top].clear();
            }
            now=node[now].net[i];
        }
        node[now].cnt=1;
    }
    void bulid_fail()
    {
        queue<int> mmp;
        /*
        建造fail指针   父节点的下面的fail指针全部求出来 然后加入队列
        */
        int now,to;
        for(int i=0; i<branch; ++i)
        {
            if(node[0].net[i])
                mmp.push(node[0].net[i]);
        }
        while(!mmp.empty())
        {
            now=mmp.front();
            mmp.pop();
            for(int i=0; i<branch; ++i)
            {
                if(node[now].net[i])
                {
                    to=node[now].fail;
                    while(to>0&&node[to].net[i]==0)//遍历以这个最大前缀(fail指针)后是否有这个字符
                    {
                        to=node[to].fail;
                    }
                    if(node[to].net[i])
                    {
                        to=node[to].net[i];
                    }
                    node[node[now].net[i]].fail=to;
                    mmp.push(node[now].net[i]);
                }
            }
        }
    }
    int find_tx(int* tx,int flag,int total)
    {
        /*
         查找tx在字典树中出现了多少个字串
        */
        int now=0,to;
        int ans=0;
        for(int j=0; j<total; ++j)
        {
            int i=hash_letter(tx[j]);
            to=now;
            while(to>0&&node[to].net[i]==0)//出错!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            {
                to=node[to].fail;
             }
            if(node[to].net[i])
                to=node[to].net[i];
            now=to;//找到下一个匹配的节点
            while(to>0&&node[to].is_calu!=flag)//遍历所有以*tx为结尾的的字串的个数
            {
                ans+=node[to].cnt;
                node[to].is_calu=flag;
                to=node[to].fail;
            }
        }
        return ans;
    }
    ~AcTree()
    {
        delete []node;
    }
};
void Print_ASSIC(int *p,int total)
{
    for(int i=0;i<total;++i)
        printf("%d ",p[i]);
    puts("");
}
char viru[1000];
int str[1000];
int main()
{
    AcTree dch;
    int n,m,ans;
    int total;
    while(~scanf("%d",&n))
    {
        dch.init();
        for(int i=0; i<n; ++i)
        {
            scanf("%s",viru);
            total=convertion(viru,str);
//            Print_ASSIC(str,total);
            dch.insert(str,total);
        }
        dch.bulid_fail();
        scanf("%d",&m);
        for(int i=1; i<=m; ++i)
        {
            scanf("%s",viru);
            total=convertion(viru,str);
//            Print_ASSIC(str,total);
            ans=dch.find_tx(str,i,total);
            printf("%d\n",ans);
        }
        printf("\n");
    }
    return 0;
}
```


 

