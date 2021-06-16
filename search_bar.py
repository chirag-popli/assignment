from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/user'
db = SQLAlchemy(app)
class Signup(db.Model):
    username = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String())
    first_name = db.Column(db.Integer)
    last_name = db.Column(db.String())
    phone_no = db.Column(db.String())
    password = db.Column(db.Integer)
    date_time = db.Column(db.DateTime)
@app.route("/search/<string:key>")
def search(key):
    res=Signup.query.filter_by(username=key).first()
    return jsonify({'name':res.username})

if __name__=='__main__':
    app.run(debug=True)