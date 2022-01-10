FROM python:3.9

COPY . /app/containerized-covid-api

WORKDIR /app/containerized-covid-api

RUN pip install -r requirements/requirements.txt

EXPOSE 8080

CMD python3 app.py