Title: Markdown 语法说明
Date: 2016-01-13
Modified: 2016-5-14
Category: markdown
Tags: table
Summary: Markdown语法
Authors: muzeet

##概述##

###宗旨###
Markdown 的目标是实现「易读易写」。
  

###兼容 HTML###
Markdown 的理念是，能让文档更容易读、写和随意改。HTML 是一种发布的格式，Markdown 是一种书写的格式。就这样，Markdown 的格式语法只涵盖纯文本可以涵盖的范围。  

不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。不需要额外标注这是 HTML 或是 Markdown；只要直接加标签就可以了。  
要制约的只有一些 HTML 区块元素――`<div>`、`<table>`、`<pre>`、`<p>` 等标签，必须在前后加上空行与其它内容区隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。Markdown 的生成器有足够智能，不会在 HTML 区块标签外加上不必要的 `<p>` 标签。   

	这是一个普通段落。

	<table>
   	 <tr>
        <td>1</td>
		<td>2</td>
		<td>3</td>
     </tr>
	</table>

	这是另一个普通段落。   

效果：

这是一个普通段落。

<table>
    <tr>
        <td>1</td>
		<td>2</td>
		<td>3</td>
    </tr>
</table>

这是另一个普通段落。

1.在 HTML 区块标签间的 Markdown 格式语法将不会被处理  
2.HTML 的区段（行内）标签如`<span>`、`<cite>`、`<del>` 可以在 Markdown 的段落、列表或是标题里随意使用。依照个人习惯，甚至可以不用 Markdown 格式，而直接采用 HTML 标签来格式化。举例说明：如果比较喜欢 HTML 的 `<a>` 或 `<img>` 标签，可以直接使用这些标签，而不用 Markdown 提供的链接或是图像标签语法。

###特殊字符自动装换###

在 HTML 文件中，有两个字符需要特殊处理： < 和 &,显示这些字符的原型必须使用实体形式： `&lt;` 和 `&amp;`  
markdown中，如果使用的 & 字符是 HTML 字符实体的一部分，它会保留原状，否则它会被转换成 `&amp;`

版权符号 ©：`&copy;`

code范围内，不论是行内还是区块， < 和 & 两个符号都一定会被转换成 HTML 实体

***

##区块元素##

###段落和换行###

一个 Markdown 段落是由一个或多个连续的文本行组成，它的前后要有一个以上的空行（空行的定义是显示上看起来像是空的，便会被视为空行。比方说，若某一行只包含空格和制表符，则该行也会被视为空行）。普通段落不该用空格或制表符来缩进。

「由一个或多个连续的文本行组成」这句话其实暗示了 Markdown 允许段落内的强迫换行（插入换行符）

依赖markdown来插入`</br>`换行符。两个以上的空格+回车

一个以上的空行和两个以上的空格+回车区别：一个以上空行是表示不同段落，空格加回车是表示同一个段落中的换行，前者间距更大。

###标题###
Markdown 支持两种标题的语法，类 Setext 和类 atx 形式。

类 Setext 形式是用底线的形式，利用 = （最高阶标题）和 - （第二阶标题），任何数量的 = 和 - 都可以有效果。例如：

	H1
	======

	H2
	------

效果：

H1标题
====

H2标题
---


类 Atx 形式则是在行首插入 1 到 6 个 # ，对应到标题 1 到 6 阶，例如：

	# 这是 H1标题

	## 这是 H2标题

	###### 这是 H6标题

效果：
# 这是 H1标题 #

## 这是 H2标题 ##

###### 这是 H6标题 ######
***

###区块引用 Blockquotes###

Markdown 标记区块引用是使用类似 email 中用 > 的引用方式。

在每行的最前面加上 >：  
	
	>区块引用  
	>
	>任然是区块引用  
	>
	>还是区块引用
	>


>区块引用    
>
>任然是区块引用  
>
>还是区块引用
>

区块引用中表示不同段落：空格+回车

Markdown 只在整个段落的第一行最前面加上 > ：

	> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
	consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.

	> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
	id sem consectetuer libero luctus adipiscing.

