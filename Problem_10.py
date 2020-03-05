primes =[]
val = 0
while val < 2000000:
    if val > 1: 
        for n in range(2, val): 
            if (val % n) == 0: 
                break
        else: 
            primes.append(val)
    val += 1
print(sum(primes))
