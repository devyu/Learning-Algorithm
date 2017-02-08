#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select_sort(ary):
    n = len(ary)
    for i in range(n):
        # 记录最小元素下标
        minNum = i
        for j in range(i + 1, n):
            if ary[j] < ary[minNum]:
                # 最小的下标
                minNum = j
        ary[minNum], ary[i] = ary[i], ary[minNum]
    return ary


if __name__ == '__main__':
    s = select_sort([3, 1, 2, 4, 6])
    print(s)
