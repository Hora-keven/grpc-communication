# server.py
from concurrent import futures

import grpc
import service_pb2
import service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)
        response = stub.GetPerson(service_pb2.PersonRequest(id=1))
        print(f"Name: {response.person.name}")

if __name__ == '__main__':
    run()

