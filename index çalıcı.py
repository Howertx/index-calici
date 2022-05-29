from requests import *

print("*--------------------*\n  İndex Çalıcı v1.0\n*--------------------*")
site = input("İndexini çalmak istediğiniz sitenin urlsini girin (https://www.turkhackteam.org gibi olmalı.) >> ")
index = get(f'{site}')
if index.status_code == 403:
    print("Hedef sitenin bot korumasından dolayı bu işlem gerçekleştirilemiyor.")
else:
  with open ("index.txt", "w") as dosya:
     dosya.write(index.text)
  print("Hedef sitenin indexi çalınıp index.txt dosyasına kaydedilmiştir.")

