from trapezium_rule import get_order, check_order

def test_check_order_valid():
    assert check_order(5) == [True, 5]
    
def test_check_order_invalid_str():
    assert check_order('s') == [False, 's']