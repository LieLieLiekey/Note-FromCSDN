

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


