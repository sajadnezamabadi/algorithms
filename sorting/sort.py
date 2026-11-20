n = int(input("Enter the number of elements: "))

numbers = list(map(int, input("Enter the elements separated by space: ").split()))

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(*numbers)