# -*- coding: utf-8 -*-

print("Dobrodošli v igri ugani skrito številko!")

skrita_stevilka = "19"

ugani_stevilko = raw_input("Vpišite številko med 1 in 100: ")

while ugani_stevilko != skrita_stevilka:
    ugani_stevilko = raw_input("Vstavite 5€ in poizkusite ponovno: ")
else:
    if ugani_stevilko == skrita_stevilka:
        print ("Čestitamo, zadeli ste 1000€!")
