#We will be using caesar cipher in which every number is shifted by a certain number.
#We will need to remeber the encription key(shifts) inorder to decode the message

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5']


def encrypt(plain_text,shift_amt):
    encoded_message = ""
    for letter in plain_text:
        position=alphabets.index(letter)
        new_position = int(position)+int(shift_amt)
        new_letter = alphabets[new_position]
        encoded_message += new_letter

    print(f"The encoded message is -> {encoded_message}")


# message = input("Enter your message : ").lower()
# shift = input("Type the shift number(Encription Key) :")

# encrypt(message,shift)