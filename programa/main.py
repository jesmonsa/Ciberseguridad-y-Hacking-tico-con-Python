
import paquete.modulo2 as m2

m2.test_func()

from paquete.modulo2 import test_func

test_func()

from paquete.modulo2 import *

test_func()

import modulo1

modulo1.test_func()

obje = modulo1.Test()

print(modulo1.variable)

from modulo1 import test_func

test_func()

from modulo1 import *

test_func()

obje = Test()

print(variable)


import modulo1 as m1

m1.test_func()

obje = m1.Test()

print(m1.variable)

import sys

print(sys.path)
