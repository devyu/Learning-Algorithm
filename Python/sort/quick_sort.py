#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quick_sort(ary):
    return qsort(ary, 0, len(ary) - 1)


def qsort(ary, left, right):
    # ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right: return ary
    key = ary[left]  # 基准数
    left_ptr, right_ptr = left, right
    while left_ptr < right_ptr:
        while ary[right_ptr] >= key and left_ptr < right_ptr:
            right_ptr -= 1
        while ary[left_ptr] <= key and left_ptr < right_ptr:
            left_ptr += 1
        # 交换两个指针对应的值
        ary[left_ptr], ary[right_ptr] = ary[right_ptr], ary[left_ptr]
    ary[left], ary[left_ptr] = ary[left_ptr], ary[left]
    qsort(ary, left, left_ptr - 1)
    qsort(ary, right_ptr + 1, right)
    return ary


if __name__ == '__main__':
    s = quick_sort([3, 2, 4, 5, 1])
    print (s)
