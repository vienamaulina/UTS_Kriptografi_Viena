def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key = key.upper()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.islower():
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ''
    key = key.upper()
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.islower():
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

def main():
    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    key = input("Masukkan kunci enkripsi: ")

    encrypted_text = vigenere_encrypt(plain_text, key)
    print("Teks terenkripsi:", encrypted_text)

    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Teks terdekripsi:", decrypted_text)

if __name__ == "__main__":
    main()
