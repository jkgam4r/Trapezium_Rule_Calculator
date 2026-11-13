from trapezium_rule import check_order, get_order

def test_check_order_valid():
    assert check_order(5) == [True, 5]
    
def test_check_order_invalid_str():
    assert check_order('s') == [False, 's']
    
def test_get_order(monkeypatch):
    inputs = iter(['f', 5])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs) )
    assert get_order() == 5

def test_get_order_2(monkeypatch):
    inputs = iter(['f', '', 'ffff', 'rejectme', 5])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs) )
    assert get_order() == 5