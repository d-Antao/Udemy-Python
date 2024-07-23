import execisio_account
import exercisio_person


class Bank:
    def __init__(
        self,
        bank_branchs:list[int]|None=None,
        clients:list[exercisio_person.Person]|None=None,
        accounts:list[execisio_account.Account]|None=None
    ):
        self.bank_branchs = bank_branchs or []
        self.clients = clients or []
        self.accounts = accounts or []
    
    def _check_bank_branch(self,bank_branch):
        if bank_branch.bank_branch in self.bank_branchs:
            return True
        return False
        
    def _check_client(self,client):
        if client in self.clients:
            return True
        return False
    
    def _check_account(self,account):
        if account in self.accounts:
            return True
        return False
    def _check_account_belongs_client(self,account,client):
        if account is client.account:
            return True
        return False
        
        
    def authenticate(self,client: exercisio_person.Person,account:execisio_account.Account):
        return self._check_account(account) and \
            self._check_client(client) and \
                self._check_bank_branch(account) and \
                    self._check_account_belongs_client(account,client)
                
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.bank_branchs!r}, {self.accounts!r}, {self.clients})'
        return f'{class_name}{attrs}'
                  
            
if __name__ == '__main__':
    c1 = exercisio_person.Client('Luiz',30)
    cc1 = execisio_account.CheckingAccount(111,222,0,0)
    c1.account = cc1
    c2 = exercisio_person.Client('Pedro',30)
    cp2 = execisio_account.SavingsAccount(112,223,100)
    c2.account = cp2
    bank = Bank()
    bank.clients.extend([c1,c2])
    bank.accounts.extend([cc1,cp2])
    bank.bank_branchs.extend([111,222])
    
    
    if bank.authenticate(c1,cc1):
        cc1.deposit(10)
        c1.account.deposit(100)
        print(c1.account)
    