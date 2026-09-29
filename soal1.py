def konversi_suhu(nilai, satuan):
    "Mengubah suhu C ke F atau F ke C"
    if satuan == 'C':
        hasil = (nilai * 9 / 5) + 32
    elif satuan == 'F':
        hasil = (nilai - 32) * 5 / 9
    else:
        hasil = "Satuan harus 'C' atau 'F'"
    return hasil

suhu = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan satuan (C/F): ").upper()
print("Hasil konversi:", konversi_suhu(suhu, unit))