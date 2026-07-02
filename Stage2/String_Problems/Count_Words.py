words = input("Enter the words : ")

space = 0

for ch in words:
    if ch == " ":
        space+=1

count = space + 1 

print(f"Total words : {count}")