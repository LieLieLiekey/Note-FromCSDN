## Java中的接口类.

## begin 接口类的简单介绍.

​	如果一个抽象类中的所有方法都是抽象的，则可以把他定义为接口类。

接口类只能做两个事情：

1. 在主函数调用接口类的静态方法或者静态常量.

2. 其他类实现该接口.

   ## 1.接口类定义的规则:

在JDk8.0往后的版本中，接口类不止可以有抽象方法，还可以有静态方法和默认方法，即下面几种

1. 抽象方法（abstrat）.
2. 静态方法（static）.
3. 默认方法（default）.
4. 静态常量.
5. 不使用class关键词，而使用interface关键词.

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

### 	2.接口类的实现

**实现接口类不用extends关键词，而是用implements关键词**，且一个类可以同时实现多个接口，接口名之间用逗号隔开。即需要注意下列几个问题

1. 一个类可同时实现多个接口.
2. 实现接口用implements关键词.
3. 接口的抽象函数在子类中必须都得实现.

下面以Dog类实现接口类Animal为例：

```java
package test;
interface Animal{
	public static  String type="Animal";
	default String getType() {
		return type;
	}
	public static void noThing() {
		System.out.println("I'm nothing.");
	}
	void speak();
}
interface LandAnimal{
	void run(String name);
}
class Dog implements Animal,LandAnimal{
	 public void speak() {
		System.out.println("I'm dog.");
	}
	 public void run(String name) {
		 System.out.println("Dog running.");
	 }
}
public class Kit {
	public static void main(String[] arg) {
		Dog dog=new Dog();
		dog.speak();
		dog.run("Dog");
        /*
        I'm dog.
		Dog running.
        */
	}
}
```

## 	3.关于接口类的其他方面

1. 一个接口类可同时继承多个接口类(其他普通类只能有一个直接父类).
2. 一个普通类可以同时继承普通类和多个接口类

Example One：

```java
package test;
interface Animal{
	public static  String type="Animal";
	default String getType() {
		return type;
	}
	public static void noThing() {
		System.out.println("I'm nothing.");
	}
	void speak();
}
interface LandAnimal{
	void run(String name);
}
interface EndAnimal extends Animal,LandAnimal{
	static void output() {
		System.out.println("This Methon of EndAnimal.");
	}
}
public class Kit {
	public static void main(String[] arg) {
		EndAnimal.output();//This Methon of EndAnimal.
	}
}

```

Example Two:

```java
package test;
interface Animal{
	public static  String type="Animal";
	default String getType() {
		return type;
	}
	public static void noThing() {
		System.out.println("I'm nothing.");
	}
	void speak();
}
interface LandAnimal{
	void run(String name);
}
interface EndAnimal extends Animal,LandAnimal{
	static void output() {
		System.out.println("This Methon of EndAnimal.");
	}
}
class Dog extends Object implements Animal,LandAnimal{
	 public void speak() {
		System.out.println("I'm dog.");
	}
	 public void run(String name) {
		 System.out.println("Dog running.");
	 }
}
```
