# server.py
from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc
from dataclasses import dataclass
@dataclass
class Person:
    name:str
    age:int
    have_car:bool
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_have_car(self):
        return self.have_car
class MyServiceServicer(service_pb2_grpc.MyServiceServicer):
    def GetPerson(self, request, context):
        people:list[Person] = [Person("Keven",14,True),Person("Antonio",15,True), Person("Davi",11,False),Person("Rosimeire",36,True)]
        person_choose = None
        
        for i in people:
            print(i)
            if i.get_name() == str(request.id):
                person_choose = i
                print("There is")
                
        person = service_pb2.Person(name=person_choose.get_name(),age=person_choose.get_age(), have_car=person_choose.get_have_car())
        return service_pb2.PersonResponse(person=person)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
