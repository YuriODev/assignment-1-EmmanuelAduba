# Your solution comes here

# Used AI to answer this question.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

for num in range(a, b+1):
    if num % c == 0:
        print(num)
