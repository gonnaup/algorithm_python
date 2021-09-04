import random

from algorithm_util import Stopwatch
from divide_and_conque.merge_sort import merge_sort as _merge_sort


def __sortedCheck(arr: []) -> bool:
    """
    检查数组是否已经排序，从小到达
    """
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def selection_sort(arr: []):
    """
    选择排序：遍历数组，每次都找到剩余段数组中的最小值和当前索引的值交换
    O(n^2)
    """
    lenght = len(arr)
    for i in range(lenght):
        index_min = i
        for j in range(i + 1, lenght):
            if arr[index_min] > arr[j]:
                index_min = j
        arr[i], arr[index_min] = arr[index_min], arr[i]  # 将最小值与当前值交换
        i += 1


def insertion_sort(arr: []):
    """
    将当前数字插入到前段数组的合适位置，对有序数组排序时时间是线性的
    只适合小规模的部分有序数组
    O(n^2)
    :param arr:
    :return:
    """
    lenght = len(arr)
    for i in range(1, lenght):
        j = i
        value = arr[i]
        while j > 0 and value < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = value


def shell_sort(arr: []):
    """
    希尔排序：基于插入排序的快速排序算法。
    使数组中任意间隔为h的元素都是有序的，（如果h很大，我们就能将元素移动到很远的地方，
    而不是像插入排序一样每次只能移动一步）然后缩小h的值，直到h的值为1，此时进行一次直接
    插入排序，使整个数组有序（此时数组基本有序，比较的次数大大减少）
    无法确定具体的时间复杂度，经测试接近O(NlogN)
    :param arr:
    :return:
    """
    length = len(arr)
    step = 3  # 三等分数组
    h = 1
    while h < length // step:
        h = step * h + 1  # 使用3^n + 1序列
    while h >= 1:
        for i in range(h, length):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j], arr[j - h] = arr[j - h], arr[j]
                j -= h
        h = h // step


def merge_sort(arr: []):
    _merge_sort(arr)


if __name__ == '__main__':
    _arr = []
    for idx in range(80000):
        _arr.append(random.randint(1, 100000))
    print("数组长度 %s" % str(len(_arr)))
    arr_default = _arr.copy()
    watcher_default = Stopwatch()
    arr_default.sort()
    time_default = watcher_default.stop()
    print("python自带排序花费%dms，" % time_default, end="数组已排序\r\n" if __sortedCheck(arr_default) else "数组未排序XXXXXXXXXXXXXX\r\n")

    # arr_selection = _arr.copy()
    # watcher_selection = Stopwatch()
    # selection_sort(arr_selection)
    # time_selection = watcher_selection.stop()
    # print("选择排序花费%dms，" % time_selection, end="数组已排序\r\n" if __sortedCheck(arr_selection) else "数组未排序XXXXXXXXXXXXXX\r\n")
    #
    # arr_insertion = _arr.copy()
    # watcher_insertion = Stopwatch()
    # insertion_sort(arr_insertion)
    # time_insertion = watcher_insertion.stop()
    # print("插入排序花费%dms，" % time_insertion, end="数组已排序\r\n" if __sortedCheck(arr_insertion) else "数组未排序XXXXXXXXXXXXXX\r\n")

    arr_shell = _arr.copy()
    watcher_shell = Stopwatch()
    shell_sort(arr_shell)
    time_shell = watcher_shell.stop()
    print("希尔排序花费%dms，" % time_shell, end="数组已排序\r\n" if __sortedCheck(arr_shell) else "数组未排序XXXXXXXXXXXXXX\r\n")

    arr_merge = _arr.copy()
    watcher_merge = Stopwatch()
    merge_sort(arr_merge)
    time_merge = watcher_merge.stop()
    print("归并排序花费%dms，" % time_merge, end="数组已排序\r\n" if __sortedCheck(arr_merge) else "数组未排序XXXXXXXXXXXXXX\r\n")
