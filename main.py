basket1 = {"Apple","Banana","Guava","Pomegranate"}
basket2 = {"Kiwi","Strawberry","Mango"}
print("Basket 1:",basket1)
print("Basket 2:",basket2)

basket1.add("Orange")
print("Basket 1 after adding orange:",basket1)

common_fruits = basket1.intersection(basket2)
print("Common fruits :",common_fruits)

import array as arr
num_of_common_fruits = arr.array('i',[3,5,2,4])
print("Number of common fruits:",num_of_common_fruits)

num_of_common_fruits.insert(0,1)
num_of_common_fruits.append(6)
print("Number of common fruits:",num_of_common_fruits)

num_of_count_4 = num_of_common_fruits.count(4)
print("The number of times 4 appears:",num_of_count_4)

num_of_common_fruits.reverse()
print("Common fruits reversed:",num_of_common_fruits)

print("")
print("=========Class Basket Fruit Organizer==========")
print("Basket 1:",basket1)
print("Basket 2:",basket2)
print("Shared fruits:",common_fruits)
print("Fruit counts:",num_of_common_fruits)
print("=====")
