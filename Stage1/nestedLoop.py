# for i in range(3):
#   for j in range(2):
#     print(f"house {i} room{j}")

rows = int(input("Enter the # of rows :"));
columns =  int(input("Enter the # of columns :"));
symbol = input("Enter the symbol you wanted to print:");

for i in range (rows):
  for j in range(columns):
    print(symbol, end="")
  print()  
