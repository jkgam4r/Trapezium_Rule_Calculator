#some main steps must be established
#the code will take the order of polynomial first
#then take input one by one for each polynomail coefficient
#will then take the number of trapeziums required as an input
#will then use the trapezium rule formula alongside the acquired data to compute the area and return it

#firstly getting the order - break into get and check order function.

def get_order(): #takes order input and checks its valid
    order = input("Input the order of your polynomial : ")
    return check_order(order)

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

def main(): #main loop
    
    order = get_order() #get polynomial order and check valid
    while not order[0]: #while the order is invalid
        print("Polynomial order must be an int greater than 2.")
        order = get_order() #gets order again
    order = order[1] #gets rid of the error message flag
    
    

if __name__ == "__main__":
    main()