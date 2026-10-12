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




# word = input("Enter a Word : ")

# left = 0 

# right = len(word)-1



# while left < right :

#     if word[left] != word[right]:
#         print("Its not a Palindrome")
#         break

#     left += 1
#     right -= 1

# else:
#     print("Its  a Palindrome")


           
