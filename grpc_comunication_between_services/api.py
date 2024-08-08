from dataclasses import dataclass
from models import Person
import grpc
 
people:list[Person] = [Person("Keven",14,False,1234.45),Person("Antonio",15,True,100.1), Person("Davi",11,False,230.3),Person("Rosimeire",36,True,300000.0)]

@dataclass
class Api:
    
    def transaction(self, who_send:str, who_receive, value:float):
        try:
            who_send_founded = None
            who_receive_founded = None
            
            for i in people:
                if i.get_name() == who_send:
                    who_send_founded = i
                else:
                    print("There is no who send")
                if i.get_name() == who_receive:
                    who_receive_founded = i
                else:
                    print("There is no who receive")
                    
            if who_send_founded.get_balance() > value:   
                who_send_founded.set_balance(round(who_send_founded.get_balance()-value,2))
                who_receive_founded.set_balance(round(who_receive_founded.get_balance()+value,2))
       
                data = {
                    "who_send":who_send_founded,
                    "who_receive":who_receive_founded,
                    "value":value,
                    "message":"Transaction successfully!"
                }
                return data
            else:
                data = {
                    "who_send":who_send_founded,
                    "who_receive":who_receive_founded,
                    "value":value,
                    "message":f"You dont have money, your balance its {who_send_founded.get_balance()}"
                }
                return data
        except:
            raise grpc.RpcError()
        
            
            
        
            
                
            
                 
            
        