

# Recipe App-API



Requirements

```py
Django>=3.2.4,<3.3
djangorestframework>=3.12.4,<3.13
```



 ### Start Django Project

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



## 