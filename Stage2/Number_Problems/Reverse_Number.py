n= int(input("Enter the N value: "))

digit = 0
reverse = 0 

while n != 0 :
    digit = n % 10
    reverse = reverse * 10 + digit 
    n //= 10

print(reverse)

