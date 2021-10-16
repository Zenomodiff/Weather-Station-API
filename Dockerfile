FROM python:3.8.2
LABEL createdby="Sashwat K <sashwat0001@gmail.com>"
LABEL maintainer="Sreeram A J<sreeramzeno@gmail.com>"

# Setting up work environment
WORKDIR /app
COPY . /app

# Update and upgrade linux container
RUN apt-get -y update --fix-missing
RUN apt-get upgrade -y

# Install useful tools
RUN apt-get -y install apt-utils nano wget dialog

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Runs app.py
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]