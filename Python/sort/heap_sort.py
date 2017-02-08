#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def heap_sort(ary):
    n = len(ary)
    # 最后一个非叶子节点
    first = int(n / 2 - 1)
    # 构造大根堆
    for start in range(first, -1, -1):
        max_heapify(ary, start, n - 1)
    for end in range(n - 1, 0, -1):
        # 堆排，将大根堆转换成有序数组
        ary[end], ary[0] = ary[0], ary[end]
        max_heapify(ary, 0, end - 1)
    return ary


# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
# start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary, start, end):
    root = start
    while True:
        # 调整节点的子节点
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and ary[child] < ary[child + 1]:
            # 取较大的子节点
            child = child + 1
        # 较大的子节点成为父节点
        if ary[root] < ary[child]:
            # 交换
            ary[root], ary[child] = ary[child], ary[root]
            root = child
        else:
            break


if __name__ == '__main__':
    s = heap_sort([3, 2, 4, 5, 1])
    print (s)
