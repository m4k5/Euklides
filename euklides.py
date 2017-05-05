"""
Algorytm Euklidesa
  ___     _   _ _    _                        
 | __|  _| |_| (_)__| |___ ___      _ __ _  _ 
 | _| || | / / | / _` / -_|_-<  _  | '_ \ || |
 |___\_,_|_\_\_|_\__,_\___/__/ (_) | .__/\_, |
                                   |_|   |__/ 
Z dedykacja dla Pani Profesor Stajno :)
"""
# Start
liczba_a = int(raw_input("Podaj liczbe a: "))
liczba_b = int(raw_input("Podaj liczbe b: "))
a = liczba_a
b = liczba_b
c = 0
licznik = 1

# Check czy b juz na poczatku nie zostalo zadeklarowane jako zero
if b == 0:
	print("b wynosi 0. Koniec liczenia. NWD wynosi: " + str(a))
	exit()
	
# Liczenie
# ( <> w Pythonie znaczy "nie rowna sie". Zamiennie != )
while b<>0:
	print("\n\n\n")
	print("Runda " + str(licznik))
	c = a % b
	a = b
	b = c
	print("a = " + str(a))
	print("c = " + str(c))
	print("b = " + str(b))
	licznik = licznik + 1
print("OK, wiec NWD(" + str(liczba_a) + ";" + str(liczba_b) + ") = " + str(a))
zeby_program_sie_nie_zamykal_na_Windowsie = raw_input("Koniec. Nacisnij Enter, aby zamknac...")
