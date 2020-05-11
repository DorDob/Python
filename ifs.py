day = 'saturday'

if day == 'sunday':
    print("I'm sleeping!")
    print("I'm eating dinner at the restaurant.")
elif day == 'saturday':
    print("I'm sleeping a bit longer")
    print("I go for a walk")
else:
    print("I'm working.")
    print("I'm not going out today.")

print('After the IF statement')


cars = ['Mercedes', 'BMW', 'Toyota', 'Honda', 'Peugeot', 'Audi', 'Nissan', 'Polonez']

car = cars[-1]

if car == 'Mercedes':
    print('Germany')
elif car == 'BMW':
    print('Germany')
elif car == 'Audi':
    print('Germany')
elif car in ['Toyota', 'Nissan', 'Honda']:
    print('Japan')
elif car == 'Peugeot':
    print('France')
else:
    print('Unknown')
