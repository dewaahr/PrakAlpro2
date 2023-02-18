# print('='*5,"Program menghitung berat badan ideal",'='*5)

tinggi_badan=float(input('Masukan Tinggi Badan Anda (m):'))
bmi_input=float(input('Masukan BMI (Body Mass Index) yang anda inginkan :'))

berat_badan = bmi_input*(tinggi_badan**2)
berat_badan= berat_badan

print(f"Jadi, Berat badan yang anda perlukan untuk memiliki BMI :{bmi_input} adalah : {berat_badan:.1f}Kg")