

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

