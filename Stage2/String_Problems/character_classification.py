word = input("Enter a word : ") 

Ucase=0
Lcase=0
digit=0
space=0
spl=0

for ch in word:
    if ch.isupper():
        Ucase+=1
    elif ch.islower():
        Lcase+=1
    elif ch.isdigit():
        digit+=1
    elif ch == " ":
        space+=1
    else :
        spl+=1

print(f"Word : {word}")
print(f"UpperCase : {Ucase}")
print(f"LowerCase : {Lcase}")
print(f"Digit : {digit}")
print(f"Space : {space}")
print(f"Special Character : {spl}")