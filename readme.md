
## Installation

- Create and activate a virtualenv

- Install all packages from pipfile

```bash
  $ pipenv install
```

- Database

```bash
  $ python manage.py makemigrations

  $ python manage.py migrate

  $ python manage.py load_defaults
```

- Run server

```bash
  $ python manage.py runserver
```