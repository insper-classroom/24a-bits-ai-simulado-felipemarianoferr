#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


def exe1(a, b, c, s):
    @always_comb
    def comb():
        s.next = (a and b and c) or ((not b) and a and (not ((not a) and (not c))))

    return instances()


def exe2(l, m, h, l_vd, l_am, l_vm, l_az, l_lj):
    @always_comb
    def comb():
        l_vd.next = l and not m and not h
        l_am.next = l and m and not h
        l_vm.next = l and m and h
        l_az.next = not l and not m and not h
        l_lj.next = (h and (not l or not m)) or (m and not l)

    return instances()


def exe3(i3, i2, i1, i0, p1, p0, v):
    @always_comb
    def comb():
        p1.next = (not i3 and i2) or (i3)
        v.next = (i3 or i2 or i1 or i0)
        p0.next = (not i3 and not i2 and i1) or i3

    return instances()


def exe4_simulando(a, b, c, d, e, f, g, h, i, j, k, l):
    @always_comb
    def comb():
        a.next = 1
        b.next = 0
        c.next = 0
        d.next = 1
        e.next = 1
        f.next = 1
        g.next = 1
        h.next = 1
        i.next = 1
        j.next = 0
        k.next = 1

    return instances()


def exe4_half_sub(x, y, b, d):
    @always_comb
    def comb():
        b.next = not x and y
        d.next = (not x and y) or (x and not y) 

    return instances()


def exe4_full_sub(x, y, z, b, d):
    @always_comb
    def comb():
        b.next = (not x and not y and z) or (not x and y and not z) or (not x and y and z) or (x and y and z)
        d.next = (not x and not y and z) or (not x and y and not z) or (x and not y and not z) or (x and y and z)

    return instances()


def exe4_sub3(v2, v1, v0, p2, p1, p0, q2, q1, q0):
    b0 = Signal(bool(0))
    b1 = Signal(bool(0))
    b2 = Signal(bool(0))

    half = exe4_half_sub(v0, p0, b0, q0)
    full_1 = exe4_full_sub(v1, p1, b0, b1, q1)
    full_2 = exe4_full_sub(v2, p2, b1, b2, q2) 


    return instances()
