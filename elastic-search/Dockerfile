FROM python:3.11-bullseye
RUN addgroup beaker && \
    adduser --disabled-password --ingroup beaker beaker
RUN apt-get update && apt-get -y upgrade
COPY /src /app
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install --upgrade --no-cache-dir -r ./requirements.txt && \
    chown -R beaker:beaker /app
USER beaker
CMD ["python", "-u", "app.py"]
