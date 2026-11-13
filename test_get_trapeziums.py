from trapezium_rule import get_trapeziums

def test_get_trapeziums_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 5)
    assert get_trapeziums() == 5
    
def test_get_trapeziums_invalid(monkeypatch):
    inputs = iter(['', 'test val', 4])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_trapeziums() == 4
