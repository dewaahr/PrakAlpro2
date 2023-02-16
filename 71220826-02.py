jarak_inch = int(input("Masukan Jarak dalam Inch :"))
feet =jarak_inch//12
inch_2=jarak_inch-(feet*12)
yard = feet//3
feet_2=feet-(yard*3)
mile = yard//1760
yard_2=yard-(mile*1760)
print('Jadi ',jarak_inch,"Inch = ",mile,"mile",yard_2,"yard",feet_2,"feet",inch_2,"inch")