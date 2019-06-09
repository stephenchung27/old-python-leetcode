'''
Compute the Greatest Common Divisor

Design an efficient algorithm for computing the GCD of two nonnegative integers without using multiplication, divison, or the modulus operators.

Key assumption is that if y > x, then GCD(x, y) == GCD(x, y - x).
This is because if y is a multiple of x then y - x is also a multiple of x so GCD(x, y - x) will result in no loss of generality.
If y is not a multiple of x, then y - x is also not a multiple of x so GCD(x, y - x) will return the correct answer anyway will no loss of generality.
'''

def gcd(x, y):
    # If equal return x
    if x == y: return x

    # If x is greater than y, flip
    if x > y:
        return gcd(y, x)

    # If x is odd and y is even
    if not x & 1 and not y & 1:
        # Multiply by 2 any return value since both are divided by 2
        return gcd(x >> 1, y >> 1) << 1
    
    # If x is even and y is odd
    if not x & 1 and y & 1:
        return gcd(x >> 1, y)
    
    # If x is odd and y is even
    if x & 1 and not y & 1:
        return gcd(x, y >> 1)

    # If they are both even and y is a multiple of x, then x and y - x are divisible
    # If not recurse down to number until both are divisible
    return gcd(x, y - x)

print(gcd(7, 3))
print(gcd(6, 3))
print(gcd(4, 8))
print(gcd(21, 27))