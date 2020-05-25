def collatz(start):
    current = start
    sequence = [current]
    while current != 1:
        if current%2 == 0:
            current = current/2
        elif current%2 != 0:
            current = 3*current +1
        sequence.append(int(current))
    return sequence

max_length = 0
greatest_collatz = 0
for i in range(10,1000000):
    current_length = len(collatz(i))
    if current_length > max_length:
        max_length = current_length
        greatest_collatz = i
print("Maximum: ", greatest_collatz, max_length)