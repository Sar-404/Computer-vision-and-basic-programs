alphabets="abcdefghijklmnopqrstuvwxyz"
def caesar(text,shift):
    new_alphabet=alphabets[shift:] + alphabets[:shift]
    transition = str.maketrans(alphabets,new_alphabet)
    new_text = text.translate(transition)
    return new_text
print(caesar(input("Enter the text"),int(input("Enter the shift number"))))
