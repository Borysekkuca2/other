def main():
    x = int(input())
    y = int(input())
    print("gcd of {} and {} is {}". format(x, y, gcd(x, y)))
    print("lcm of {} and {} is {}". format(x, y, lcm(x, y)))

def gcd(x, y):
    
    # if variables are not integers, return error
    if not (isinstance(x, int) or isinstance(y, int)):
        print("need integers")
        return False
    
    # if variables are nonpositive, return error    
    if x <= 0 or y <= 0:
        print("need positive integers")
        return False
        
    # call the larger variable "larger", and the smaller "smaller"    
    if x > y:
        larger = x
        smaller = y
    else:
        larger = y
        smaller = x
    
    # define the divisor
    remainder = larger - ((larger // smaller) * smaller)

    # this while loop corresponds to the steps in the Euclidean Algorithm. For details of how the algorithm works, see here: https://www.math.rutgers.edu/~greenfie/gs2004/euclid.html
    while remainder != 0:
        temp = larger
        larger = smaller
        smaller = remainder
        remainder = larger - ((larger // smaller) * smaller)
        
    # if the smaller number divides the larger, then the remainder is zero and the gcd equals the smaller number
    if remainder == 0:
        return smaller

def lcm(x, y):
    # if variables are not integers, return error
    if not (isinstance(x, int) or isinstance(y, int)):
        print("need integers")
        return False
    
    # if variables are nonpositive, return error    
    if x <= 0 or y <= 0:
        print("need positive integers")
        return False
    
    # compute the lcm using tha fact that lcm(x,y) * gcd(x,y) = x*y
    lcm = (x*y)/gcd(x,y)
    
    # write down lcm as an integer
    lcm = int(lcm)
    
    return lcm

if __name__ == "__main__":
    main()
