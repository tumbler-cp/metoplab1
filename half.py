from conf import function as f
from conf import E, delta, it_count
from tabulate import tabulate

def solve(a, b):
    it = 0
    table = [['Итерация','x_1','x_2','a','b']]
    while True:
        x_1 = (b + a - delta) / 2
        x_2 = (b + a + delta) / 2
        it += 1
        if f(x_1) <= f(x_2):
            b = x_2
        else:
            a = x_1
        table.append([str(it), '%.5f' % x_1, '%.5f' % x_2, '%.5f' % a, '%.5f' % b])
        if (b - a) / 2 <= E or it == it_count: break

    x_s = (a + b) / 2
    f_s = f(x_s)

    print('Метод половинного деления')
    print(tabulate(table))
    print('Результат: x* = ', '%.5f' % x_s, ', f(x*) = ', '%.5f' % f_s, '\n\n')

    return x_s, f_s
        
