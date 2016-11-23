def main():
    n = input()
    m = input()
    print(polynomial(n, m))

def polynomial(n, m):
    
    # define the degrees of the dividend and divisor
    n = int(n)
    m = int(m)
    
    # make sure the degrees of both polynomials are non-negative
    if n < 0 or m < 0:
        print("Both polynomials should have non-negative degrees.")
        
    # make sure the dividend has greater degree than the divisor    
    if n < m:
        print("The degree of the dividend should exceed the degree of the divisor.")
        return False
    
    # create the list of coefficients of the dividend
    dividend = []
    print("dividend:")
    
    for i in range(n+1):
        
        # prompt the user for the coefficients of the dividend
        print("{}-th coefficient: ".format(n-i), end="")
        coeff = int(input())
        
        # append the coefficients to the list of coefficients
        dividend.append(coeff)


    # create the list of coefficients of the divisor
    divisor = []
    print("divisor:")

    for i in range(m+1):

        # prompt the user for the coefficients of the divisor
        print("{}-th coefficient: ".format(m-i), end="")
        
        # make sure the quotient is a monic polynomial
        if i == 0:
            coeff = 1
            print("1")
            divisor.append(coeff)    
        
        # append the coefficients to the list of coefficients of the divisor
        else:
            coeff = int(input())
            divisor.append(coeff)    
        
    # declare the lists of coefficients of the quotient and remainder
    quotient = []
    remainder = []
    result = [quotient, remainder]
    
    deg = n
    
    # In each step of the Division Algorithm, we mod out the dividend by the divisor to reduce the degree of the dividend by one. 
    # We repeat this procedure until the dividend has a lesser degree than the divisor.
    while deg >= m:
        
        # create the list of coefficient of the new dividend, obtained by moding out the dividend by the divisor
        temp_dividend = []
        
        # compute the coefficients of the new dividend
        for i in range(deg):
            
            # the first m coefficients are obtained by subtracting multiples of the coefficient of the divisor from the respective coefficients of the dividend
            if i < m:
                x = int(dividend[i+1]) - (int(dividend[0]) * int(divisor[i+1]))
                temp_dividend.append(x)
            
            # the remaining coefficients of the new dividend equal the respective coefficients of the old dividend
            else:
                x = int(dividend[i+1])
                temp_dividend.append(x)
        
        # in each step, append the leading coefficient of the divisor to the list of the coefficients of the quotient
        quotient.append(int(dividend[0]))
        
        # after each step, replace the old dividend by the new dividend
        dividend = temp_dividend
        
        # after each step, the degree of the dividend decreases by at least one
        deg = deg - 1

    # when the divisor has a greater degree than the dividend, the division is completed, and the remaining terms form the remainder
    if deg < m:

        # append the remaining terms of the dividend to the remainder
        for i in range(len(dividend)):
            remainder.append(dividend[i])
        
        # remove all the zeroes at the beginning of the remainder    
        #while(remainder[0] == 0):
            #remainder.remove(0)
    
    return result
    
if __name__ == "__main__":
    main()
