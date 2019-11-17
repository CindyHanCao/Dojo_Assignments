from config import app, db
from flask import render_template, redirect, request
from sqlalchemy.sql import func
#### ADDING THIS CLASS ####
# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database
class Dojos(db.Model):	
    # __tablename__ = "users"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Ninjas(db.Model):	
    # __tablename__ = "users"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojo_id = db.Column(db.Integer, db.ForeignKey('dojos.id'), nullable=False)
    dojo = db.relationship('Dojos', foreign_keys=[dojo_id], backref="dojo_ninjas", cascade="all")
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

# routes go here...
@app.route('/')
def home_page():
    all_dojos = Dojos.query.all()
    all_ninjas = Ninjas.query.all()
    return render_template('index.html', dojos=all_dojos, ninjas=all_ninjas)

@app.route('/process', methods=['POST'])
def add_dojo():
    new_dojo = Dojos(name=request.form['dojoName'], city=request.form['cityName'], state=request.form['state'])
    db.session.add(new_dojo)
    db.session.commit()
    print(new_dojo)
    return redirect('/')

@app.route('/process/ninja', methods=['POST'])
def add_ninja():
    new_ninja = Ninjas(first_name=request.form['fname'], last_name=request.form['lname'], dojo_id=request.form['dojo'])
    db.session.add(new_ninja)
    db.session.commit()
    print(new_ninja)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)