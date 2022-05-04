from cmath import log
from crypt import methods
import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "databasename.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file


db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String)

    def __repr__(self):
        return f"<Book(fullname={self.title}, nickname={self.author})>"

    def toDict(self):
        return {
          'id': self.id,
          'title': self.title,
          'author': self.author
        }

### ROUTE

@app.route('/', methods=["GET", "POST"])
def home():
  return "Flask REST API Boilerplate v1.0"


@app.route('/add', methods=["GET", "POST"])
def add():
    books = None
    if request.json:
        try:
            book = Book(title=request.json['title'], author = request.json['author'])
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed to add")
            print(e)
            return(("Failed to add"))
    return book.toDict()


@app.route('/read', methods=["GET"])
def read():
  if request.json:
      try:
          book = Book.query.get(request.json["id"])
          db.session.commit()
          print(book.toDict())
          return book.toDict()
      except Exception as e:
          print("Failed to add")
          print(e)
          return(("Failed to add"))


@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


  




