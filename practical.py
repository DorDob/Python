# Fizz buzz
number = 2

if number % 15 == 0:
    print('fizz buzz')
elif number % 5 == 0:
    print('fizz')
elif number % 3 == 0:
    print('buzz')
else:
    print('Nothing')

# Iteracja po liście słowników
songs = [
    {'title': 'Black Dog', 'artist': 'Led Zeppelin'},
    {'title': 'Smoke on the water', 'artist': 'Deep Purple'},
    {'title': 'Like a stone', 'artist': 'Audioslave'},
    {'title': 'Catch the Rainbow', 'artist': 'Rainbow'},
    {'title': 'One', 'artist': 'Metallica'}
]

for song in songs:
    print(song['title'])

for song in songs:
    if song['title'] == 'One':
        artist = song['artist']
        print(f'"One" by {artist}')

# Dopisywanie liczb podzielnych przez 3
numbers = [1, 3, 5, 18, 44, 139, 999, 1309, 2167, 49006]

divisible_by_three = []
non_divisible_by_three = []
for n in numbers:
    if n % 3 == 0:
        divisible_by_three.append(n)
    else:
        non_divisible_by_three.append(n)
print(f'Divisible by 3:{divisible_by_three}')
print(f'Non-divisible by 3: {non_divisible_by_three}')
