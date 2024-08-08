# server.py
from concurrent import futures

import grpc
import service_pb2 
import service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:90090') as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)
        response = stub.GetPerson(service_pb2.PersonRequest(who_send="Keven",who_receive="Rosimeire",value=1100))
        print(f"Name: {response.person_send}")

if __name__ == '__main__':
    run()

