n = int(input("Enter the number : "))

original=n
strong_num=0
result=1


while n != 0 :
    digit = n % 10

    for i in range (1, digit+1):
        result = result * i

    strong_num += result
    result=1
    n //= 10

if original == strong_num:
    print("Its a strong number . ")
else:
    print("Its not a strong number . ")

