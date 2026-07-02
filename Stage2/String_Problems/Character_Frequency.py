word = input("Enter a word : ") 
char = input("Enter the Character : ")

count=0

for ch in word:
    if ch == char:
     count +=1

print(f"'{char}' appears {count} times .")
char = input("Enter the Character : ")

count=0

for ch in word:
    if ch == char:
     count +=1

print(f"'{char}' appears {count} times .")