import math
from conf import function as f
from conf import E, delta, it_count
from tabulate import tabulate

def solve(a, b):
    it = 0

    table = [['Итерация','x_1','x_2','a','b']]

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

        table.append([str(it), '%.5f' % x_1, '%.5f' % x_2, '%.5f' % a, '%.5f' % b])   
        if (b - a) / 2 <= E or it == it_count: break

    x_s = (a + b) / 2
    f_s = f(x_s)

    print('Метод золотого сечения')
    print(tabulate(table))
    print('Результат: x* = ', '%.5f' % x_s, ', f(x*) = ', '%.5f' % f_s, '\n\n')

    return x_s, f_s