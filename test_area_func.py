from trapezium_rule import get_area

def test_get_area():
    #i didnt know until just now tgat tests could all go in the same func
    assert get_area([27, 25, 30, 36, 48, 127], 4) == 864
    assert get_area([10,20], 4) == 60
    assert get_area([5,5,5,5], 2) == 30
    assert get_area([2,3,8,1,6], 3) == 48
    assert get_area([0, 0, 0, 0], 10) == 0
    assert get_area([-3, -7, -11, -5], 4) == -88
    assert get_area([-10, 5, 20, -5, 10], 2) == 40
    assert get_area([-5, 0, 5], 2) == 0
    assert get_area([1.5, 2.25, 3.75, 4.5], 2) == 18