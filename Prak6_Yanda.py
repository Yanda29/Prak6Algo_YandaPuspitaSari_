# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:19:52 2021

@author: Yanda Puspita Sari
"""
from math import *
print("@   @  @@@@@  @    @  @@@@    @@@@@")
print(" @ @   @   @  @ @  @  @   @   @   @")
print("  @    @@@@@  @  @ @  @    @  @@@@@")
print("  @    @   @  @   @@  @   @   @   @")
print("  @    @   @  @    @  @@@@    @   @")

def hitung_jarak_tempuh(v0,t,a) :
    b=(v0*t)+(0.5*(a*t**2))
    print('kecepatan awal = ',v0,' masukan waktu = ',t,'dan percepatan : ',a,'hasil',b)
    return b

v0=int(input("kecepatan awal : "))
t=int(input(" masukan waktu : "))
a=int(input("percepatan :"))
hitung_jarak_tempuh(v0, t, a)
