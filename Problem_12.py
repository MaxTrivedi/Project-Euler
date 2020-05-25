
def divisors(n):
    result = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            result += 1
    result *= 2
    if sqrt_n**2 == n:
        result -= 1
    return result

triangle_numers = [1]
for i in range(2, 1000000):
    triangle_numers.append(i+triangle_numers[-1])
    triangle_numers.pop(0)
    if divisors(triangle_numers[0]) > 0:
        print(triangle_numers[0], divisors(triangle_numers[0]))
    if divisors(triangle_numers[0]) > 500:
        break