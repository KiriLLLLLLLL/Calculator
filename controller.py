import sum as sum
import user_int


def console():
    value_a = user_int.get_value()
    value_b = user_int.get_value()
    sum.init(value_a, value_b)
    result = sum.do_it()
    user_int.user_data(result, 'sum')
