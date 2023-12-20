FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip3 install pipenv
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock
RUN python3 -m pipenv install

WORKDIR /app
COPY ./ ./

CMD exec pipenv run uvicorn main:app --host 0.0.0.0 --reload
