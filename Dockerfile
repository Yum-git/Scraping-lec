FROM python:3.7.9
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./main.py /app/
COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]