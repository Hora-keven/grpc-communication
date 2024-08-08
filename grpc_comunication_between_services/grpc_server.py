# server.py
from concurrent import futures
import grpc
import service_pb2
import  service_pb2_grpc
from api import Api

    
class MyServiceServicer(service_pb2_grpc.MyServiceServicer):
    def GetPerson(self, request, context):
        api = Api()
        person_choose = api.transaction(request.who_send,request.who_receive,request.value)
      
        person_send = service_pb2.Person(name=person_choose.get("who_send").get_name(),age=person_choose.get("who_send").get_age(),balance=person_choose.get("who_send").get_balance(),have_debts=person_choose.get("who_send").get_have_debts())
        person_receive = service_pb2.Person(name=person_choose.get("who_receive").get_name(),age=person_choose.get("who_receive").get_age(),balance=person_choose.get("who_receive").get_balance(),have_debts=person_choose.get("who_receive").get_have_debts())
        return service_pb2.PersonResponse(person_send=person_send,value=request.value,person_receive=person_receive, message=person_choose.get("message"))
         

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:90090')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
