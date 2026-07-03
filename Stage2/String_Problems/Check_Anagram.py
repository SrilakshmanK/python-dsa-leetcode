word1 = input("Enter the word1 : ")
word2 = input("Enter the word2 : ")

is_anagram = True

if len(word1) != len(word2):
    print("Its not an Anagram.")
    exit()
else:
   
    for ch in word1 :
    
        count_1=0
        count_2=0

        for i in word1:
            if ch == i:
                count_1 += 1  
        
        for j in word2:
            if ch == j:
                count_2 += 1 

        if count_1 != count_2:
            is_anagram=False
            break

  
if is_anagram :
   print("Its an Anagram")
else:
   print("Its not an Anagram")