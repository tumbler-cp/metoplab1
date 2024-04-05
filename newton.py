import math
from conf import function as f
from conf import E, delta, it_count
from conf import f_prime as fp
from conf import f_double_prime as fpp
from tabulate import tabulate


def solve(a, b):

    x_0 = (b - a) / 2
    x =  x_0 - fp(x_0) / fpp(x_0)
    
    it = 0

    while True:
        it += 1
        x = x - fp(x) / fpp(x)
        if abs(fp(x)) <= E or it == it_count: break

    f_s = f(x)
    return x, f_s