FROM python:3.8-alpine

RUN pip install flask

WORKDIR /app

COPY . .

EXPOSE 5000

CMD [ "python", "hello1.py" ]
