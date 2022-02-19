FROM python:3.9.10-slim-buster
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
CMD ["python3","manage.py","runserver","0:8000"]