ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION}

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    libpq-dev \
    software-properties-common

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN yes | python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Install fixtures
# RUN python manage.py loaddata myapp/fixtures/pets.json

EXPOSE 8080

CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "config.wsgi"]
