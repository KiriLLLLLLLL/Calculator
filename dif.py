from fractions import Fraction

x = 0
y = 0

# Модуль инициализации - ввода данных только внутри метода а не для всей программы без строк 6 и 7
def init_comp(a, b):
    global x
    global y
    x = a
    y = b


def do_it_comp():
    return complex(x) - complex(y)


def init_frac(a, b, c, d):
    global x
    global y
    x = [a, b]
    y = [c, d]


def do_it_frac():
    return Fraction(x[0], x[1]) - Fraction(y[0], y[1])