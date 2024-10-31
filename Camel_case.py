def camel_case(text):
    case=""
    for char in text:
        if char.isupper():
            case+="_"+char.lower()
        else:
            case+=char
    return case
text=input("\nEnter the text: ")
name=camel_case(text)
print("The snake case is: ",name)

    