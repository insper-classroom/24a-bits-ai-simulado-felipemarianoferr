#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


def exe1(a, b, c, s):
    @always_comb
    def comb():
        s.next = (not ((not a) and (not c)) and a and (not b)) or (a and b and c) 

    return instances()


def exe2(l, m, h, l_vd, l_am, l_vm, l_az, l_lj):
    @always_comb
    def comb():
        l_vd.next = l and not m and not h

        l_am.next = l and m and not h

        l_vm.next = l and m and h

        l_az.next =  not l and not m and not h
            
        l_lj.next =  (h and (not l or not m)) or (m and not l)
            
        
    return instances()


def exe3(i3, i2, i1, i0, p1, p0, v):
    @always_comb
    def comb():
        p1.next = i3 or i2
        p0.next = ((not i3) and (not i2) and i1) or (i3)
        v.next = i1 or i2 or i3 or i0

    return instances()


def exe4_simulando(a, b, c, d, e, f, g, h, i, j, k, l):
    @always_comb
    def comb():
        a.next = 0
        b.next = 0
        c.next = 0
        d.next = 0
        e.next = 0
        f.next = 0
        g.next = 0
        h.next = 0
        i.next = 0
        j.next = 0
        k.next = 0

    return instances()


def exe4_half_sub(x, y, b, d):
    @always_comb
    def comb():
        b.next = (not x) and y
        d.next = ((not x) and y) or (x and (not y))

    return instances()


def exe4_full_sub(x, y, z, b, d):
    @always_comb
    def comb():
        d.next = (
            ((not x) and (not y) and z)
            or (not x and y and (not z))
            or ((not x) and y and z)
            or (x and y and z)
        )
        b.next = ((not x) and y) or ((not x) and z) or (y and z)

    return instances()


def exe4_sub3(v2, v1, v0, p2, p1, p0, q2, q1, q0):
    return instances()
