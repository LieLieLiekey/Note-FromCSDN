

### 1.字符编码和字符集


+  **ANSI编码** ​ 不同的国家和地区制定了不同的标准，由此产生了 GB2312、GBK、Big5、Shift_JIS 等各自的编码标准。这些使用 1 至 4 个字节来代表一个字符的各种汉字延伸编码方式，称为 ANSI 编码。在简体中文Windows操作系统中，ANSI 编码代表 GBK 编码；在日文Windows操作系统中，ANSI 编码代表 Shift_JIS 编码。 +  **ASCII码** ​ 最普通常见的编码集合。可见字符只包含半角的英文字符和数字字符等。**只占用一个字节**，有效值范围为0~127 +  **GB2312** ​ 是ANSI编码的一种，实现了ASIIC编码上对中午字符的扩充，**占用两个字节**。不过在该编码下的只能译出中文，其他国家的打开改使用改编码存储的文件可能会出现乱码。 +  **GBK** ​ GBK即汉字内码扩展规范，K为扩展的汉语拼音中“扩”字的声母。英文全称Chinese Internal Code Specification。GBK编码标准兼容GB2312，共收录汉字21003个、符号883个，并提供1894个造字码位，简、繁体字融于一库。**占用两个字节**。 +  Unicode ​ 因为世界上存在所有编码方式，所以进行交流时有时会很不方便，这和就促使了Unicode的诞生，Unicode将世界上所有的符号都纳入其中，无论是英文、日文、还是中文等，但是占用四个字节，所以 +  **UTF-8** 


​ 可变长编码。对于不同字符存储占用的字节不同，具体实现原理像ipv4地址分级的方法一样。

### 2.全角和半角


