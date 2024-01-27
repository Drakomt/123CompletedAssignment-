# FROM python:3.8

# WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the consumer script into the container
# COPY main.py .

# # Command to run the consumer script
# CMD ["python", "main.py"]


FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
