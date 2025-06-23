import random

# 1. Kullanıcının parolasını içerebileceği tüm karakterleri içeren bir değişken oluşturun
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# 2. Bir değişken oluşturun ve kullanıcıdan parolanın uzunluğunu girmesini isteyin
uzunluk = int(input("Parolanızın kaç karakter olmasını istersiniz? "))

# 3. Programın oluşturulan parolayı saklayacağı bir değişken oluşturun
parola = ""

# 4. Karakter değişkeninden rastgele bir karakter seçmek ve bunu oluşturulan parolanın bulunduğu değişkene eklemek için bir döngü ve random kütüphanesi kullanın
for i in range(uzunluk):
    parola += random.choice(karakterler)

# 5. Elde edilen parolayı konsola yazdırın
print("Oluşturulan Parola:", parola)