+  全角 ​ **全角**指一个字符占用两个标准字符位置的状态。汉字字符和规定了全角的英文字符及国标GB2312-80中的图形符号和特殊字符都是全角字符 一般的系统命令是不用全角字符的，只是在作文字处理时才会使用全角字符。 +  半角 ​ 半角，即一个[字符](https://baike.baidu.com/item/%E5%AD%97%E7%AC%A6/4768913)占用一个标准字符的位置。 


#### 3.java实现对数组的排序​


+ 方法一：使用Arrays.sort()


```java
package test;
import java.util.Arrays;
public class Kit {
	public static void main(String[] args) {
		int[] arr=new int[]{2,878,89,7,78,78,45,21};
		Arrays.sort(arr);
		for(int i:arr)
			System.out.println(i);
	}
}

```


+  方法二： ​ 自行编写程序或函数实现。 


### 4.java中三种注释形式


​

```java
//第一种

/*
第三种
*/ 


/*
 *第
 *三
 *种
*/
```




## 关于java中的==与equals(Object)方法


对于基本类型而言，判断两个变量的值是否相等用==即可

但是非基本类型而言，==只是判断两个变量是否指向同一对象，或者更确切的说判断两个对象的指向的地址是否相等。

```java
class Ceshi{
	public int a;
	public Ceshi() {}
	public Ceshi(int a) {this.a=a;}
};
public class Learn {

	public static void main(String[] args) {
		Ceshi a=new Ceshi(5);
		Ceshi b=new Ceshi(5);
		Ceshi c=a;
		if(a==b) {//a b虽然内存块的值相等，不过并不是同一个对象（同一个地址） 所以为false
			System.out.println("a==b");
		}
		if(a==c) {//a c指向同一个对象，所以为true
			System.out.println("a==c");
		}
	}
    //程序输出：a==c
}
```


学过c++的应该知道，对于结构体或者类，==号是判断其变量的成员变量(内存值)是否相等。

但是在java中所有的类用一个对象引用，引用代表的是java中( 非基本类型的 )变量储存的是对象的地址，所以==也就自然而然的只是判断两个变量是否指的同一个对象(内存)。


**如果想判断两个对象是否相等，可以用equals函数**，这个函数在Object类中，换句话说所有类都有这个函数，不过需要自己重写才能达到相应的功能。

String类重写了equals函数，所以两个String对象是否相等可以用equals函数进行判断

```java
public class Learn {

	public static void main(String[] args) {
		String a=new String("abc"),b=new String("abc");
		if(a==b) {
			System.out.println("a==b");
		}
		if(a.equals(b)) {
			System.out.println("a.equals(b)");
		}
	}
}
//程序输出：a.equals(b)
```


特别注意的是 StringBuffer类并没有重写equals函数



## Java的Lambda表达式和函数接口


下面主要将四个方面，并会给出具体的例子


+ 函数接口
+ lambda表达式
+ 使用Lambda表达式作为函数接口参数
+ 使用方法引用或构造器作为函数接口参数



#### 1.函数接口


函数式接口(Functional Interface)就是**一个有且仅有一个抽象方法的接口**。

函数式接口可以被隐式转换为 lambda 表达式。

Lambda 表达式和方法引用（实际上也可认为是Lambda表达式）上。

如定义了一个函数式接口如下：

```java
@FunctionalInterface //该注解只是显示的标注了接口用是一个函数接口，并强制编译器进行更严格的检查，如果不是就会报错。但也如果保证该接口是一个函数式接口也也可以不加该注解。
interface GreetingService 
{
   
    void sayMessage(String message);
}
```


函数式接口可以对现有的函数友好地支持 lambda。

#### 2.lambda表达式


Lambda 表达式，也可称为闭包，它是推动 Java 8 发布的最重要新特性。

Lambda 允许把函数作为一个方法的参数（函数作为参数传递进方法中）。

使用 Lambda 表达式可以使代码变的更加简洁紧凑。

lambda 表达式的语法格式如下：

```bash
(parameters) -> expression
或 
(parameters) ->{ statements; }
```


组成格式即：


+ （数据类型 参数名，数据类型 参数名…）：用来向表达式主体传递接口方法需要的参数。在编写Lambda表达式时**，可以省略参数的数据类型，后面的表达式主体会自动进行校对和匹配**。同时，如果只有参数，则可以省略括号（）
+ -> : 表示lambda表达式箭牌，用来指向参数数据指向，**不能省略**，且必须用英文符号。
+ {表达式主体}：由单个表达式或语句块组成的主体，**本质就是接口中抽象方法的具体实现**。**如果表达式主体只有一条语句，那么可以省略包含主体的大括号**。另外，在lambda表达式主体中允许有返回值，**当只有一条return语句时，也可以省略return关键字** 。



lambda表达式多用于实现函数接口作为方法参数。

#### 3.使用Lambda表达式实现函数接口


举一个例子

```java
package learn;
import java.util.*```




## Java的Set、Map和数组的自定义排序


该文章讲述下面三点并给出相应实例


+ Set的三种自定义排序和遍历
+ Map的三种自定义排序和遍历
+ 数组的三种自定义排序



#### 1.Set的三种自定义排序和遍历


这里的三种自定义排序分别是


+  实现Comparator接口的compare方法并传入构造函数 
+  传入Lambda表达式作为函数接口的参数 
+  以类名::静态方法名作为函数接口的参数 



当然还有常用的第四种方法，让存储元素的类实现Comparabel接口的comparaTo(Object)函数，不过这里不再阐述。

这里的三种遍历集合的方式是

​ 1. 使用**迭代器**遍历set集合

​ 2. 使用forEach函数**用Lambda表达式**实现遍历集合

​ 3. 使用forEach函数用**类名::静态方法名**实现遍历集合

下面以重载String的排序为例，将默认的字典序改为按字符串长度排序。

使用第一种方法自定义排序

```java
package learn;
import java.util.*;
class EachInterface{
   
	static void fuc(String key) {
   
		System.out.println(key);
	}
}
class compare implements Comparator{
    //第一种方式所需的接口实现类
	public int compare(Object _a,Object _b) {
   
		String a=(String)_a;
		String b=(String)_b;
		return a.length()-b.length();
	}
}
public class Learn {
   

	public static void main(String[] args) {
   
		TreeSet<String> mmp=new TreeSet<String>(new compare());//自定义排序的第一种方式
		mmp.add("abccc");
		mmp.add("dch2");
		mmp.add("qwe");
		/*遍历的第一种方式*/
		Iterator it=mmp.iterator();
		while(it.hasNext()) {
   
			System.out.println(it.next());
		}
		System.out.println("===================");
		
		/*遍历的第二种方式*/
		mmp.forEach( (a)->{
   System.out.println(a);}	);
		System.out.println("===================");
		
		/*遍历的第三种方式*/
		mmp.forEach(EachInterface::fuc);
		
	}
	
}

/*
输出：
qwe
dch2
abccc
===================
qwe
dch2
abccc
===================
qwe
dch2
abccc
*/
```



使用第二种方法自定义排序

```java
package learn;
import java.util.*;
public class ```




### Java中的接口类.


### begin 接口类的简单介绍.


​ 如果一个抽象类中的所有方法都是抽象的，则可以把他定义为接口类。

接口类只能做两个事情：


+  在主函数调用接口类的静态方法或者静态常量. 
+  其他类实现该接口. 
### 1.接口类定义的规则:
 



在JDk8.0往后的版本中，接口类不止可以有抽象方法，还可以有静态方法和默认方法，即下面几种


+ 抽象方法（abstrat）.
+ 静态方法（static）.
+ 默认方法（default）.
+ 静态常量.
+ 不使用class关键词，而使用interface关键词.



甚至可以这么说，接口类不允许有普通方法、普通变量和静态变量.

**接口类不使用class关键词来定义 ，而是使用interface关键词**，下面来演示一下：

```java
import java.util.Arrays;
interface Animal{
   
    public static  String type="Animal";
    default String getType() {
   
        return type;
    }
    public static void noThing() {
   
        System.out.println("I'm nothing.");
    }
    void speak();//普通方法会被自动变成public abstract修饰
}
```


接口的静态方法可以直接用 **类名.方法名 **访问：

```java
public class Kit {
   
	public static void main(String[] arg) {
   
		Animal.noThing();//I'm nothing.
	}
```


#### 




### Java的抽象类abstract


​ 只要含有抽象函数的类都是抽象类，抽象类不能被实例化。

抽象类和抽象函数用abstract修饰，下面是一个正确的例子：

```java
package test;

abstract class A {
	int a;
	public abstract void speak();
}

class B extends A {
	public void speak() {
		System.out.println("B speak");
	}
}

```


**下面注意两点：**

+ 用abstract修饰的函数没有函数体+ 抽象方法在子类中必须重写。否则就会报错+ 重写的方法不能用 default 修饰




### Java的final关键字


```bash
>引言
>
>Java中的final 与C++中的const 差不多，其代表修饰的变量不可改变。不过final 可以修饰类
```


final修饰有下面几种：

+ 修饰局部变量+ 修饰非局部变量+ 修饰函数+ 修饰类


#### 1.修饰局部变量


​ final修饰的局部变量是常量，只能赋值一次。

```java
public class Kit {
	public static void main(String[] arg) {
		final int a;
		a=10;//不能再修改了
		//a=100;//这里报错，初始化后的值不能被修改
        final int b=100;//不能再修改了
	}
}
```


#### 2.修饰非局部变量


​ 用final定义成员变量的必须对它进行初始化（也可以在构造函数中初始化），之后该变量的值不能被改变。

这是一个错误的示范：

```java
package test;
class A {
	int a;
	public final int PI;
	A(){};//errors:The blank final field PI may not have been initialized
	public String toString() {
		return "This class A of toString function";
	}
}
```


#### 3.修饰方法


​ 用final修饰的方法不能被子类重写。

```bash
>这里与c++稍有不同，c++中用const修饰成员函数不能修改该对象成员的值。
```


#### 4.修饰类


​ 用final修饰的类被称为最终类，该类不能被继承。比如String类



### Java中所有类的父类——非常重要的Object类。

​ 在Java中，所有的基类都有一个默认的父类，那就是Object类。Object类有下面几种方法

```java
boolean equals(Object obj);//判断某个对象与此对象是否相等
final Class<?> getClass()；//返回此Object的运行时类
int hashCode();//返回该对象的哈希码值
String toString();//返回该对象的字符串表示
void finalize();//垃圾回收器调用此方法来清理没有被任何引用变量所引用的资源
Object clone();//返回该对象的克隆
```


​ 在Object类中，这些函数需要我们重写才能达到相应的功能。下面以重载toString函数为例：


我们发现可以直接用System.out.println()输出自己的字符串表示。


```java
package test;
class A {
	int a;
	A(){};
	public String toString() {
		return "This class A of toString function";
	}
}

public class Kit {
	public static void main(String[] arg) {
		A aa = new A();
		System.out.println(aa);//输出 This class A of toString function
	}
}
```


另外Object的equals函数是判断两个对象是否引用的同一个对象，**更确切的说是变量引用的对象内存地址是否为相等，而不是比较他们的内容是否一样** 。
但是我们可以对equals函数进行重载，来达到我们的目的(判断对象的内容是否一样)。


这里需要注意的是’=='也是判断两个对象变量引用的对象是否相同，而不是比较他们的内容（或者你可以理解为对象变量里面存的都是引用对应的地址）




### Java中继承、类构造函数、方法重写，this以及super关键词。



Java与C++有很多相似之处,下面的概念有很多地方会跟c++牵扯在一起。，没有c++基础者慎重！


下面介绍四个部分

+  继承的概念以及语法 +  构造函数 +  方法重写 +  this关键字和super关键字 


### 1.继承的概念以及关键词


​ Java中继承与C++稍有不同，C++允许多继承，但**Java不允许**，**即Java只支持一个类最多有一个直接父类**。

与c++继承的概念相同，父类所拥有的函数和属性，子类同样具有，且子类可以增添加自己的函数。(不过会受访问权限的约束)
​Java中的继承的语法：

```java
[修饰符] class 子类名 extends 父类名{
    //类的内容
}
```


#####下面是继承的一个例子：

```java
package test;
class A{
	int a;
	public  void speak1() { System.out.println("A speak");};
}
class B extends A{
	public  void speak2() {	System.out.println("B speak");}
}
public class Kit{
	public static void main(String [] arg) {
		B bb=new B();
		bb.speak1();
		bb.speak2();
	}
}
```


### 2.构造函数

构造函数： 对象生成会直接（非语句调用）执行自己的构造函数，一般构造函数是对象进行初始化的操作；构造函数可以重载


这里需要注意的是构造函数里面**调用其他构造函数的语句**只能出现一次。


```java
package test;
class A{
	int a;
	A(){System.out.println("A 无参构造函数");}
	A(int a){ 
		this.a=a; 
		System.out.println("A  int 构造函数");
	}
	A(A b){this.a=b.a;
	System.out.println("A  class 构造函数");
	}
}
public class Kit{
	public static void main(String [] arg) {
		A aa=new A();//A 无参构造函数
		A bb=new A(10);//A  int 构造函数
		A cc=new A(bb);//A  class 构造函数
	}
}
```


注：与C++稍有不同，Java的类的无参构造函数在生成类时后面的 ‘()’ 不可以省略

比如C++类A为:

```cpp
#include<bits/stdc++.h>
using namespace std;
class A
{
public:
    int a;
    A()
    {
        puts("A 无参构造函数");
    }
    A(int a)
    {
        this->a=a;
        puts("A  int 构造函数");
    }
    A(const A &b)
    {
        this->a=b.a;
        puts("A  class 构造函数");
    }
};
int main(){
    A *aa=new A;//java 就需要A()。
    delete aa;
}

```



根据学了几门语言的经验，总是觉得Java的对象变量皆为指针（Python也相同）。


#### 3.子类可以重写父类方法

子类重写父类方法，那么原父类方法就会被覆盖，若想在子类中调用父类方法，可以用super关键词。

​

```java
package test;

 class A {
	int a;
	public void speak(){System.out.println("A speak");}
}

class B extends A {
	public void speak() {
		System.out.println("B speak");
		super.speak();
	}
}

public class Kit {
	public static void main(String[] arg) {
		B bb = new B();
		bb.speak();/*B speakA speak*/
	}
}
```


### 4.this关键字和super关键字


​ **this表示自身对象，在对象中可以用this访问自身的属性和方法** 。

```java
package test;
class A {
	int a;
	A(){};
	A(int a){this.a=a;}
	A(boolean a){
		this(a?1:0);
	}
	public void speak(){System.out.println("A speak");}
}
```


​ **super表示父类对象** ，**可以使用super访问父类的方法或属性** 。

想调用父类的构造函数？

不过super和this调用构造函数时候都只能出现在函数的第一个语句，否则就会编译错误。


你确实没看错，在构造函数中，super和this调用构造函数只**能出现其中一个**，若出现则必须出现在该**构造函数**的第一个语句。


例子：

```java
package test;
class A{
	int a;
	A(){System.out.println("A 无参构造函数");}
	A(int a){ 
		this.a=a; 
		System.out.println("A  int 构造函数");
	}
	A(A b){this.a=b.a;
	System.out.println("A  class 构造函数");
	}
}
class B extends A{
	B(){System.out.println("B 无参构造函数");};
	B(int a){
		super(a);
		//this(); 这里this()就会报错
	}
}
```




### 1. Java中关于类的修饰符


+  
##### 访问控制符。



与C++的访问控制符相似，Java中类的属性和方法都有访问权限的规定，且与C++意思相近。

当然，该类成员可以访问自己类的所有成员。访问级只对外部做出限制。


+ private（当前类访问级别）。相当于私有，被修饰的属性或者方法**不能被外部或者其他类访问。**+ default（包访问级别）。 默认的访问级别，**如果一个类或者类的成员不使用任何访问控制修饰**，则默认为包访问级别，被修饰的属性或者方法**只能被当前包下的类访问。**+ protected（子类访问级别）。被修饰的属性或者方法**只有该类子类才能访问。 **+ public（公共的访问级别）。被修饰的属性或者方法**外界类皆可访问** 。



思考总结：

一个类的访问控制符为 **子类**和**外部类** 限制了访问权限（仅此而已）
 +  
##### static修饰符号


+  **类中的成员**被static修饰。表示该成员只属于类，不属于任何对象。只有一份。

+ static修饰的方法只能访问static修饰的方法。(传参的对象的方法除外)+ static修饰的变量
 +  **类中代码块**被static修饰 。在类的加载过程中，会加载该代码块，因为类只会被加载一次，故静态代码块也只会被执行一次。 
```java
package test;

public class Kit {
	static {
		System.out.println("Kit的静态代码块");
	}
	static public void  main(String [] args) {
		System.out.println("THis-----");
		Kit kp=new Kit();
		
	}
}
/*输出：
Kit的静态代码块
THis-----
*/
```
 



思考总结：

与C++static的用法意义相同。 不过多了个static代码块的修饰
 


##2.面向对象的基本原则都有哪些？

​ 百度了一下有下面五个吧。引用的链接https://www.jianshu.com/p/e1de87625f43

+  单一职责原则（SRP） +  开放封闭原则（OCP） +  里氏替换原则（LSP） +  依赖倒置原则（DIP） +  接口隔离原则（ISP）


其实我没听懂太多，下面是我从中思考和以前的经验的理解：

1.类的设计要符合其根本意义，且不可随意的继承。

2.为了多态而实现的基类尽量作为抽象类。

3.类的方法接口尽量独立，出了依赖参数，不依赖其他可变的属性。
 


##3.对象的关系都有哪些？

+ 继承+ 封装




## 使用JAVA语言Swing进行GUI程序设计


在扫雷S项目的GUI设计中主要遇到了一下问题并且解决。


+ 怎么在JDIalog对象中添加组件
+ 怎么自定义容器中组件的位置和大小
+ 在设定了布局管理器的容器中怎么控制某一块的高度或者宽度
+ 怎么返回一个指定大小的ImageIcon对象
+ 怎么给按钮设置三种（四种状态的Icon）
+ 怎么给窗口设置半透明




注：大多数查找API文档和从网络论坛中查找较为方便


#### 1.怎么在JDIalog对象中添加组件


向对话框JDialog对象中组件只能通过添加一个JPanel，在JPanel中添加组件即可。


参考博客：[https://blog.csdn.net/xietansheng/article/details/75948933](https://blog.csdn.net/xietansheng/article/details/75948933)


```java
JFrame jf=new JFrame();
jf.setSize(1200,960);		
jf.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
JDialog dialog=new JDialog(jf);
dialog.setContentPane(contentPanel);
dialog.setVisible(true)
```



#### 2.怎么自定义容器中组件的位置和大小


如果一个容器使用的布局管理器为null，那么可以使用组件的setBounds(x,y,width,height)函数可以设置组件在容器中的位置

```java
JFrame jf=new JFrame();```


