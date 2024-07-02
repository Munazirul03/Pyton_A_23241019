nama = input('masukan nama anda terlebih dahulu!!!: ')
print(f'selamat datang di program pembeda bilangan ganjil genap 1 sampai dengan 500 sederhana dengan ka {nama}')
user = int(input('masukan angka yang mau anda bedakan: '))
batas = 500

for angka in range(user, batas + 1):
    if angka % 2 == 0:
        print(f'{angka} ini adalah bilangan genap')
    else:
        print(f'{angka} ini adalah bilangan ganjil')


# print(60*'=')
# # tes khodam
# import random
# print('selamat datang di cek khodam')


# while True:
#     nama = input('masukan nama anda terlebih dahulu: ')
#     tanya = input('apakah anda mau cek khodam?: ')
#     if tanya.lower() == 'iya':
#         khodam = ['kebab rendang', 'sundel bolong', 'tuyul mullet', 'ayam kayang', 'sapi birahi',  ]

#         hasil =random.choice(khodam)

#         print(f'khodam {nama} adalah {hasil}')
#         break

#     else:
#         print('program close')


    


print(60*'=')
# random

import random
random = random.randint(1, 10)

while True:
    user =int(input('pilih angka 1 sampai 10: '))
    if user == random:
        print('tebakan anda benar')
        break
    else:
        print('tebakan anda salah!!!\nsilahkan menebak ulang!')


