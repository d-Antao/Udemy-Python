import execisio_account


class Person:
    def __init__(self,name:str,age:int)->None:
        self.name = name
        self.age = age
        
    
    @property    
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name:str):
        self._name = name
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age:int):
        self._age = age 
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'
    
    
    
    
class Client(Person):
    def __init__(self,name:str,age:int)->None:
        super().__init__(name,age,)
        self.account: execisio_account.Account | None = None
        






if __name__ == '__main__':
    
    p1 = Person('Maria',22)
    c1 = Client('Miguel',25)
    c1.account = execisio_account.CheckingAccount(111,222,0,0)
    print(p1)
    print(c1)
    print(c1.account)