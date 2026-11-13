from trapezium_rule import calculate_y_fx


def test_calc_y_fx_valid1():
    assert calculate_y_fx([1,2,4,8], 2) == 32

def test_calc_y_fx_valid2():
    assert calculate_y_fx([2,1,3], 3) == 24
    
def test_calc_y_fx_valid3():
    assert calculate_y_fx([1,1,1], 1) == 3
    
def test_calc_y_fx_valid4():
    assert calculate_y_fx([2,0,3], 5) == 53 #lots of tests for this func, complex
    
def test_calc_y_fx_valid5():
    assert calculate_y_fx([1,1,2,1,1,4,5,6], 3) == 3567
    
def test_calc_y_fx_valid6():
    assert calculate_y_fx([1,1,2,0,1,4,5,6], 3) == 3486 #all passed, function is fully functional
#make tests here. this file will be for testing xval and yval coordinate calculating functions

