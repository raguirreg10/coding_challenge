# coding_challenge
## Romell's WindRiver Coding Challenge

This readme provides the instructions to build and run the web service, this service was built using Python Flask, for more information check the official documentation at https://flask.palletsprojects.com/en/1.1.x/.

## Web Service Workflow

This Web service should accept a json document and execute a encrypt/decrypt procedure,it provides 3 Endpoints 

- /api/encrypt => Encrypt the value provided by the JSON document
- /api/decrypt => Decrypt the output from the encrypt endpoint
- /api/health => simple proof of liveness of the web service

## Build and Run in Docker

This repository contains the Dockerfile to build the image and run in any environment with Docker Installed, such as local computer - an EC2 instance - remote VM, follow the steps to build the image

1. Clone the repository using the `git clone` command and navigate into the root directory by running `cd coding_challenge`
2. Using `docker` command run `docker build -t flask:latest .` (be aware there is a dot at the end) this command will look for the Dockerfile inside the root directory and build the image providing the name and tag after the -t argument.
3. Once the process finishes, run the following command to create the container `docker run -dp 5000:5000 --name flask_app flask:latest`, docker run takes the image and create a container `-d` argument runs the container in detached mode or in the background for simple purpose, `-p` maps the ports between the host and the container following this format _host_port_:_container_port_ and finally the `--name` provides the name for the container.
4. Access the application from outside system by using the *Container Host IP Address:5000* which is the port used by the application, you can grab this information by running the commands `ifconfig` for Linux or `ipconfig` for Windows machines, for instance the Host IP is 172.0.0.1 you can access the application by using 172.0.0.1:5000

## Run in Kubernetes

This repository contains the resource file to run the application in Kubernetes, this file named **kubernetes_deployment.yml** contains the necessary resources to deploy and expose the application, a Service kind NodePort should be created and expose the Pods created by the Deployment Object which runs 3 replicas of the Pods.

To run on a Kubernetes Cluster use the `kubectl create` command as follow `kubectl create -f kubernetes_deployment.yml`, after running this command the neccesary resources will be created and these can be shown by running `kubectl get all` which enlist the objects in the namespace, finally you can access the application by providing the _nodeMachineIP:30007_ (30007 is the port opened by the service NodePort which enables outside communication and redirected to port 5000 of the application)

## Run Application Locally

To run the application locally run the container on your local machine and can be accesible at _localhost:5000_ or _127.0.0.1:5000_

## Docker Image Location

The official docker image can be found at the following link https://hub.docker.com/r/romellaguirre1008/flask-api or running the `docker pull` command `docker pull romellaguirre1008/flask-api`

![Image of Docker](https://hackernoon.com/hn-images/0*m-xEibEV8ttbhv7W.png)



