FROM ubuntu:xenial # we are using an ubuntu xenial client
COPY . /src
WORKDIR /src
RUN apt-get update -y #runs updates in docker
RUN apt-get install -y python3 # installs python3 in docker
RUN apt-get install -y python3-pip #installs pip for python
RUN pip3 install flask # installs flask for our app
EXPOSE 8080 # exposes port 8080 

RUN python3 raiders_test.py

#Remember to capitalize Dockerfile or it wont run!!!!