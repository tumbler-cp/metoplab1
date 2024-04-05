import math
from conf import function as f
from conf import E, delta, it_count

def solve(a, b):
    it = 0

    x_1 = a + (((3 - math.sqrt(5)) / 2) * (b - a))
    x_2 = a + (((math.sqrt(5) - 1) / 2) * (b - a))
    f_x1 = f(x_1)
    f_x2 = f(x_2) 
    tau = (math.sqrt(5) - 1) / 2

    while True:
        it += 1

        if (f_x1 <= f_x2):
            b = x_2
            x_2 = x_1
            f_x2 = f_x1
            x_1 = b - (tau * (b - a))
            f_x1 = f(x_1)
        else:
            a = x_1
            x_1 = x_2
            f_x1 = f_x2
            x_2 = a + (tau * (b - a))
            f_x2 = f(x_2)

        
        if (b - a) / 2 <= E or it == it_count: break
    x_s = (a + b) / 2
    f_s = f(x_s)
    return x_s, f_s