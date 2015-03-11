from __future__ import absolute_import

from sqlalchemy import Column, Integer, String, Date
from flask import Flask, Response, abort, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS


app = Flask(__name__)
app.config.from_pyfile('config.py')
cors = CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql+psycopg2://%s:%s@%s/%s' %
                                         (app.config['USER'],
                                          app.config['PASSWORD'],
                                          app.config['HOST'],
                                          app.config['DBNAME']))

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user_in_sails'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    accountType = Column(String)


class Groundtruth(db.Model):
    __tablename__ = 'groundtruth'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    activity = Column(String)
    user = Column(Integer)


@app.route('/groundtruths', methods=['POST'])
def create_groundtruth():
    try:
        groundtruth = Groundtruth(id=request.form['id'],
                                  activity=request.form['activity'],
                                  user=request.form['user'],
                                  date=request.form['date'])
        db.session.add(groundtruth)
        db.session.commit()
        return Response(None, status=201)
    except Exception as e:
        raise e
        abort(403)


@app.route('/users')
def get_users():
    users = {'users': [{'id': row.id, 'name': row.name,
                        'accountType': row.accountType}
                       for row in db.session.query(User.name, User.id,
                                                   User.accountType). \
                       filter(User.accountType == 'Personal')]}
    return jsonify(**users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
