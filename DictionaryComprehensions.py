d1 = {x:x**2 for x in range(1,10)}
print("Squares: ",d1)

d2 = {x for x in range(1,11) if x%2==0}

print("EvenNumbers: ",d2)


my_contacts = {
    "Alice": {
        "phone_number": "123-456-7890",
        "email_address": "alice@example.com"
    },
    "Bob": {
        "phone_number": "987-654-3210",
        "email_address": "bob@example.com"
    }
}

new_contact = {
    "Naga":{
"phone_number": "123-456-8580",
        "email_address": "naga@example.com"
    }
}

print(my_contacts)
print(100*'*')
my_contacts.update(new_contact)
print("After Merging dictonary: ", my_contacts)


