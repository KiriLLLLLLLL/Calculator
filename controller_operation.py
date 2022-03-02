import sum, mult, dif, div
from user_int import get_operation

sign_operation = \
    {
        '+': sum,
        '*': mult,
        '-': dif,
        '/': div
    }

def operation():
    sign_op = get_operation()
    oper = sign_operation[sign_op]
    return oper