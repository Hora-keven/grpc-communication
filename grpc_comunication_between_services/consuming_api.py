from flask import Flask, request, jsonify, abort
import requests
import grpc
import service_pb2
import service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)
        response = stub.GetPerson(service_pb2.PersonRequest(id=1))
        print(f"Name: {response.person.name}")
        print(f"{response.person}")
        
    return f"{response.person}"



app = Flask(__name__)
SERIVCE_URL = '10.234.149.119:8000/api/v1'

@app.route('/grpc_server_message', methods=['GET'])
def service():
    server_message = run()
    return (server_message, 200)

if __name__ == "__main__":
    app.run("127.0.0.1",port=8080,debug=True)