from trapezium_rule import get_coefficient

############################### get coefficient testing############################
    
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
    