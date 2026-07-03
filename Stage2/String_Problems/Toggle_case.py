word = input("Enter a word : ")

result= ""

for ch in word:
    if ch.isupper():
     
        result+=ch.lower()
    elif ch.islower():
        result+=ch.upper()
    else:
        result+=ch
 
  

print(result)