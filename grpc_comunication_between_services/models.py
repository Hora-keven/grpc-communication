from dataclasses import dataclass
@dataclass
class Person:
    name:str
    age:int
    have_debts:bool
    balance:float
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_have_debts(self):
        return self.have_debts
    def get_balance(self):
        return self.balance
    def set_balance(self, new_value:float):
        self.balance = new_value