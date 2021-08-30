from typing import Callable

from treestruct import TreeNode


# 求二叉树的度
def degreeOfTree(root: TreeNode) -> int:
    if root:
        # 递归求左子树的度
        leftDegree = degreeOfTree(root.left)
        # 递归求右子树的度
        rightDegree = degreeOfTree(root.right)
        # 取两边度较大的一个
        return max(leftDegree + 1, rightDegree + 1)
    else:
        return 0


def searchOfTree(root: TreeNode, data: any) -> bool:
    if root:
        if root.data() == data:
            return True
        return searchOfTree(root.left, data) or searchOfTree(root.right, data)
    else:
        return False


def LDR_traversal(root: TreeNode, fn: Callable):
    """
    中序遍历二叉树
    :param fn: 节点数据处理函数
    :param root: 二叉树根节点
    """
    if root:
        LDR_traversal(root.left, fn)
        fn(root.data())
        LDR_traversal(root.right, fn)


if __name__ == '__main__':
    print("开始求二叉树的度。。。。。。。。。。。")
    tree_node = TreeNode(1)
    l1 = TreeNode(2)
    r1 = TreeNode(5)
    l1l = TreeNode(3)
    l1r = TreeNode(4)
    tree_node.left = l1
    tree_node.right = r1
    l1.left = l1l
    l1.right = l1r
    print("二叉树的度是 %s" % degreeOfTree(tree_node))
    print("二叉树搜索数据4 %s" % searchOfTree(tree_node, 4))
