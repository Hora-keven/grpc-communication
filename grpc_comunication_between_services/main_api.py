from flask import Flask, jsonify
import grpc
import service_pb2
import service_pb2_grpc 
from google.protobuf.json_format import MessageToDict

def run(who_send:str, who_receive:str, value:float):
    with grpc.insecure_channel('localhost:90090') as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)
        response = stub.GetPerson(service_pb2.PersonRequest(who_send=who_send, who_receive=who_receive,value=value))
        new_format_response = MessageToDict(response)
        
    return new_format_response



app = Flask(__name__)

@app.route('/transaction/<string:who_send>/<string:who_receive>/<float:value>', methods=['GET'])
def get_transaction(who_send:str, who_receive:str,value:float):
    try:
        server_message = run(who_send=who_send,who_receive=who_receive,value=value)
        return jsonify(server_message), 200
    except grpc.RpcError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run("127.0.0.1",port=8080,debug=True)