import random
import time

print("Tere! See programm genereerib sulle automaatselt ees- ja perekonnanime ning muud andmed sinu virtuaalse uue karakteri kohta.")  
print("")

nimed = ["Mari", "Kati", "Kadi", "Kristi", "Karmen", "Lea", "Laili", "Lembi", "Laine", "Laura", "Maarika", "Made", "Marianne", "Imbi", "Helvi", "Jüri", "Jaanus", "Kaarel", "Väino", "Peeter", "Toomas", "Kalev", "Sulev", "Aare", "Tauno", "Mauno", "Janek", "Rauno", "Raul", "Rein"]
perenimed = ["Tamm", "Saar", "Sepp", "Mägi", "Kask", "Kukk", "Ilves", "Oja", "Lepik", "Mitt", "Saks", "Järv", "Raud", "Tuuleklaas", "Mehine", "Lambine", "Tuuline"]
töökohad = ["Rätsep", "Politseinik", "Kiirabiametnik", "Medõde", "Ortopeed", "IT-spetsialist", "Selveri klienditeenindaja", "Rimi laojuhataja", "Maxima kärulükkaja", "Tarkvaraarendaja", "Günekoloog", "Automehaanik", "Kokk", "Kaubavedaja", "Kalapoe teenindaja", "Kaitseväe juhataja", "Tuletõrjuja"]


vanus = random.randint(1,100)
pikkus1 = random.randint(50,70)
pikkus2 = random.randint(70,100)
pikkus3 = random.randint(100,130)
pikkus4 = random.randint(130,190)
pikkus5 = random.randint(177,194)

eesnimi = random.choice(nimed)
perenimi = random.choice(perenimed)
pikknimi = f"{eesnimi} {perenimi}"
töökoht = random.choice(töökohad)

print("Nimi: " + str(pikknimi))
print("Vanus: " + str(vanus))
if vanus > 17 and vanus < 88:
    print("Töökoht: " + str(töökoht))
    
if vanus == 1 and vanus == 2:
    print("Pikkus: " + str(pikkus1))
    
elif vanus > 3 and vanus < 6:
    print("Pikkus: " + str(pikkus2))
        
elif vanus > 6 and vanus < 9:
    print("Pikkus: " + str(pikkus3))
        
elif vanus > 10 and vanus < 79:
    print("Pikkus: " + str(pikkus4))
        
elif vanus > 79:
    print("Pikkus: " + str(pikkus5))
    
time.sleep(2)
print("")    
print("Uuesti genereerimiseks taasjooksuta käesolev skript (F5)")
####
