import random, os, sys, time


def Letters(lType = 0, LType):
    A = [
    '░█████╗░',
    '██╔══██╗',
    '███████║',
    '██╔══██║',
    '██║░░██║',
    '╚═╝░░╚═╝',
    ]
    B = [
    '██████╗░',
    '██╔══██╗',
    '██████╦╝',
    '██╔══██╗',
    '██████╦╝',
    '╚═════╝░'
    ]
    return A[:]

for i in range (6):   
    print(Letters())
input()