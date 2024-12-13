'''
mobile_model_name = input("Enter mobile model name : ")
tuple = (mobile_model_name , )
print("Mobile model name tuple : ",tuple)
'''

'''
mobile_models = ("iPhone 14", "OnePlus 11", "Oppo Find X5")

# Finding the length of the tuple
#length = len(mobile_models)
print("Length of the tuple:", len(mobile_models))

# Finding the index of an element
element = "OnePlus 11"
index = mobile_models.index(element)
print("Index of tuple :",index)
'''

'''
# Sample tuples for movie names
tuple1 = ("Inception", "The Matrix", "Interstellar")
tuple2 = ("The Shawshank Redemption", "Pulp Fiction", "The Godfather")

# Concatenating the two tuples
tuple3 = tuple1 + tuple2
print("tuple1",tuple1,"\ntuple2",tuple2)
# Display the result
print("Concatenated tuple:", tuple3)
'''

'''
tuple = ("Apple","Banana","cherry","Apple","Mango")
print("Apple count in tuple :",tuple.count("Apple"))
'''

'''
# Sample tuple
tuple = ("Inception", "The Matrix", "Interstellar", "The Shawshank Redemption")
print("Tuple : ",tuple)
# Display the results
print("Accessing first element :",tuple[0])
print("Accessing second element :",tuple[1])
print("Accessing third element :",tuple[2])
'''

'''
# Sample tuple for bike model names
bike_models = ("Harley-Davidson", "Ducati Panigale", "Yamaha YZF-R1", "Kawasaki Ninja")

# Element to check
#model_to_check = "Ducati Panigale"

# Checking if the model exists in the tuple
if "Ducati Panigale" in bike_models:
    print("yes")
else:
    print("no")
'''

'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
'''

'''
# Sample tuple of integers
numbers_tuple = (34, 67, 23, 89, 12, 45)
print(numbers_tuple)
# Finding the maximum and minimum elements
#max_number = max(numbers_tuple)
#min_number = min(numbers_tuple)

# Display the results
print("Maximum number:", max(numbers_tuple))
print("Minimum number:", min(numbers_tuple))
'''

'''
brands_tuple = ("Apple", "Samsung", "Nike", "Adidas", "Sony")
print("Tuple : ",brands_tuple)
x = list(brands_tuple)
x.remove("Adidas")
z = tuple(x)
print("After removing adidas from tuple :",z)
'''


tuple1 = (10, 20, 60, 30, 60, 40, 60)
# Count all occurrences of item 60
count = tuple1.count(60)
print(count)
# Output 3

count = tuple1.count(600)
print(count)
print(sorted(tuple1))