# Time complexity: O(log(n))
# Space complexity: 0(1)
# Power is a O(log(n)) function
def nth_fibonacci(n: int) -> int:
    sqrt5 = math.sqrt(5)
    fibn = pow((1 + sqrt5) / 2, n + 1) - pow((1 - sqrt5) / 2, n + 1)
    return int(fibn / sqrt5)

# Time complexity: O(n)
# Space complexity: O(1)
# Dynamic programming with previous two fibonacci numbers
def nth_fibonacci(n: int) -> int:
    if n <= 0: return 0
    if n <= 2: return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Time complexity: O(n)
# Space complexity: O(n)
# Dynamic programming with recursion
def nth_fibonacci(n: int) -> int:
    if n <= 0: return 0
    cache = {}
    def _nth_fibonacci(n: int) -> int:
        if n == 1: return 1
        if n == 2: return 1
        if n in cache: return cache[n]
        res = _nth_fibonacci(n - 1) + _nth_fibonacci(n - 2)
        cache[n] = res
        return res
    return _nth_fibonacci(n)