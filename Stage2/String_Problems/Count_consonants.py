word = input("Enter a word : ")

count=0

for ch in word:
    if ch in "aeiouAEIOU":
        continue
    elif ch.isdigit():
        continue
    elif ch.isalpha() :
        count +=1
   

print(f"Consonants = {count}")
