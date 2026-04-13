def greet_user():
    name = input("What is your name? ")
    return f"Hello, {name}! Welcome to the Python programming world."

if __name__ == "__main__":
    greeting = greet_user()
    print(greeting)
    
