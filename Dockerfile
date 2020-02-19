FROM python:3

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

#COPY ./mongo_ver.py ./script.py

ENTRYPOINT [ "python", "./main.py" ]