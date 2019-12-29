import random

print('='*50)
print("Permainan Tebak Angka Ajaib Antara 1-50")
print('='*50)


#komputer memiliki angka acak dari 1-50
angka= random.randint(1,51)
#atur angka
maksim_tebak = 5
nomor_tebakan = 0
tebakan_benar = False
teks_soal = 'Tebakan ke-{} .Masukan Angka Tebakan Anda [1-50]:'   #?

#Bagian Perulangan

while not tebakan_benar and not nomor_tebakan >= maksim_tebak:     #?
    nomor_tebakan = nomor_tebakan +1
    tebakan = input (teks_soal.format(nomor_tebakan))   #?
    tebakan = int (tebakan)
    if tebakan == angka:
        tebakan_benar =True
    elif tebakan >angka:
        print("Angka Anda Lebih Besar")
    else:
        print("Angka Anda Lebih Kecil")
#Kondisi
if tebakan_benar:
    print("Hebat Angka Ajaib {} Berhasil Anda Tebak Dalam {} kali tebakan ".format(angka,nomor_tebakan))
    masukan=str(input("apakah ingin bermaian lagi [y/t]"))
    if masukan == 'y':
        import tebak
    elif masukan == 't':
        print ("selamat tinggal")
   
else:
    print("*"*50)
    print(" ANDA TIDAK BERHASIL MENEBAK ANGKA AJAIB {}".format(angka))
    print("*"*50)
    masukan=str(input("Apakah Anda Ingin bermaian lagi [y/t]: "))
    if masukan == 'y':
        import tebak
    elif masukan == 't':
        print ("Selamat Tinggal !!!")
        print("#"*50)
    else:
        print("Error")
   

    
   