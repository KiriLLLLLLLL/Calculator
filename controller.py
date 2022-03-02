
import user_int, controller_operation


def console():
    type_value = user_int.get_type()
    if type_value == 1:
        value_a = user_int.get_comp_value()
        value_b = user_int.get_comp_value()
        oper_sign = controller_operation.operation()
        oper_sign.init_comp(value_a, value_b)
        result = oper_sign.do_it_comp()
        user_int.user_data(result, oper_sign)
    else:
        value_a = user_int.get_frac_value()
        value_b = user_int.get_frac_value()
        value_c = user_int.get_frac_value()
        value_d = user_int.get_frac_value()
        oper_sign = controller_operation.operation()
        oper_sign.init_frac(value_a, value_b, value_c, value_d)
        result = oper_sign.do_it_frac()
        user_int.user_data(result, oper_sign)