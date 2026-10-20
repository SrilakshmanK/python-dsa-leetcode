n = int(input("Enter the number : "))

for row in range (1 , n + 1):

   if row == n : 
      for i in range (2 * n - 1):
         print("*",end="")
   else:      
       
        for j in range (n - row):
            print(" ",end="")

        print("*",end="")

        if row > 1 : 
          for k in range (2 * row - 3 ):
             print(" ",end="")
          print("*",end="")

   print()