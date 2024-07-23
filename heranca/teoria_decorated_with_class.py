def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict =self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

#class MyReprMixin:
#    def __repr__(self):
#       class_name = self.__class__.__name__
#        class_dict =self.__dict__
#        class_repr = f'{class_name}({class_dict})'
#        return class_repr


@add_repr
class Time:
    def __init__(self,name) :
        self.name = name
        
   
@add_repr   
class Planet:
    def __init__(self,name):
        self.name = name
        
#Time = add_repr(Time)
#Planet = add_repr(Planet)

portugal = Time('Portugal')
brazil = Time('Brazil')

terra = Planet('Terra')
marte = Planet('Marte')


print(portugal)
print(marte)