from dataclasses import dataclass
from models import Person
 
@dataclass
class Api:
    people:list[Person] = [Person("Keven",14,False,1234.45),Person("Antonio",15,True,100.1), Person("Davi",11,False,230.3),Person("Rosimeire",36,True,300000.0)]
    
    
    def transaction(self, who_send:str, who_receive, value:float):
        try:
            who_send_founded = None
            who_receive_founded = None
            
            for i in self.people:
                if i.get_name() == who_send:
                    who_send_founded = i
                else:
                    print("There is no who send")
                if i.get_name() == who_receive:
                    who_receive_founded = i
                else:
                    print("There is no who receive")
                    
            who_send_founded.get_balance()-=value
            who_receive_founded.get_balance()+=value
            
            data = {
                "who_send":who_send_founded,
                "who_receive":who_receive_founded,
                "value":value
            }
            return data
        except:
            print("ERRRO")
        
            
            
        
            
                
            
                 
            
        