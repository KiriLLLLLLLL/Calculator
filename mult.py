x = 0
y = 0


# Модуль инициализации - ввода данных только внутри метода а не для всей программы без строк 6 и 7
def init(a, b):
    global x
    global y
    x = a
    y = b


def do_it():
    return complex(x) * complex(y)