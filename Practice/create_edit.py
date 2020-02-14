def create_edit(name, content):
    try:
        with open(name, "a+") as file:
            file.read()
            file.write(content)
    except FileNotFoundError:
        with open(name, "w") as file:
            file.write(content)

filename = input('Full name(with ext.) of file to edit/create: ')
addcontent = input("Enter content that you want: ")
addcontent += "\n"

create_edit(filename, addcontent)
