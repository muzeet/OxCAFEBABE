Title: 代码高亮（pygment）
Date: 2017-07-01
Modified: 2017-07-01
Category: 博客设计
Tags: 代码高亮
Slug:Test-Code-Highlight-by-pygment
Authors: muzeet
Summary: 使用pygment进行代码高亮处理。

##1. 测试code block ##
下面是一段代码，代码使用pygment进行高亮处理。

求二叉树的第k个节点：

	public class KthNode
    {
		 public TreeNode kthNode(TreeNode pRoot, int k)
		 {
	        //求二叉排序树的第k个节点，只需要中序遍历，即可
	        if(pRoot == null || k < 1)
	            return null;
	        Stack<TreeNode> stack = new Stack<TreeNode>();
	        TreeNode p = pRoot;
	        TreeNode kthNode = null;
	        int count = 0;
	        while(p != null || !stack.empty() && count !=k ){
	            if(p != null){
	                stack.push(p);
	                p = p.left;
	            }
	            else{
	               p = stack.pop();
	               count++;
	               if(count == k)
	                   kthNode = p;
	               p = p.right;
	            }
	        }
	        return kthNode;
		 }
    }
