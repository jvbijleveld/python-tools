FROM python:3.12-slim-bullseye
EXPOSE 80

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# nl_NL.UTF-8 UTF-8/nl_NL.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

RUN pip3 install pipenv

COPY Pipfile* /tmp/
RUN chmod 755 -R /tmp

WORKDIR /tmp

RUN pipenv requirements > requirements.txt

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app/app
RUN chmod 755 -R /app/app

WORKDIR /app

CMD ["uvicorn", "app.main:app", "--port", "80"]