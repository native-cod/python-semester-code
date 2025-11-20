name = "sample file.txt"
# Create file if not exist
file = open(name, "w")
file.close()

# Read file r mode
file = open(name, "r")
print(file.read()+ "nothing in file line added in print() method")
file.close()

# Write into file w mode
file = open(name, "w")
file.write("Welcome to file handling in python")
file.close()


file = open("name.txt", "w+")

prev = file.tell()
print(f"{prev} pointer position at start")
file.write("Added content")
print(f"{file.tell()} pointer position mid")
file.write("Extra added content")
# print(file.read())
print(f"{file.tell()} pointer position end")
file.close()

file = open("businessman.png", "rb")
content = file.read()
file.close()

file = open("copied.png", "wb")
file.write(content)
file.close()