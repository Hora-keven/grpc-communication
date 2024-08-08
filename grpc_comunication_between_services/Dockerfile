FROM ubuntu:20.04
RUN api-get update && apt-get-install -y python3.9 python3.9-dev
COPY . .
RUN pip install -r requirements.txt
CMD ["python"]
EXPOSE 8081