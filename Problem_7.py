start = 0
end = 104743
primes =[]
for val in range(start, end + 1): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           primes.append(val)
print(primes[10001-1])