from typing import List, Dict


class TreeNode:
    """ 二叉树节点 """

    def __init__(self, data: any):
        self.__data = data
        self.__left = None  # 左子树
        self.__right = None  # 右子树

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: any):
        self.__data = data

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
            huff_root_weight = huff_left.data + huff_right.data
            huff_root = HuffmanTree(huff_root_weight)
            huff_root.left = huff_left
            huff_root.right = huff_right
            # 将新创建的二叉树节点添加到查找范围内，同时确保节点列表有序
            for index, node in enumerate(huffNodes):
                if node.data <= huff_root.data:
                    huffNodes.insert(index, huff_root)
                    break
                elif index == len(huffNodes) - 1:  # 如果没有比此root节点小的数据，直接将此节点添加到最后
                    huffNodes.append(huff_root)
                    break  # 注意break，不然还会循环一次而两次插入节点
        return huff_root

    @staticmethod
    def createHuffmanCode(weight_str: Dict) -> Dict:
        """
        生成一颗Huffman树，由于所有带权重的节点都是叶子节点，
        所以从根节点递归遍历此哈夫曼树，遇到左子树编码+'0'，
        遇到右子树编码+'1'，得到每个叶子节点的编码
        :param weight_str: (int -> str) 比重和对应字符的字典
        :return str_code: (str -> str) 字符和对应编码的字典
        """
        weights = list(weight_str.keys())  # 获取所有比重值
        root_huffman = HuffmanTree.createHuffmanTree(weights)  # 构建huffman树

        # 遍历每个叶子节点，生成对应编码
        str_code = {}

        # 先序遍历哈夫曼树生成哈夫曼编码，左子树编码+'0'，右子树编码+'1'
        def code_generater(tree: HuffmanTree, code: str = ""):
            if tree.left is None:  # 哈夫曼树中的非叶子节点左右子树都不为None
                weight = tree.data
                str_code[weight_str.get(weight)] = code
                return
            code_generater(tree.left, code + "0")
            code_generater(tree.right, code + "1")

        code_generater(root_huffman)
        return str_code


