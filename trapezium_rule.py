#some main steps must be established
#the code will take the order of polynomial first
#then take input one by one for each polynomail coefficient
#will then take the number of trapeziums required as an input
#will then use the trapezium rule formula alongside the acquired data to compute the area and return it

#firstly getting the order - break into get and check order function.

def get_order(): #takes order input and checks its valid
    order = input("Input the order of your polynomial : ")
    order = check_order(order)
    while not order[0]: #while the order is invalid
        print("Polynomial order must be an int greater than 2.")
        order = get_order() #gets order again
    return order[1] #gets rid of the error message flag and returns

def check_order(num): #function that checks that an input is a number and greater than 2
    try:
        num = int(num) #converts input to int, if error then exception raised
        if num >= 2: #if the number is not >= 2 then it is also invalid and an exception is raised
            return [True, num]
        raise Exception
    except:
        return [False, num] #returns a list, bool represents valid or not
    
    
#this will be a subfunction of get_coefficients, will be called 'order' number of times
#takes order of x as input so it knows which value it is going to be recieving, 
#that way the input message can vary


def get_coefficient(order_of_x):  #param must be int, validated by parent functions
    
    def get_input_message(order): #func that takes order of x and figures out which input message to display to user
            
        input_messages = [f"Input value for coefficent of x^{order}, term : ", #options of input messages
            "Input value for coefficient of x term : ",
            "Input value for constant term : "]
        
        if order >= 2:
            input_message = input_messages[0]
        elif order == 1:
            input_message = input_messages[1] #figures out which input message to use
        else:
            input_message = input_messages[2]
            
        return input_message
    
    def validate_input_coefficient(input_val): #func that returns true or false based on whether an input can be converted to a float
        try:
            input_val = float(input_val)
            return True
        except:
            return False
    
    #function recursivley takes inputs until input is valid, then returning it
    input_message = get_input_message(order_of_x)
    
    valid_coefficient = False #loop flag for validating input
    
    while not valid_coefficient: #loop until the input is valid
        coefficient = input(input_message)
        valid_coefficient = validate_input_coefficient(coefficient) #func returns true or false whether the input is valid, if true then the loop will end
        
    return float(coefficient)

def get_coefficients(order): #order is known to be an int, validated by check_order in main 
    coefficients = [] #empty list to store coefficient terms
    for i in range (order, -1, -1): #loops through each x term one by one
        coefficients.append(get_coefficient(i))
    return coefficients

def get_trapeziums(): #function to take input of number of trapeziums

    while True: #loop until input value valid
        num = input("How many trapeziums should be used to compute the area? : ")
        try: #if the number is an int that is greater than 0 then return it otherwise loop with error message
            num = int(num)
            if num >= 1:
                return num
            raise Exception
        except:
            print ("Input value must be an whole number greater than 0.")
    
    
def get_range(): #func must validate a and b, both floats with b > a
 
    while True:
        a = input("Input bottom/starting range for definite integration")
        b = input("Input top/ending range for definite integration")
        try:
            a = float(a)
            b = float(b) #checks both values are floats
            if b > a: #and that b is greater than a
                return (a, b)
            else:
                print("The top value must be greater than the bottom value")
        except:
            print("Both input values must be numbers : eg 1.1, -3, 5.6")
    
def get_x_vals(trapeziumsVal, rangeVal): #function that takes the number of trapeziums and range and returns a list of x values
    height = (rangeVal[1] - rangeVal[0]) / trapeziumsVal
    n = trapeziumsVal + 1
      
    x_vals = []
    for widths in range (0, n):
        x_vals.append(rangeVal[0] + (widths*height)) #starting point + additional per point
        #height*width represents as you go through each point, 1 additional width is added on the x value
        
    return x_vals

# def get_y_vals(x_values_lst, coefficients_lst):
#     order = len(coefficients_lst)-1
#     y_values = []
#     for x in x_values_lst:
#         for coefficient in coefficients_lst:
#             y_val = 0
#             for power in range(order, -1, -1):
#                 yval+=(coefficient * (x**power))
#         y_values.append(y_val)
#     return y_values
                


def calculate_y_fx(formula, xval):
    value = 0
    order = len(formula) - 1
    for i in range (0, order):
        value += (formula[i] * (xval**(order-i)))
        print (value)
    value += formula[order]
    return value

print (calculate_y_fx([1,2,4,8], 2))

def main(): #main loop
    
    print ("""
               --*** INTEGRATION CALCULATOR ***--
           
           Program uses trapezium rule to find the area 
                under a curve between 2 points
                
                
                """)
    
    order = get_order() #get polynomial order and check valid
 
    coefficients = get_coefficients(order) #list of coefficients of polynomial
    
    trapeziums = get_trapeziums() #int representing number of trapeziums
    
    rangeAB= get_range() #gets tuple of a, b floats
    
    height = (rangeAB[1] - rangeAB[0]) / trapeziums #height between each x value
    
    x_vals = get_x_vals(trapeziums, rangeAB) #points that trapeziums are made
    

    
if __name__ == "__main__":
    main()