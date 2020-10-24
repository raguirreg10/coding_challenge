FROM alpine:3.12

LABEL maintainer="romellaguirre@gmail.com"

#########################################
# Install initial packages
#########################################
RUN apk add --no-cache bash git python3 py3-pip

#########################################
# Python dependencies installation
#########################################
RUN pip3 install requests flask pybase64

#########################################
# Expose port 5000 for flask app
#########################################
EXPOSE 5000

#########################################
# Copy python code to docker image
#########################################
RUN mkdir /tmp/romell_coding
COPY romell_challenge.py /tmp/romell_coding/romell_challenge.py

#########################################
# Setting working directory
#########################################
WORKDIR /tmp/romell_coding

#########################################
# Run application
#########################################
CMD [ "python3", "romell_challenge.py" ]
