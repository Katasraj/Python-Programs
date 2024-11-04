def greet(name):
    return f"hello {name}"


def main():
    user_name = input("Enter User name: ")
    greeting = greet(user_name)
    print(greeting)

def adding(a,b):
    print(a+b)


# This block will only execute if the script is run directly, not if it's imported as a module
if __name__ == main():
    main()
    adding()






