FROM python:3.8-slim-buster

WORKDIR /root

COPY requirement.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "hello.py"]
