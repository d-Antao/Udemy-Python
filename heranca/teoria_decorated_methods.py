

def my_repr(self):
    class_name = self.__class__.__name__
    class_dict =self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr
    

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

def my_planet(method):
    def intern(self,*args,**kwarg):
        result = method(self,*args,**kwarg)
        if 'Earth' in result:
            return 'You are in home'
        return result
    return intern


@add_repr
class Time:
    def __init__(self,name) :
        self.name = name
        
   
@add_repr   
class Planet:
    def __init__(self,name):
        self.name = name
    
    @my_planet   
    def say_name(self):
        return f'Name of this Planet is {self.name}'
        
#Time = add_repr(Time)
#Planeta = add_repr(Planeta)

portugal = Time('Portugal')
brazil = Time('Brazil')

earth = Planet('Earth')
mars = Planet('Marte')


print(portugal)
print(mars)

print(earth.say_name())
print(mars.say_name())