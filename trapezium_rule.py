def get_order():
    try:
        order = int(input("What order polynomial? (eg 3rd order includes x^3 terms):  ")) #eg 2 = quadratic, 3 = cubic etc
        
        if order <= 1: #ensures all orders are greater than one, aka minimum input is a quadratic
            print("Input must be greater than 1")
            return get_order()
            
        return order
    
    except: #if input is invalid then give error message and recursively call function 
        print ("Input must be a whole number")
        return get_order()        
        
        
def get_coefficients(order): #takes order as input, returns list of ints for coefficients of each term
    coefficients = [] #create empty list that will store coefficients
    
    for i in range (order, 1, -1): #loop through coeficients of all terms where power is >= 2
        
        valid = False 
        while not valid: #loops on the same coefficient input until the input is valid
            try: 
                coefficient = float(input((f"Input the coefficient for the x^{i} term : ")))
                valid = True #if there is no error on input then flag this loop to end 
                coefficients.append(coefficient) #and append the coefficient to the list
            except:
                print ("Input must be a number, decimals and negatives are permitted") #otherwise give error message and take input again
                
    coefficients.append(float(input("Input coefficient for x term : "))) #then get coefficients for x term and constant term
    coefficients.append(float(input("Input constant term : ")))
        
    return(coefficients)
        
coefficients = get_coefficients(get_order())
print(coefficients)