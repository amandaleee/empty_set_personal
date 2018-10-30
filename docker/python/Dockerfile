FROM python:3.7

# Send python stdout directly to terminal without buffering
ENV PYTHONUNBUFFERED 1

# Install mysql-client
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    mysql-client

# Install pipenv
RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

COPY . .

RUN pipenv install

STOPSIGNAL SIGINT

CMD ["pipenv", "run", "gunicorn", "--chdir", "empty_set", "--bind", ":8000", "empty_set.wsgi:application"]