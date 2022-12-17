

# Recipe App-API



Requirements

```py
Django>=3.2.4,<3.3
djangorestframework>=3.12.4,<3.13
psycopg2>=2.8.6,<2.9
```



 ### Part 1: Start Django Project

```bas
 docker-compose run --rm app sh -c "django-admin startproject app ."
```

This is what the file structure should look like at this point.

```bash
.
├── Dockerfile
├── NOTES.MD
├── README.md
├── app
│   ├── app
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── docker-compose.yml
├── requirements.dev.txt
├── requirements.md
└── requirements.txt
```

This is what the file structure should look like at this point.



### Part 2: Create DB

Add the below to your docker-compose file

```yaml
 environment:
      - DB_HOST=db
      - DB_NAME=devdb
      - DB_USER=devuser
      - DB_PASS=changeme
    depends_on:
      - db

  db:
    image: postgres:13-alpine
    volumes:
      - dev-db-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=devdb
      - POSTGRES_USER=devuser
      - POSTGRES_PASSWORD=changeme

volumes:
  dev-db-data:
  dev-static-data:
```



Replace the Database section of the settings config file

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PORT': os.environ.get('5432'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}
```

We updated the D ockerfile to install the dependencies need to install Psycopg2 but then we also added a line to remove them after the install



```yaml
FROM python:3.9-alpine3.13
LABEL maintainer='roger@mukaiguy.com'

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Add Dependencies
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    #Start Dev Logic
    if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt ;\
    fi && \
    #End Dev Logic
    rm -rf /tmp && \
    # Remove Dependencies
    apk del .tmp-build-deps && \

    adduser \
    --disabled-password \
    --no-create-home \ 
    django-user 

ENV PATH="/py/bin:$PATH"

USER django-user


```



### Part 3: Adding An App to the Django Project

```bash
docker-compose run --rm app sh -c "python manage.py startapp core"
```

This 'core' app will host the code that is shared across our services/apps 

We will delete tests.py and views.py 

we will add a test dir instead (don't forget to add "____init____.py")

Now that we created a 'core' app we need to register in the settings.py file by adding it to the INSTALLED_APPS list



##### This is what your project should look like at this point

```bash
.
├── Dockerfile
├── MyRequirements.md
├── NOTES.MD
├── README.md
├── app
│   ├── app
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── asgi.py
│   │   ├── calc.py
│   │   ├── settings.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   └── tests
│   └── manage.py
├── docker-compose.yml
├── requirements.dev.txt
└── requirements.txt

6 directories, 19 files
```

