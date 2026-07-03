word = input("Enter a word : ")

result= ""

for ch in word:
    if ch not in " ":
        result+=ch

print(result)