from flask import Flask, render_template, redirect, request			# same as before
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from sqlalchemy.sql import func     # ADDED THIS LINE FOR DEFAULT TIMESTAMP
from flask_migrate import Migrate			# this is new
app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_authors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)
#### ADDING THIS CLASS ####
# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database

author_book_table = db.Table('author_book', db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True), db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True))

class Books(db.Model):	
    # __tablename__ = "users"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    author_book = db.relationship('Authors', secondary=author_book_table)

    def __repr__(self):
        return f"<Book title: {self.title}>"

class Authors(db.Model):	
    # __tablename__ = "users"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    notes = db.Column(db.String(255))
    # dojo_id = db.Column(db.Integer, db.ForeignKey('dojos.id'), nullable=False)
    # dojo = db.relationship('Dojos', foreign_keys=[dojo_id], backref="dojo_ninjas", cascade="all")
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    authors_for_this_book = db.relationship('Books', secondary=author_book_table)

    def full_name(self):
        return self.first_name + ' ' + self.last_name

# routes go here...
@app.route('/')
def home_page():
    all_books = Books.query.all()
    authors = Authors.query.all()
    return render_template('books.html', books = all_books, authors = authors)

@app.route('/addBooks', methods=['POST'])
def add_book():
    new_book = Books(title=request.form['title'], description=request.form['description'])
    db.session.add(new_book)
    db.session.commit()
    print(new_book)
    return redirect('/')

@app.route("/books/<id>")
def detail(id):
    print('GOT HERE')
    book = Books.query.get(id)
    print('GOT NEXT')
    return render_template('book_detail.html', book=book)

@app.route('/authors')
def authorMain():
    all_authors = Authors.query.all()
    # all_ninjas = Ninjas.query.all()
    return render_template('authors.html', authors = all_authors)

@app.route('/addAuthors', methods=['POST'])
def add_author():
    new_author = Authors(first_name=request.form['fname'], last_name=request.form['lname'],notes=request.form['notes'])
    db.session.add(new_author)
    db.session.commit()
    print(new_author)
    return redirect('/authors')

@app.route("/authors/<id>")
def oneAuthor(id):
    print('GOT HERE')
    author = Authors.query.get(id)
    print('GOT NEXT')
    return render_template('author_detail.html', author=author)

@app.route('/authors_for_this_book', methods=["POST"])
def add_author_book():
    author=Authors.query.get(request.form['author_id'])
    book=Books.query.get(request.form['book_id'])
    print(author, book)
    author.authors_for_this_book.append(book)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)