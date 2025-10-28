name = input("user name : ")
password = input("password : ")

file_name = name + ".txt"
try:
    file_write = open(file_name, 'x')
    file_write.write(f"user name: {name} password: {password}")
    file_write.close()

    file_read = open(file_name, 'r')
    print(file_read.read())

except FileExistsError:
    print("Sorry File already exists choose a different name")

# FileExistsError
