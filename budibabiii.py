gajiperJam = int(input('Masukan Gaji perjam yang anda inginkan : '))
jamkerjaSeminggu = int(input('Masukan jumlah jam kerja dalam seminggu : '))

gajiKotor = 5*(gajiperJam*jamkerjaSeminggu)
gajiBersih = gajiKotor-(gajiKotor*0.14)
uangBaju = gajiBersih*0.1
uangAlatTulis = gajiBersih*0.01
sisaUang = gajiBersih-uangBaju-uangAlatTulis
uangSedekah = sisaUang*0.25
# uangSedekahYatim = ((uangSedekah-uangSedekah%1000)*0.3)
uangSedekahYatim= 0.3 * uangSedekah
# uangSedekahYatim=(1000*0.3)*(uangSedekah//1000)
uanguntukDuafa = uangSedekah-uangSedekahYatim



print("Total gaji yang dapatkan selama libur musim panas adalah \t\t\t: Rp",gajiKotor)
print("Total gaji yang dapatkan selama libur musim panas setelah membayar pajak adalah : Rp",gajiBersih)
print("Jumlah uang yang digunakan untuk membeli baju adalah \t\t\t\t: Rp",uangBaju)
print("Jumlah uang yang digunakan untuk membeli Alat tulis adalah \t\t\t: Rp",uangAlatTulis)
print("Total uang yang disedekahkan adalah \t\t\t\t\t\t: Rp",uangSedekah)
print("Jumlah uang yang disedekahkan kepada Anak Yatim adalah \t\t\t\t: Rp",uangSedekahYatim)
print("Jumlah uang yang disedekahkan kepada Kaum Dhuafa adalah \t\t\t: Rp",uanguntukDuafa)