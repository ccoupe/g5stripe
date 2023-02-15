#
from elc_ng import ELC, ColorCommand
import time
import sys

if len(sys.argv) == 2:
  if sys.argv[1] == 'red':
    c = (255,0,0)
  elif sys.argv[1] == 'green':
    c = (0,255,0)
  elif sys.argv[1] == 'blue':
    c = (0,0,255)
  elif sys.argv[1] == 'off':
    c = (0,0,0)
  elif sys.argv[1] == 'white':
    c = (255,255,255)
  elif sys.argv[1] == 'on':
    c = (50, 50, 50)
  else:
    print("Unknown value")
    exit()
else:
    exit()

elc = ELC(0x187c, 0x0550)

with elc:
    elc.execute(ColorCommand([1], c[0], c[1], c[2]))
