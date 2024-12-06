person = {
    "name": "John",
    "surname": "Doe",
    "age": 30,
    "hobbies": ["reading", "travelling", "coding"],
    "city": "New York",
    "occupation": "Software Developer",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "married": False,
}
# Display name
print("Name:", person["name"])

# Display hobby
print("Hobby:", person["hobbies"][0])

# Display the entire contents of the dictionary
print("Entire dictionary:", person)

# Change surname to 'Nowak'
person["surname"] = "Nowak"

# Change person's marriage status
person["married"] = not person["married"]

# Add gender: 'male'
person["gender"] = "male"

# Add a new hobby: 'bicycle'
person["hobbies"].append("bicycle")

# Add work phone to existing phones: '313131444'
person["work_phone"] = "313131444"

# Display the entire contents of the dictionary (iterate over dictionary items)
for key, value in person.items():
    print(f"{key}: {value}")
