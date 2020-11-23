print('Fitur Pengisian Rencana Studi')

# cek kondisi tahun masuk dan max pengambilan sks
nim = input('Masukkan NIM : ')     # input nim user
panjang_nim = 10    # nim harus berisi 10 angka
max_sks = 0     # nilai default sks
if nim[5:7] == '20' and len(nim) == panjang_nim:    # jika diantara index 5-7 nim berisi angka 20
    max_sks = 20    # max sks yang bisa diambil 20
    print('Anda mahasiswa tahun pertama. Anda bisa mengambil paling banyak', max_sks, 'SKS.\n')
elif nim[5:7] == '19' and len(nim) == panjang_nim:    # jika diantara index 5-7 nim berisi angka 19
    max_sks = 22    # max sks yang bisa diambil 22
    print('Anda mahasiswa tahun kedua. Anda bisa mengambil paling banyak', max_sks, 'SKS.\n')
elif nim[5:7] == '18' and len(nim) == panjang_nim:    # jika diantara index 5-7 nim berisi angka 18
    max_sks = 24    # max sks yang bisa diambil 24
    print('Anda mahasiswa tahun ketiga. Anda bisa mengambil paling banyak', max_sks, 'SKS.\n')
elif nim[5:7] == '17' and len(nim) == panjang_nim:    # jika diantara index 5-7 nim berisi angka 17
    max_sks = 26    # max sks yang bisa diambil 26
    print('Anda mahasiswa tahun keempat. Anda bisa mengambil paling banyak', max_sks, 'SKS.\n')
else:
    print('NIM Tidak Valid\n')   # jika nim salah program akan mencetak pesan NIM tidak valid
    print('Pengisian Rencana Studi Selesai')
    finish = False

jum_sks = 0
while True:
    print('Jumlah SKS yang diambil : ', jum_sks)    # otomatis mencetak jumlah sks yang diambil
    matkul = input('Masukkan nama mata kuliah yang diambil atau X untuk selesai : ')    # input matkul yang diambil
    if matkul == "X" or matkul =="x":   # Jika user input 'X'
        print('Pengisian Rencana Studi Selesai')
        break       # program berhenti jika matkul berisi 'x' atau 'X'
    else:   # jika tidak program akan meminta user memasukkan beban sks
        sks = int(input('Masukkan beban SKS mata kuliah tersebut : '))    # input beban sks
        print('Berhasil mengambil matakuliah', matkul, 'dengan bobot', sks, 'SKS.\n')
        jum_sks += sks    # jumlah sks bertambah ketika user memasukkan beban sks
        if jum_sks == max_sks:      # program berhenti jika jumlah sks setara dengan maximal sks
            print('Jumlah SKS yang diambil : ', jum_sks)
            print('Pengisian Rencana Studi Selesai')
            break
        elif jum_sks > max_sks:     # program akan berhenti jika jumlah sks melebihi maximal sks, dan akan mencetak pesan berikut
            print('Jumlah SKS melebihi SKS maksimal. Pengisian Rencana Studi selesai')
            break