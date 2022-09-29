ARG PYTHON_VERSION=3.7

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
RUN python manage.py loaddata my_django21_project/fixtures/pets.json

EXPOSE 8080

# replace APP_NAME with module name
CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "my_django21_project.wsgi"]
