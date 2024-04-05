from conf import function as f
from conf import E, delta, it_count

def solve(a, b):
    it = 0
    while True:
        x_1 = (b + a - delta) / 2
        x_2 = (b + a + delta) / 2
        it += 1
        if f(x_1) <= f(x_2):
            b = x_2
        else:
            a = x_1
        if (b - a) / 2 <= E or it == it_count: break
    x_s = (a + b) / 2
    f_s = f(x_s)
    return x_s, f_s
        
