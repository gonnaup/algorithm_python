from typing import List


class TreeNode:
    """ 二叉树节点 """

    def __init__(self, data: any):
        self.__data = data
        self.__left = None  # 左子树
        self.__right = None  # 右子树

    def data(self):
        return self.__data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    def __str__(self):
        return "data = " + str(self.__data)


class HuffmanTree(TreeNode):
    """
    哈夫曼树（Huffman Tree）：又叫最优二叉树，指一组具有确定权值的叶子节点的具有最小帯权路径长度（WPL）的二叉树。
    树的帯权路径长度：树中所有叶子节点的帯权路径长度之和就是树的帯权路径长度WPL(weighted path length)
    """

    """
    构造步骤：
    1. 首先根据n个有权值的节点构造n棵单节点二叉树，将权值保存在根节点中，其左右子树均为空
    2. 在这n棵单节点二叉树中找出两棵根节点权值最小的树，用这两棵树作为左右子树构造一颗新的
        二叉树，将左右子树的根节点的权值相加作为新二叉树根节点的权值。
    3. 将上一步找到的两棵权值最小的二叉树排查在下次查找的范围之外，将新创建的二叉树添加到查找范围之内。
    4. 重复步骤2和步骤3，直到查找范围只剩下一颗树为止
    """

    @staticmethod
    def createHuffmanTree(weighteds: List[int]):
        lenght = len(weighteds)
        if lenght == 0:
            raise AttributeError("构造哈夫曼树时权重列表不能为空！")
        if lenght == 1:
            return HuffmanTree(weighteds[0])
        weighteds.sort(reverse=True)  # 将权重从大到小排序
        huffNodes = list(map(lambda weight: HuffmanTree(weight), weighteds))  # 生成单节点二叉树
        huff_root = None
        while len(huffNodes) >= 2:
            # 弹出两个最小权重的单节点二叉树组成成一颗新的二叉树
            huff_left = huffNodes.pop()
            huff_right = huffNodes.pop()
            huff_root_weight = huff_left.data() + huff_right.data()
            huff_root = HuffmanTree(huff_root_weight)
            huff_root.left = huff_left
            huff_root.right = huff_right
            # 将新创建的二叉树节点添加到查找范围内，同时确保节点列表有序
            for index, node in enumerate(huffNodes):
                if node.data() <= huff_root.data():
                    huffNodes.insert(index, huff_root)
                    break
                elif index == len(huffNodes) - 1:  # 如果没有比此root节点小的数据，直接将此节点添加到最后
                    huffNodes.append(huff_root)
                    break  # 注意break，不然还会循环一次而两次插入节点
        return huff_root


if __name__ == '__main__':
    def LDR_traversal(root: TreeNode, fn):
        """
        中序遍历二叉树
        :param fn:
        :param root: 二叉树根节点
        """
        if root:
            LDR_traversal(root.left, fn)
            fn(root.data())
            LDR_traversal(root.right, fn)


    huffman_weight = [[5, 7, 2, 13], [7, 5, 2, 4], [7, 19, 2, 6, 32, 3, 21, 10], [13, 7, 8, 3, 29, 6, 1],
                      [3, 12, 7, 4, 2, 8, 11]]
    for weighted in huffman_weight:
        huffmane_tree = HuffmanTree.createHuffmanTree(weighted)
        LDR_traversal(huffmane_tree, lambda node: print(node))
        print("===================== next>>>>>>")
