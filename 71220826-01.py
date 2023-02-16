#INPUT
X_satu=int(input('Masukan Nilai X-1:'))
Y_satu=int(input('Masukan Nilai Y-1:'))
X_dua=int(input('Masukan Nilai X-2:'))
Y_dua=int(input('Masukan Nilai Y-2:'))
#PROSES
rumus_jarak=float(((X_dua-X_satu)**2)+((Y_dua-Y_satu)**2))**0.5
rumus_jarak=int(rumus_jarak*10)/10
#OUTPUT
print("Jarak Antara Titik Satu dan Titik Dua adalah %.1f"% rumus_jarak)
