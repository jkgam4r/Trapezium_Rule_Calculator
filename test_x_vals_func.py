from trapezium_rule import get_x_vals

def calc_get_X_vals():
    assert get_x_vals(5, (0,10)) == [0,2,4,6,8,10]

def calc_get_X_vals2():
    assert get_x_vals(10, (0,10)) == [0, 1,2,3,4,5,6,7,8,9,10]