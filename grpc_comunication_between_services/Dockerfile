FROM python:3.9-alpine3.19
COPY ./requirements.txt /etc
RUN pip install -r /etc/requirements.txt
COPY . .
CMD ["python", 'main_api.py',"grpc_server.py"]
EXPOSE 8081