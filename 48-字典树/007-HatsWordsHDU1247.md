

 

A hat’s word is a word in the dictionary that is the concatenation of exactly two other words in the dictionary.  You are to find all the hat’s words in a dictionary. 

**Input**

Standard input consists of a number of lowercase words, one per line, in alphabetical order. There will be no more than 50,000 words.  Only one case. 

**Output**

Your output should contain all the hat’s words, one per line, in alphabetical order.

**Sample Input**
a
ahat
hat
hatword
hziee
word

**Sample Output**
ahat
hatword


题意:

给你一堆单词，让你输出其中的hat's单词(由两个单词拼接成)

简单字典树

将所有单词插入字典树后，对于每个单词枚举其字串，若左右两字串都出现的话是一个hat's 输出即可

注意

1.不要用构造函数清空节点，不要用构造函数清空节点，不要用构造函数清空节点！会内存超限（手动清空）

2.查找单词时注意判断单词该节点是否为一个单词

 

```cpp
#include<iostream>
#include<string.h>
#include<string>
#include<stdio.h>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
const int maxn=500000+20;
struct Node
{
    int cnt;
    int net[26];
    void clear()
    {
        cnt=0;
        memset(net,-1,sizeof(net));
    }
} node[maxn];//每个节点都代表一个路径
int top;
void clear_tree()
{
    node[0].clear();
    top=0;
}
int hash_letter(char c)
{
    return c-'a';
}
void insert_node(char *str)
{
    int now=0;
    while(*str)
    {
        int i=hash_letter(*str);
        if(node[now].net[i]==-1)
        {
            node[top+1].clear();
            node[now].net[i]=++top;
        }
        now=node[now].net[i];
        ++str;
    }
    node[now].cnt=1;
}
int search_node(char *str)//查看是否有这个单词
{
    //根据str返回前缀结束指针
    int now=0;
    while(*str)//根据当前节点和字符选择该字符对应的节点
    {
        now=node[now].net[hash_letter(*str)];
        if(now==-1)
            return 0;
        ++str;
    }
    if(node[now].cnt)
        return 1;
    return 0;
}
char words[50100][100];
int main()
{
    int n=0;
    clear_tree();
    top=0;
    while(~scanf("%s",words[n]))
        insert_node(words[n++]);
    for(int i=0;i<n;++i)
    {
        char w1[100];
        for(char *p=words[i]+1;*p;++p)//枚举字串
        {
            strcpy(w1,words[i]);
            w1[p-words[i]]='\0';
            if(search_node(w1)&&search_node(p))
            {
                 printf("%s\n",words[i]);
                 break;
            }
        }
    }
}```


 

