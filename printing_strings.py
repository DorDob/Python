imie = 'Adrian'
nazwisko = "Gonciarz"

ksiazka = 'Dziady'
print('Przeczytałem ostatnio "Dziady"')
print("Jadłem coś w McDonald's")
print('Jadłem coś w McDonald\'s')

print('Mam na imię ' + imie + '. Moje nazwisko to ' + nazwisko + '.')
print('Mam na imię {}. Nazywam się {}.'.format(imie, nazwisko))
print('Nazywam się {1}. Mam na imię {0}.'.format(imie, nazwisko))
print(f'Nazywam się {nazwisko}. Mam na imię {imie}.')

print(f'Przeczytałem ostatnio "{ksiazka}"')

moj_tekst = f'Nazywam się {nazwisko}. ' \
            f'Mam na imię {imie}. ' \
            f'Przeczytałem ostatnio "{ksiazka}"'

moj_opis = """Mieszkam w Krakowie.
Pracuję w IT.
Lubię kawę."""

print(moj_opis)

city = 'Kraków'
job = 'IT'
favourite_drink = 'coffee'

moj_opis_2 = f"""I live in {city}.
I work in {job}.
I love drinking {favourite_drink}."""
print(moj_opis_2)
