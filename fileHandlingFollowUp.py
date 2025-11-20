file_name_prompt = input("Enter name of the file :")
file_name = f"{file_name_prompt}.txt"


def createReadFile(name_of_file):
    f = open(name_of_file, "x")
    f.close()

    contents = input("File contents here ... :")
    f = open(name_of_file, "w")
    if len(contents) > 0:
        f.write(contents)
    else:
        f.write("This is temporary file content")
    f.close()

    f = open(name_of_file, "r")
    print(f.read())


try:
    createReadFile(file_name)
except FileExistsError as e:
    print("File already Exists")
    command = input("Do you want to proceed yes/no :").lower()
    if command == "yes":
        file_name_prompt = input("Enter name of the file :")
        file_name = f"{file_name_prompt}.txt"
        try:
            createReadFile(file_name)
        except FileExistsError:
            print("File Exists end of program...")
    elif command == "no":
        print("Program ends here...")
    else:
        print("Program ends here... Invalid Command")
        print(e)
