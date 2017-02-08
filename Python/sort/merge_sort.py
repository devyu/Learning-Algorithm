#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def merge_sort(ary):
    if len(ary) <= 1: return ary
    # 二分分解
    num = int(len(ary) / 2)
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])

    # 合并数组
    return merge(left, right)

def merge(left, right):
    print ('left = ', left)
    print ('right = ', right)
    '''
    将两个有序数组left[]和right[]合并成一个大的有序数组
    '''
    # left和right数组的下标指针
    l,r = 0,0
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]

    return result

if __name__ == '__main__':
    s = merge_sort([5, 4, 3, 2, 1])
    print ('sort result = ', s)

