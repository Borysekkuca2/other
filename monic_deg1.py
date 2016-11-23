def main():
    n = input()
    print(polynomial(n))

def polynomial(n):
    
    # define the degree of the dividend
    deg = int(n)
    
    # prompt the user for the coefficients of the dividend
    dividend = []
    for i in range(deg+1):
        print("{}-th coefficient: ".format(deg-i), end="")
        coeff = int(input())
        dividend.append(coeff)
        
    # prompt the user for the coefficients of the divisor   
    print("divisor: ", end="")
    divisor = int(input())
    
    # declare the lists of coefficients
    quotient = []
    remainder = []
    result = [quotient, remainder]
    
    for i in range(deg):
        if i == 0: 
            quotient.append(dividend[0])
        else:
            coeff = int(dividend[i]) - (int(quotient[i-1]) * int(divisor)) 
            quotient.append(coeff)
    
    rem = int(dividend[deg]) - (int(quotient[deg-1]) * int(divisor)) 
    remainder.append(rem)

        
    return result
    
    
if __name__ == "__main__":
    main()
