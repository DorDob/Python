import datetime
import random

# Listy zawierające dane do losowania
female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']

people_list = []
current_year = datetime.datetime.now().year
for i in range(0, 10):
    firstname = random.choice(female_fnames) if i < 5 else random.choice(male_fnames)
    lastname = random.choice(surnames)
    age = random.randint(5, 45)
    people_list.append(
        {
            'firstname': firstname,
            'lastname': lastname,
            'email': f'{firstname}.{lastname}@example.com',
            'age': age,
            'country': random.choice(countries),
            'adult': age > 17,
            'birth_year': current_year - age
        }
    )

for p in people_list:
    print(f"Hi! I'm {p['firstname']} {p['lastname']}. I come from {p['country']} and I was born in {p['birth_year']}")
