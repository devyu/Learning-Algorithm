#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def shell_sort(ary):
    n = len(ary)
    # 初始增量，round四舍五入取整
    gap = int(round(n / 2))
    while gap > 0:
        for i in range(gap, n):
            temp = ary[i]
            j = i
            while (j >= gap and ary[j - gap] > temp):
                # 插入排序
                ary[j] = ary[j - gap]
                j = j - gap
            ary[j] = temp
        gap = int(round(gap / 2))
    return ary


if __name__ == '__main__':
    s = shell_sort([3, 2, 4, 5, 1, 6, 8, 7])
    print (s)
