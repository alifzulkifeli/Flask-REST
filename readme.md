# Flask REST Starter

## Quickstart
```bash
 - git clone ~
 - pyhton3 app.py
```


## How tu use
- change the name `databasename.db`
- run below commands
 ``` py
 >>> from bookmanager import db
 >>> db.create_all()
 >>> exit()
 ```
- edit model
```py
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String)

    def __repr__(self):
        return f"<Book(fullname={self.title}, nickname={self.author})>"
```

- Ready for CRUD
