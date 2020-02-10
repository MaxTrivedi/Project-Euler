n = 600851475143
factor = 5
while factor * factor < n:
     while n % factor == 0:
         n = n / factor
     factor += 1
print(n)