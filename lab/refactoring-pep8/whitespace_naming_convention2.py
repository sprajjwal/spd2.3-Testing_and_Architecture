# By Kami Bigdely
# PEP8 - whitespaces and variable names.
class pizza:

    def __init__ (
        self, obj, mybread_type, CHEESE_TYPE, 
        meatType,pizza_toppings,size
    ):
        obj.bread_type= mybread_type
        obj.cheese_type = CHEESE_TYPE
        obj.meatType= meatType
        obj.toppings = pizza_toppings
        obj.size = size        
    
    @classmethod
    def Create_ChicagoPizza(cls, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meatType= 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 
                    'chunky tomato sauce', 'onion']
        return cls(bread, cheese, meatType, toppings, size)    

    @classmethod
    def createCalifornia_pizza(cls, meat_Type,size):
        bread = 'thin crust'
        CHEESE = 'feta cheese'
        toppings =[ 'garlic', 'spinach', 'broccoli', 'olives', 
                    'red onion', 'red bell pepper']
        return cls(bread, CHEESE, meat_Type, toppings, size) 
    
    def printInfo(self):
        print('bread type is: ', self.bread_type)
        print('cheese type is: ', self.cheese_type)
        print('meat type is: ', self.meatType)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))

    
myPizza = pizza.createCalifornia_pizza('chicken', 'large')
myPizza.printInfo()