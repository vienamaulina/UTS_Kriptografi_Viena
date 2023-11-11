import string

# Fungsi untuk mengenkripsi teks dengan Vigenère Cipher
def vigenere_encrypt(text, key):
    result = []
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char in string.ascii_letters:
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            if char.islower():
                result_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result.append(result_char)
        else:
            result.append(char)
    return ''.join(result)

# Daftar pengguna dan kata sandi yang telah dienkripsi
users = {
    "user1": "KEY",  # Ganti "KEY" dengan kata sandi yang ingin digunakan
    "user2": "SECRET",
}

def register():
    username = input("Masukkan username: ")
    if username in users:
        print("Username sudah digunakan. Silakan coba lagi.")
        return
    password = input("Masukkan password: ")
    encrypted_password = vigenere_encrypt(password, username)
    users[username] = encrypted_password
    print("Pendaftaran berhasil.")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in users:
        encrypted_password = vigenere_encrypt(password, username)
        if users[username] == encrypted_password:
            print("Login berhasil. Selamat datang, " + username + "!")
        else:
            print("Login gagal. Password salah.")
    else:
        print("Login gagal. Username tidak ditemukan.")

while True:
    print("\nMenu:")
    print("1. Daftar")
    print("2. Login")
    print("3. Keluar")
    choice = input("Pilih tindakan (1/2/3): ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
