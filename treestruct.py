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
