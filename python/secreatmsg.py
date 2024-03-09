message = input("type your secret msg here: ")

encryted_message = ""
for letter in message:
    encryted_message += chr(ord(letter) + 3)

print("your encryted message is: ", encryted_message)

