sum_of_squares = 0
square_of_sums = 0
for i in range(1,100+1):
    sum_of_squares += i*i
    square_of_sums += i 
square_of_sums = square_of_sums**2
print(square_of_sums - sum_of_squares)