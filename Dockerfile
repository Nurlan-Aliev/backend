FROM python:3.13

WORKDIR /myapp

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /myapp/requirements.txt

COPY . .

CMD ["python", "main.py"]