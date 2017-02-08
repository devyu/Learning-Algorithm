#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array



# 优化1：某一天遍历如果没有数据交换，说明已经排序完毕，不需要进行遍历
def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = True
        for j in range(n - i - 1):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
                flag = False
        # 已经全部排序完毕
        if flag:
            break

    return ary


# 优化2：在遍历的过程当中，记录住最后发生数据交换的位置，这个位置之后的数据已经是有序的，不用再进行排序了。
def bubble_sort3(ary):
    n = len(ary)
    # 最后交换的位置范围，默认为 n
    k = n
    for i in range(n):
        flag = True
        # 只遍历到最后交换的位置
        for j in range(1, k):
            if ary[j-1] > ary[j]:
                ary[j-1], ary[j] = ary[j], ary[j-1]
                # 最后交换的位置
                k = j
                flag = False
        if flag:
            break

    return ary

if __name__ == '__main__':
    s = bubble_sort3([3, 2, 4, 5, 1])
    print (s)