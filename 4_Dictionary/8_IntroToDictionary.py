# Dictionaries are Key:value pairs.
# Example: Our mobile phone directory.
# The Key is name and Value is phone number

car_companies = {
    "Toyota": "Japan",
    "General Motors": "USA",
    "Volkswagen": "Germany",
    "Ford": "USA",
    "Honda": "Japan",
    "PSA Peugeot Citreon": "France",
    "Hyundai-Kia": "South Korea",
    "Mercedes Benz": "USA",
    "Suzuki Motor Corporation": "Japan"
}

print(car_companies)

car_companies['Tata Motors'] = "India"  # add a value
print(car_companies)

print(car_companies.keys())  # print keys
print(car_companies.values())  # print values

car_companies["Mercedes Benz"] = "Germany"  # update a value
print(car_companies)

print(car_companies.pop("Toyota"))
print(car_companies)

print("Lenth of Dictionary:", len(car_companies))  # prints length of dictionary

print("Sorted Dictionary: ", sorted(car_companies))  # sorted, on basis of keys.

print("Hyundai" in car_companies)  # checks if the given value is present or not, then returns True or false
print("Tata Motors" in car_companies)
print("Germany" in car_companies)  # tests for key only not value

print(car_companies.items())  # prints them as a pair of tuples

###########------------------BONUS------------------###########

# TUPLES in Python
'''
A tuple is a collection which is ordered and "unchangeable".
You can neither add anything to it, nor remove anything from it.  
In Python tuples are written with round brackets.
'''
print("\n") # adds new lines

tuple1 = (23.56, "hello", 89, "mumbai city", 2018 / 6, 7, 23.56, 5, 7, 89)
print("Tuple: ", tuple1)
print("Length of Tuple: ", len(tuple1)) # length of tuple
print("Value at 3rd index: ",tuple1[3]) # indexing, finding out value at index 2

# Tuple Methods
x = tuple1.count(89) # this will count the number of times, "89" occurs in tuple
print("89 occurs: ", x , " :times in this tuple")

y = tuple1.index(7) # this will print the first index of "7" in the tuple
print("Index of '7' in tuple is: ", y)
