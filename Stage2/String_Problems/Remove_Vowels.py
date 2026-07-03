word = input("Enter a word : ")

result= ""

for ch in word:
    if ch not in "aeiouAEIOU":
  
        result += ch

print(result)