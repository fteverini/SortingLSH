#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:06:29 2021
"""


def construct_ordered_binaries(n: int):
    if n == 1:
        return  ['0', '1']
    ordered_binaries_previous = construct_ordered_binaries(n - 1)
    ordered_binaries = ['0' + p for p in ordered_binaries_previous] + \
                       ['1' + p for p in ordered_binaries_previous[::-1]]
    return ordered_binaries


if __name__=="__main__":
    n = 4
    ordered_binaries = construct_ordered_binaries(n)
    print(ordered_binaries)
    
    