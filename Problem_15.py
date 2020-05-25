def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

i = 20
j = 20

routes = (factorial(i+j)/(factorial(i)*factorial(j)))
print(int(routes))