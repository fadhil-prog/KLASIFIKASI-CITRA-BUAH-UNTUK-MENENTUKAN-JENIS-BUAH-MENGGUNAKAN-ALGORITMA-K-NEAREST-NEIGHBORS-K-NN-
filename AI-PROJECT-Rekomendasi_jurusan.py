def tanya_fakta(pertanyaan):
    while True:
        jawaban = input(pertanyaan + " (y/n): ").lower()
        if jawaban == 'y':
            return True
        elif jawaban == 'n':
            return False
        else:
            print("Masukkan hanya 'y' untuk ya atau 'n' untuk tidak.")

print("=== Sistem Rekomendasi Jurusan Kuliah ===")
print("Silakan jawab pertanyaan berikut untuk menentukan minat dan kemampuan Anda:\n")

fakta_siswa = {
    'suka_logika': tanya_fakta("Apakah Anda suka logika?"),
    'suka_matematika': tanya_fakta("Apakah Anda suka matematika?"),
    'suka_teknologi': tanya_fakta("Apakah Anda tertarik pada teknologi?"),
    'suka_gambar': tanya_fakta("Apakah Anda suka menggambar?"),
    'suka_estetika': tanya_fakta("Apakah Anda menyukai estetika visual (keindahan tampilan)?"),
    'suka_biologi': tanya_fakta("Apakah Anda suka biologi?"),
    'suka_laboratorium': tanya_fakta("Apakah Anda suka kegiatan di laboratorium?")
}

def cocok_teknik_informatika(fakta):
    return fakta['suka_logika'] and fakta['suka_matematika'] and fakta['suka_teknologi']

def cocok_dkv(fakta):
    return fakta['suka_gambar'] and fakta['suka_estetika']

def cocok_kedokteran(fakta):
    return fakta['suka_biologi'] and fakta['suka_laboratorium']

def backward_chaining(fakta):
    hasil = []

    if cocok_teknik_informatika(fakta):
        hasil.append("Teknik Informatika")
    if cocok_dkv(fakta):
        hasil.append("Desain Komunikasi Visual (DKV)")
    if cocok_kedokteran(fakta):
        hasil.append("Kedokteran")

    return hasil

rekomendasi = backward_chaining(fakta_siswa)

print("\n=== Rekomendasi Jurusan ===")
if rekomendasi:
    for jurusan in rekomendasi:
        print("- " + jurusan)
else:
    print("Maaf, tidak ditemukan jurusan yang cocok berdasarkan jawaban Anda.")
