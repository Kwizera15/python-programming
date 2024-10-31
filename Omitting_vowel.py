def remove_vowels(name):
    vowels="aeiouAEIOU"
    text=""
    for char in name:
        if char not in vowels:
            text+="".join(char)
    return text
name=input("\nEnter the name: ")
print(f"Omitted name is: {remove_vowels(name)}")
