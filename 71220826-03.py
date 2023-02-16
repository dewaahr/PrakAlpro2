#INPUT
input_detik=int(input("Masukan Jumlah Detik :"))

#PROSES
detik_hari= 24*3600
jumlah_hari=input_detik//detik_hari
sisa_detik=input_detik%detik_hari
jumlah_jam=sisa_detik//3600
sisa_detik=sisa_detik%3600
jumlah_menit=sisa_detik//60
sisa_detik=sisa_detik%60

#OUTPUT
print('Jadi ',input_detik,"detik = ",jumlah_hari,"hari",jumlah_jam,"jam",jumlah_menit,"menit",sisa_detik,"detik")