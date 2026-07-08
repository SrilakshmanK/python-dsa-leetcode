arr = [1 , 3 , 4 , 9 , 7]

target = int(input("Enter the search value : "))



for i in range (len(arr)):
    if arr[i] == target:
        print(f"Target ({arr[i]}) is found in index : {i}")
        break
 
else:
    print("Not found")

