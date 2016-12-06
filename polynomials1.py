def main():
    dividend = input()
    divisor = input()
    print(polynomial(dividend, divisor))

def polynomial(dividend, divisor):
    
    # define the degrees of the dividend and divisor
    n = len(dividend) - 1
    m = len(divisor) - 1
    
    # make sure the degrees of both polynomials are non-negative
    if n < 0 or m < 0:
        print("Both polynomials should have non-negative degrees.")
        return False
        
    # make sure the dividend has no smaller degree than the divisor    
    if n < m:
        print("The degree of the dividend should exceed the degree of the divisor.")
        return False
    
    # remember the leading coefficient of the divisor (will need it later)
    div = float(divisor[0])
    
    # rescale the divisor to a monic polynomial to make the algorithm easier 
    # while this conversion is not required by the division algorithm, it makes the program easier to write
    if divisor[0] != 1:
        
        # temporary storage
        temp_divisor =[]
        
        # add the rescaled coefficients to the temporary list
        for i in range(m+1):
            rescaled_coeff = (float(divisor[i]))/div
            temp_divisor.append(float(rescaled_coeff))
        
        # replace the initial divisor with the rescaled polynomial
        divisor = temp_divisor
            
    # declare the lists of coefficients of the quotient and remainder
    quotient = []
    remainder = []
    
    # the degree of the dividend
    deg = n
    
    # Here the Long Division Algorithm starts. For the explanation of how it works, see here: http://www.purplemath.com/modules/polydiv2.htm
    # In each step of the division algorithm, we mod out the dividend by the divisor to reduce the degree of the dividend by one. 
    # We repeat this procedure until the degree of dividend is less than the degree of the divisor.
    while deg >= m:
        
        # create the temporary list of coefficients of the new dividend; the new dividend will be obtained by moding out the old dividend by the divisor
        temp_dividend = []
        
        # compute the coefficients of the new dividend
        for i in range(deg + 1):
            
            # obtain the first m coefficients of the new dividend & store them
            # they are obtained by subtracting the product of the divisor and the leading coefficient of the dividend from the dividend
            if i < m + 1:
                x = float(dividend[i]) - (float(dividend[0]) * float(divisor[i]))
                
                # append the coefficient of the new dividend to the temporary list. The first coefficient will always be zero, so don't store it.
                if i != 0:
                    temp_dividend.append(x)
            
            # the remaining coefficients of the new dividend equal the respective coefficients of the old dividend
            else:
                x = float(dividend[i])
                temp_dividend.append(x)
        
        # in each step, append the leading coefficient of the dividend to the list of the coefficients of the quotient
        quotient.append(float(dividend[0]))
        
        # after each step, replace the old dividend by the new dividend
        dividend = temp_dividend
        
        # after each step, the degree of the dividend decreases by one
        deg = deg - 1

    # when the divisor has a greater degree than the dividend, the division is completed, and the remaining terms form the remainder
    if deg < m:

        # append the remaining terms of the dividend to the remainder
        for i in range(len(dividend)):
            remainder.append(dividend[i])
        
        # if the remainder is non-trivial, and the list of remainder coefficients has some extraneous zeros at the beginning, remove them from the list
        if len(remainder) != 0 and remainder[0] == 0:
            
            # remove each zero one at a time as long as the first coefficient in the list is nonzero or the list does not reduce to one element 
            while(remainder[0] == 0 and len(remainder) != 1):
                remainder.remove(0)
        # if the list of the remainder coefficients is empty, that means that the remainder is zero, so just add one zero to this list
        else:
            remainder.append(0)
    
    # earlier, we rescaled the divisor polynomial to a monic polynomial to simplify computations. To account for this, we have to rescale the quotient back
    # that is because of the equation: dividend = quotient * divisor + remainder = (quotient*div) * (divisor/div) + remainder
    # to obtain the actual quotient, we need to multiply all coefficients of the quotient we obtained by div (= the rescaling factor)
    actual_quotient =[]

    # if div = 1, we don't need to rescale, so we only consider the case when div != 1   
    if div != 1:
        
        # iterate over each coefficient of the quotient
        for i in range(len(quotient)):
            
            # append the coefficient after rescaling back 
            actual_quotient.append(float(quotient[i] / div))
    
    # as said above, if div = 1, we're done        
    else:
        actual_quotient = quotient
    
    # return two lists: the coefficients of the quotient & the coefficients of the remainder
    result = [actual_quotient, remainder] 
    return result
    
if __name__ == "__main__":
    main()
