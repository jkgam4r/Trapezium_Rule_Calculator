from trapezium_rule import check_order, get_coefficient

def test_check_order_valid():
    assert check_order(5) == [True, 5]
    
def test_check_order_invalid_str():
    assert check_order('s') == [False, 's']
    
def test_get_coefficient_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 5)
    assert get_coefficient(2) == 5.0
    
def test_get_coefficient_str_then_valid(monkeypatch):
    inputs = iter(['s', '5', 5]) #iterate through invalid to valid input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)) #inputs series of input requests when prompted
    assert get_coefficient(2) == 5.0
    
def test_get_coefficient_constant_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5) #tests that constant inputs work too
    assert get_coefficient(0) == 5.0
    
def test_get_coefficient_constant_invalid(monkeypatch):
    inputs = iter(['s', '175.6']) #iterate through invalid to valid input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)) #inputs series of input requests when prompted
    assert get_coefficient(0) == 175.6
    
def test_get_coefficient_linear_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5) #tests that constant inputs work too
    assert get_coefficient(1) == 5.0
    
def test_get_coefficient_linear_invalid(monkeypatch):
    inputs = iter(['s', '5.3']) #iterate through invalid to valid input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs)) #inputs series of input requests when prompted
    assert get_coefficient(1) == 5.3
    