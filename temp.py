### search 
file= []
def search(name):
    if name in file:
        print(file)
    else:
        print("not available")
name = input("Enter name")
search(name)
return

def search(extension):
    if extension in file:
        print(file)
    else:
        print("not available")
extension = input("Enter extension")
search(extension)
return

def search(content):
    if content in file:
        print(file)
    else:
        print("not available")
content = input("Enter content")
search(content)
return
