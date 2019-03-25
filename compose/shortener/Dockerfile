FROM python:3.7
RUN mkdir -p /app
WORKDIR /app
ADD ./shortener /app
RUN pip install -r /app/requirements.txt

CMD ["python3", "/app/main.py", "--log=INFO"]
