#!/usr/bin/python3

from elc_ng import ELC, ColorCommand
import time

elc = ELC(0x187c, 0x0550)
print('elc:', elc)

with elc:
    # red: elc.execute(ColorCommand([1], 1, 1, 1))
    # off for two seconds. Command [1] works.
    print("Off:")
    elc.execute(ColorCommand([1], 0, 0, 0))
    time.sleep(2)
    print("Red:")
    elc.execute(ColorCommand([1], 255, 0, 0))
    time.sleep(1)
    print("Green:")
    elc.execute(ColorCommand([1], 0, 255, 0))
    time.sleep(1)
    print("Blue")
    elc.execute(ColorCommand([1], 0, 0, 255))
    time.sleep(1)
    print("Whites")
    r = 4
    inc = int(255/r)
    for z in range(r):
        print("z",z)
        elc.execute(ColorCommand([1], inc*z, inc*z, inc*z))
        time.sleep(1)
        

