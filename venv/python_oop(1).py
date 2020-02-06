# CS1527
# A collection of vehicle classes used to illustrate various aspects of
# OO programming in Python 3.
# Last edit: 9 January 2020

class Boat:
    __doc__ = 'Simple Boat Class'
    
    """Represent boat characteristics."""
    
    def __init__(self, dis ='', blst = '', **kwargs):
        super().__init__(**kwargs)
        self._displacement = dis
        self._ballast = blst

    def __str__(self):
        return "Boat: " + self.get_fullname()
        
    def get_fullname(self):
        """Return an aquatic descriptive name."""       
        long_name = '~~ ' + str(self._displacement) + ', ' + str(self._ballast) + ' ~~'
        return long_name.title()
        
    def clean_hull(self):
        """Simple method on boat class that prints a message."""
        print('Stripping barnacles...')
               
class Car:
    __doc__ = 'Car Class'
    
    """Class attribute to hold list of Cars created."""
    all_cars = []
    
    def __init__(self, ma ='', mo = '', yr = '', **kwargs):
        super().__init__(**kwargs)
        self._make = ma
        self._model = mo
        self._year = yr
        """_odometer_reading should only be 
        accessed/modified via internal methods"""
        self.__odometer_reading = 0
        Car.all_cars.append(self)
    
    @classmethod
    def print_inventory(cls):
        for item in cls.all_cars:
            print(item.get_fullname())
    
    def __str__(self):
        return "Car: " + self.get_fullname()
        
    def __len__(self):
        return self.get_car_age() 
        
    def __eq__(self, other):
        return (self._make == other._make and 
             self._model == other._model)
        
    def get_fullname(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self._year) + ', ' + self._make + \
            ' ' + self._model
        return long_name.title()

    def get_car_age(self, current_year=2017):
        """Return the age of the car in years."""
        return current_year - self._year
        
    def increment_odometer(self,miles):
        """Increment private odometer reading by a distance in miles."""
        self.__odometer_reading += miles      
    
class AmphibiousVehicle(Car, Boat):
    __doc__ = 'Amphibious Vehicle Class'
    
    """Represent amphibious vehicle – using multiple inh."""

    def __init__(self, fp ='', **kwargs):
        """Initialize attributes of the parent classes."""
        super().__init__(**kwargs)
        """Initialize attrs specific to an amphibious vehicle."""
        self._snorkel = False
        self._folding_prop = fp  
        
    def convert(self):
        """Convert the vehicle for travel in water."""
        if self._folding_prop:
            print('Waiting for propeller ...')
        print('Preparing to sail ...')
        
    # No str() or get_fullname() defined here
    # Can we call print(<object>) on an AmphibiousVehicle instance?
        
class ElectricCar(Car):
    """Represent aspects specific to electric vehicles."""

    def __init__(self, **kwargs):
        """Initialize attributes of the parent class."""
        super().__init__(**kwargs)
        """Initialize attributes specific to an electric car."""
        self._max_range = 300
        self.__battery_level = 100
        
    def __str__(self):
        return "ElectricCar: " + self.get_fullname()

    def report_battery(self):
        """Report private attribute holding battery level."""
        print(self.__battery_level)

    def charge_battery(self):
        """Increase __battery_level as charging."""
        if self.__battery_level < 100:
            self.__battery_level +=1
        else:
            print('Danger - overcharging!')
            
    def get_fullname(self):
        """Return a high voltage descriptive name."""       
        long_name = '** ' + super().get_fullname() + ' **'
        return long_name.title()

# To create instances, try:

# boat1 = Boat(dis=200,blst=True)



boat=Boat(dis=200,blst=True)
print(boat)
car1 = Car(ma='Audi',mo='Q7',yr=2004)
car2=Car(ma='adasd',mo='asas',yr=2002)
Car.print_inventory()
print(car2.get_car_age())
car1.increment_odometer(23)
print(car1._Car__odometer_reading)
print(Car.all_cars[0])

amph1 = AmphibiousVehicle(ma='VW',mo='Schwimmwagen',yr=1944,dis=900,blst=True,fp=True)
print(amph1)
print(amph1._snorkel)
ecar1 = ElectricCar(ma='Tesla',mo='Model S',yr=2016)
print(ecar1.get_fullname())
ElectricCar.print_inventory()
print(ElectricCar.all_cars[3])