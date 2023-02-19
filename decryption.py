import encryption

def decryption(encoded,shift_amt):
    decoded = ""
    for letter in encoded:
        position = encryption.alphabets.index(letter)
        new_position = int(position) - int(shift_amt)
        new_letter = encryption.alphabets[new_position]
        decoded = decoded + new_letter

    print(f"The decoded message is -> {decoded}")

# a = input("Enter the encoded message : ")
# b = input("Type the shift number : ")
# decryption(a,b)