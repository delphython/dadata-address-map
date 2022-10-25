# Dadata api example site

## Install and launch via Docker

**1. Clone this repository**

```bash
git clone https://github.com/delphython/dadata-address-map.git
```

**2. Go inside the repository folder**

```bash
cd dadata-address-map
```

**3. Set environment variables**

- Create `.env` files in the root folder based on the `.example-env` within the same folder

**4. Build with `docker-compose`**

```bash
docker-compose up --build
```

**5. Migrate the database, add superuser and export data from city.scv file**

```bash
docker-compose exec backend ./manage.py migrate
```

```bash
docker-compose exec backend ./manage.py createsuperuser
```

```bash
docker-compose exec backend ./manage.py export_csv city.scv
```

**6. Launch the site**

[http://127.0.0.1:8000](http://127.0.0.1:8000)


## Install and launch in local environment

**1. Clone this repository**

```bash
git clone https://github.com/delphython/dadata-address-map.git
```

**2. Go inside the repository folder**

```bash
cd dadata-address-map
```

**3. Set environment variables**

- Create `.env` files in the root folder based on the `.example-env` within the same folder

**4. Use `pip` to install dependencies**

```bash
python -m pip install -r requirements.txt
```

**5. Migrate the database, add superuser and export data from city.scv file**

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py export_csv city.scv
```

**6. Launch the site**

[http://127.0.0.1:81](http://127.0.0.1:81)


## Environment variables
### Django variables

- `ALLOWED_HOSTS` - allowed hosts (default: `["127.0.0.1", "localhost"]`)
- `DJANGO_DEBUG` - debug mode (default: `False`)
- `DJANGO_SECRET_KEY` - Django secret key
- `DADATA_TOKEN` - Dadata service personal token
- `DADATA_SECRET` - Dadata service personal secret

## Meta

Vitaly Klyukin — [@delphython](https://t.me/delphython) — [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
