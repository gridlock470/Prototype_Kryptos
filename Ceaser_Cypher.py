def Ceaser_Cypher(A):

    Shift_value_1 = 21
    Shift_value_2 = 139

    Encrypted_text = ""

    for char in A:
        if char.isalpha():
            if char.isupper():
                Encrypted_text = Encrypted_text + chr((ord(char) - 65 + Shift_value_1)% 26 + 65)
            else:
                Encrypted_text = Encrypted_text + chr((ord(char) - 97 + Shift_value_1) % 26 + 97)
        else:
            Encrypted_text = Encrypted_text + chr((ord(char) + Shift_value_2) % 256)

    print(Encrypted_text)


if __name__ == "__main__":
    A = input("Enter your message: ")
    Ceaser_Cypher(A)