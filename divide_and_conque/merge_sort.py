def merge_sort(arr: []):
    __sort_merge(arr, 0, len(arr))


def __sort_merge(arr: [], start: int, end: int):
    """
    二路归并：分割数组为两部分，分别对这两部分排序，然后将两个有序数组合并
    """

    # 结束条件，当分割部分只剩一个元素时已有序，结束分割
    if end - start <= 1:
        return
    mid = (start + end) // 2
    __sort_merge(arr, start, mid)
    __sort_merge(arr, mid, end)
    # 递归合并
    __merge_array(arr, start, mid, end)


def __merge_array(arr: [], start: int, mid: int, end: int):
    """
    合并数组，使数组有序，其中每段数组是有序的
    :param arr: 数组
    :param start: 开始inex
    :param mid: 中间index
    :param end: 结束index
    """
    dump = []
    i = start  # 数组1的起始
    j = mid  # 数组2的起始
    while i < mid and j < end:
        if arr[i] <= arr[j]:
            dump.append(arr[i])
            i += 1
        else:
            dump.append(arr[j])
            j += 1

    # 将剩余一数组添加在dump后
    while i < mid:
        dump.append(arr[i])
        i += 1
    while j < end:
        dump.append(arr[j])
        j += 1

    #  替换值
    for index, x in enumerate(dump):
        arr[start + index] = x


if __name__ == '__main__':
    array = [849, 232, 1, 44, 634, 1366, 3232, 43231, 3453, 0, -293, -9984]
    print("原数组 => %s" % array)
    merge_sort(array)
    print("归并排序后数组 => %s" % array)
    array = [849, 232, 1, 44, 634, 1366, 3232, 43231, 3453, 0, -293, -9984, 3242, 22, 75, 64, 4335, 678, 4454, 54544,
             87, 8, 5, 565, 4545, 2, 23, 67, 8]
    print("原数组 => %s" % array)
    merge_sort(array)
    print("归并排序后数组 => %s" % array)
    array = [849, 232, 1, 44, 634, 435, 3224, 1231, 5475, 867, 3534, 766, 75765, 3242, 2, 2, 242411, 6545675, 1366,
             3232, 43231, 3453, 0, -293, -9984]
    print("原数组 => %s" % array)
    merge_sort(array)
    print("归并排序后数组 => %s" % array)
    array = [849, 232, 1, 44, 634, 1366, 3232, 43231, 243234, 2412, 75687, 79676, 2343, 2342, 11, 4353, 645, 7658, 4,
             23, 23, 57, 23, 435, 4412, 32467, 143, 3454, 25, 3453, 0, -293, -9984]
    print("原数组 => %s" % array)
    merge_sort(array)
    print("归并排序后数组 => %s" % array)
    array = ["DDCSAD", "ADADSD", "ACSDSF", "skfais", "sliiiiilsdj"]
    print("原数组 => %s" % array)
    merge_sort(array)
    print("归并排序后数组 => %s" % array)
