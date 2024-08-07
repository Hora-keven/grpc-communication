from flask import Flask, request, jsonify, abort
import requests
import grpc
import service_pb2
import service_pb2_grpc
from google.protobuf.json_format import MessageToDict

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)
        response = stub.GetPerson(service_pb2.PersonRequest(id='Keven'))
        new_format_response = MessageToDict(response)
        
    return new_format_response



app = Flask(__name__)

@app.route('/grpc_server_message', methods=['GET', "PUT","DELETE", "POST"])
def get_server_message():
    try:
        server_message = run()
        return jsonify(server_message), 200
    except grpc.RpcError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run("127.0.0.1",port=8080,debug=True)