import numpy as np

def prepare_input(text, key_size):
    # Mengubah teks menjadi matriks sesuai dengan ukuran kunci
    matrix = []
    for char in text:
        if char.isalpha():
            matrix.append(ord(char) - ord('A') if char.isupper() else ord(char) - ord('a'))

    # Menambahkan padding dengan nilai 0 jika diperlukan
    while len(matrix) % key_size != 0:
        matrix.append(0)

    return np.array(matrix)

def hill_encrypt(plain_text, key_matrix):
    key_size = len(key_matrix)
    plain_matrix = prepare_input(plain_text, key_size)

    # Mengubah matriks teks menjadi matriks terenkripsi menggunakan kunci
    encrypted_matrix = np.dot(plain_matrix.reshape(-1, key_size), key_matrix) % 26

    # Mengembalikan teks terenkripsi
    return ''.join([chr(x + ord('A')) for x in encrypted_matrix.flatten()])

def main():
    # Memasukkan teks dan kunci enkripsi dari pengguna
    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    key_text = input("Masukkan kunci enkripsi (sebagai matriks, contoh: '9 7 11 13'): ")

    # Mengonversi kunci enkripsi menjadi matriks
    key_matrix = np.array([int(x) for x in key_text.split()]).reshape(-1, int(len(key_text.split())**0.5))

    # Memanggil fungsi enkripsi
    encrypted_text = hill_encrypt(plain_text, key_matrix)

    # Menampilkan teks terenkripsi
    print("Teks terenkripsi:", encrypted_text)

if __name__ == "__main__":
    main()
