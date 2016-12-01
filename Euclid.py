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
    
    # define the remainder
    remainder = larger - ((larger // smaller) * smaller)

    # The Euclidean Algorithm begins here. For more details, see: https://www.math.rutgers.edu/~greenfie/gs2004/euclid.html
    # In a given step of the algorithm, the larger number is divided by the smaller number to get the remainder.
    # Then, the smaller number becomes the new larger number, and the remainder becomes the new smaller number.
    # The algorithm ends when the smaller number divides the larger (equivalently, when the remainder is zero).
    # gcd is equal to the smaller number in the last step.

    # Repeat the division as long as remainder is nonzero
    while remainder != 0:
        
        # store the larger number temporarily
        temp = larger
        
        # the smaller number becomes the new larger number
        larger = smaller
        
        # the remainder becomes the new smaller number
        smaller = remainder
        
        # compute the new remainder
        remainder = larger - ((larger // smaller) * smaller)
        
    # when the remainder is zero, the gcd equals the smaller number
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