区块引用可以嵌套（例如：引用内的引用），只要根据层次加上不同数量的 > ：

	>第一级别的区块引用
	>
	>>第二级的区块引用  
	>
	>>第二级的区块引用
	>
	>回到第一级别的区块引用

>第一级别的区块引用
>
>>第二级的区块引用  
>
>>第二级的区块引用
>
>回到第一级别的区块引用

引用的区块内也可以使用其他的 Markdown 语法，包括标题、列表、代码区块等：

	>## 这是一个标题。##
	>
	>列表: 
	>
	>1.   这是第一行列表项。
	>2.   这是第二行列表项。
	> 
	>给出一些例子代码：
	> 
	>     return shell_exec("echo $input | $markdown_script");

>## 这是一个标题。##
>
>列表: 
>
>1.   这是第一行列表项。
>2.   这是第二行列表项。
> 
>给出一些例子代码：
> 
>     return shell_exec("echo $input | $markdown_script");

###列表###

Markdown 支持有序列表和无序列表。



无序列表使用**\*** 、**+** 或是 **-** 作为列表标记（标记与列表名称有一个以上空格）：

	* 第一行
	* 第二行
	* 第三行

*  第一行
*  第二行
*  第三行



有序列表则使用数字接着一个英文句点：（数字句点与文字之间至少一个空格）

	1.  Bird
	2.  McHale
	3.  Parish
	
1.  Bird
2.  McHale
3.  Parish





列表项目标记(* 或者 1.)通常是放在最左边，但是其实也可以缩进，最多 3 个空格，项目标记(* 或者 1.)后面则一定要接着至少一个空格或制表符。




如果列表项目间用空行分开，在输出 HTML 时 Markdown 就会将项目内容用 `<p>` 标签包起来：

	*   Bird
	
	*   Magic

会被转换为：

	<ul>
	<li><p>Bird</p></li>
	<li><p>Magic</p></li>
	</ul>





列表项目可以包含多个段落（多个段落用一个以上空行），每个项目下的段落都必须缩进 4 个空格或是 1 个制表符：(一个以上空行+下面段落的每一行首部缩进4个空格)

1.  This is a list item with two paragraphs. Lorem ipsum 	dolor sit amet,
	consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.  

    Vestibulum enim wisi, viverra nec, fringilla in laoreet vitae, 
	risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.





列表项目中存在引用:（4个空格 or 1个制表符）

	*   A list item with a blockquote:
    	> This is a blockquote
    	> inside a list item.
	*   Another

*   A list item with a blockquote

    > This is a blockquote
    > inside a list item.
    > 
*   Another



列表项目中存在代码区块:(8个空格 or 2个制表符)

	*   一列表项包含一个列表区块：

 	       <代码写在这>


*   一列表项包含一个列表区块：

        <代码写在这>




列表项首说出现数字-句点-空白，原样显示:句点前面加上反斜杠。

	code:
	1.	一列表项包含数字-句点-空白。

		1986\.  What a great season
		
		1987\.  what a shame  

	2.	一列表项包含数字-句点-空白	


不加\ 效果:

1.	一列表项包含数字-句点-空白。

	1986.  What a great season
	
	1987.  what a shame  

2.	一列表项包含数字-句点-空白

加\ 效果:

1.	一列表项包含数字-句点-空白。

	1986\.  What a great season
	
	1987\.  what a shame  

2.	一列表项包含数字-句点-空白


列表项中又存在列表项：

只需要在列表项中继续加列表项标记，前面加4个空格或者制表符。

***

###代码区块###

Markdown 会用 `<pre>` 和 `<code>` 标签来把代码区块包起来。

标记为代码区块：缩进 4 个空格或是 1 个制表符。一直持续到没有缩进的那一行（或是文件结尾）

    这是一个普通段落：
	
    	这是一个代码区块。

Markdown 会转换成：

	<p>这是一个普通段落：</p>

	<pre><code>这是一个代码区块。
	</code></pre>

java `main()`：

	public static void main(String[] args){
		
	}


在代码区块里面， & 、 < 和 > 会自动转成 HTML 实体

 	<div class="footer">
        &copy; 2004 Foo Corporation
    </div>

