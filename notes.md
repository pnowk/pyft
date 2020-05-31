## migrations

```bash
flask db init
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
