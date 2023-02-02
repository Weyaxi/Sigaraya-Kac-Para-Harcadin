pakette_kac_sigara = "20"
kac_yil = input("\nKaç yıldır sigara kullanıyorsunuz: ")
gunde_kac_tane = input("Bir günde kaç tane sigara içtiğinizi yazınız: ")
paket_fiyati = input("Bir paket sigaraya kaç lira harcıyorsunuz: (Eğer bu değer yıldan yıla farklılık göseriyorsa lütfen ortalama bir değer giriniz): ")

haftada_ictigin = (int(gunde_kac_tane)) * 7
ayda_ictigin = (int(gunde_kac_tane)) * 30
yilda_ictigin = (int(gunde_kac_tane)) * 365
toplam_ictigin = (int(gunde_kac_tane) * int(kac_yil)) * 365

haftada_harcadigin = (int(gunde_kac_tane) / int(pakette_kac_sigara) * int(paket_fiyati)) * 7
ayda_harcadigin = (int(gunde_kac_tane) / int(pakette_kac_sigara) * int(paket_fiyati)) * 30
yilda_harcadigin = (int(gunde_kac_tane) / int(pakette_kac_sigara) * int(paket_fiyati)) * 365
toplam_harcadigin = (int(gunde_kac_tane) / int(pakette_kac_sigara) * int(paket_fiyati) * int(kac_yil)) * 365

print("""
 ____
|  _ \ __ _ _ __   ___  _ __ _   _ _ __  _   _ ____
| |_) / _` | '_ \ / _ \| '__| | | | '_ \| | | |_  /
|  _ < (_| | |_) | (_) | |  | |_| | | | | |_| |/ /
|_| \_\__,_| .__/ \___/|_|   \__,_|_| |_|\__,_/___|
           |_|
""")

print("--------------------------------------------")
print(f"Bir haftada içtiğiniz toplam sigara sayısı: {haftada_ictigin}")
print(f"Bir haftada sigaraya harcadığınız toplam para: {haftada_harcadigin} TL")
print("-------------------------------------------- \n")

print("--------------------------------------------")
print(f"Bir ayda içtiğiniz toplam sigara sayısı: {ayda_ictigin}")
print(f"Bir ayda sigaraya harcadığınız toplam para: {ayda_harcadigin} TL")
print("-------------------------------------------- \n")

print("--------------------------------------------")
print(f"Bir yılda içtiğiniz toplam sigara sayısı: {yilda_ictigin}")
print(f"Bir yılda sigaraya harcadığınız toplam para: {yilda_harcadigin} TL")
print("-------------------------------------------- \n ")

print("--------------------------------------------")
print(f"Girdiğiniz verilere göre {kac_yil} yılda içtiğiniz toplam sigara sayısı: {toplam_ictigin}")
print(f"Girdiğiniz verilere göre {kac_yil} yılda sigaraya harcadığınız toplam para: {toplam_harcadigin}")
print("--------------------------------------------")