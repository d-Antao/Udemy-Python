"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Account(ABC):
    
    def __init__(self,bank_branch:int,num_account:int,balance:float = 0):
        self.bank_branch = bank_branch
        self.num_account = num_account
        self.balance = balance
    
    @abstractmethod    
    def withdraw(self,value:float) -> float:... 
    
    
    def deposit(self,value:float) :
        self.balance += value
        self.details(f'(Deposit = {value} $)')
     
    def details(self,msg:str='')->None:
        print('--------------------------------------------')
        print(f'Your bank branch is {self.bank_branch}')
        print(f'Your number account is {self.num_account} {self.__class__.__name__}')
        print(f'{msg} \nYour balance is {self.balance:.2f}')
        print('--------------------------------------------')
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.bank_branch!r}, {self.num_account!r}, {self.balance})'
        return f'{class_name}{attrs}'
        

class CheckingAccount(Account):
    def __init__(self,bank_branch:int,num_account:int,balance:float = 0, limit:float =0):
        super().__init__(bank_branch, num_account, balance)
        self.limit = limit
     
    def withdraw(self, value:float)->float:
        value_after_withdrawal = self.balance - value
        MAX_LIMIT = -self.limit
        
        if value_after_withdrawal < MAX_LIMIT:
            self.details(f'Withdrawal denied')
            raise ValueError(f'The withdrawal amount exceeds the balance')
        
        self.balance -= value
        self.details(f'(withdrew = {value} $ your limit is {MAX_LIMIT})')
        return self.balance 
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.bank_branch!r}, {self.num_account!r}, {self.balance}, {self.limit})'
        return f'{class_name}{attrs}'
            

class SavingsAccount(Account):
    def __init__(self,bank_branch:int,num_account:int,balance:float = 0):
        super().__init__(bank_branch, num_account, balance)
        
    def withdraw(self, value:float) -> float:
        value_after_withdrawal = self.balance - value
             
        if value_after_withdrawal < 0:
            self.details(f'Withdrawal denied')
            raise ValueError(f'The withdrawal amount exceeds the balance')
        
        self.balance -= value
        self.details(f'(withdrew = {value} $ )')
        return self.balance 

    

            
if __name__ == '__main__':
    cp1 = SavingsAccount(123,12345,200)
    cp1.withdraw(200)
    cp1.deposit(40)
    print('########')
    cc1 = CheckingAccount(0000,345,0,500)
    cc1.withdraw(500)
    cc1.deposit(40)