class BinarySearchTree:
    """
    二叉搜索树（Binary Search Tree）：又称二叉排序树，有如下性质：
    若它的左子树不空，则左子树上所有的节点的值均小于它的根节点，
    若它的右子树不空，则右子树上所有的节点的值均大于它的根节点；
    它的左、右子树也分别为二叉搜索树。
    每次操作的时间复杂度为O(logn)，和树的高度成正比
    """

    def __init__(self):
        self.__root = TreeNode(None)

    def search(self, data: any) -> bool:
        """
        查找数据是否存在
        :param data: 数据
        :return: True - 数据存在，False - 数据不存在
        """
        node = self.__root
        while node:
            node_data = node.data
            if node_data == data:
                return True
            elif node_data < data:
                node = node.right
            else:
                node = node.left
        return False

    def insert(self, data: any) -> any:
        """
        插入数据，如果有重复数据则忽略
        :param data: 数据
        :return: 成功插入则返回data，有重复数据返回 None
        """
        node = self.__root
        if node.data is None:  # 整颗树为空
            node.data = data
            return data
        while node:
            node_data = node.data
            if node_data == data:
                return None
            elif node_data < data:
                if node.right:
                    node = node.right
                else:  # 直到右子树为空时，构造节点插入到此节点的右子树
                    node.right = TreeNode(data)
                    return data
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(data)
                    return data
        return None

    def delete(self, data: any) -> any:
        """
        删除数据
        :param data: 数据
        :return: 如果删除成功，返回此数据，如果无此数据，返回None
        """
        ######## 非递归实现 #######
        pre_node = None  # 前驱节点
        node = self.__root
        left_side = None  # 当前节点为父节点的左节点？
        while node:
            node_data = node.data
            if node_data == data:  # 找到节点位置
                data_node = node
                if (data_node.left is not None) & (data_node.right is not None):
                    # 节点的度为2，从此节点的左子树中选出一个最大值的节点替换此节点
                    left_max_node: TreeNode = data_node.left
                    pre_left_max_node: TreeNode = data_node  # 前驱节点
                    while left_max_node.right:
                        pre_left_max_node, left_max_node = left_max_node, left_max_node.right
                    left_max_node_left = left_max_node.left  # 最大节点的左节点
                    # 将data_node替换成left_max_node
                    data_node.data = left_max_node.data
                    # 删除left_max_node, 此节点无右子树，且有前驱节点
                    if left_max_node == data_node.left:  # 左节点
                        pre_left_max_node.left = left_max_node_left
                        left_max_node.left = None
                    else:
                        # 左节点的右子树
                        pre_left_max_node.right = left_max_node_left
                        left_max_node.left = None
                    #
                elif (data_node.left is not None) | (data_node.right is not None):
                    # 节点的度为1，直接将子节点移到本节点
                    node_child = data_node.left if data_node.left else data_node.right
                    if pre_node:
                        #  子节点替换本节点
                        if left_side:
                            pre_node.left = node_child
                        else:
                            pre_node.right = node_child
                    else:  # 根节点为要删除的节点
                        self.__root = node_child  # 无前驱节点时不能使用left_side标记判断
                    data_node.left, data_node.right, data_node.data = None, None, None  # 释放节点资源
                else:
                    # 节点的度为0，直接删除本节点
                    data_node.data = None
                    if pre_node:  # 有前驱节点，即本节点不是根节点
                        if left_side:  # 判断是前驱节点的左节点还是右节点
                            pre_node.left = None
                        else:
                            pre_node.right = None
                break
            elif node_data < data:  # 向右遍历
                pre_node = node
                node = node.right
                left_side = False
            else:  # 向左遍历
                pre_node = node
                node = node.left
                left_side = True
        return None

    def traversal(self):
        self.__traversal(self.__root)
        print()

    def __traversal(self, node: TreeNode):
        if not node:
            return
        self.__traversal(node.left)
        print(node.data, end='  ')
        self.__traversal(node.right)


def createBinarySearchTree(datas: []) -> BinarySearchTree:
    tree = BinarySearchTree()
    for data in datas:
        tree.insert(data)
    return tree


if __name__ == '__main__':
    def LDR_traversal(root: TreeNode, fn):
        """
        中序遍历二叉树
        :param fn:
        :param root: 二叉树根节点
        """
        if root:
            LDR_traversal(root.left, fn)
            fn(root.data)
            LDR_traversal(root.right, fn)


    huffman_weight = [[5, 7, 2, 13], [7, 5, 2, 4], [7, 19, 2, 6, 32, 3, 21, 10], [13, 7, 8, 3, 29, 6, 1],
                      [3, 12, 7, 4, 2, 8, 11]]
    for weighted in huffman_weight:
        huffmane_tree = HuffmanTree.createHuffmanTree(weighted)
        LDR_traversal(huffmane_tree, lambda node: print(node, end="\t"))
        print("\r\n===================== next>>>>>>")
    weight_char = {6: "A", 3: "B", 8: "C", 2: "D", 10: "E", 4: "F"}
    print(HuffmanTree.createHuffmanCode(weight_char))
    print("==================  二叉搜索树 >>>>>>>")
    arr = [5, 3, 4, 0, 2, 1, 8, 6, 9, 7]
    bst = createBinarySearchTree(arr)
    for x in arr[::-1]:
        print("after delete", x, end=",BST in-order is = ")
        bst.delete(x)
        bst.traversal()
        print()
    arr1 = [20, 9, 8, 15, 12, 13, 11, 23]
    bst1 = createBinarySearchTree(arr1)
    bst1.delete(20)
    bst1.traversal()
    bst1.delete(9)
    bst1.traversal()
    bst1.delete(8)
    bst1.traversal()
    bst1.delete(11)
    bst1.traversal()
    bst1.delete(15)
    bst1.traversal()
