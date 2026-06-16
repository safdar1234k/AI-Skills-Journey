with open("file.txt", "w") as file:
    file.write("Hello, Safdar!\nWelcome to AI skills journey.\n")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)

with open("file.txt", "a") as file:
    file.write("This is an additional line for checking append mode.\n")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)
