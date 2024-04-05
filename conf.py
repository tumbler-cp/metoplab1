import yaml
import math
import numpy as np

with open('config.yml') as c:
    dict = yaml.safe_load(c)
    it_count = dict['iter']
    e_pow = dict['e_pow']

E = 1 / (math.e ** e_pow)
delta = E


def function(x):
    return x**2 + x + math.sin(x)

def f_prime(x):
    return 2*x + 1 + math.cos(x)

def f_double_prime(x):
    return 2 - math.sin(x)

def is_continous():
    k = True
    for i in np.arange(-1, 0, 0.01):
        if math.isnan(f_prime(i)):
            k = False
            break
    if not k: return k
    for i in np.arange(-1, 0, 0.01):
        if math.isnan(f_double_prime(i)):
            k = False
            break
    return k
