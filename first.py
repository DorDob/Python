print('Hello World!')

title = 'Ghost Dog'
age = 31
email = 'adrian.gonciarz@gmail.com'
likes_pizza = False

print(type(title))
type(age)
type(email)
type(likes_pizza)

print(f'My favourite movie is {title}. '
      f'My age is {age}. '
      f'My email is {email}. '
      f'Do I like Hawaiian pizza? {likes_pizza}')

animals = ['dog', 'cat', 'fish']
numbers = [13, 44, 18.4]

print(animals[1])
print(numbers[2])
print(numbers[-2])

animals.append('elephant')
animals.append('monkey')
# komentarz
print(len(animals))
print(animals)

numbers.append(137)
numbers.append(6.16)
numbers.append(.02)

print(f'Ilość liczb: {len(numbers)}')

actor = {
    'name': 'Johnny Depp',
    'age': 60,
    'country': 'United States',
    'alive': True
}

print(actor['age'])
print(actor['alive'])

actor['movie'] = 'Pirates of the Carribean'
actor['age'] = 45