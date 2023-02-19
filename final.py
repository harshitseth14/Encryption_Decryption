#Final
import decryption

choice = input("Would you like to Encrypt of decrypt your message : ").lower()

if choice == "encrypt":
    message = input("Enter your message : ").lower()
    shift = input("Type the shift number(Encription Key) :")

    decryption.encryption.encrypt(message,shift)
elif choice == "decrypt":
    a = input("Enter the encoded message : ")
    b = input("Type the shift number : ")
    decryption.decryption(a,b)