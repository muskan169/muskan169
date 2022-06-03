# syntax=docker/dockerfile:1
#FROM python:3.8
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#WORKDIR /blogapp
#COPY requirements.txt /blogapp/
#RUN pip install -r requirements.txt
#COPY . /blogapp/

# base image  
FROM python:3.8   

# set work directory  
#RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR /eshop 

ADD . /eshop

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . /Eshop /
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver 1:8000