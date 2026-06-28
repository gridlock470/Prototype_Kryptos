import random 

def Ceaser_Cypher(A):

    Shift_value_1 = random.randint(0, 25)
    Shift_value_2 = random.randint(0, 255)

    Encrypted_text = ""

    for char in A:
        if char.isalpha():
            if char.isupper():
                Encrypted_text = Encrypted_text + chr((ord(char) - 65 + Shift_value_1)% 26 + 65)
            else:
                Encrypted_text = Encrypted_text + chr((ord(char) - 97 + Shift_value_1) % 26 + 97)
        else:
            Encrypted_text = Encrypted_text + chr((ord(char) + Shift_value_2) % 256)

    return Encrypted_text, \Shift_value_1, Shift_value_2


if __name__ == "__main__":
    A = input("Enter your message: ")
    Ceaser_Cypher(A)
