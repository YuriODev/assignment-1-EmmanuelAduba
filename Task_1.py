# Your solution comes here

# Don't know how to fix the code

seconds = int(input("Enter the number of seconds: "))

hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60

zero = "0"
if hours < 10:
    seconds = zero + str(seconds)
    minutes = zero + str(minutes)
print(f"{hours}:{minutes}:{seconds}")