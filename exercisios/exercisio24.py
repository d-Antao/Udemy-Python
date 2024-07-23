

class Carro:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,nome):
        self._motor = nome
        
    @property    
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self,nome):
        self._fabricante = nome
        
        
class Motor:
    def __init__(self,nome):
        self.nome = nome
        
class fabricante:
    def __init__(self,nome):
        self.nome = nome
        
        
fusca = Carro('Fusca')
volkswagen = fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0

print(fusca.nome,fusca.fabricante.nome,fusca.motor.nome)

fiat_uno = Carro('Uno')
fiat = fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0

print(fiat_uno.nome,fiat_uno.fabricante.nome,fiat_uno.motor.nome)

focus = Carro('Focus titanium')
ford = fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome,focus.fabricante.nome,focus.motor.nome)