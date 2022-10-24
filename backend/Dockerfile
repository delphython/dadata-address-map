# syntax=docker/dockerfile:1

FROM nginx/unit:1.26.1-python3.10
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir \
    && apt autoremove --purge -y \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

COPY unit_config.json /docker-entrypoint.d/
COPY . .

RUN DJANGO_SECRET_KEY=empty python manage.py collectstatic --noinput
