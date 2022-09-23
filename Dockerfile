FROM python:3.9.12-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app/

USER root
RUN apt-get update && apt-get install
RUN pip3 install --upgrade setuptool pip
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY ./DisasterTweetsAPI /app/

EXPOSE 5035

CMD ["python", "app.py"]
