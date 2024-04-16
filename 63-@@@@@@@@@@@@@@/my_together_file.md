

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


