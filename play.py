
seznam_starosti= ["tina", 25, "metka", 30, "marko", 27]

dictionary_starosti= {"tina": 25, "metka": 30, "marko": 27}


print(dictionary_starosti["tina"])
#ali
print(dictionary_starosti.get("kaja", 1)) #bolje to , ker ne izpiše errorja če ključ ne obstaja(prim.:"kaja"), lahko tudi dodamo podatke v tem načinu
print(dictionary_starosti) #kaja še ni zares dodana

dictionary_starosti["kaja"] =22
print(dictionary_starosti) #kaja je zdej na seznamu