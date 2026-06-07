# | Feature    | List | Tuple | Set |
# | ---------- | ---- | ----- | --- |
# | Ordered    | ✅    | ✅     | ❌   |
# | Changeable | ✅    | ❌     | ✅   |
# | Duplicates | ✅    | ✅     | ❌   |

# List → ordered collection
# Tuple → ordered, read-only collection
# Set → unique items + fast existence checks

cart = ['bread' , 'coffee' , 'banana']  # lists
cart.append('milk');

location = (11.0168, 76.9558 , 11.0168)  #tuples 
total_location = location.count(11.0168)

Student_Ids = {112 , 113 ,114 , 115 , 116 , 117 , 118 , 119 , 110 , 111 , 111}

print(f"Lists : {cart}")
print(f"Tuples : {location}")
print(f"Total Locations : {total_location}")
print(f"Sets : {Student_Ids}")