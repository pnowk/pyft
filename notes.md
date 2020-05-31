# Resources

- https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku

- https://flask-migrate.readthedocs.io/en/latest/

# Examples

## Migrations

```bash
flask db init

python manage.py db init
python  manage.py db migrate -m "migration name"
```


### first migration

this will generate migration script

```bash
flask db migrate -m 'users table'
```

this will detect the changes in the model and modify the database

```bash
flask db migrate
```


```bash
python manage.py db upgrade

```
