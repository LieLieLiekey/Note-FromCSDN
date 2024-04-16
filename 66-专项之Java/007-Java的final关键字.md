

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

