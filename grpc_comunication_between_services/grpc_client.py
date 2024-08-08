# server.py
from concurrent import futures

import grpc
from . import service_pb2
from . import service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:90090') as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)
        response = stub.GetPerson(service_pb2.PersonRequest(search="person name"))
        print(f"Name: {response.person.name}")

if __name__ == '__main__':
    run()

