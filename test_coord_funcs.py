from trapezium_rule import get_x_vals, calculate_y_fx

#for these tests I will use the known curve of x^3 + 3x^2 + 6x + 5 
#between the ranges of -10 and 10 

def test_calc_y_fx_valid1():
    assert calculate_y_fx([1,2,4,8], 2) == 32

def test_calc_y_fx_valid2():
    assert calculate_y_fx([2,1,3], 3) == 24
    
def test_calc_y_fx_valid3():
    assert calculate_y_fx([1,1,1], 1) == 3
    
    
def test_calc_y_fx_valid4():
    assert calculate_y_fx([2,0,3], 5) == 53
#make tests here. this file will be for testing xval and yval coordinate calculating functions