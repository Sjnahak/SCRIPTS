customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified" : True
}

print (customer["name"])

###use "get" it will retun none if any key does not exist
print (customer.get("age"))


#############################################################
phone = input("Phone: ")

digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "Four"
    }

output = ""
for ch in phone:
    #output += digits_mapping.get(ch, "!") + " "
    output = output + digits_mapping.get(ch, "!") + " "
print(output)

#############################################################
