word = input("Enter a word : ") 

left = 0

right = len(word) - 1


is_Palindrome = True

while left < right :
    if word[left] == word[right]:
        left += 1
        right -=1
       
    else:
        is_Palindrome = False
        break

if(is_Palindrome):
    print("Its a Palindrome ")
else:
    print("Its not a Palindrome ")
   