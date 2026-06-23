n= int(input("Enter the N value: "))


sum = 0
temp = 0

while n != 0 :
    temp = n % 10
    sum += temp
    n //= 10

print(sum)

