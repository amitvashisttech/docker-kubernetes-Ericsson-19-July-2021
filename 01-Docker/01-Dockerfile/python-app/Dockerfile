# Base Image for Python App.
FROM python:2.7-slim

# Set the working dir for the app is /app
WORKDIR /app

# Add the data
ADD . /app

#Install python required packages
RUN pip install --trusted-host pypi.python.org -r req.txt

# Expose Port
EXPOSE 80

#Run my python app. 
CMD ["python", "app.py"]
