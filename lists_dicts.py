cars = ['Audi', 'BMW', 'Honda', 'Hyundai', 'Peugeot', 'Mercedes']
user = ['John', 56.5, 44, True]

animals = ['dog', 'fish', 'lion', 'eagle']
first_animal = animals[0]
second_animal = animals[1]
print(first_animal)

last_animal = animals[-1]
print(last_animal)

animals.append('bee')
animals.append('cat')
animals.append('ant')
print(animals)
print(f'Number of animals is {len(animals)}')

print(cars[0:3])
print(cars[-3:-1])

emails = []
emails.append('a1@example.com')
emails.append('a2@example.com')
emails.append('a3@example.com')
print(emails)

friend = {
    'first_name': 'Dave',
    'age': 30,
    'hobby': 'music',
    'city': 'Wrocław',
    'average_grade': 3.76
}
friends_name = friend['first_name']
print(friends_name)
print(friend['average_grade'])

friend['average_grade'] = 4.45
print(friend['average_grade'])

friend['favourite_car'] = cars[-2]
print(friend)


song1 = {'title': 'Black Dog', 'artist': 'Led Zeppelin'}
song2 = {'title': 'Smoke on the water', 'artist': 'Deep Purple'}
song3 = {'title': 'Like a stone', 'artist': 'Audioslave'}

songs = [song1, song2, song3]
print(songs)

print(f'Second song title is {songs[1]["title"]}')