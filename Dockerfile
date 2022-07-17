FROM python:3.10-slim-buster
WORKDIR /app

# Dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# App
COPY . .
# -u forces the output to display as soon as its printed
ENTRYPOINT ["python3", "-u", "app.py"]
