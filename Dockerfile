FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim
EXPOSE 80

RUN pip install pipenv

COPY Pipfile* /tmp/
RUN chmod 755 -R /tmp

RUN cd /tmp && pipenv lock && pipenv requirements > requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app/app
RUN chmod 755 -R /app/app

