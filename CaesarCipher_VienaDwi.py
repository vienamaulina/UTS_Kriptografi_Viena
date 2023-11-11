def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 256) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

def main():
    choice = input("Pilih operasi (1: Enkripsi, 2: Dekripsi): ")

    if choice == "1":
        plaintext = input("Masukkan teks yang akan dienkripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (angka): "))
        encrypted_text = caesar_cipher(plaintext, shift)
        print(f"Hasil enkripsi: {encrypted_text}")
    elif choice == "2":
        ciphertext = input("Masukkan teks yang akan didekripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (angka): "))
        decrypted_text = caesar_cipher(ciphertext, -shift)
        print(f"Hasil dekripsi: {decrypted_text}")
    else:
        print("Pilihan tidak valid. Pilih 1 untuk enkripsi atau 2 untuk dekripsi.")

if __name__ == "__main__":
    main()
