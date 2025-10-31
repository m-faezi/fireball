# Fireball


Setting up development Environment on Linux
----------------------------------

### Install Project (edit mode)

#### Working copy
    
    $ cd /path/to/workspace
    $ git clone git@github.com:m-faezi/fireball.git
    $ python3.11 -m venv ./venvs/mmto
    $ source ./venvs/mmto/bin/activate
    $ cd fireball
    $ pip install -e .
 
### Setup Database

#### Configuration

```yaml

db:
  url: postgresql://postgres:postgres@localhost/fireball_dev
  test_url: postgresql://postgres:postgres@localhost/fireball_test
  administrative_url: postgresql://postgres:postgres@localhost/postgres

messaging:
  default_messenger: restfulpy.messaging.SmtpProvider

smtp:
  host: <example.com>
  port: 587
  username: <smtp-user>
  password: <smtp-password>
  local_hostname: carrene.com
   
```

#### Remove old abd create a new database **TAKE CARE ABOUT USING THAT**

    $ fireball db create --drop --mockup

And or

    $ fireball db create --drop --basedata 

#### Drop old database: **TAKE CARE ABOUT USING THAT**

    $ fireball [-c path/to/config.yml] db --drop

#### Create database

    $ fireball [-c path/to/config.yml] db --create

Or, you can add `--drop` to drop the previously created database: **TAKE CARE ABOUT USING THAT**

    $ fireball [-c path/to/config.yml] db create --drop


### Running tests

```bash
pip install -r requirements-dev.txt
pytest
```

### Running server

#### Single threaded 

```bash
fireball [-c path/to/config.yml] serve
```

#### WSGI

wsgi.py

```python
from fireball import fireball

fireball.configure(files=...)
app = fireball
```

```bash
gunicorn wsgi:app
```

### How to start

Checkout `fireball/controllers/foo.py`, 
`fireball/models/foo.py` and `fireball/tests/test_foo.py` to
learn how to create an entity.

