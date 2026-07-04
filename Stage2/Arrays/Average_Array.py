arr = [ 3 , 2 , 4 , 1 , 5]
# arr = []


sum_array=0
no_of_elements = len(arr)

if no_of_elements == 0:
 print("None")
 exit()

for i in range (no_of_elements):
 sum_array += arr[i]

average = sum_array/no_of_elements

print(average)





