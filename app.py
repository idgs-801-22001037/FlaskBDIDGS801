from flask import Flask, render_template,request,redirect,url_for
from flask import flash 
from flask_wtf import CSRFProtect
from flask import g
from config import DevelomentConfig
import forms

from models import db
from models import Alumnos



app = Flask(__name__)
app.config.from_object(DevelomentConfig)
csrf = CSRFProtect()


@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index():
    create_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    
    return render_template("index.html", form=create_form, alumnos=alumno)
@app.route('/detalles', methods=['GET','POST'])
def detalles():
    if request.method=='GET':
        id=request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        id = request.args.get('id')
        nombre=alumno.nombre
        apaterno=alumno.apaterno
        email=alumno.email
    return render_template('detalles.html', id=id, nombre=nombre, apaterno=apaterno, email=email)
if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)