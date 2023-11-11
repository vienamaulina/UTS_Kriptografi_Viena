def prepare_text(plain_text):
    # Menghapus spasi dan mengganti J dengan I
    plain_text = plain_text.replace(" ", "").replace("J", "I")
    # Menyusun teks dalam pasangan jika ada huruf ganda
    i = 0
    while i < len(plain_text) - 1:
        if plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[:i + 1] + 'X' + plain_text[i + 1:]
        i += 2
    # Menyusun teks dalam pasangan jika jumlah huruf ganjil
    if len(plain_text) % 2 != 0:
        plain_text += 'X'
    return plain_text

def create_playfair_matrix(key):
    key = key.replace(" ", "").replace("J", "I")
    key = "".join(dict.fromkeys(key))  # Menghapus duplikat karakter
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = list(key)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_char_positions(matrix, char):
    for row in range(5):
        if char in matrix[row]:
            col = matrix[row].index(char)
            return row, col

def playfair_cipher(plain_text, key):
    plain_text = prepare_text(plain_text)
    matrix = create_playfair_matrix(key)
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i + 1]
        row1, col1 = find_char_positions(matrix, char1)
        row2, col2 = find_char_positions(matrix, char2)

        if row1 == row2:  # Jika dalam baris yang sama
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Jika dalam kolom yang sama
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]
        else:  # Jika tidak ada yang sama
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]

    return cipher_text

def playfair_decipher(cipher_text, key):
    matrix = create_playfair_matrix(key)
    decrypted_text = ""
    for i in range(0, len(cipher_text), 2):
        char1, char2 = cipher_text[i], cipher_text[i + 1]
        row1, col1 = find_char_positions(matrix, char1)
        row2, col2 = find_char_positions(matrix, char2)

        if row1 == row2:  # Jika dalam baris yang sama
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Jika dalam kolom yang sama
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
        else:  # Jika tidak ada yang sama
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]

    return decrypted_text

def main():
    key = input("Masukkan kunci: ").upper()
    plain_text = input("Masukkan teks yang ingin dienkripsi: ").upper()
    
    cipher_text = playfair_cipher(plain_text, key)
    decrypted_text = playfair_decipher(cipher_text, key)
    
    print("Teks asli:", plain_text)
    print("Teks yang dienkripsi:", cipher_text)
    print("Teks yang didekripsi:", decrypted_text)

if __name__ == "__main__":
    main()