会被转换为：

	<pre><code>&lt;div class="footer"&gt;
 	   &amp;copy; 2004 Foo Corporation
	&lt;/div&gt;
	</code></pre>


###分隔线###

在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。可以在星号或是减号中间插入空格。

	* * * 

	---

	___


* * * 

---

___



##区段元素##

###链接###

Markdown 支持两种形式的链接语法： 行内式和参考式两种形式。不管是哪一种，链接文字都是用 [方括号] 来标记。


*	行内式链接：只要在方块括号后面紧接着圆括号并插入网址链接即可，如果你还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可。
	
		这是链接到[百度](http://www.baidu.com/ "百度")的链接.

		这是链接到[百度](http://www.baidu.com/)的无title属性链接.

	这是链接到[百度](http://www.baidu.com/ "百度")的链接.

	这是连接到[百度](http://www.baidu.com/)的无title属性链接.

*	参考式：链接文字的括号后面再接上另一个方括号，而在第二个方括号里面要填入用以辨识链接的标记

		这是链接到[百度][baidu]的参考式链接.

	这是链接到[百度][baidu]的参考式链接.

	你也可以选择性地在两个方括号中间加上一个空格：

		这是链接到[百度] [baidu]的参考式链接.
	这是链接到[百度] [baidu]的参考式链接.

	接着，在文件的任意处，你可以把这个标记的链接内容定义出来：
		
		[baidu]:http://www.baidu.com "百度"

	[baidu]:http://www.baidu.com "百度"

	链接内容定义的形式为：

	*	方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字
	*	接着一个冒号
	*	接着一个以上的空格或制表符
	*	接着链接的网址
	*	选择性地接着 title 内容，可以用单引号、双引号或是括弧包着

	下面这三种链接的定义都是相同：

		[foo]: http://example.com/  "Optional Title Here"
		[foo]: http://example.com/  'Optional Title Here'
		[foo]: http://example.com/  (Optional Title Here)
	
	链接网址也可以用尖括号包起来

		[id]: <http://example.com/>  "Optional Title Here"

	可以把 title 属性放到下一行，也可以加一些缩进，若网址太长的话

		[id]: http://example.com/longish/path/to/resource/here
   		 "Optional Title Here"
		
	链接辨别标签可以有字母、数字、空白和标点符号，但是并不区分大小写，因此下面两个链接是一样的：

		[link text][a]
		[link text][A]

	隐式链接标记功能让你可以省略指定链接标记，这种情形下，链接标记会视为等同于链接文字，要用隐式链接标记只要在链接文字后面加上一个空的方括号:

		[Google][]
	[Google][]

	然后定义链接内容：

		[Google]: http://google.com/

	[Google]: http://google.com/

	
*	下面是一个参考式链接的范例：

		I get 10 times more traffic from [Google] [1] 
		than from [Yahoo] [2] or [MSN] [3].

  		[1]: http://google.com/        "Google"
 	 	[2]: http://search.yahoo.com/  "Yahoo Search"
  		[3]: http://search.msn.com/    "MSN Search"

	下面是用行内式写的同样一段内容的 Markdown 文件，提供作为比较之用：

		I get 10 times more traffic from 
		[Google](http://google.com/ "Google")
		than from 
		[Yahoo](http://search.yahoo.com/ "Yahoo Search" 
		or
		[MSN](http://search.msn.com/ "MSN Search").


###强调###

Markdown 使用星号（*）和底线（_）作为标记强调字词的符号，被 * 或 _ 包围的字词会被转成用 `<em>` 标签包围，用两个 * 或 _ 包起来的话，则会被转成 `<strong>`，例如：

	*single asterisks*

	_single underscores_

	**double asterisks**

	__double underscores__

会转成：

	<em>single asterisks</em>

	<em>single underscores</em>

	<strong>double asterisks</strong>

	<strong>double underscores</strong>

*single asterisks*

_single underscores_

**double asterisks**

__double underscores__



**如果你的 \* 和 _ 两边都有空白的话，它们就只会被当成普通的符号，表示强调的 \* 和 _ 之间不能有空格。**

	叫号机** 哈哈 **

叫号机* 哈哈 *  
叫号机** 哈哈 **



如果要在文字前后直接插入普通的星号或底线，你可以用反斜线：
**this is text**，注意反斜线要匹配。

		
		this \**is\** text

		this \*\*is\*\* text

		\*this **is** text\*

this \**is*\* text

this \*\*is\*\* text

\*this **is** text\*


###代码###

如果要标记一小段行内代码，你可以用反引号把它包起来（`），例如：

	Use the `printf()` function.
Use the `printf()` function.

会产生：

	<p>Use the <code>printf()</code> function.</p>



如果要在代码区段内插入反引号，你可以用多个反引号来开启和结束代码区段：

	``There is a literal backtick (`) here.``
这段语法会产生：

	<p><code>There is a literal backtick (`) here.</code></p>

``There is a literal backtick (`) here.``


代码区段的起始和结束端都可以放入一个空白，起始端后面一个，结束端前面一个，这样你就可以在区段的一开始就插入反引号：

	A single backtick in a code span: `` ` ``

	A backtick-delimited string in a code span: `` `foo` ``
	
	`` ` ``,开始出插入反引号

A single backtick in a code span: `` ` ``

A backtick-delimited string in a code span: `` `foo` ``

`` ` ``,开始出插入反引号


在代码区段内，& 和尖括号都会被自动地转成 HTML 实体，这使得插入 HTML 原始码变得很容易

	Please don't use any `<blink>` tags.
Please don't use any `<blink>` tags.

转为：

	<p>Please don't use any <code>&lt;blink&gt;
	</code> tags.</p>


###图片###
Markdown 使用一种和链接很相似的语法来标记图片，同样也允许两种样式： 行内式和参考式。

* 行内式的图片语法

		![Alt text](/path/to/img.jpg)

		![Alt text](/path/to/img.jpg "Optional title")

	详细叙述如下：

	*	一个惊叹号 !
	*	接着一个方括号，里面放上图片的替代文字
	*	接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上 选择性的 'title' 文字。

* 参考式的图片语法

		![Alt text][id]

		「id」是图片参考的名称，图片参考的定义方式则和连结参考一样：
		[id]: url/to/image  "Optional title attribute"
 
行内式：
![qiniu](http://7xq1t9.com1.z0.glb.clouddn.com/night_dribbble.gif "行内式")

参考式：
![七牛][qiniu]
[qiniu]:http://7xq1t9.com1.z0.glb.clouddn.com/night_dribbble.gif "参考式"

**Markdown 还没有办法指定图片的宽高，如果你需要的话，你可以使用普通的 `<img>` 标签。**


##其他##

###自动链接###

Markdown 支持以比较简短的自动链接形式来处理网址和电子邮件信箱，只要是用尖括号包起来， Markdown 就会自动把它转成链接。

网址：

	<http://example.com/>
<http://example.com/>

Markdown 会转为：

	<a href="http://example.com/">http://example.com/</a>

电子邮箱：

邮址的自动链接也很类似，只是 Markdown 会先做一个编码转换的过程，把文字字符转成 16 进位码的 HTML 实体，这样的格式可以糊弄一些不好的邮址收集机器人，例如：

	<address@example.com>
<address@example.com>

Markdown 会转成：

	<a href="&#x6D;&#x61;i&#x6C;&#x74;&#x6F;:&#x61;&#x64;&#x64;&#x72;&#x65;
	&#115;&#115;&#64;&#101;&#120;&#x61;&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;
	&#109;">&#x61;&#x64;&#x64;&#x72;&#x65;&#115;&#115;&#64;&#101;&#120;&#x61;
	&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;&#109;</a>

在浏览器里面，这段字串（其实是 `<a href="mailto:address@example.com">address@example.com</a>`）会变成一个可以点击的「address@example.com」链接。


###反斜杠###

Markdown 可以利用反斜杠来插入一些在语法中有其它意义的符号。

Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

	\   反斜线
	`   反引号
	*   星号
	_   底线
	{}  花括号
	[]  方括号
	()  括弧
	#   井字号
	+   加号
	-   减号
	.   英文句点
	!   惊叹号