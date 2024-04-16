

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


