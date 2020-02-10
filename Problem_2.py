count = 0
x = 0
y = 1
count = 0
sum = 0
#while count < 10:
while x < 4000000:
    #print(x)
    z = x + y
    x = y
    y = z
    count+=1
    if x%2 == 0:
        sum += x
print(sum)