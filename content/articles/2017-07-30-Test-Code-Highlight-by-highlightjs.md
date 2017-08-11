Title: 测试代码高亮
Date: 2016-06-06
Modified: 2016-06-07
Category: Code
Tags: code
Authors: muzeet
Summary: 测试代码高亮by highlight.js。


highlight.js设置代码高亮

	<pre>
	<code class="java">
	public class HelloWorld {
	    /**
	    * 输出一行字符串“Hello World!”
	    * @param args
	    */
	    public static void main(String[] args) {
	         System.out.println("Hello World!");
	    }
	}
	</code>
	</pre>

pygments+pelican插件better_codeblock_line_numbering

：：：+语言，可以选择不同语言高亮

	:::java Thisisajava http://www.muzeet.cn/cn link
	public class HelloWorld {
    /**
    * 输出一行字符串“Hello World!”
    * @param args
    */
    public static void main(String[] args) {
         System.out.println("Hello World!");
    }
	}
