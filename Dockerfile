# Use the official lightweight Python image.
FROM python:3.8
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY src/ /src
WORKDIR /src

ENTRYPOINT [ "python", "main.py"]
