print('Cześć!')

imie = 'Dorota'
print(imie)

nazwisko = "Dobro" # str
# int
wiek = 111
wzrost_cm = 183
wzrost_m = 1.83
waga = 74.5

# bool
mieszka_w_krakowie = True
mieszka_w_warszawie = False

mat1 = 2 + 4*5
print(mat1)
bmi = waga / wzrost_m**2
print(bmi)

print(2 == 4)
dwa_rowne_cztery = 2 == 4

print(dwa_rowne_cztery)

print(type(dwa_rowne_cztery))
print(type(imie))
print(type(wiek))

czy_imie_jest_stringiem = isinstance(imie, str)
print('Wartość zmiennej:', czy_imie_jest_stringiem)
