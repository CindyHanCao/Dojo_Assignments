from config import app, db
from flask import render_template, redirect, request
from models import Dojos, Ninjas
#### ADDING THIS CLASS ####
# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database


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