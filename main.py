'''
Vizsga
​
A program vizsgázók nevét és pontszámát kéri be. Eldönti és kiírja, hogy a vizsgázó sikeresen vizsgázott-e. 
A vizsga sikeres, ha legalább 48 pontot ért el a vizsgázó.
A program kérje be a vizsgázók nevét és az elért pontszámokat! 
Írja meg azt a függvényt, ami eldönti, hogy a vizsga sikeres-e! 
A függvény paramétere a vizsgázó által elért pontszám, a visszatérési értéke logikai érték: igaz, ha a vizsga sikeres, hamis, ha sikertelen. 
Ezt a függvényt használja fel a programjában!
A program kérdezgesse addig újabb és újabb vizsgázó nevét és pontszámát, amíg a vizsgázó nevének megadásakor üres bemenetet nem kap! 
Ilyen akkor történik, ha a felhasználó egyszerűen Entert nyom, anélkül hogy bármit is begépelne.
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Add meg a vizsgázó nevét! Linus Torvalds
Add meg a pontszámát! 121
Linus Torvalds vizsgája sikeres.
Add meg a vizsgázó nevét! Dennis Ritchie
Add meg a pontszámát! 119
Dennis Ritchie vizsgája sikeres.
Add meg a vizsgázó nevét! Steve Ballmer
Add meg a pontszámát! 27
Steve Ballmer vizsgája sikertelen.
Add meg a vizsgázó nevét! 

-----
'''

def sikeres(vizsga):
  if vizsga >= 48:
     return True
  else:
      return  False

while True:
  nev = input("Add meg a vizsgázó nevét! ")
  if nev == "":
      break

  else:
       pontszam =int(input("Add meg a pontszámát!"))
       if sikeres(pontszam):
           print(f'{nev} vizsgája sikeres. ')
       else:
          print(f'{nev} vizsgája sikertelen.')