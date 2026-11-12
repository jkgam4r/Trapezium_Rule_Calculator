from trapezium_rule import get_range

def test_get_range(monkeypatch):
    inputs = iter([0, 10])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_range() == (0,10)
    
def test_get_range_invalid_B(monkeypatch):
    inputs = iter([0, 's', 0, 10])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_range() == (0,10)
    
def test_get_range_invalid_A(monkeypatch):
    inputs = iter(['s', 10, 0, 10])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_range() == (0,10)
    
