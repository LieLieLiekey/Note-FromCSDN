

  给你两个容器，分别能装下A升水和B升水，并且可以进行以下操作 


  FILL(i)        将第i个容器从水龙头里装满(1 ≤ i ≤ 2); 


  DROP(i)        将第i个容器抽干 


  POUR(i,j)      将第i个容器里的水倒入第j个容器（这次操作结束后产生两种结果，一是第j个容器倒满并且第i个容器依旧有剩余，二是第i个容器里的水全部倒入j中，第i个容器为空） 


  现在要求你写一个程序，来找出能使其中任何一个容器里的水恰好有C升，找出最少操作数并给出操作过程 
Input 

有且只有一行，包含3个数A,B,C（1<=A,B<=100,C<=max(A,B)）Output 

  第一行包含一个数表示最小操作数K 


  随后K行每行给出一次具体操作，如果有多种答案符合最小操作数，输出他们中的任意一种操作过程，如果你不能使两个容器中的任意一个满足恰好C升的话，输出“impossible” 
Sample Input 
3 5 4

Sample Output 
6
FILL(2)
POUR(2,1)
DROP(1)
POUR(2,1)
FILL(2)
POUR(2,1)




**回溯搜索**

**记下搜索路径的父亲即可.**

****

**此代码中（map[i][j][0],map[i][j][1]）代表父亲的坐标。 map[i][j][2]来表示父状态到此状态所经历的方法，map[i][j][2]=0也就表示没有从父状态到此状态的方法或者未出现过此路径**



```cpp
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<stdlib.h>
#define N 300
#include<string>
using namespace std;
int a,b,c,ans,flag,map[110][110][3],res[100];
struct node
{
    int aa;
    int bb,step;
};
queue<struct node>mmp;
void dfs()
{
    int aa,bb,ss;
    struct node qq;
    qq=mmp.front();
    aa=qq.aa;
    bb=qq.bb;
    ss=qq.step;
    if(aa==c||bb==c)//判断是否为答案
    {
        flag=1;
        ans=ss;
        return;
    }
    mmp.pop();
    if(!map[a][bb][2])
    {
        struct node mm;
        mm.aa=a;
        mm.bb=bb;
        mm.step=ss+1;
        map[a][bb][0]=aa;
        map[a][bb][1]=bb;
        map[a][bb][2]=1;
        mmp.push(mm);
    }
    if(!map[aa][b][2])
    {
        struct node mm;
        mm.aa=aa;
        mm.bb=b;
        mm.step=ss+1;
        mmp.push(mm);
        map[aa][b][0]=aa;
        map[aa][b][1]=bb;
        map[aa][b][2]=2;
    }
    if(!map[0][bb][2])
    {
        struct node mm;
        mm.aa=0;
        mm.bb=bb;
        mm.step=ss+1;
        mmp.push(mm);
        map[0][bb][0]=aa;
        map[0][bb][1]=bb;
        map[0][bb][2]=3;
    }
    if(!map[aa][0][2])
    {
        struct node mm;
        mm.aa=aa;
        mm.bb=0;
        mm.step=ss+1;
        mmp.push(mm);
        map[aa][0][0]=aa;
        map[aa][0][1]=bb;
        map[aa][0][2]=4;
    }
    //方法5
    int ii,jj;
    if((aa+bb)>a)
    {
        jj=aa+bb-a;
        ii=a;
    }
    else
    {
        ii=aa+bb;
        jj=0;
    }
    if(!map[ii][jj][2])
    {
        struct node mm;
        mm.aa=ii;
        mm.bb=jj;
        mm.step=ss+1;
        mmp.push(mm);
        map[ii][jj][0]=aa;
        map[ii][jj][1]=bb;
        map[ii][jj][2]=5;
    }
    //方法6
    if((aa+bb)>b)
    {
        ii=aa+bb-b;
        jj=b;
    }
    else
    {
        ii=0;
        jj=aa+bb;
    }
    if(!map[ii][jj][2])
    {
        struct node mm;
        mm.aa=ii;
        mm.bb=jj;
        mm.step=ss+1;
        mmp.push(mm);
        map[ii][jj][0]=aa;
        map[ii][jj][1]=bb;
        map[ii][jj][2]=6;
    }
}
void bfs()
{
    struct node qq;
    qq.aa=qq.bb=qq.step=0;
    map[0][0][0]=map[0][0][1]=-1;
    map[0][0][2]=-1;
    mmp.push(qq);
    while(!mmp.empty())
    {
        dfs();
        if(flag)
            return ;
    }
}
int main()
{
    scanf("%d %d %d",&a,&b,&c);
    bfs();
    if(flag)
    {
        int ii,jj,mod1=1,mod2=2;
        struct node mm;
        mm=mmp.front();
        ii=mm.aa;
        jj=mm.bb;
        int k=0;
        while((ii!=-1)||(jj!=-1))
        {
            res[k++]=map[ii][jj][2];
            mod1=map[ii][jj][0];
            mod2=map[ii][jj][1];
            ii=mod1;
            jj=mod2;
        }
        printf("%d\n",ans);
        for(int i=k-1; i>=0; i--)
        {
            if(res[i]==1)
            {
                printf("FILL(1)\n");
                continue;
            }
            if(res[i]==2)
            {
                printf("FILL(2)\n");
                continue;
            }

            if(res[i]==3)
            {
                printf("DROP(1)\n");
                continue;
            }

            if(res[i]==4)
            {
                printf("DROP(2)\n");
                continue;
            }

            if(res[i]==5)
            {
                printf("POUR(2,1)\n");
                continue;
            }

            if(res[i]==6)
            {
                printf("POUR(1,2)\n");
                continue;
            }
        }
    }
    else
        printf("impossible\n");
}```






