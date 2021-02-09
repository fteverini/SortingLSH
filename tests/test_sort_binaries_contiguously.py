#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:24:08 2021
"""

import pytest
from sort_binaries_contiguously import  construct_ordered_binaries

def check_contiguous(a, b):
    assert(len(a)==len(b))
    ct = 0
    for char_a, char_b in zip(a, b):
        if char_a!=char_b:
            ct +=1
            if ct>1:
                return False
    return ct==1


@pytest.mark.parametrize('n', [1, 4, 10, 13, 16])
def test_contain_all_binaries(n):
    elements = construct_ordered_binaries(n)
    assert([len(a)==n for a in elements])
    s = set(elements)
    assert len(elements) == len(s) == 2 ** n 

@pytest.mark.parametrize('n', [1, 4, 10, 13, 16])
def test_elements_are_contiguous(n):
    elements = construct_ordered_binaries(n)
    m = len(elements)
    for k in range(m-1):
        assert check_contiguous(elements[k], elements[k+1])
