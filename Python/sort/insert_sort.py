#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        if array[i] < array[i - 1]:
            temp = array[i]  # 取出待插入的元素
            index = i  # 取出待插入元素的下标
            # 从后往前扫描，从 i-1 循环到 0 (包括0)
            for j in range(i - 1, -1, -1):
                if array[j] > temp:
                    array[j + 1] = array[j]  # 将该扫描的元素向后移动一位
                    index = j  # 记录待插入的下标
                else:
                    break
            array[index] = temp
            print(array)
    return array


if __name__ == '__main__':
    s = insert_sort([3, 2, 4, 5, 1])
    print (s)
