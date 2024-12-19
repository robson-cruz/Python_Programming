# Even or odd number with index
# Given a list of numbers, create a list of tuplas where the first element is the index and the second,
# a "pair" or "unique" string corresponding to the number.
numbers = [10, 15, 20, 25]

# Saída esperada: [(0, 'even'), (1, 'odd'), (2, 'even'), (3, 'odd')]
print([(number[0], 'even' if number[1] % 2 == 0 else 'odd') for number in enumerate(numbers)])
