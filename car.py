class Car:
    def __init__(self, model, color, tank_volume, average_mpg):
        self.model = model
        self._color = color
        self.tank_volume = tank_volume
        self.avg_mpg = average_mpg
        self.gas = 2
        self.total_distance = 0


    @property
    def color(self):
        return self._color

    @color.setter
    def distance_remaining(self):
        return  self.gas / self.avg_mpg *100
    def color(self, value):
        self._color = value
    def fill_gas(self, gas_liters):
        self.gas = self.gas = gas_liters
    def drive(self, distance_km):
        gas_required = distance_km/100 * self.avg_mpg
        if gas_required > self.gas:
            print("There's not enough gas in tank!")
        else:
            print('Driving')
            self.total_distance += distance_km
            self.gas -= gas_required

my_car = Car ('Hyundai', 'Gray', 50, 10)
my_car.drive(200)
my_car.fill_gas(22.5)
my_car.drive(200)
my_car.drive(50)
my_car.fill_gas(20)
my_car.drive(200)
