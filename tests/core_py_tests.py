#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# this is too hacky, remove this and find some standard way
# ----------- adding .. in sys path ---------------
import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path
# ------------- .. added in sys.path --------------
from pygolomb.core import Golomb

def golomb_test(m, inputs):
    G = Golomb(m)
    for x in inputs:
        a = G.encode(x)
        b = G.decode(a)
        # TODO: do not print them, just log them. and raise an exception
        #       for errors
        print '{4}\t\t{0}\t\t{1}\t\t{2}\t\t\t -- {3}'.format(
            x, a, b[0],
            "pass" if x == b[0] else "fail",
            bin(x)
        )

if __name__ == '__main__':
    for x in xrange(8):
        golomb_test(1 << x, range(256))
        print '{0:->{1}}'.format('>', 80)
