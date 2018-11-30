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

print(car_companies.items())  # prints them as a pair of tuples
