def hanoi_move(n, x, y, z):
    """
    汉诺塔问题，主要使用分治和递推算法思想
    表示将n个金盘从x柱移动到z柱
    """
    if n == 1:
        # 只有一个盘时，直接 x -> z
        print("%s -> %s" % (x, z))
        return

    # 先将(n-1)个盘从x -> y
    hanoi_move(n - 1, x, z, y)
    # 将第n个从x -> z
    print("%s -> %s" % (x, z))
    # 再讲(n - 1)个从y -> z
    hanoi_move(n - 1, y, x, z)


if __name__ == '__main__':
    print("=================== 汉诺塔问题开始 =================>>>>")
    hanoi_move(5, 'A', 'B', 'C')
    print("=================== 汉诺塔问题结束 =================>>>>")
