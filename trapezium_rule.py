#some main steps must be established
#the code will take the order of polynomial first
#then take input one by one for each polynomail coefficient
#will then take the number of trapeziums required as an input
#will then use the trapezium rule formula alongside the acquired data to compute the area and return it

#firstly getting the order - break into get and check order function.

def get_order():
    order = input("Input the order of your polynomial : ")
    return check_order(order)

def check_order(num): #function that checks that an input is a number and greater than 2
    try:
        num = int(num)
        if num >= 2:
            return [True, num]
        raise Exception
    except:
        return [False, num] #returns a list, bool represents valid or not

def main():
    order = get_order()
    while not order[0]: #while the order is invalid
        print("Polynomial order must be an int greater than 2.")
        order = get_order()
    print(order[1])

if __name__ == "__main__":
    main()