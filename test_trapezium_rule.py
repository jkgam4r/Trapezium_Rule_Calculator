from trapezium_rule import check_order, get_coefficient

def test_check_order_valid():
    assert check_order(5) == [True, 5]
    
def test_check_order_invalid_str():
    assert check_order('s') == [False, 's']
    
def test_get_coefficient_valid(monkeypatch, capsys):
    
    monkeypatch.setattr("builtins.input", lambda _: 5)
    
    assert get_coefficient(2) == 5.0