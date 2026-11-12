from trapezium_rule import get_coefficients
#############################################################

def test_get_coefficients_quadratic_valid(monkeypatch):
    inputs = iter([1, 2, 4])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_coefficients(2) == [1.0, 2.0, 4.0]
    
    
def test_get_coefficients_cubic_valid(monkeypatch):
    inputs = iter([1, 2, 4, 5.345456])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_coefficients(3) == [1.0, 2.0, 4.0, 5.345456]
    
def test_get_coefficients_quadratic_invalid_multiple_strings(monkeypatch):
    inputs = iter([1, 2, 'asd', 'asdwfadf', '', 4])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_coefficients(2) == [1.0, 2.0, 4.0]
    
def test_get_coefficients_quadratic_invalid_string(monkeypatch):
    inputs = iter(['', 1, 2, 4])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_coefficients(2) == [1.0, 2.0, 4.0]
