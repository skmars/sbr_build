FROM python:3.10.8-slim-buster

# Get the project into the docker container
WORKDIR /app
COPY . .

# Installing all python dependencies
RUN python3 -m pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]

