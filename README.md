# telegram-bot


## Structure
- app
    - db
      - models
        - `__init__.py`
        - `user.py`
      - `db.py`
      - `base.py`
      - `base_class.py`
      - `init_db.py`
      - `session.py`
      - `utils.py`
    - deps
      - `__init__py`
      - `db.py`
    - enums
      - `base.py`
      - `user_sex.py`
      - `user_state.py`
    - `bot.py`
    - `bot_handlers.py`
    - `config.py`
    - `keyboards.py`
    - `messages.py`
    - `state_handler.py`
    - `states.py`
    - `validator.py`
    
- `run_server.py`


# local run

First we need to create python virtual environment, if it doesn't exist.
```shell
which python

# if 'python not found'
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate
```


Install packages.
```shell
# create requirements.txt
# pip3 freeze > requirements.txt
# install requirements-dev
pip install -r requirements-dev.txt
```

### Install postgres.
```shell
psql -V
# >> psql (PostgreSQL) 12.7 (Ubuntu 12.7-0ubuntu0.20.04.1)
# if 'command not found: psql'
sudo apt install postgresql postgresql-contrib
sudo -i -u postgres

# create a new database
psql
>> CREATE DATABASE name

Commands:
   \q - close psql terminal
   \l - get list of databases
   \d - get info about new database

Connection string:
'postgresql://username:pass@localhost/database_name'
```


### .env
    export APP_NAME=''
    export TOKEN=''
    export SQLALCHEMY_DATABASE_URI=''

### Run python and execute code to initialize db:
```python
from app.deps import db
from app.db.init_db import init_db

db = next(db.get_db())
init_db(db.get_bind())
```

###  Run server
```bash
# Edit run_server.py: line 31. bot.polling(none_stop=True) use to local run
# Edit run_server.py: line 32. # server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
python run_server.py
```